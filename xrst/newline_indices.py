# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
import re
# {xrst_begin newline_indices dev}
# {xrst_spell
#  newline
#  newlines
# }
# {xrst_comment_ch #}
#
# Find index of all the newlines in a string
# ##########################################
#
# data
# ****
# The string we are searching for newlines.
#
# newline_list
# ************
# The return newline_list is the list of indices in data that
# represent all of the newlines; i.e. '\n'.
#
# {xrst_code py}
# newline_list =
def newline_indices(data) :
   assert type(data) == str
   # assert type(newline_indices) == list
   # assert type(newline_indices[i]) == int
   # {xrst_code}
   # {xrst_end newline_indices}
   pattern_newline  = re.compile( r'\n')
   newline_itr      = pattern_newline.finditer(data)
   newline_list     = list()
   for m_obj in newline_itr :
      next_index = m_obj.start()
      newline_list.append( next_index )
   return newline_list
