# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
import xrst
# ----------------------------------------------------------------------------
# page_index =
def page_name2index(pinfo_list, page_name) :
   for (page_index, info) in enumerate(pinfo_list) :
      if info['page_name'] == page_name :
         return page_index
   return None

# ----------------------------------------------------------------------------
# Create the table of contents and replace the '{xrst_page_number}'
# for this page and all its child pages.
#
# tmp_dir
# is the temporary directory whre the rst files are written.
#
# target:
# is either 'html' or 'pdf'. If target is 'pdf',  in the file
# tmp_dir/page_name.rst the text {xrst_page_number}
# is replaced by the page number which includes the counter for each level.
# If target is 'html', {xrst_page_number} is removed with not replacement.
#
# count:
# is a list where each element is a non-negative int.
# count[-1] is the number of pages before this page.
# count[-1] is the number of pages before this secions parent.
# ...
# If this list is empty, this page is the root of the table of
# contents tree.
#
# page_index:
# is the index of this page in pinfo_list
#
# pinfo_list:
# is a list with length equal to the number of pages.
# The value pinfo_list[page_index] is a dictionary for this page
# with the following key, value pairs (all the keys are strings:
# key            value
# page_name   a str continaing the name of this page.
# page_title  a str containing the title for this page.
# parent_page an int index in page_info for the parent of this page.
# in_parent_file True if this page in same input file as its parent.
#
# content:
# The return content is the table of contents entries for this page
# and all the pages below this page.
#
# content =
def page_table_of_contents(
   tmp_dir, target, count, pinfo_list, page_index
) :
   assert type(tmp_dir) == str
   assert type(target) == str
   assert type(count) == list
   assert type(pinfo_list) == list
   assert type(page_index) == int
   #
   assert target in [ 'html', 'pdf' ]
   #
   # page_name, page_title
   page_name   = pinfo_list[page_index]['page_name']
   page_title  = pinfo_list[page_index]['page_title']
   #
   # page_number, content
   page_number = ''
   if 0 == len(count) :
      content = ''
   else :
      content = '| '
   if 0 < len(count) :
      assert type( count[-1] ) == int
      for i in range( len(count) - 1 ) :
         content += ' |space| '
      for (i, c) in enumerate(count) :
         page_number += str(c)
         if i + 1 < len(count) :
            page_number += '.'
   #
   # content
   if len(count) == 0 :
      content  += f':ref:`{page_name}-0`' '\n\n'
   else :
      content  += f':ref:`{page_number}<{page_name}>` '
      content  += page_title + '\n'
   #
   # file_name
   # temporary file corresponding to this page name
   if page_name.endswith('.rst') :
      file_name = tmp_dir + '/' + page_name
   else :
      file_name = tmp_dir + '/' + page_name + '.rst'
   #
   # page_data
   file_ptr  = open(file_name, 'r')
   page_data = file_ptr.read()
   file_ptr.close()
   if target == 'pdf' :
      page_data = xrst.replace_page_number(page_data, page_number, page_name)
   else :
      page_data = xrst.replace_page_number(page_data, '', page_name)
   #
   # file_name
   file_ptr  = open(file_name, 'w')
   file_ptr.write(page_data)
   file_ptr.close()
   #
   # in_parent_file_list, in_toc_cmd_list
   in_parent_file_list = list()
   in_toc_cmd_list   = list()
   for child_index in range( len( pinfo_list ) ) :
      if pinfo_list[child_index]['parent_page'] == page_index :
         if pinfo_list[child_index]['in_parent_file'] :
            in_parent_file_list.append(child_index)
         else :
            in_toc_cmd_list.append(child_index)
   #
   #
   # child_count, child_content
   child_count   = count + [0]
   child_content = ''
   #
   # child_count, child_content
   for child_index in in_toc_cmd_list + in_parent_file_list :
      #
      # child_count
      child_count[-1] += 1
      child_content += page_table_of_contents(
         tmp_dir, target, child_count, pinfo_list, child_index
      )
   #
   # child_content
   # if the number of children greater than one, put a blank line before
   # and after the child table of contents
   if 1 < child_count[-1] :
      if not child_content.startswith('|\n') :
         child_content = '|\n' + child_content
      if not child_content.endswith('|\n') :
         child_content = child_content + '|\n'
   #
   # content
   content += child_content
   #
   return content
# ----------------------------------------------------------------------------
# {xrst_begin table_of_contents dev}
# {xrst_spell
#  tmp
#  dir
#  pinfo
#  bool
#  dict
# }
# {xrst_comment_ch #}
#
# Create the table of contents
# ############################
# and replace the '{xrst_page_number}' for all pages in pinfo_list.
#
# Arguments
# *********
#
# tmp_dir
# =======
# is the temporary directory whre the rst files are written.
#
# target
# ======
# is either 'html' or 'pdf'.
#
#  #. If target is 'pdf',  in the file
#     tmp_dir/page_name.rst the text { ``xrst_page_number`` }
#     is replaced by the page number which includes the counter for each level.
#  #. If target is 'html', { ``xrst_page_number`` } is removed with not
#     replacement.
#
# pinfo_list
# ==========
# is a list with length equal to the number of pages.
# The value pinfo_list[page_index] is a dictionary for this page
# with the following key, value pairs (all the keys are strings):
#
# ..  csv-table::
#     :header: key, value, type
#
#     page_name, contains the name of this page, str
#     page_title,  contains the title for this page, str
#     parent_page, index in pinfo_list for the parent of this page, int
#     in_parent_file, is this page in same input file as its parent, bool
#
# root_page_list
# ==============
# is a list of strings containing the root page name for each group.
# The order of the root page names determine the order of the groups
# int the table of contents.
#
# Returns
# *******
#
# content
# =======
# The return content is the table of contents entries for all the pages.
# The title Table of Contents and the label xrst_table_of_contents
# are placed at the beginning of the of content.
#
# {xrst_code py}
def table_of_contents(
   tmp_dir, target, pinfo_list, root_page_list
) :
   assert type(tmp_dir) == str
   assert type(target) == str
   assert target in [ 'html', 'pdf']
   assert type(pinfo_list) == list
   assert type(pinfo_list[0]) == dict
   assert type(root_page_list) == list
   assert type(root_page_list[0]) == str
   # {xrst_code}
   # {xrst_literal
   #  BEGIN_return
   #  END_return
   # }
   # {xrst_end table_of_contents}
   #
   # content
   content  = '\n.. _xrst_table_of_contents-0:\n\n'
   content += 'Table of Contents\n'
   content += '*****************\n'
   #
   # content
   if len(root_page_list) == 1 :
      count = []
      page_name  = root_page_list[0]
      page_index = page_name2index(pinfo_list, page_name)
      content += page_table_of_contents(
         tmp_dir, target, count, pinfo_list, page_index
      )
   else :
      count = [0]
      for page_name in  root_page_list :
         page_index = page_name2index(pinfo_list, page_name)
         count[0]     += 1
         content      += page_table_of_contents(
            tmp_dir, target, count, pinfo_list, page_index
         )
   #
   # BEGIN_return
   assert type(content) == str
   return content
   # END_return
