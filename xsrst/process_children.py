# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
import re
import xsrst
#
pattern = re.compile( r'{xsrst_(children|child_list|child_table)}' )
#
def process_children(
    data_in,
    section_name,
    list_children,
    line_increment,
) :
    #
    # split section data into lines
    newline_list = xsrst.newline_indices(data_in)
    #
    # data_out
    data_out = ''
    #
    # put hidden toctree next
    if len(list_children) > 0  :
        data_out += '.. toctree::\n'
        data_out += '   :maxdepth: 1\n'
        data_out += '   :hidden:\n\n'
        for child in list_children :
            data_out += '   ' + child + '\n'
        data_out += '\n'
    #
    # now output the section data
    startline         = 0
    previous_empty    = True
    has_child_command = False
    for newline in newline_list :
        line  = data_in[startline : newline + 1]
        # commands that delay some processing to this point
        children_command       = line.startswith('{xsrst_children')
        child_list_command     = line.startswith('{xsrst_child_list')
        child_table_command    = line.startswith('{xsrst_child_table')
        if children_command or child_list_command or child_table_command:
            assert not has_child_command
            assert len(list_children) > 0
            has_child_command = True
            #
            if child_list_command:
                data_out += '\n'
                for child in list_children :
                    data_out += '-  :ref:`' + child + '`\n'
                data_out += '\n'
            previous_empty = True
            if child_table_command:
                data_out += '.. csv-table::\n'
                data_out += '    :header:  "Child", "Title"\n'
                data_out += '    :widths: 20, 80\n\n'
                for child in list_children :
                    data_out += '    "' + child + '"'
                    data_out += ', :ref:`' + child + '`\n'
                data_out += '\n'
            previous_empty = True
        else :
            m_obj = xsrst.pattern['line'].search(line)
            if m_obj :
                empty_line = m_obj.start() == 0
            else :
                if len( line.strip(' \t') ) == 0 :
                    empty_line = True
                else :
                    empty_line = False
            if empty_line :
                    line = '\n'
            #
            if line != '\n' :
                data_out += line
            elif not previous_empty :
                data_out += line
            #
            previous_empty = line == '\n'
        startline = newline + 1
    #
    # The last step in converting xsrst commands is removing line numbers
    # (done last so mapping from output to input line number is correct)
    data_out, line_pair = xsrst.remove_line_numbers(data_out)
    # -----------------------------------------------------------------------
    if not previous_empty :
        data_out += '\n'
    #
    # If there is no child command in this section, automatically generate
    # links to the child sections at the end of the section.
    if len(list_children) > 0 and not has_child_command :
        data_out += '.. csv-table::\n'
        data_out += '    :header: "Child", "Title"\n'
        data_out += '    :widths: 20, 80\n\n'
        for child in list_children :
            data_out += '    "' + child + '"'
            data_out += ', :ref:`' + child + '`\n'
        data_out += '\n'
    #
    if line_increment > 0 :
        data_out += '\n.. csv-table:: Line Number Mapping\n'
        data_out += 4 * ' ' + ':header: rst file, xsrst input\n'
        data_out += 4 * ' ' + ':widths: 10, 10\n\n'
        previous_line = None
        for pair in line_pair :
            if previous_line is None :
                data_out   += f'    {pair[0]}, {pair[1]}\n'
                previous_line = pair[1]
            elif pair[1] - previous_line >= line_increment :
                data_out   += f'    {pair[0]}, {pair[1]}\n'
                previous_line = pair[1]
    #
    return data_out
