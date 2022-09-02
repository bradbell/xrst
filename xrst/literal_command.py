# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
"""
{xrst_begin literal_cmd user}

Literal Command
###############

Syntax
******

| ``\{xrst_literal}``
|
| ``\{xrst_literal``
| |tab| *display_file*
| :code:`}`
|
| ``\{xrst_literal``
| |tab| *start*
| |tab| *stop*
| :code:`}`
|
| ``\{xrst_literal``
| |tab| *display_file*
| |tab| *start*
| |tab| *stop*
| :code:`}`

Purpose
*******
A code block, from any where in any file,
can be included by the command above.

White Space
***********
Leading and trailing white space is not included in
*start*, *stop* or *display_file*.
The new line character separates these tokens.
The line containing the ``}`` must have nothing but white space after it.

display_file
************
If *display_file* is not in the syntax,
the code block is in the current input file.
Otherwise, the code block is in *display_file*.
The file name *display_file* is relative to the directory
where the :ref:`run_xrst@root_file` is located.
This may seem verbose, but it makes it easier to write scripts
that move files and automatically change references to them.

No start or stop
****************
In the case where there is no *start* or *stop*,
the entire display file is displayed.
In the case of the ``\{xrst_literal}`` syntax,
the entire current input file is displayed.

start
*****
The code block starts with the line following the occurrence
of the text *start* in *display_file*.
If this is the same as the file containing the command,
the text *start* will not match any text in the command.
There must be one and only one occurrence of *start* in *display_file*,
not counting the command itself when the files are the same.

stop
****
The code block ends with the line before the occurrence
of the text *start* in *display_file*.
If this is the same as the file containing the command,
the text *stop* will not match any text in the command.
There must be one and only one occurrence of *stop* in *display_file*,
not counting the command itself when the files are the same.

Spell Checking
**************
Spell checking is **not** done for these code blocks.


Example
*******
see :ref:`literal_example` .

{xrst_end literal_cmd}
"""
# ----------------------------------------------------------------------------
import os
import re
import xrst
#
# ----------------------------------------------------------------------------
def file_extension(display_file) :
   index = display_file.rfind('.')
   extension = ''
   if 0 <= index and index + 1 < len(display_file) :
      extension = display_file[index + 1 :]
      if extension == 'xrst' :
         extension = 'rst'
      elif extension == 'hpp' :
         extension = 'cpp' # pygments does not recognize hpp ?
   return extension
# ----------------------------------------------------------------------------
#
# Process the literal commands in a page.
#
# data_in:
# is the data for a page before the literal commands have been removed.
#
# file_name:
# is the name of the file that this data comes from. This is used
# for error reporting and for the display file (when the display file
# is not incuded in the command).
#
# page_name:
# is the name of the page that this data is in. This is only used
# for error reporting.
#
# rst_dir:
# is the directory, relative to the current working directory,
# where xrst will place the final rst files.
#
# data_out:
# Each xrst literal command is convertd to its corresponding sphinx commands.
#
# data_out =
def literal_command(data_in, file_name, page_name, rst_dir) :
   assert type(data_in) == str
   assert type(file_name) == str
   assert type(page_name) == str
   assert type(rst_dir) == str
   #
   assert xrst.pattern['literal_0'].groups == 1
   assert xrst.pattern['literal_1'].groups == 4
   assert xrst.pattern['literal_2'].groups == 6
   assert xrst.pattern['literal_3'].groups == 8
   #
   # work_dir
   depth    = rst_dir.count('/') + 1
   work_dir = depth * '../'
   #
   # data_out
   data_out = data_in
   #
   # key
   for key in [ 'literal_0', 'literal_1' ] :
      #
      # m_file
      m_file  = xrst.pattern[key].search(data_out)
      while m_file != None :
         #
         # display_file
         if key == 'literal_0' :
            display_file = file_name
         else :
            display_file = m_file.group(2).strip()
            if not os.path.isfile(display_file) :
               msg  = 'literal command: can not find the display_file.\n'
               msg += f'display_file = {display_file}'
               xrst.system_exit(msg,
                  file_name    = file_name,
                  page_name = page_name,
                  m_obj        = m_file,
                  data         = data_out
               )
            if os.path.samefile(display_file, file_name) :
               display_file = file_name
         #
         # cmd
         cmd       = f'.. literalinclude:: {work_dir}{display_file}\n'
         extension = file_extension( display_file )
         if extension != '' :
            cmd += 3 * ' ' + f':language: {extension}\n'
         cmd = '\n' + cmd + '\n'
         if data_out[m_file.start() ] != '\n' :
            cmd = '\n' + cmd
         #
         # data_out
         data_tmp  = data_out[: m_file.start() + 1 ]
         data_tmp += cmd
         data_tmp += data_out[ m_file.end() : ]
         data_out  = data_tmp
         #
         # m_file
         m_file  = xrst.pattern[key].search(data_out)
         if m_file and key == 'literal_0' :
            msg  = 'More than one {xrst_literal} command in this page.\n'
            msg += 'This command includes the entire current input file.'
            xrst.system_exit(msg,
               file_name    = file_name,
               page_name = page_name,
               m_obj        = m_file,
               data         = data_out
            )
   #
   # key
   for key in [ 'literal_2', 'literal_3' ] :
      #
      # m_file
      m_file  = xrst.pattern[key].search(data_out)
      while m_file != None :
         #
         # display_file, start_text, stop_text, display_file, cmd_line
         if key == 'literal_2' :
            display_file  = file_name
            start_text    = m_file.group(2).strip()
            stop_text     = m_file.group(4) .strip()
            cmd_stop_line = int( m_file.group(6) )
         else :
            display_file  = m_file.group(2).strip()
            start_text    = m_file.group(4).strip()
            stop_text     = m_file.group(6) .strip()
            cmd_stop_line = int( m_file.group(8) )
            if not os.path.isfile(display_file) :
               msg  = 'literal command: can not find the display_file.\n'
               msg += f'display_file = {display_file}'
               xrst.system_exit(msg,
                  file_name    = file_name,
                  page_name = page_name,
                  m_obj        = m_file,
                  data         = data_out
               )
            same_file   = os.path.samefile(display_file, file_name)
            if same_file :
               display_file = file_name
         cmd_start_line = int( m_file.group(1) )
         cmd_line       = (cmd_start_line, cmd_stop_line)
         #
         # start_line, stop_line
         start_line, stop_line = xrst.start_stop_file(
            page_name = page_name,
            file_cmd     = file_name,
            display_file = display_file,
            cmd_line     = cmd_line,
            start_text   = start_text,
            stop_text    = stop_text
         )
         #
         # locations in display_file
         start_line  = start_line + 1
         stop_line   = stop_line  - 1
         #
         # cmd
         cmd      = f'.. literalinclude:: {work_dir}{display_file}\n'
         cmd     += 3 * ' ' + f':lines: {start_line}-{stop_line}\n'
         #
         # cmd
         # Add language to literalinclude, sphinx seems to be brain
         # dead and does not do this automatically.
         extension = file_extension( display_file )
         if extension != '' :
            cmd += 3 * ' ' + f':language: {extension}\n'
         cmd = '\n' + cmd + '\n\n'
         if m_file.start() > 0 :
            if data_out[m_file.start() - 1] != '\n' :
               cmd = '\n' + cmd
         #
         # data_out
         data_tmp  = data_out[: m_file.start() + 1 ]
         data_tmp += cmd
         data_tmp += data_out[ m_file.end() : ]
         data_out  = data_tmp
         #
         # m_file
         m_file  = xrst.pattern[key].search(data_out)
         #
   #
   xrst.check_syntax_error(
      command_name    = 'literal',
      data            = data_out,
      file_name       = file_name,
      page_name    = page_name,
   )
   return data_out
