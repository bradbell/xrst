# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
# Replace {xsrst_section_number} by it section number or empty string.
#
# data_in:
# data before replacement. This must contain {xsrst_section_number}
# at the end of a line. Referred to as the command. There must be a
# section title after the command. The section tittle may have an rst
# overline directly before it and must have an underline directly after it.
# If both an overline and underline follow, they must be equal.
#
# section_number:
# The replacement for the command. This may be empty;
# i.e., the replacement text is the empty string.
#
# data_out:
# the return data_out is the data after replacement. This is a python str
#
# data_out =
def replace_section_number(data_in, section_number) :
    assert type(data_in) == str
    assert type(section_number) == str
    #
    # pattern
    pattern   = '\n{xsrst_section_number}'
    if section_number == '' :
        # data_out
        return data_in.replace(pattern,'')
    #
    # punctuation
    # Headings used repeated copies of one of these characters
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    #
    # start_cmd
    start_cmd = data_in.find(pattern)
    assert 0 <= start_cmd
    #
    # check first character after command
    ch  = data_in[start_cmd + len(pattern)]
    assert ch == '\n'
    #
    # second_index, third_index
    # index of second and third newline after command
    second_index = data_in.index('\n', start_cmd + len(pattern) + 1)
    third_index  = data_in.index('\n', second_index + 1)
    #
    # first_line, second_line
    first_line   = data_in[start_cmd + len(pattern) + 1 : second_index ]
    second_line  = data_in[ second_index + 1 : third_index ]
    #
    # overline
    # check for an overline directly after the command
    overline = False
    if first_line[0] * len(first_line) == first_line :
        if first_line[0] in punctuation :
            overline = True
    #
    if not overline :
        # If no overline so the section title followed the command and then
        # an underline after the title.
        assert second_line[0] in punctuation
        #
        # new version of first and second lines
        if section_number != '' :
            first_line   = section_number + ' ' + first_line
            second_line += second_line[0] * ( len(section_number) + 1 )
        #
    else :
        # fourth_index
        fourth_index = data_in.index('\n', third_index + 1)
        #
        # third_line
        third_line   = data_in[third_index + 1 : fourth_index]
        assert first_line == third_line
        #
        # new version of first, second, and third lines
        if section_number != '' :
            first_line += first_line[0] * ( len(section_number) + 1 )
            second_line = section_number + ' ' + second_line
            third_line  = first_line
    #
    # data_out
    data_out  = data_in[: start_cmd] + '\n'
    data_out += first_line + '\n'
    data_out += second_line + '\n'
    if overline :
        data_out += third_line
    data_out += data_in[third_index :]
    #
    return data_out
