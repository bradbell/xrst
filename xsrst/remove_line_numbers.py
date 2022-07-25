# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
import xsrst
#
# Remove the number numbers that were added by add_line_number.
#
# data_in
# is the string we are removing the line numbers from {xsrst_line number@.
#
# data_out
# The first return data_out is a copy of data_in with the lin numbers removed.
#
# line_pair
# The second return line_pair is a list of tuples with two elements in each
# tuple. The first element is the line number in data_out. The second element
# is the corresponding line number that has been removed.
#
# data_out, line_pair =
def remove_line_numbers(data_in) :
    #
    # previous_end
    # index of the end of the previous match
    previous_end  = 0
    #
    # line_out
    # index of next line in data_out
    line_out  = 1
    #
    # data_out, line_pair
    data_out  = ''
    line_pair = list()
    #
    # data_out, line_pair
    for m_obj in xsrst.pattern['line'].finditer(data_in) :
        #
        # start of this match
        this_start = m_obj.start()
        #
        # before
        # character from end of previous match to start of this match
        before = data_in[previous_end  : this_start]
        #
        line_match = m_obj.group(1)
        line_out  += before.count('\n')
        #
        line_pair.append( ( line_out, int(line_match) ) )
        data_out += before
        #
        previous_end = m_obj.end()
    #
    # data_out
    data_out += data_in[previous_end  :]
    #
    return data_out, line_pair
