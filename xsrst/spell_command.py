# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
# process spell command
#
#
import re
import xsrst
def spell_command(
    section_data, file_in, section_name, spell_checker
) :
    #
    # pattern
    pattern = dict()
    pattern['spell']       = re.compile( r'\n[ \t]*\{xsrst_spell([^}]*)\}' )
    #
    pattern['child']  = xsrst.pattern['child']
    pattern['code']   = xsrst.pattern['code']
    pattern['file_2'] = xsrst.pattern['file_2']
    pattern['file_3'] = xsrst.pattern['file_3']
    # local pattern values
    pattern['directive']   = re.compile( r'\n[ ]*[.][.][ ]+[a-z-]+::' )
    pattern['double_word'] = re.compile(
        r'[^a-zA-Z]([\\A-Za-z][a-z]*)\s+\1[^a-z]'
    )
    pattern['http']        = re.compile( r'(https|http)://[A-Za-z0-9_/.]*' )
    pattern['ref_1']       = re.compile( r':ref:`[^\n<`]+`' )
    pattern['ref_2']       = re.compile( r':ref:`([^\n<`]+)<[^\n>`]+>`' )
    pattern['url_1']       = re.compile( r'`<[^\n>`]+>`_' )
    pattern['url_2']       = re.compile( r'`([^\n<`]+)<[^\n>`]+>`_' )
    pattern['word']        = re.compile( r'[\\A-Za-z][a-z]*' )
    #
    #
    match_spell   = pattern['spell'].search(section_data)
    special_used  = dict()
    double_used   = dict()
    if match_spell != None :
        section_rest   = section_data[ match_spell.end() : ]
        match_another  = pattern['spell'].search(section_rest)
        if match_another :
            msg  = 'there are two spell xsrst commands'
            xsrst.system_exit(
                msg, file_name=file_in, section_name=section_name
            )
        previous_word = ''
        spell_arg = match_spell.group(1)
        spell_arg = xsrst.pattern['line'].sub('', spell_arg)
        for itr in pattern['word'].finditer( spell_arg ) :
            word_lower = itr.group(0).lower()
            if len(word_lower) > 1 :
                special_used[ word_lower ] = False
                if word_lower == previous_word :
                    double_used[ word_lower ] = False
            previous_word = word_lower
        #
        # remove spell command
        start        = match_spell.start()
        end          = match_spell.end()
        section_data = section_data[: start] + section_data[end :]
    # This suppress reporting \ \ as a double word error
    double_used['\\'] = True
    #
    # version of section_data with certain commands removed
    section_tmp = section_data
    #
    # commands with file names as arugments
    section_tmp = pattern['file_2'].sub('', section_tmp)
    section_tmp = pattern['file_3'].sub('', section_tmp)
    section_tmp = pattern['child'].sub('', section_tmp)
    section_tmp = pattern['http'].sub('', section_tmp)
    section_tmp = pattern['directive'].sub('', section_tmp)
    #
    # command with section names and headings as arguments
    section_tmp = pattern['ref_1'].sub('', section_tmp)
    section_tmp = pattern['ref_2'].sub(r'\1', section_tmp)
    section_tmp = pattern['code'].sub('', section_tmp)
    #
    # commands with external urls as arguments
    section_tmp = pattern['url_1'].sub('', section_tmp)
    section_tmp = pattern['url_2'].sub(r'\1', section_tmp)
    #
    # check for spelling errors
    first_spell_error = True
    for itr in pattern['word'].finditer( section_tmp ) :
        word = itr.group(0)
        if len( spell_checker.unknown( [word] ) ) > 0 :
            word_lower = word.lower()
            if not word_lower in special_used :
                if first_spell_error :
                    msg  = '\nwarning: file = ' + file_in
                    msg += ', section = ' + section_name
                    print(msg)
                    first_spell_error = False
                # line_number
                offset = itr.start()
                match  = xsrst.pattern['line'].search(section_tmp[offset :] )
                assert match
                line_number = match.group(1)
                #
                # msg
                msg  = 'spelling = ' + word
                suggest = spell_checker.correction(word)
                if suggest != word :
                    msg += ', suggest = ' + suggest
                msg += ', line ' + line_number
                #
                print(msg)
            special_used[word_lower] = True
    #
    # check for double word errors
    for itr in pattern['double_word'].finditer(section_tmp) :
        word_lower = itr.group(1).lower()
        if not word_lower in double_used :
            if first_spell_error :
                msg  = 'warning: file = ' + file_in
                msg += ', section = ' + section_name
                print(msg)
                first_spell_error = False
            # line_number
            offset = itr.start()
            match  = xsrst.pattern['line'].search(section_tmp[offset :] )
            assert match
            line_number = match.group(1)
            # first and last character in pattern is not part of double word
            double_word = itr.group(0)[1 : -1]
            msg         = 'double word error: "' + double_word + '"'
            msg        += ', line ' + line_number
            print(msg)
        double_used[word_lower]  = True
        special_used[word_lower] = True
    #
    # check for words that were not used
    for word_lower in special_used :
        if not special_used[word_lower] :
            if first_spell_error :
                msg  = '\nwarning: file = ' + file_in
                msg += ', section = ' + section_name
                print(msg)
                first_spell_error = False
            msg = 'spelling word "' + word_lower + '" not needed'
            print(msg)
    for word_lower in double_used :
        if not double_used[word_lower] :
            if first_spell_error :
                msg  = '\nwarning: file = ' + file_in
                msg += ', section = ' + section_name
                print(msg)
                first_spell_error = False
            msg  = 'double word "' + word_lower + ' ' + word_lower
            msg += '" not needed'
            print(msg)
    #
    return section_data
