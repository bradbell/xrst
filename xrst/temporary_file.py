# -----------------------------------------------------------------------------
#                      xrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
import re
import xrst
pattern_line_number = re.compile( r'\n[ \t]*\{xrst_line [0-9]+@' )
pattern_newline_3   = re.compile( r'(\n[ \t]*){2,}\n' )
# ----------------------------------------------------------------------------
# Write the temporary RST file for a section.
#
# line_increment:
# is an int version of the line_increment arguemnt to the xrst program.
#
# pseudo_heading:
# is the pseudoc heading for this section. It is placed before
# all the other headings in this section.
#
# file_in:
# is the name of the xrst input file for this section.
#
# tmp_dir
# is the directory where the output file will be saved.
#
# section_name
# is the name of this section.  The output file is tmp_dir/section_name.rst.
#
# data_in
# is the data for this seciton with all the xrst commands coverted to
# their sphinx RST values, except the {xrst_section_number} command.
# The following is added to this deta before writing it to the output file:
# 1. The preamble is included at the beginning.
# 2. The name of the input file file_in is dispalyed near the end .
# 3. There or more lines with only tabs or space are conver to two empty lines.
# 4. The line numbers are removed.
# 5. if increment > 0, a mapping from RST line numbers to file_in line numbers
#    is included at the end.
#
def temporary_file(
    line_increment,
    pseudo_heading,
    file_in,
    tmp_dir,
    section_name,
    data_in,
) :
    assert type(line_increment) == int
    assert type(pseudo_heading) == str
    assert type(file_in) == str
    assert type(section_name) == str
    assert type(data_in) == str
    #
    # before
    # start output by including preamble and then pesudo_heading
    before = '.. include:: xrst_preamble.rst\n\n' + pseudo_heading
    #
    # after
    # end output with input file name
    after = '\n----\n\n' + f'xrst input file: ``{file_in}``\n'
    #
    # data_out
    data_out = before + data_in + after
    #
    # Convert three or more sequential emtpty lines to two empty lines.
    data_out = pattern_line_number.sub('\n', data_out)
    data_out = pattern_newline_3.sub('\n\n', data_out)
    #
    # The last step removing line numbers. This is done last for two reasons:
    # 1. So mapping from output to input line number is correct.
    # 2. We are no longer able to give line numbers for errors after this.
    data_out, line_pair = xrst.remove_line_numbers(data_out)
    #
    # after
    # If line number increment is non-zero, include mapping from
    # rst file line number to xrst file line number
    if line_increment > 0 :
        after  = '\n.. csv-table:: Line Number Mapping\n'
        after += 4 * ' ' + ':header: rst file, xrst input\n'
        after += 4 * ' ' + ':widths: 10, 10\n\n'
        previous_line = None
        for pair in line_pair :
            if previous_line is None :
                after        += f'    {pair[0]}, {pair[1]}\n'
                previous_line = pair[1]
            elif pair[1] - previous_line >= line_increment :
                after         += f'    {pair[0]}, {pair[1]}\n'
                previous_line = pair[1]
        #
        data_out = data_out + after
    #
    # open output file
    file_out = tmp_dir + '/' + section_name + '.rst'
    file_ptr = open(file_out, 'w')
    file_ptr.write(data_out)
    file_ptr.close()
