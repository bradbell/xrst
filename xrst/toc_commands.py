# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
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
These commands specify the page that are children
of the current page; i.e., pages that are at the
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
Each of the files may contain multiple :ref:`pages<begin_cmd@page>`.
The first of these pages may use a
:ref:`parent begin<begin_cmd@parent_page>` command.

#. The first page in a file is always a child of the
   page where the toc command appears..

#. If the first page in a file is a begin parent page,
   the other pages in the file are children of the frist page.
   Hence the other pages are grand children of the page
   where the begin toc command appears.

#. If there is no begin parent command in a file,
   all the pages in the file are children of the
   page where the toc command appears.

#. If the first page in a file is a begin parent page,
   and there is also a toc command in this page,
   links to the toc command children come first and then links to
   the children that are other pages in the same file.

Child Links
***********
#. The toc_list syntax generates links to the children that
   display the title for each page.
   The toc_table syntax generates links to the children that
   display both the page name and page tile.

#. If a page has a toc_list or toc_table command,
   links to all the children of the page are placed where the
   toc command is located.
   You can place a heading directly before the these commands
   to make the links easier to find.

#. If a page uses the hidden syntax,
   no automatic links to the children of the current page are generated.

#. If a page does not have a toc command,
   and it has a begin parent command,
   links to the children of the page are placed at the end of the page.

toctree
*******
This command replaces the sphinx ``toctree`` directive.
A ``toctree`` directive is automatically generated and includes each
page that is a child of the current page.

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
# is the data for the page before the toc commands have been processed.
# Line numbers have been added to this data: see add_line_numbers.
#
# file_name:
# is the name of the file that this data comes from. This is only used
# for error reporting.
#
# page_name:
# is the name of the page that this data is in. This is only used
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
# child_page_list:
# Is the a list of page names corresponding to the children of the
# this page that are in the files specified by file_list.
# If a file in file_list has a begin_parent command, it only has
# one page in child_page_list for that file. Otherwise all of the
# pages in the file are in child_page_list.
#
# data_out, file_list, page_list =
def toc_commands(data_in, file_name, page_name) :
   assert type(data_in) == str
   assert type(file_name) == str
   assert type(page_name) == str
   #
   # data_out
   data_out = data_in
   #
   # file_list, file_line, page_list
   file_list    = list()
   file_line    = list()
   page_list = list()
   #
   # m_obj
   m_obj        = xrst.pattern['toc'].search(data_out)
   if m_obj is None :
      xrst.check_syntax_error(
         command_name    = 'toc',
         data            = data_out,
         file_name       = file_name,
         page_name    = page_name,
      )
      return data_out, file_list, page_list
   #
   # m_tmp
   m_tmp = xrst.pattern['toc'].search(data_out[m_obj.end() :] )
   if m_tmp is not None :
      msg = 'More than one children or toc_list command in a page.'
      xrst.system_exit(msg,
         file_name=file_name,
         page_name=page_name,
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
   # page_list
   assert len(page_list) == 0
   for i in range( len(file_list) ) :
      #
      # child_file, child_line
      child_file = file_list[i]
      child_line = file_line[i]
      if not os.path.isfile(child_file) :
         msg  = 'The file ' + child_file + '\n'
         msg += 'in the ' + command + ' command does not exist'
         xrst.system_exit(msg,
            file_name=file_name, page_name=page_name, line=child_line
         )
      #
      # file_data
      # errors in the begin and end commands will be detected later
      # when this file is processed.
      file_ptr    = open(child_file, 'r')
      file_data   = file_ptr.read()
      file_ptr.close()
      file_index  = 0
      #
      # m_obj
      m_obj  = xrst.pattern['begin'].search(file_data)
      if m_obj is None :
         msg  = 'The file ' + child_file + '\n'
         msg += 'in the ' + command + ' command does not contain any '
         msg += 'begin commands.\n'
         xrst.system_exit(msg,
            file_name=file_name, page_name=page_name, line=child_line
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
               page_name=page_name,
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
      # page_list
      page_list += list_children
   #
   xrst.check_syntax_error(
      command_name    = 'toc',
      data            = data_out,
      file_name       = file_name,
      page_name    = page_name,
   )
   return data_out, file_list, page_list
