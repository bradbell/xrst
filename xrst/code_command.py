# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
"""
{xrst_begin code_cmd user}

Code Command
############

Syntax
******
- ``\{xrst_code`` *language* :code:`}`
- ``\{xrst_code}``

Purpose
*******
A code block, directly below in the current input file, begins (ends) with
a code command that contains *language* (not containing *language*).
Lines containing the code commands are not included in the rst output.
One can use these lines to end and begin comments so that the
code also executes.
If this is not useful, one can instead use a sphinx code-block directive.

Requirements
************
Each code section ends with
a line containing the second version of the command; i.e., ``\{xrst_code}``.
Hence there must be an even number of code commands.

language
********
A *language* is a non-empty sequence of lower case letters.
It determines the language for highlighting the code block.

Rest of Line
************
Other characters on the same line as a code commands
are not included in the xrst output.
This enables one to begin or end a comment block
without having the comment characters in the xrst output.

Spell Checking
**************
Code blocks as usually small and
spell checking is done for these code blocks.
(Spell checking is not done for code blocks included using the
:ref:`literal command<literal_cmd>` .)

Example
*******
:ref:`code_example`

{xrst_end code_cmd}
"""
# ----------------------------------------------------------------------------
import xrst
# {xrst_begin code_cmd_dev dev}
# {xrst_spell
#  dir
# }
# {xrst_comment_ch #}
#
# Process the xrst code commands for a page
# #########################################
#
# data_in
# *******
# is the data for the page before the
# :ref:`code commands <code_cmd>` have been processed.
#
# file_name
# *********
# is the name of the file that this data comes from. This is only used
# for error reporting.
#
# page_name
# *********
# is the name of the page that this data is in. This is only used
# for error reporting.
#
# rst_dir
# *******
# is the directory, relative to the current working directory,
# where xrst will place the final rst files.
#
# data_out
# ********
# is a copy of data_in with the xrst code commands replaced by a corresponding
# sphinx command.
#
# {xrst_code py}
# data_out =
def code_command(data_in, file_name, page_name, rst_dir) :
   assert type(data_in) == str
   assert type(file_name) == str
   assert type(page_name) == str
   assert type(rst_dir) == str
   # assert type(data_out) == str
   # {xrst_code}
   # {xrst_end code_cmd_dev}
   #
   # work_dir
   depth    = rst_dir.count('/') + 1
   work_dir = depth * '../'
   #
   # data_out
   data_out = data_in
   #
   # m_begin
   m_begin = xrst.pattern['code'].search(data_out)
   #
   if m_begin == None :
      return data_out
   #
   while m_begin != None :
      #
      # m_end
      start = m_begin.end()
      m_end = xrst.pattern['code'].search(data_out, start)
      #
      # language
      language  = m_begin.group(4).strip()
      if language == '' :
         msg = 'missing language in first command of a code block pair'
         xrst.system_exit(msg,
            file_name=file_name,
            page_name=page_name,
            m_obj=m_begin,
            data=data_out
         )
      for ch in language :
         if ch < 'a' or 'z' < ch :
            msg = 'code block language character not in a-z.'
            xrst.system_exit(msg,
               file_name=file_name,
               page_name=page_name,
               m_obj=m_begin,
               data=data_out
            )
      #
      if m_end == None :
         msg = 'Start code command does not have a corresponding stop'
         xrst.system_exit(msg,
            file_name=file_name,
            page_name=page_name,
            m_obj=m_begin,
            data=data_out
         )
      if m_end.group(4).strip() != '' :
         msg ='Stop code command has a non-empty language argument'
         xrst.system_exit(msg,
            file_name=file_name,
            page_name=page_name,
            m_obj=m_end,
            data=data_out
         )
      #
      # language
      # fix cases that pygments has trouble with ?
      if language == 'hpp' :
         language = 'cpp'
      if language == 'm' :
         language = 'matlab'
      #
      # data_before, data_after
      data_before = data_out[: m_begin.start()]
      data_after  = data_out[m_end.end() : ]
      #
      # start_line, stop_line
      assert data_out[m_begin.end()] == '\n'
      assert data_out[m_end.end()] == '\n'
      start_line = int(m_begin.group(5)) + 1
      stop_line  = int(m_end.group(5)) - 1
      #
      # cmd
      command  = f'.. literalinclude:: {work_dir}{file_name}\n'
      command += 3 * ' ' + f':lines: {start_line}-{stop_line}\n'
      command += 3 * ' ' + f':language: {language}\n'
      command = '\n' + command + '\n'
      assert data_after.startswith('\n')
      if not data_before.strip(' ').endswith('\n') :
         command = '\n' + command
      #
      # data_left, data_after
      data_left  = data_before + command
      data_out   = data_left + data_after
      #
      # m_begin
      m_begin = xrst.pattern['code'].search(data_out, len(data_left) )
   #
   # check_syntax_error
   xrst.check_syntax_error(
      command_name  = 'code',
      data          = data_out,
      file_name     = file_name,
      page_name     = page_name,
   )
   #
   return data_out
