# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
"""
{xrst_begin begin_cmd user}
{xrst_spell
   dir
   underbar
}

Begin and End Commands
######################

Syntax
******
- ``\{xrst_begin_parent`` *page_name* *group_name* :code:`}`
- ``\{xrst_begin``        *page_name* *group_name* :code:`}`
- ``\{xrst_end``          *page_name* :code:`}`

Page
****
The start (end) of a page of the input file is indicated by a
begin (end) command.

page_name
*********
The *page_name* is a non-empty sequence of the following characters:
period ``.``, underbar ``_``, the letters a-z, and decimal digits 0-9.
The page name can not be ``index``
and it can not begin with the characters ``xrst_``.
A link is included in the index under the page name
to the first heading the page.
The page name is also added to the html keyword meta data.

group_name
**********
This is the group that this page belongs to; see
:ref:`run_xrst@group_list`.
If *group_name* is empty, this page is part of the empty group.
Note that it is the group name and not the group that is empty.

Output File
***********
The output file corresponding to *page_name* is

| |tab| *sphinx_dir*\ ``/xrst/``\ *page_name*\ ``.rst``

see :ref:`sphinx_dir<run_xrst@sphinx_dir>`

Parent Page
***********
The following conditions hold for each *group_name*:

#. There can be at most one begin parent command in an input file.
#. If there is a begin parent command, it must be the first begin command
   in the file and there must be other pages in the file.
#. The other pages are children of the parent page.
#. The parent page is a child
   of the page that included this file using a
   :ref:`toc command<toc_cmd>`.
#. If there is no begin parent command in an input file,
   all the pages in the file are children
   of the page that included this file using a
   :ref:`toc command<toc_cmd>`.

Note that there can be more than one begin parent command in a file if
they have different group names. Also note that pages are only children
of pages that have the same group name.

{xrst_end begin_cmd}
"""
# ---------------------------------------------------------------------------
import xrst
import re
pattern_group_name  = re.compile( r'[^ \t]+' )
pattern_group_valid = re.compile( r'[a-z]+' )
# ---------------------------------------------------------------------------
#
# Get all the information for a file.
#
# page_info:
# a list of the information for pages that came before this file.
# We use infor below for one eleemnt of this list:
#
#  info['page_name']
#  is an str containing the name of a seciton that came before this file.
#
# group_name:
# We are only retrieving information for pages in this group.
#
# parent_file:
# name of the file that included file_in.
#
# file_in:
# is the name of the file we are getting all the information for.
#
# file_info:
# The value file_info is a list of dict. Each dict contains the information
# for one page in this file. We use info below for one element of the list:
#
#  info['page_name']:
#  is an str containing the name of a seciton in this file.
#
#  info['page_data']:
#  is an str containing the data for this seciton.
#  1. Line numbers have been added using add_line_numbers.
#  2. If present in this file, the comment character and possilbe space
#      after have been removed.
#  3. The begin and end commands are not include in this data.
#  4. The first (last) line number corresponds to the begin (end) command
#  5. The suspend / resume comands and data between such pairs
#      have been removed.
#  6. If there is a common indentation for the entire page,
#      it is removed.
#
#  info['is_parent']:
#  is true (false) if this is (is not) the parent page for the other
#  pages in this file. The parent page must be the first, and hence
#  have index zero in file_info. In addition, if there is a parent page,
#  there must be at least one other page; i.e., len(file_info) >= 2.
#
#  info['is_child']:
#  is true (false) if this is (is not) a child of the first page in
#  this file.
#
# file_info =
def get_file_info(
      page_info,
      group_name,
      parent_file,
      file_in,
) :
   assert type(page_info) == list
   assert type(group_name) == str
   assert type(file_in) == str
   #
   # file_data
   file_ptr   = open(file_in, 'r')
   file_data  = file_ptr.read()
   file_ptr.close()
   #
   # file_data
   file_data = xrst.add_line_numbers(file_data)
   #
   # comment_ch
   comment_ch = xrst.get_comment_ch(file_data, file_in)
   #
   # file_info
   file_info = list()
   #
   # parent_page_name
   parent_page_name = None
   #
   # data_index
   # index to start search for next pattern in file_data
   data_index  = 0
   #
   # found_group_name
   found_group_name = False
   #
   # for each page in this file
   while data_index < len(file_data) :
      #
      # m_begin
      m_begin = xrst.pattern['begin'].search(file_data, data_index)
      #
      # this_group_name
      if m_begin != None :
         #
         this_group_name = m_begin.group(4)
         m_group         = pattern_group_name.search(this_group_name)
         if m_group == None :
            this_group_name = ''
         else :
            this_group_name = m_group.group(0)
            m_group    = pattern_group_valid.search(this_group_name)
            if this_group_name != m_group.group(0) :
               msg = f'"{this_group_name}" is not a valid group name'
               xrst.system_exit(msg,
                  file_name = file_in,
                  m_obj     = m_begin,
                  data      = file_data,
               )
      if m_begin == None :
         if not found_group_name :
            msg  = 'can not find a begin command with \n'
            if group_name == '' :
               msg += 'the empty group name and '
            else :
               msg += f'group_name = {group_name} and '
            msg += f'parent file = {parent_file}'
            xrst.system_exit(msg, file_name=file_in)
         #
         # data_index
         # set so that the page loop for this file terminates
         data_index = len(file_data)
      elif this_group_name != group_name :
         #
         # data_index
         # place to start search for next page
         data_index = m_begin.end()
      else :
         #
         # found_group_name
         found_group_name = True
         #
         # page_name, is_parent
         page_name = m_begin.group(3)
         is_parent = m_begin.group(2) == 'begin_parent'
         #
         # check_page_name
         xrst.check_page_name(
            page_name,
            file_name     = file_in,
            m_obj         = m_begin,
            data          = file_data
         )
         #
         # check if page_name appears multiple times in this file
         for info in file_info :
            if page_name == info['page_name'] :
               msg  = 'xrst_begin: page appears multiple times'
               xrst.system_exit(msg,
                  file_name      = file_in,
                  page_name   = page_name,
                  m_obj          = m_begin,
                  data           = file_data
               )
         #
         # check if page_name appears in another file
         for info in page_info :
            if page_name == info['page_name'] :
               msg  = f'page_name = "{page_name}", '
               msg += f'group_name = {group_name} appears twice\n'
               msg += 'Once  in file ' + file_in + '\n'
               msg += 'Again in file ' + info['file_in'] + '\n'
               xrst.system_exit(msg)
         #
         # check if parent pages is the first seciton in this file
         if is_parent :
            if len(file_info) != 0 :
               msg  = 'xrst_begin_parent'
               msg += ' is not the first begin command in this file'
               xrst.system_exit(msg,
                  file_name     = file_in,
                  page_name  = page_name,
                  m_obj         = m_begin,
                  data          = file_data
               )
            #
            # parent_page_name
            parent_page_name = page_name
         #
         # is_child
         is_child = (not is_parent) and (parent_page_name != None)
         #
         # data_index
         data_index = m_begin.end()
         #
         # m_end
         m_end     = xrst.pattern['end'].search(file_data, data_index)
         #
         if m_end == None :
            msg  = 'Expected the followig text at start of a line:\n'
            msg += '    {xrst_end page_name}'
            xrst.system_exit(
               msg, file_name=file_in, page_name=page_name
            )
         if m_end.group(1) != page_name :
            msg = 'begin and end page names do not match\n'
            msg += 'begin name = ' + page_name + '\n'
            msg += 'end name   = ' + m_end.group(1)
            xrst.system_exit(msg,
               file_name = file_in,
               m_obj     = m_end,
               data      = file_data
            )
         #
         # page_data
         page_start = data_index
         page_end   = m_end.start() + 1
         page_data  = file_data[ page_start : page_end ]
         #
         # page_data
         # order of these operations is important
         page_data  = xrst.suspend_command(
            page_data, file_in, page_name
         )
         page_data, indent = xrst.remove_indent(
            page_data, file_in, page_name
         )
         if comment_ch :
            data_before = file_data[: m_begin.start()]
            index       = data_before.rfind('\n')
            if data_before.find(comment_ch, index) < 0 :
               line = data_before.count('\n') + 1
               msg  = f'In line {line} in file {file_in}\n'
               msg += 'This line does not contain the comment character '
               msg += comment_ch + '\n'
               msg += 'before the begin command in that line.'
               xrst.system_exit(msg,
                  file_name = file_in,
                  line      = line,
               )
            #
            pattern_ch  = re.compile( r'\n[' + comment_ch + r'] ?' )
            page_data   = pattern_ch.sub(r'\n', page_data)
         #
         # file_info
         file_info.append( {
            'page_name' : page_name,
            'page_data' : page_data,
            'is_parent'    : is_parent,
            'is_child'     : is_child,
         } )
         #
         # data_index
         # place to start search for next page
         data_index = m_end.end()
   #
   if parent_page_name != None and len(file_info) < 2 :
      msg  = 'begin_parent command appears with '
      if group_name == '' :
         msg += 'the empty group name\n'
      else :
         msg += f'group_name = {group_name}\n'
      msg += 'and this file only has one page with that group name.'
      xrst.system_exit(
         msg, file_name=file_in, page_name=parent_page_name
      )
   #
   # file_data
   file_data = xrst.pattern['begin'].sub('', file_data)
   file_data = xrst.pattern['end'].sub('', file_data)
   #
   for command_name in [ 'begin' , 'end' ] :
      xrst.check_syntax_error(
         command_name   = command_name,
         data           = file_data,
         file_name      = file_in,
         page_name   = None,
      )
   #
   return file_info
