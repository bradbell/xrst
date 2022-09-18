# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
import re
import xrst
pattern_indent = re.compile( r'\n[ \t]*' )
#
# Check that some lines of input data has a specific indentation.
# (Exit with an error message if not.)
#
# page_name:
# is the name of this page (used for error reporting)
#
# file_name:
# is the name of the original input file that data appears in
# (used for error reporting).
#
# page_name:
# is the name of the current page (used for error reporting)
#
# command_name:
# is the name of the xrst comand this data is for
# (used for error reporting).
#
# data:
# is that data that is checked for this indentation.
# This must start with a newline.
#
# indent:
# is the indentation that is expected a the beginning of each line of data.
# All of its characters are spaces or tabs.
def check_indent(file_name, page_name, command_name, data, indent) :
   assert type(file_name) == str
   assert type(page_name) == str
   assert type(command_name) == str
   assert type(data) == str
   assert type(indent) == str
   assert data[0] == '\n'
   #
   # indent
   assert '\n' not in indent
   indent = '\n' + indent
   #
   # first_line
   m_line = xrst.pattern['line'].search(data)
   line_before_data = None
   if m_line :
      line              = int( m_line.group(1) )
      line_before_data = line - data[: m_line.start() ].count('\n')
   #
   # m_indent
   m_indent = pattern_indent.search(data)
   while m_indent :
      #
      # start
      start = m_indent.start()
      #
      # white_space
      white_space = m_indent.group(0)
      #
      # line
      end = data.find('\n', start + 1)
      if end < 0 :
         end = len(data)
      line = data[start : end ]
      #
      # empty_line
      empty_line = m_indent.group(0) == line
      if not ( empty_line or white_space.startswith(indent) ) :
         indent      = indent[1:]
         white_space = white_space[1:]
         msg  = f"Expected indent  = '{indent}'\n"
         msg += f"but found indent = '{white_space}'\n"
         msg += f'in an {command_name} command'
         if line_before_data :
            line = line_before_data + data[: start].count('\n') + 1
         else :
            line = None
         xrst.system_exit(
            msg,
            file_name = file_name,
            page_name = page_name,
            line      = line,
         )
      #
      # m_indent
      m_indent = pattern_indent.search(data, m_indent.end())
   #
   return
