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
| |tab| *pattern_1* *separator* *replace_1*
| |tab| *pattern_2* *separator* *replace_2*
| |tab| ...
| ``}``

Purpose
*******
The template command enables use one xrst input file in multiple pages.

Rst Include
***********
The template command is different from the sphinx include directive

| |tab| .. include \{xrst_dir *file_name* }

see :ref:`dir_cmd-name` .
To be specific, xrst commands in *template_file* ( *file_name* )
will get interpreted (will not get interpreted).
In addition, the xrst template command allows for text replacement
during the include.

White Space
***********
The newline character separates the lines of input above.
Other leading and trailing white space around
*separator* , *template_file* , the patterns , and the replacements
are ignored.

separator
*********
The *separator* argument is a single character that separates
patterns from their replacements.

template_file
*************
Is the name of the template file.
It is different for a normal xrst input file because it cannot have
any of the following xrst commands (after the template expansion):
:ref:`begin or end <begin_cmd-name>` ,
:ref:`comment character <comment_ch_cmd-name>` ,
:ref:`indent<indent_cmd-name>` ,
:ref:`suspend, resume <suspend_cmd-name>` ,
:ref:`spell<spell_cmd-name>` ,
:ref:`template command <template_cmd-name>` .

pattern
*******
Each pattern is a python regular expression that is used
to match text in the template file.

replace
*******
Each replacement is a python replacement string.
The replacements are done in order using the python regular expression
function:

   ``re.sub`` ( *pattern* , *replace* )

Command End
***********
The first occurrence of a right brace ``}`` ,
directly after a newline ,
terminates the template command.

Example
*******
{xrst_comment :ref:`template_example-name` }

{xrst_end template_cmd}
"""
# ----------------------------------------------------------------------------
import os
import re
import xrst
#
#
# template_pattern
# 0. preceding character + the command.
# 1. characters, not including line number or command name, on first line.
# 2. rest of command, not including first \\n or final }.
pattern_template    = re.compile(
   r'[^\\]\{xrst_template([^\n}]*)@xrst_line [0-9]+@\n([^}]*)}'
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
# file_name
# *********
# is the name of the file that this data comes from. This is used
# for error reporting and for the display file (when the display file
# is not included in the command).
#
# page_name
# *********
# is the name of the page that this data is in. This is only used
# for error reporting.
#
# data_out
# ********
# Each xrst template command is expanded.
#
# {xrst_end template_cmd_dev}
# BEGIN_DEF
def template_command(data_in, file_name, page_name) :
   assert type(data_in) == str
   assert type(file_name) == str
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
      separator = m_template.group(1).strip()
      if len(separator) != 1 :
         msg  =  '{xrst_template separator\n'
         msg += f'separator = "{separator}" must be one character'
         xrst.system_exit(
            msg,
            file_name = file_name,
            page_name = page_name,
            m_obj     = m_template,
            data      = data_out
         )
      #
      # arg_text
      arg_text = m_template.group(2)
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
            file_name = file_name,
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
               file_name = file_name,
               page_name = page_name,
               m_obj     = m_arg,
               data      = m_arg.group(0)
            )
         #
         # substitute_list
         pattern = arg[0].strip()
         replace = arg[1].strip()
         line    = m_arg.group(2)
         substitute_list.append( (pattern, replace, line) )
         #
         # m_arg
         m_arg = pattern_arg.search(arg_text, m_arg.end())
      #
      # template_data
      if not os.path.isfile(template_file) :
         msg  = 'template command: can not find the template file.\n'
         msg += f'template file name = {template_file}'
         xrst.system_exit(msg,
            file_name = file_name,
            page_name = page_name,
            line      = template_list
         )
      file_obj       = open(template_file, 'r')
      template_data  = file_obj.read()
      file_obj.close()
      #
      # template_expansion
      template_expansion = template_data
      for pattern, replace, line in substitute_list :
         #
         try :
            m_obj = re.search(pattern, template_expansion)
            if m_obj == None :
               msg  = 'template_command: This pattern did not match any text'
               msg += f'\npattern = {pattern}'
               xrst.system_exit(msg,
                  file_name = file_name,
                  page_name = page_name,
                  line      = line
               )
            template_expansion = re.sub(pattern, replace, template_expansion)
         except Exception as error :
            msg = str(error)
            xrst.system_exit(msg,
               file_name = file_name,
               page_name = page_name,
               line      = line
            )
      #
      # template_expansion
      for cmd in [
         'begin',
         'end',
         'comment_ch',
         'suspend',
         'indent',
         'resume',
         'spell',
         'template'
      ] :
         pattern = r'[^\\]{xrst_' + cmd
         m_obj   = re.search(pattern, template_expansion)
         if m_obj != None :
            msg  = f'found {cmd} command in template expansion ='
            breakpoint()
            xrst.system_exit(msg,
               file_name = file_name,
               page_name = page_name,
               m_obj     = m_template,
               data      = data_out
            )
      #
      # template_expansion
      template_expansion = xrst.add_line_numbers(template_expansion, file_name)
      #
      # data_done, data_out
      data_done = data_out[: m_template.start()] + template_expansion
      data_out  = data_done + data_out[m_template.end() :]
      #
      # m_template
      m_template  = pattern_template.search(data_out , len(data_done))
   #
   # BEGIN_RETURN
   assert type(data_out) == str
   return data_out
   # END_RETURN
