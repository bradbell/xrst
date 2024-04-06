# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-24 Bradley M. Bell
# ----------------------------------------------------------------------------
r"""
{xrst_begin template_cmd user}

Template Command
################

Syntax
******
| ``\{xrst_template`` *separator*
| |tab| *template_file*
| |tab| *match_1* *separator* *replace_1*
| |tab| *match_2* *separator* *replace_2*
| |tab| ...
| ``}``

Input File
**********
During the expansion of a template command,
the current input file is its *template_file* .
Otherwise, the current input file is the current :ref:`begin_cmd@Page File` .

Rst Include
***********
A similar sphinx include directive, in the context of xrst, is:

| |tab| .. include \{xrst_dir *file_name* }

see :ref:`dir_cmd-name` .
The template command differs form the include directive in the following ways:

#. The template command allows for text replacement
   during the include so that *template_file* is like function or macro.

#. It also allows for conditional incuding of sections of the template file
   (when combined with the :ref:`suspend_cmd@boolean` argument in the
   suspend command).

#. Errors and warnings in a template expansion will include both
   the line in the template file and the line where it is used.
   Errors and warnings in a sphinx include only report the
   line number in the include file.

#. xrst commands in *template_file* ( *file_name* )
   will get interpreted (will not get interpreted).

White Space
***********
The newline character separates the lines of input above
and excluded from white space in the discussion below..

separator
*********
The *separator* argument is a single character that separates
matches from their replacements.
Leading and trailing white space around *separator* is ignored.

template_file
*************
is the name of the template file.
Leading and trailing white space around *template_file* is ignored
and *template_file* cannot contain the ``@`` character.
It is different for a normal xrst input file because it cannot have
any of the following xrst commands in a template expansion:

:ref:`begin or end <begin_cmd-name>` ,
:ref:`comment character <comment_ch_cmd-name>` ,
:ref:`indent<indent_cmd-name>` ,
:ref:`spell<spell_cmd-name>` ,
:ref:`template <template_cmd-name>` .

match
*****
Each occurrence of a match in the template file gets replaced.
Leading and trailing white space around *match* is ignored.

replace
*******
For each match, the corresponding replacement is used in its place.
Leading and trailing white space around *replace* is ignored.

Command End
***********
The first occurrence of a right brace ``}`` ,
directly after a newline ,
terminates the template command.

Example
*******
:ref:`template_example-name`

{xrst_end template_cmd}
"""
# ----------------------------------------------------------------------------
import os
import re
import xrst
#
#
# pattern_template:
# 1: character preceeding the template command
# 2. the separator (including surrounding white space)
# 3. line number where the template command appeared
# 4. rest of template command
pattern_template    = re.compile(
   r'([^\\]){xrst_template([^\n}]*)@xrst_line ([0-9]+)@\n([^}]*)}'
)
# pattern_arg
pattern_arg       = re.compile( r'([^\n]*)@xrst_line ([0-9]+)@\n|\n' )
# ----------------------------------------------------------------------------
# {xrst_begin template_cmd_dev dev}
# {xrst_comment_ch #}
#
# Expand the template commands in a page
# ######################################
#
# Prototype
# *********
# {xrst_literal ,
#    # BEGIN_DEF, # END_DEF
#    # BEGIN_RETURN, # END_RETURN
# }
#
# Restrictions
# ************
# The template expansion must come before processing any other commands
# except for the following:
# begin, end, comment_ch, indent, suspend, resume, spell, template.
#
# data_in
# *******
# is the data for a page before the
# :ref:`template commands <template_cmd-name>` have been expanded.
#
# page_file
# *********
# is the name of the file, for this page, where the begin command appears.
# This is used for error reporting .
#
# page_name
# *********
# is the name of the page that this data is in. This is only used
# for error reporting.
#
# data_out
# ********
# Each xrst template command is expanded and
# xrst.add_line_numbers is used to add line numbers corresponding to the
# template file.
# In addition, the following text is added at the beginning and end of the
# expansion:
#
# | |tab| @ ``\{xrst_template_begin`` @ *template_file* @ *page_line* @ ``}`` @
# | |tab| @ ``\{xrst_template_end}`` @
#
# where *page_line* is the line where the line number in *page_file*
# where the template command appeared. There is no white space between
# the tokens above.
#
#
# {xrst_end template_cmd_dev}
# BEGIN_DEF
def template_command(data_in, page_file, page_name) :
   assert type(data_in) == str
   assert type(page_file) == str
   assert type(page_name) == str
   # END_DEF
   #
   # data_out
   data_out = data_in
   #
   # m_template
   m_template  = pattern_template.search(data_out , 0)
   while m_template != None :
      #
      # separator
      separator = m_template.group(2).strip()
      if len(separator) != 1 :
         msg  =  '{xrst_template separator\n'
         msg += f'separator = "{separator}" must be one character'
         xrst.system_exit(
            msg,
            file_name = page_file,
            page_name = page_name,
            m_obj     = m_template,
            data      = data_out
         )
      #
      # arg_text
      # rest of template command
      arg_text = m_template.group(4)
      #
      # template_file, template_file_line
      template_file = ''
      m_arg         = pattern_arg.search(arg_text)
      if m_arg != None :
         template_file =  m_arg.group(1).strip()
      if template_file == '' :
         msg = 'template command: the template_file is missing.'
         xrst.system_exit(
            msg,
            file_name = page_file,
            page_name = page_name,
            m_obj     = m_arg,
            data      = arg_text
         )
      if 0 < template_file.find('@')  :
         msg = 'template command: template_file contains the @ character.'
         xrst.system_exit(
            msg,
            file_name = page_file,
            page_name = page_name,
            m_obj     = m_arg,
            data      = arg_text
         )
      template_file_line = m_arg.group(2)
      #
      # substitute_list
      substitute_list = list()
      #
      # m_arg
      m_arg = pattern_arg.search(arg_text, m_arg.end())
      while m_arg != None :
         arg = m_arg.group(1).split(separator)
         if len( arg ) != 2 :
            msg  =  f'xrst_template separator = {separator}\n'
            msg += 'separator must appear once, and only once, in each line '
            msg += 'below the template file line.'
            xrst.system_exit(
               msg,
               file_name = page_file,
               page_name = page_name,
               m_obj     = m_arg,
               data      = m_arg.group(0)
            )
         #
         # substitute_list
         match   = arg[0].strip()
         replace = arg[1].strip()
         line    = m_arg.group(2)
         substitute_list.append( (match, replace, line) )
         #
         # m_arg
         m_arg = pattern_arg.search(arg_text, m_arg.end())
      #
      # template_data
      if not os.path.isfile(template_file) :
         msg  = 'template command can not find the template file:\n'
         msg += f'template file name = {template_file}'
         #
         # template command cannot be inside a template file so we can use
         # line number to report the error.
         xrst.system_exit(msg,
            file_name = page_file,
            page_name = page_name,
            line      = template_file_line,
         )
      file_obj       = open(template_file, 'r')
      template_data  = file_obj.read()
      file_obj.close()
      #
      # template_expansion
      template_expansion = template_data
      for match, replace, line in substitute_list :
         #
         index = template_expansion.find(match)
         if index == -1 :
            msg  = 'template_command: This match did not appear in template'
            msg += f'\nmatch = {match}'
            xrst.system_exit(msg,
               file_name = page_file,
               page_name = page_name,
               line      = line
            )
         template_expansion = template_expansion.replace(match, replace)
      #
      # template_expansion
      # no newlines in before of after so that add_line_numbers works properly
      line    = m_template.group(3).strip()
      before  = '@{xrst_template_begin@'
      before += template_file + '@'
      before += line + '@'
      before += '}@'
      after   = '@{xrst_template_end}@'
      assert xrst.pattern['template_begin'].match(before) != None
      assert xrst.pattern['template_end'].match(after) != None
      template_expansion = before + template_expansion + after
      #
      # template_expansion
      template_expansion = xrst.add_line_numbers(template_expansion, page_file)
      #
      # template_expansion
      for cmd in [
         'begin',
         'end',
         'comment_ch',
         'indent',
         'spell',
         'template'
      ] :
         pattern = r'[^\\]{xrst_' + cmd + r'[^a-zA-Z_]'
         m_obj   = re.search(pattern, template_expansion)
         if m_obj != None :
            msg  = f'found {cmd} command in template expansion'
            xrst.system_exit(msg,
               file_name = page_file,
               page_name = page_name,
               m_obj     = m_obj,
               data      = template_expansion
            )
      #
      # data_done, data_out
      data_done = data_out[: m_template.start() + 1] + template_expansion
      data_out  = data_done + data_out[m_template.end() :]
      #
      # m_template
      m_template  = pattern_template.search(data_out , len(data_done))
   #
   # suspend_command
   # need to run this for suspends in the template expansions
   data_out = xrst.suspend_command(data_out, page_file, page_name)
   #
   # BEGIN_RETURN
   assert type(data_out) == str
   return data_out
   # END_RETURN
