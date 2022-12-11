# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
import xrst
# {xrst_begin start_stop_file dev}
# {xrst_spell
#     cmd
#     newlines
# }
# {xrst_comment_ch #}
#
# Convert literal command start, stop from text to line numbers
# #############################################################
#
# Arguments
# *********
#
# file_cmd
# ========
# is the name of the file where the xrst_literal command appears.
#
# page_name
# =========
# is the name of the page where the xrst_literal command appears.
#
# display_file
# ============
# is the name of the file that we are displaying. If it is not the same as
# file_cmd, then it must have appeared in the xrst_literal command.
#
# cmd_line
# ========
# If file_cmd is equal to display_file, the lines of the file
# between line numbers cmd_line[0] and cmd_line[1] inclusive
# are in the xrst_literal command and are excluded from the search.
#
# start_text
# ==========
# is the starting text. There must be one and only one copy of this text in the
# file (not counting the excluded text). This text has no newlines and cannot
# be empty.  If not, an the error is reported and the program stops.
#
# stop_text
# =========
# is the stopping text. There must be one and only one copy of this text in the
# file (not counting the excluded text). This text has no newlines and cannot
# be empty.  Furthermore, the stopping text must come after the end of the
# starting text. If not, an the error is reported and the program stops.
#
# Returns
# *******
#
# start_line
# ==========
# is the line number where start_text appears.
#
# stop_line
# =========
# is the line number where stop_text appears.
#
# {xrst_code py}
def start_stop_file(
   file_cmd,
   page_name,
   display_file,
   cmd_line,
   start_text,
   stop_text
) :
   assert type(file_cmd) == str
   assert type(page_name) == str
   assert type(display_file) == str
   assert type(cmd_line[0]) == int
   assert type(cmd_line[1]) == int
   assert cmd_line[0] <= cmd_line[1]
   assert type(start_text) == str
   assert type(stop_text) == str
   # {xrst_code}
   # {xrst_literal
   #  BEGIN_return
   #  END_return
   # }
   # {xrst_end start_stop_file}
   # ------------------------------------------------------------------------
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
   file_obj  = open(display_file, 'r')
   data      = file_obj.read()
   file_obj.close()
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
      msg += f'\nstart         = "{start_text}"'
      msg += f'\ndisplay_file  =  {display_file}'
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
      msg += f'\nstop         = "{stop_text}"'
      msg += f'\ndisplay_file =  {display_file}'
      msg += f'\nfound {count} matches expected 1'
      if file_cmd == display_file :
         msg += ' not counting the literal command'
      xrst.system_exit(msg,
         file_name=file_cmd, page_name=page_name, line = cmd_line[0]
      )
   # ------------------------------------------------------------------------
   # BEGIN_return
   assert type(start_line) == int
   assert type(stop_line) == int
   #
   return start_line, stop_line
   # END_return
