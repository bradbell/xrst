# -----------------------------------------------------------------------------
#                      xrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
import xrst
# ----------------------------------------------------------------------------
# page_index =
def page_name2index(sinfo_list, page_name) :
   for (page_index, info) in enumerate(sinfo_list) :
      if info['page_name'] == page_name :
         return page_index
   return None

# ----------------------------------------------------------------------------
# Create the table of contents and replace the '{xrst_page_number}'
# for this section and all its child sections.
#
# tmp_dir
# is the temporary directory whre the rst files are written.
#
# target:
# is either 'html' or 'pdf'. If target is 'pdf',  in the file
# tmp_dir/page_name.rst the text {xrst_page_number}
# is replaced by the section number which includes the counter for each level.
# If target is 'html', {xrst_page_number} is removed with not replacement.
#
# count:
# is a list where each element is a non-negative int.
# count[-1] is the number of sections before this section.
# count[-1] is the number of sections before this secions parent.
# ...
# If this list is empty, this section is the root of the table of
# contents tree.
#
# page_index:
# is the index of this section in sinfo_list
#
# sinfo_list:
# is a list with length equal to the number of sections.
# The value section[page_index] is a dictionary for this seciton
# with the following key, value pairs (all the keys are strings:
# key            value
# page_name   a str continaing the name of this section.
# page_title  a str containing the title for this section.
# parent_section an int index in page_info for the parent of this section.
# in_parent_file True if this section in same input file as its parent.
#
# content:
# The return content is the table of contents entries for this section
# and all the sections below this section.
#
# content =
def page_table_of_contents(
   tmp_dir, target, count, sinfo_list, page_index
) :
   assert type(tmp_dir) == str
   assert type(target) == str
   assert type(count) == list
   assert type(sinfo_list) == list
   assert type(page_index) == int
   #
   assert target in [ 'html', 'pdf' ]
   #
   # page_name, page_title
   page_name   = sinfo_list[page_index]['page_name']
   page_title  = sinfo_list[page_index]['page_title']
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
      content  += f':ref:`@{page_name}`' '\n\n'
   else :
      content  += f':ref:`{page_number}<{page_name}>` '
      content  += page_title + '\n'
   #
   # file_name
   # temporary file corresponding to this section name
   if page_name.endswith('.rst') :
      file_name = tmp_dir + '/' + page_name
   else :
      file_name = tmp_dir + '/' + page_name + '.rst'
   #
   # file_data
   file_ptr  = open(file_name, 'r')
   file_data = file_ptr.read()
   file_ptr.close()
   if target == 'pdf' :
      file_data = xrst.replace_page_number(file_data, page_number)
   else :
      file_data = xrst.replace_page_number(file_data, '')
   #
   # file_name
   file_ptr  = open(file_name, 'w')
   file_ptr.write(file_data)
   file_ptr.close()
   #
   # in_parent_file_list, in_toc_cmd_list
   in_parent_file_list = list()
   in_toc_cmd_list   = list()
   for child_index in range( len( sinfo_list ) ) :
      if sinfo_list[child_index]['parent_section'] == page_index :
         if sinfo_list[child_index]['in_parent_file'] :
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
         tmp_dir, target, child_count, sinfo_list, child_index
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
# Create the table of contents and replace the '{xrst_page_number}'
# for all sections in sinfo_list.
#
# tmp_dir
# is the temporary directory whre the rst files are written.
#
# target:
# is either 'html' or 'pdf'. If target is 'pdf',  in the file
# tmp_dir/page_name.rst the text {xrst_page_number}
# is replaced by the section number which includes the counter for each level.
# If target is 'html', {xrst_page_number} is removed with not replacement.
#
# sinfo_list:
# is a list with length equal to the number of sections.
# The value section[page_index] is a dictionary for this seciton
# with the following key, value pairs (all the keys are strings:
# key            value
# page_name   a str continaing the name of this section.
# page_title  a str containing the title for this section.
# parent_section an int index in sinfo_list for the parent of this section.
# in_parent_file is this section in same input file as its parent.
#
# content:
# The return content is the table of contents entries for all the sections.
# The title Table of Contents and the label xrst_tble_of_contents
# are placed at the beginning of the of content.
#
# content =
def table_of_contents(
   tmp_dir, target, sinfo_list, root_page_list
) :
   assert type(tmp_dir) == str
   assert type(target) == str
   assert type(root_page_list) == list
   assert type(root_page_list[0]) == str
   #
   assert target in [ 'html', 'pdf']
   #
   # content
   content  = '\n.. _@xrst_table_of_contents:\n\n'
   content += 'Table of Contents\n'
   content += '*****************\n'
   #
   # content
   if len(root_page_list) == 1 :
      count = []
      page_name  = root_page_list[0]
      page_index = page_name2index(sinfo_list, page_name)
      content += page_table_of_contents(
         tmp_dir, target, count, sinfo_list, page_index
      )
   else :
      count = [0]
      for page_name in  root_page_list :
         page_index = page_name2index(sinfo_list, page_name)
         count[0]     += 1
         content      += page_table_of_contents(
            tmp_dir, target, count, sinfo_list, page_index
         )
   #
   return content
