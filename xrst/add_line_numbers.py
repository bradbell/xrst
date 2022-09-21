# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
import re
import xrst
#
# pattern
pattern = re.compile( r'^\n[ \t]*' )
#
# {xrst_begin add_line_numbers dev}
# {xrst_spell
#     newlines
# }
# {xrst_comment_ch #}
#
# Add Line Numbers to File Data
# #############################
# Add line numbers to a string in a way that is useful for reporting errors
# (for modified versions of string) using line number in the original string.
#
# data_in
# *******
# The original string.  An empty line is a line with just spaces or tabs.
# line_number is the number of newlines before a line plus one; i.e.,
# the first line is number one.
#
# data_out
# ********
# The return data_out is a modified version of data_in. The text
#
#  | ``\{xrst_line`` *line_number@*
#
# is added at the end of each non-empty line.
# Spaces and tabs in empty lines are removed (so they are truely empty).
#
# {xrst_code py}
# data_out =
def add_line_numbers(data_in) :
   assert type(data_in) == str
   # assert type(data_out) == str
   # {xrst_code}
   # {xrst_end add_line_numbers}
   #
   # newline_list, line_start
   newline_list = xrst.newline_indices(data_in)
   if newline_list[0] == 0 :
      line_start = 2
      newline_list .pop(0)
   else :
      line_start = 1
   #
   # data_out, previous
   data_out     = ""
   previous     = 0
   #
   for i in range( len(newline_list) ) :
      #
      # current
      current = newline_list[i]
      assert previous < current
      #
      # line
      line = data_in[previous : current]
      #
      # empty_line
      if previous == 0 :
         m_obj = pattern.search( '\n' + line )
         empty_line = m_obj.end() == len(line) + 1
      else :
         m_obj = pattern.search( line )
         empty_line = m_obj.end() == len(line)
      #
      # line
      if empty_line :
         line = '\n'
      else :
         line += '{xrst_line ' + str(i + line_start) + '@'
      #
      # data_out, previous
      data_out  += line
      previous = current
   #
   # data_out
   assert previous == len(data_in) - 1
   data_out += '\n'
   #
   return data_out
