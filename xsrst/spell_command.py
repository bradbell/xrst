# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
# Process the spell command for a section
#
# data_in:
# is the data for this section before the spell command is removed.
#
# file_name:
# is the name of the file that this data comes from. This is only used
# for error reporting.
#
# section_name:
# is the name of the section that this data is in. This is only used
# for error reporting.
#
# spell_checker:
# Is the pyspellchecker object used for error checking.
#
# data_out:
# is the data for this section after the spell command (if it exists)
# is removed.
#
# Spelling Warnings:
# A spelling warning is reported for each word (and double word) that is not
# in the spell_checker dictionary or the speical word list. A word is two or
# more letter characters. If a word is directly precceded by a backslash,
# it is ignored (so that latex commands do not generate warnings).
#
import re
import xsrst
def spell_command(
    data_in, file_name, section_name, spell_checker
) :
    #
    # pattern
    pattern = dict()
    pattern['spell']     = re.compile( r'\n[ \t]*\{xsrst_spell([^}]*)\}' )
    pattern['word_list'] = re.compile( r'[A-Za-z\s]*' )
    #
    # pattern
    # global pattern values used by spell command
    pattern['child']  = xsrst.pattern['child']
    pattern['code']   = xsrst.pattern['code']
    pattern['file_2'] = xsrst.pattern['file_2']
    pattern['file_3'] = xsrst.pattern['file_3']
    pattern['line']   = xsrst.pattern['line']
    #
    # pattern
    # local pattern values only used by spell command
    pattern['directive']   = re.compile( r'\n[ ]*[.][.][ ]+[a-z-]+::' )
    pattern['double_word'] = re.compile(
        r'[^a-zA-Z]([A-Za-z][a-z]+)\s+\1[^a-z]'
    )
    pattern['http']  = re.compile( r'(https|http)://[A-Za-z0-9_/.]*' )
    pattern['ref_1'] = re.compile( r':ref:`[^\n<`]+`' )
    pattern['ref_2'] = re.compile( r':ref:`([^\n<`]+)<[^\n>`]+>`' )
    pattern['url_1'] = re.compile( r'`<[^\n>`]+>`_' )
    pattern['url_2'] = re.compile( r'`([^\n<`]+)<[^\n>`]+>`_' )
    pattern['word']  = re.compile( r'\\?[A-Za-z][a-z]+' )
    #
    #
    # m_spell
    m_spell       = pattern['spell'].search(data_in)
    #
    # special_used, double_used
    special_used  = dict()
    double_used   = dict()
    #
    # data_out
    data_out = data_in
    #
    if m_spell != None :
        #
        # check for multiple spell commands in one section
        m_tmp  = pattern['spell'].search(data_in, m_spell.end() )
        if m_tmp :
            msg  = 'There are two spell xsrst commands in this section'
            xsrst.system_exit(
                msg,
                file_name=file_name,
                section_name=section_name,
                m_obj=m_tmp,
                data=data_in
            )
        #
        # word_list
        word_list = m_spell.group(1)
        word_list = pattern['line'].sub('', word_list)
        m_tmp     = pattern['word_list'].search(word_list)
        if m_tmp.group(0) != word_list :
            msg  = 'The word list in spell command contains '
            msg += 'charactes that are not letters or white space.'
            xsrst.system_exit(
                msg,
                file_name=file_name,
                section_name=section_name,
                m_obj=m_spell,
                data=data_in
            )
        #
        # special_used, double_used
        previous_word = ''
        for m_obj in pattern['word'].finditer( word_list ) :
            word_lower = m_obj.group(0).lower()
            special_used[ word_lower ] = False
            if word_lower == previous_word :
                double_used[ word_lower ] = False
            previous_word = word_lower
        #
        # remove spell command
        start    = m_spell.start()
        end      = m_spell.end()
        data_out = data_in[: start] + data_in[end :]
    #
    # data_tmp
    # version of data_in with certain commands removed
    data_tmp = data_out
    #
    # commands with file names as arugments
    data_tmp = pattern['file_2'].sub('', data_tmp)
    data_tmp = pattern['file_3'].sub('', data_tmp)
    data_tmp = pattern['child'].sub('', data_tmp)
    data_tmp = pattern['http'].sub('', data_tmp)
    data_tmp = pattern['directive'].sub('', data_tmp)
    #
    # command with section names and headings as arguments
    data_tmp = pattern['ref_1'].sub('', data_tmp)
    data_tmp = pattern['ref_2'].sub(r'\1', data_tmp)
    data_tmp = pattern['code'].sub('', data_tmp)
    #
    # commands with external urls as arguments
    data_tmp = pattern['url_1'].sub('', data_tmp)
    data_tmp = pattern['url_2'].sub(r'\1', data_tmp)
    #
    # first_spell_error
    first_spell_error = True
    #
    # first_spell_erro, special_used, m_obj
    for m_obj in pattern['word'].finditer( data_tmp ) :
        word = m_obj.group(0)
        if word[0] != '\\' and len( spell_checker.unknown( [word] ) ) > 0 :
            word_lower = word.lower()
            if not word_lower in special_used :
                #
                # first_spell_error
                if first_spell_error :
                    msg  = '\nwarning: file = ' + file_name
                    msg += ', section = ' + section_name
                    print(msg)
                    first_spell_error = False
                #
                # line_number
                m_tmp  = pattern['line'].search(data_tmp, m_obj.end() )
                assert m_tmp
                line_number = m_tmp.group(1)
                #
                # msg
                msg  = 'spelling = ' + word
                suggest = spell_checker.correction(word)
                if suggest != word :
                    msg += ', suggest = ' + suggest
                msg += ', line ' + line_number
                #
                print(msg)
            #
            # special_used
            special_used[word_lower] = True
    #
    # first_spell_erro, special_used, double_used, m_obj
    for m_obj in pattern['double_word'].finditer(data_tmp) :
        word_lower = m_obj.group(1).lower()
        if not word_lower in double_used :
            #
            # first_spell_error
            if first_spell_error :
                msg  = 'warning: file = ' + file_name
                msg += ', section = ' + section_name
                print(msg)
                first_spell_error = False
            #
            # line_number
            m_tmp = pattern['line'].search(data_tmp, m_obj.end() )
            assert m_tmp
            line_number = m_tmp.group(1)
            #
            # first and last character in pattern is not part of double word
            double_word = m_obj.group(0)[1 : -1]
            msg         = 'double word error: "' + double_word + '"'
            msg        += ', line ' + line_number
            print(msg)
        #
        # double_used, special_used
        double_used[word_lower]  = True
        special_used[word_lower] = True
    #
    # check for words that were not used
    for word_lower in special_used :
        if not special_used[word_lower] :
            if first_spell_error :
                msg  = '\nwarning: file = ' + file_name
                msg += ', section = ' + section_name
                print(msg)
                first_spell_error = False
            msg = 'spelling word "' + word_lower + '" not needed'
            print(msg)
    for word_lower in double_used :
        if not double_used[word_lower] :
            if first_spell_error :
                msg  = '\nwarning: file = ' + file_name
                msg += ', section = ' + section_name
                print(msg)
                first_spell_error = False
            msg  = 'double word "' + word_lower + ' ' + word_lower
            msg += '" not needed'
            print(msg)
    #
    return data_out
