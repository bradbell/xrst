#! /usr/bin/env python3
# -----------------------------------------------------------------------------
#                      xrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
#
import sys
import re
import os
#
# usage
usage = \
'''
usage: update_xrst.py operation file_in file_out

operation: is one of the following: dot2atsign
file_in:   is the name of the file we are updating.
file_out:  is the name of the updated file. It can be the samle as file_in.

space4to3:
Change tab stop from 4 spaces to 3 spaces.

file2literal:
change xrst_file -> xrst_literal.

child2toc:
Change xsrt_children ->, xrst_toc_hidden, xrst_child_list -> xrst_toc_list,
and xrst_child_table -> xrst_toc_table.

ref_section:
Change :ref:`section_name` -> :ref:`@section_name`,
Change :ref:`section_name<section_name>` -> :ref:`section_name`

dot2atsign:
Change the '.' to '@' character in all text of the form :ref:`text` and
text of the form (at the betinning of a line) .. _text:

xsrst2xrst:
Change 'xsrst' to 'xrst' in all the text.

'''
#
#
# abort
def abort(msg) :
   msg = '\nupdate_xstst.py: ' + msg
   sys.exit(msg)
#
# space4to3:
def space4to3(data_in) :
   # data_out
   data_out = data_in
   #
   # data_out
   pattern  = re.compile( r'(^|\n)([0-9#.]\.)  ([^ ])' )
   data_out = pattern.sub(r'\1\2 \3', data_out)
   #
   # data_out
   pattern = re.compile( r'(^|\n)-   ([^ ])' )
   data_out = pattern.sub(r'\1-  \2', data_out)
   #
   # pattern
   pattern = re.compile( r'(^|\n)([# ]   (    ){0,})[^ ]' )
   #
   # m_obj
   m_obj   = pattern.search(data_out)
   while m_obj :
      #
      # start, end
      start = m_obj.start() + len( m_obj.group(1) )
      end   = m_obj.end() - 1
      assert end - start == len( m_obj.group(2) )
      #
      # n_indent
      n_indent = int ( (end - start) / 4 )
      assert (end - start) == n_indent * 4
      #
      # data_out
      replace  = n_indent * '   '
      if data_out[start] != ' ' :
         replace = data_out[start] + replace[1 :]
      data_out = data_out[: start] + replace + data_out[end :]
      #
      # m_obj
      m_obj    = pattern.search(data_out, start + n_indent * 3 )
   #
   # data_out
   pattern = re.compile( r'(^|\n)((   ){0,}){   ([^ ])' )
   data_out = pattern.sub( r'\1\2{  \4', data_out )
   #
   pattern  = re.compile( r'(\n# {8})(Copyright \(C\))' )
   data_out = pattern.sub( r'\1   \2', data_out )
   #
   pattern  = re.compile( r'(\n {3})(GNU Affero General Public)' )
   data_out = pattern.sub( r'\1 \2', data_out )
   # -----------------------------------------------------------------------
   return data_out
#
# fiile2literal:
def file2literal(data_in) :
   data_out = data_in.replace('{xrst_file', '{xrst_literal')
   return data_out
#
# child2toc:
def child2toc(data_in) :
   data_out = data_in.replace('{xrst_children', '{xrst_toc_hidden')
   data_out = data_out.replace('{xrst_child_list', '{xrst_toc_list')
   data_out = data_out.replace('{xrst_child_table', '{xrst_toc_table')
   return data_out
#
# ref_section
def ref_section(data_in) :
   #
   # pattern
   pattern = dict()
   pattern['title']        = re.compile( r':ref:`([._a-z0-9]+)`' )
   pattern['section_name'] = re.compile( r':ref:`([._a-z0-9]+)<\1>`' )
   #
   # data_out
   data_out  = data_in
   data_out  = pattern['title'].sub( r':ref:`@\1`', data_out)
   data_out  = pattern['section_name'].sub( r':ref:`\1`', data_out)
   data_out  = data_out.replace(':ref:`@genindex`', ':ref:`genindex`')
   return data_out
#
# dot2atsign
def dot2atsign(data_in) :
   # pattern
   pattern        = dict()
   pattern['ref'] = re.compile( r'(:ref:`[^`]*)\.' )
   #
   # data_out
   data_out = data_in
   #
   # m_ref
   m_ref    = pattern['ref'].search(data_out)
   while m_ref :
      # data_out
      data_out = pattern['ref'].sub(r'\1@', data_out)
      #
      # m_ref
      m_ref  = pattern['ref'].search(data_out, m_ref.start() )
   #
   return data_out
#
# xsrst2xrst
def xsrst2xrst(data_in) :
   data_out = data_in.replace('xsrst', 'xrst')
   return data_out
#
# main
def main() :
   if( len(sys.argv) != 4 ) :
      print(usage)
   #
   # operation_dict
   operation_dict = {
      'space4to3'    :  space4to3,
      'file2literal' :  file2literal,
      'child2toc'    :  child2toc,
      'ref_section'  :  ref_section,
      'dot2atsign'   :  dot2atsign,
      'xsrst2xrst'   :  xsrst2xrst,
   }
   #
   # operation
   operation = sys.argv[1]
   if operation not in operation_dict :
      msg  = f'operation = {operation} is not a valid operation'
      abort(msg)
   #
   # file_in,
   file_in = sys.argv[2]
   if not os.path.isfile(file_in) :
      msg = f'file_in = {file_in} is not an existing file'
      abort(msg)
   #
   # file_out
   file_out = sys.argv[3]
   #
   # file_data
   file_ptr   = open(file_in, 'r')
   file_data  = file_ptr.read()
   file_ptr.close()
   #
   # file_out
   file_data = operation_dict[operation](file_data)
   #
   # file_out
   file_ptr = open(file_out, 'w')
   file_ptr.write(file_data)
   file_ptr.close()
#
main()
print('update_xrst.py: OK')
sys.exit(0)
