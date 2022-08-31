# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
import xrst
#
# Convert start,  stop text for a literal command to start, stop line numbers.
#
# page_name:
# is the name of the page where the xrst_literal command appears.
#
# file_cmd:
# is the name of the file where the xrst_literal command appears.
#
# display_file:
# is the name of the file that we are displaying. If it is not the same as
# file_cmd, then it must have appeared in the xrst_literal command.
#
# cmd_line:
# If file_cmd is equal to display_file, the page of the file between
# between line numbers cmd_line[0] and cmd_line[1] inclusive
# are in the xrst_literal command and are excluded from the search.
#
# start_text:
# is the starting text. There must be one and only one copy of this text in the
# file (not counting the excluded text). This text has no newlines and cannot
# be empty.  If not, an the error is reported and the program stops.
#
# stop_text:
# is the stopping text. There must be one and only one copy of this text in the
# file (not counting the excluded text). This text has no newlines and cannot
# be empty.  Furthermore, the stopping text must come after the end of the
# starting text. If not, an the error is reported and the program stops.
#
# start_line:
# The first element of the return start_line is the line number where
# start_text appears.
#
# stop_line:
# The second element of the return stop_line is the line number where
# stop_text appears.
#
# start_line, stop_line =
def start_stop_file(
   page_name = None,
   file_cmd     = None,
   display_file  = None,
   cmd_line     = None,
   start_text   = None,
   stop_text    = None
) :
   assert type(page_name) == str
   assert type(file_cmd) == str
   assert type(display_file) == str
   assert type(cmd_line[0]) == int
   assert type(cmd_line[1]) == int
   assert type(start_text) == str
   assert type(stop_text) == str
   #
   assert cmd_line[0] <= cmd_line[1]
   #
   # exclude_line
   if file_cmd == display_file :
      exclude_line = cmd_line
   else :
      exclude_line = (0, 0)
   #
   # msg
   msg  = f'in literal command:'
   #
   if start_text == '' :
      msg += ' start is empty'
      xrst.system_exit(msg,
         file_name=file_cmd, page_name=page_name, line = cmd_line[0]
      )
   if stop_text == '' :
      msg += ' stop is empty'
      xrst.system_exit(msg,
         file_name=file_cmd, page_name=page_name, line = cmd_line[0]
      )
   if 0 <= start_text.find('\n') :
      msg += ' a newline appears in start'
      xrst.system_exit(msg,
         file_name=file_cmd, page_name=page_name, line = cmd_line[0]
      )
   if 0 <= stop_text.find('\n') :
      msg += ' a newline appears in stop'
      xrst.system_exit(msg,
         file_name=file_cmd, page_name=page_name, line = cmd_line[0]
      )
   #
   # data
   file_ptr  = open(display_file, 'r')
   data      = file_ptr.read()
   file_ptr.close()
   #
   # start_line
   start_index = data.find(start_text)
   count = 0
   while 0 <= start_index :
      line = data[: start_index].count('\n') + 1
      if  line < exclude_line[0] or exclude_line[1] < line :
         start_line = line
         count      = count + 1
      start_index = data.find(start_text, start_index + len(start_text) )
   if count != 1 :
      msg += f'\nstart = "{start_text}"'
      msg += f'\nfile  =  {display_file}'
      msg += f'\nfound {count} matches expected 1'
      if file_cmd == display_file :
         msg += ' not counting the literal command'
      xrst.system_exit(msg,
         file_name=file_cmd, page_name=page_name, line = cmd_line[0]
      )
   #
   # stop_line
   stop_index = data.find(stop_text)
   count = 0
   while 0 <= stop_index :
      line = data[: stop_index].count('\n') + 1
      if  line < exclude_line[0] or exclude_line[1] < line :
         stop_line = line
         count     = count + 1
      stop_index = data.find(stop_text, stop_index + len(stop_text) )
   if count != 1 :
      msg += f'\nstop = "{stop_text}"'
      msg += f'\nfile =  {display_file}'
      msg += f'\nfound {count} matches expected 1'
      if file_cmd == display_file :
         msg += ' not counting the literal command'
      xrst.system_exit(msg,
         file_name=file_cmd, page_name=page_name, line = cmd_line[0]
      )
   #
   return start_line, stop_line
