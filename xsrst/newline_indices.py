# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
# Find index of all the newlines in a string
#
# data:         The string we are searching for newlines
# newline_list: The return newline_list is the list of indices in data
import re
def newline_indices(data) :
    pattern_newline  = re.compile( r'\n')
    newline_itr      = pattern_newline.finditer(data)
    newline_list     = list()
    for itr in newline_itr :
        next_index = itr.start()
        newline_list.append( next_index )
    return newline_list
