# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
import re
#
# Find index of all the newlines in a string
#
# data:         The string we are searching for newlines
# newline_list: The return newline_list is the list of indices in data
#
# newline_list =
def newline_indices(data) :
   pattern_newline  = re.compile( r'\n')
   newline_itr      = pattern_newline.finditer(data)
   newline_list     = list()
   for m_obj in newline_itr :
      next_index = m_obj.start()
      newline_list.append( next_index )
   return newline_list
