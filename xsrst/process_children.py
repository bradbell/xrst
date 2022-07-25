# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
import xsrst
def process_children(
    section_data,
    list_children,
    pseudo_heading,
    section_name,
    line_increment,
) :
    # split section data into lines
    newline_list = xsrst.newline_indices(section_data)
    #
    # start output by including preamble
    rst_output = '.. include:: ../preamble.rst\n\n'
    #
    # put pseudo heading next
    rst_output += pseudo_heading
    #
    # put hidden toctree next
    if len(list_children) > 0  :
        rst_output += '.. toctree::\n'
        rst_output += '   :maxdepth: 1\n'
        rst_output += '   :hidden:\n\n'
        for child in list_children :
            rst_output += '   ' + child + '\n'
        rst_output += '\n'
    #
    # now output the section data
    startline         = 0
    previous_empty    = True
    has_child_command = False
    for newline in newline_list :
        line  = section_data[startline : newline + 1]
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
                rst_output += '\n'
                for child in list_children :
                    rst_output += '-  :ref:`' + child + '`\n'
                rst_output += '\n'
            previous_empty = True
            if child_table_command:
                rst_output += '.. csv-table::\n'
                rst_output += '    :header:  "Child", "Title"\n'
                rst_output += '    :widths: 20, 80\n\n'
                for child in list_children :
                    rst_output += '    "' + child + '"'
                    rst_output += ', :ref:`' + child + '`\n'
                rst_output += '\n'
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
                rst_output += line
            elif not previous_empty :
                rst_output += line
            #
            previous_empty = line == '\n'
        startline = newline + 1
    #
    # The last step in converting xsrst commands is removing line numbers
    # (done last so mapping from output to input line number is correct)
    rst_output, line_pair = xsrst.remove_line_numbers(rst_output)
    # -----------------------------------------------------------------------
    if not previous_empty :
        rst_output += '\n'
    #
    # If there is no child command in this section, automatically generate
    # links to the child sections at the end of the section.
    if len(list_children) > 0 and not has_child_command :
        rst_output += '.. csv-table::\n'
        rst_output += '    :header: "Child", "Title"\n'
        rst_output += '    :widths: 20, 80\n\n'
        for child in list_children :
            rst_output += '    "' + child + '"'
            rst_output += ', :ref:`' + child + '`\n'
        rst_output += '\n'
    #
    if line_increment > 0 :
        rst_output += '\n.. csv-table:: Line Number Mapping\n'
        rst_output += 4 * ' ' + ':header: rst file, xsrst input\n'
        rst_output += 4 * ' ' + ':widths: 10, 10\n\n'
        previous_line = None
        for pair in line_pair :
            if previous_line is None :
                rst_output   += f'    {pair[0]}, {pair[1]}\n'
                previous_line = pair[1]
            elif pair[1] - previous_line >= line_increment :
                rst_output   += f'    {pair[0]}, {pair[1]}\n'
                previous_line = pair[1]
    #
    return rst_output
