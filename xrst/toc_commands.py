# -----------------------------------------------------------------------------
#                      xrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xrst_begin toc_cmd user}
{xrst_spell
   toctree
}

Table of Children Commands
##########################

Syntax
******

hidden
======
| ``\{xrst_toc_hidden``
|   *file_1*
|   ...
|   *file_n*
| :code:`}`


list
====
| ``\{xrst_toc_list``
|   *file_1*
|   ...
|   *file_n*
| :code:`}`

table
=====
| ``\{xrst_toc_table``
|   *file_1*
|   ...
|   *file_n*
| :code:`}`

Table of Contents
*****************
These commands specify the section that are children
of the current section; i.e., sections that are at the
next level in the table of contents.

File Names
**********
A new line character must precede and follow each
of the file names *file_1* ... *file_n*.
Leading and trailing white space is not included in the names
The file names are  relative to the directory where
:ref:`run_xrst@root_file` is located.
This may seem verbose, but it makes it easier to write scripts
that move files and automatically change references to them.

Children
********
Each of the files may contain multiple :ref:`sections<begin_cmd@section>`.
The first of these sections may use a
:ref:`parent begin<begin_cmd@parent_section>` command.

#. The first section in a file is always a child of the
   section where the toc command appears..

#. If the first section in a file is a begin parent section,
   the other sections in the file are children of the frist section.
   Hence the other sections are grand children of the section
   where the begin toc command appears.

#. If there is no begin parent command in a file,
   all the sections in the file are children of the
   section where the toc command appears.

#. If the first section in a file is a begin parent section,
   and there is also a toc command in this section,
   links to the toc command children come first and then links to
   the children that are other sections in the same file.

Child Links
***********
#. The toc_list syntax generates links to the children that
   display the title for each section.
   The toc_table syntax generates links to the children that
   display both the section name and section tile.

#. If a section has a toc_list or toc_table command,
   links to all the children of the section are placed where the
   toc command is located.
   You can place a heading directly before the these commands
   to make the links easier to find.

#. If a section uses the hidden syntax,
   no automatic links to the children of the current section are generated.

#. If a section does not have a toc command,
   and it has a begin parent command,
   links to the children of the section are placed at the end of the section.

toctree
*******
This command replaces the sphinx ``toctree`` directive.
A ``toctree`` directive is automatically generated and includes each
section that is a child of the current section.

Example
*******
:ref:`toc_list_example`

{xrst_end toc_cmd}
"""
# ---------------------------------------------------------------------------
import os
import xrst
#
# process toc commands
#
# data_in:
# is the data for the section before the toc commands have been processed.
# Line numbers have been added to this data: see add_line_numbers.
#
# file_name:
# is the name of the file that this data comes from. This is only used
# for error reporting.
#
# section_name:
# is the name of the section that this data is in. This is only used
# for error reporting.
#
# data_out:
# The first retrun data_out is a copy of data_in with the
# toc commands replaced by  {xrst_command} where comamnd is TOC_hidden,
# TOC_list, or TOC_table depending on which command was in data_in.
# There is a newline directly before and after the {xrst_command}.
#
# file_list:
# The second return file_list is the list of files in the toc command
# (and in same order as in the toc command).
#
# child_section_list:
# Is the a list of section names corresponding to the children of the
# this section that are in the files specified by file_list.
# If a file in file_list has a begin_parent command, it only has
# one section in child_section_list for that file. Otherwise all of the
# sections in the file are in child_section_list.
#
# data_out, file_list, section_list =
def toc_commands(data_in, file_name, section_name) :
   assert type(data_in) == str
   assert type(file_name) == str
   assert type(section_name) == str
   #
   # data_out
   data_out = data_in
   #
   # file_list, file_line, section_list
   file_list    = list()
   file_line    = list()
   section_list = list()
   #
   # m_obj
   m_obj        = xrst.pattern['toc'].search(data_out)
   if m_obj is None :
      xrst.check_syntax_error(
         command_name    = 'toc',
         data            = data_out,
         file_name       = file_name,
         section_name    = section_name,
      )
      return data_out, file_list, section_list
   #
   # m_tmp
   m_tmp = xrst.pattern['toc'].search(data_out[m_obj.end() :] )
   if m_tmp is not None :
      msg = 'More than one children or toc_list command in a section.'
      xrst.system_exit(msg,
         file_name=file_name,
         section_name=section_name,
         m_obj=m_tmp,
         data=data_out[m_obj.end():]
      )
   #
   # command
   command = m_obj.group(1)
   assert command in [ 'hidden', 'list', 'table']
   #
   # preceeding_character
   preceeding_character = data_out[ m_obj.start() ]
   assert preceeding_character != '\\'
   #
   # data_out
   replace = preceeding_character + '{xrst_TOC_' + command + '}\n'
   data_out = xrst.pattern['toc'].sub(replace, data_out)
   #
   # file_list, file_line
   for child_line in m_obj.group(2).split('\n') :
      if child_line != '' :
         m_child = xrst.pattern['line'].search(child_line)
         assert m_child != None
         line_number = m_child.group(1)
         child_file  = xrst.pattern['line'].sub('', child_line).strip()
         if child_file != '' :
            file_list.append(child_file)
            file_line.append(line_number)
   #
   # section_list
   assert len(section_list) == 0
   for i in range( len(file_list) ) :
      #
      # child_file, child_line
      child_file = file_list[i]
      child_line = file_line[i]
      if not os.path.isfile(child_file) :
         msg  = 'The file ' + child_file + '\n'
         msg += 'in the ' + command + ' command does not exist'
         xrst.system_exit(msg,
            file_name=file_name, section_name=section_name, line=child_line
         )
      #
      # file_data
      # errors in the begin and end commands will be detected later
      # when this file is processed.
      file_ptr    = open(child_file, 'r')
      file_data   = file_ptr.read()
      file_ptr.close()
      file_index  = 0
      file_data   = xrst.remove_comment_ch(file_data, child_file)
      #
      # m_obj
      m_obj  = xrst.pattern['begin'].search(file_data)
      if m_obj is None :
         msg  = 'The file ' + child_file + '\n'
         msg += 'in the ' + command + ' command does not contain any '
         msg += 'begin commands.\n'
         xrst.system_exit(msg,
            file_name=file_name, section_name=section_name, line=child_line
         )
      #
      # list_children
      found_parent  = m_obj.group(2) == 'begin_parent'
      child_name    = m_obj.group(3)
      list_children = [ child_name ]
      #
      # m_obj
      m_obj = xrst.pattern['begin'].search(file_data, m_obj.end() )
      #
      while not found_parent and m_obj != None :
         is_parent = m_obj.group(2) == 'begin_parent'
         if is_parent :
            msg  = 'Found a begin_parent command that is'
            msg += ' not the first begin command in this file'
            xrst.system_exit(msg,
               file_name=child_file,
               section_name=section_name,
               m_obj=m_obj,
               data=file_data
            )
         child_name = m_obj.group(3)
         #
         # list_children
         list_children.append( child_name )
         #
         # m_obj
         m_obj   = xrst.pattern['begin'].search(file_data, m_obj.end() )
      #
      # section_list
      section_list += list_children
   #
   xrst.check_syntax_error(
      command_name    = 'toc',
      data            = data_out,
      file_name       = file_name,
      section_name    = section_name,
   )
   return data_out, file_list, section_list