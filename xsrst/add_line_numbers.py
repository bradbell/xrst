# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
# Add line numbers to a string in a way that is useful for reporting errors
# (for modified versions of string) using line number in the origianl string.
#
# data_in:
# The original string.
#
# data_out:
# The return data_out is a modified version of data_in.
# It has has added {xsrs_line number@ at the end of each non-empty line.
# Here number is the line number in data_in where the
# first line number is one (not zero).
#
import xsrst
def add_line_numbers(data) :
    newline_list = xsrst.newline_indices(data)
    result       = ""
    previous     = 0
    for i in range( len(newline_list) ) :
        current = newline_list[i]
        line    = data[previous : current]
        if previous == current :
            assert i == 0
        elif line[-1] != '\n' :
            line += '{xsrst_line ' + str(i + 1) + '@'
        result  += line
        previous = current
    #
    assert previous == len(data) - 1
    result += '\n'
    return result
