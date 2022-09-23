# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
import re
import xrst
#
#
pattern_error = re.compile( r'{xrst_line [0-9]+@[^\n]' )
# {xrst_begin remove_line_numbers dev}
# {xrst_spell
#  tuples
# }
# {xrst_comment_ch #}
#
# Remove the number numbers
# #########################
#
# Arguments
# *********
#
# data_in
# =======
# is a string with line numbers added by :ref:`add_line_numbers` .
# These have the form: ``{xrst_line`` *number* ``@`` .
#
# Returns
# *******
#
# data_out
# ========
# The return data_out is a copy of data_in with the line numbers removed.
#
# line_pair
# =========
# The second return line_pair is a list of two element tuples.
# The first element is the line number in data_out not counting the
# { ``xrst_page_number`` } lines. The second element is the corresponding
# line number (not line) that has was removed.
#
# {xrst_code py}
def remove_line_numbers(data_in) :
   assert type(data_in) == str
   # {xrst_code}
   # {xrst_literal
   #  BEGIN_return
   #  END_return
   # }
   # {xrst_end remove_line_numbers}
   #
   # m_error
   m_error = pattern_error.search(data_in)
   if m_error :
      start = max(m_error.start() - 50, 0)
      end   = min(m_error.end() + 50, len(data_in))
      msg   = 'Program error: Line number tracking is confused:\n'
      msg  += '\nText before the bad line number ='
      msg  += '\n---------------------------------\n'
      msg  +=  data_in[start : m_error.start()]
      msg  += '\nText after the bad line number ='
      msg  += '\n--------------------------------\n'
      msg  +=  data_in[m_error.end() :  end]
      xrst.system_exit(msg)
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
   for m_obj in xrst.pattern['line'].finditer(data_in) :
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
      line_out  -= before.count('{xrst_page_number}\n')

      line_pair.append( ( line_out, int(line_match) ) )
      data_out += before
      #
      previous_end = m_obj.end()
   #
   # data_out
   data_out += data_in[previous_end  :]
   #
   # BEGIN_return
   assert type(data_out) == str
   assert type(line_pair) == list
   if 0 < len(line_pair) :
      assert type(line_pair[0]) == tuple
      assert type(line_pair[0][0]) == int
      assert type(line_pair[0][1]) == int
   #
   return data_out, line_pair
   # END_return
