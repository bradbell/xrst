# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
# add labels and indices for headings
import xsrst
def process_headings(
        section_data, file_in, section_name, index_list
) :
    #
    # punctuation
    punctuation      = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    assert len(punctuation) == 34 - 2 # two escape sequences
    #
    # overline_used
    overline_used = set()
    #
    # heading_list, heading_index, heading_text, underline_text
    heading_list     = list()
    data_index       = 0
    heading_index, heading_text, underline_text = \
        xsrst.next_heading(section_data, data_index)
    #
    while 0 <= heading_index :
        if 0 < heading_index :
            assert section_data[heading_index-1] == '\n'
        # overline
        m_obj = xsrst.pattern['line'].search(section_data, heading_index)
        index = m_obj.start()
        overline = underline_text == section_data[heading_index : index]
        #
        # character
        character = underline_text[0]
        #
        # heading
        heading   = {
            'overline' : overline,
            'character': character,
            'text':      heading_text
        }
        #
        # underline_end
        underline_end = section_data.find('\n', heading_index)
        underline_end = section_data.find('\n', underline_end+1)
        if overline :
            underline_end = section_data.find('\n', underline_end+1)
        assert section_data[underline_end] == '\n'
        #
        # overline_used
        if overline :
            overline_used.add(character)
        #
        # heading_list
        if len( heading_list ) == 0 :
            # first heading in this section
            heading_list.append( heading )
        else :
            # level_zero
            level_zero = overline == heading_list[0]['overline']
            if level_zero :
                level_zero = character == heading_list[0]['character']
            if level_zero :
                m_obj = \
                    xsrst.pattern['line'].search(section_data, heading_index)
                msg = 'There are multiple titles for this section'
                xsrst.system_exit(
                    msg,
                    file_name=file_in,
                    section_name=section_name,
                    m_obj=m_obj,
                    data=section_data
                )
            #
            # found_level
            found_level = False
            level       = 1
            while level < len(heading_list) and not found_level :
                found_level = overline == heading_list[level]['overline']
                if found_level :
                    found_level = character == heading_list[level]['character']
                if found_level :
                    #
                    # heading_list
                    heading_list = heading_list[: level ]
                    heading_list.append(heading)
                else :
                    level += 1
            #
            # heading_list
            if not found_level :
                # this heading at a deeper level
                heading_list.append( heading )

        label = ''
        for level in range( len(heading_list) ) :
            if level == 0 :
                label = section_name.lower().replace(' ', '_')
                label = label.replace('.', '_')
                assert label == section_name
            else :
                heading = heading_list[level]
                text   = heading['text'].lower().replace(' ', '_')
                label += '.' + text.replace('.', '_')
        #
        # index_entry
        if len(heading_list) == 1 :
            index_entry = section_name
        else :
            index_entry = ''
        for word in heading_list[-1]['text'].lower().split() :
            skip = False
            for regexp in index_list :
                m_obj = regexp.fullmatch(word)
                if m_obj :
                    skip = True
            if not skip :
                if index_entry == '' :
                    index_entry = word
                else :
                    index_entry += ',' + word
        #
        cmd  = '{xsrst_label '
        cmd += index_entry + ' '
        cmd += label + ' }\n'
        if len(heading_list) == 1 :
            cmd += '{xsrst_section_number}\n'
        #
        # data_left
        # data that comes before this heading
        data_left   = section_data[: heading_index]
        #
        # data_left
        # add new xsrst command before the heading
        data_left  += cmd
        #
        # data_left
        # add data from stat to end of heading
        data_left  += section_data[heading_index : underline_end]
        #
        # data_left
        # at level zero, add jump table command
        if len(heading_list) == 1 :
            data_left += '\n{xsrst_jump_table}'
        #
        # section_data
        data_right  = section_data[underline_end : ]
        section_data = data_left + data_right
        #
        # next heading
        data_index = len(data_left)
        heading_index, heading_text, underline_text = \
            xsrst.next_heading(section_data, data_index + 1)
    #
    if len(heading_list) == 0 :
        msg = 'There are no headings in this section'
        xsrst.system_exit(msg, file_name=file_in, section_name=section_name)
    #
    # pseudo_heading
    i = 0
    while punctuation[i] in overline_used :
        i += 1
        if i == len(punctuation) :
            msg  = 'more than ' + len(punctuation) - 1
            msg += ' overlined heading levels'
            xsrst.system_exit(
                msg, file_name=file_in, section_name=section_name
            )
    line           = len(section_name) * punctuation[i] + '\n'
    pseudo_heading = line + section_name + '\n' + line + '\n'
    #
    # section_title
    section_title = heading_list[0]['text']
    #
    return section_data, section_title, pseudo_heading
