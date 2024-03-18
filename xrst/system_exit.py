# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-24 Bradley M. Bell
# ----------------------------------------------------------------------------
import sys
import os
import re
import xrst
#
pattern_template_begin  = re.compile( r'\n{xrst_template_begin ([^\n]*)}\n' )
pattern_template_end    = re.compile( r'\n{xrst_template_end}\n' )
#
# {xrst_begin system_exit dev}
# {xrst_spell
#     msg
# }
# {xrst_comment_ch #}
#
# Form error message and exit
# ###########################
#
# msg
# ***
# Reason for aborting xrst
#
# file_name
# *********
# input file that error appeared in
#
# page_name
# *********
# name of page that the error appeared in
#
# m_obj
# *****
# The error was detected in the values returned by this match object.
#
# data
# ****
# is the data that was searched to get the match object m_obj.
#
# line
# ****
# is the line number in file specified by file_name where the error
# was detected.
#
# {xrst_code py}
def system_exit(
   msg, file_name=None, page_name=None, m_obj=None, data=None, line=None
) :
   assert type(msg)       == str
   assert type(file_name) == str or file_name == None
   assert type(page_name) == str or page_name == None
   assert type(line)  in [ int, str ] or line == None
   if m_obj != None :
      assert file_name != None
      assert data      != None
      assert line      == None
   # {xrst_code}
   # {xrst_end system_exit}
   #
   # extra
   project_directory = os.getcwd()
   extra          = f'\nproject_directory = {project_directory}\n'
   #
   # line, template_file, template_line
   template_file = None
   template_line = None
   if m_obj :
      m_line  = xrst.pattern['line'].search( data[m_obj.start() :] )
      assert m_line
      line = m_line.group(1)
      #
      # begin_index, end_index
      begin_index = data[: m_obj.start()].rfind( r'\n{xrst_template_begin' )
      end_index   = data[: m_obj.start()].rfind( r'\n{xrst_template_end' )
      if end_index < begin_index :
         #
         # tempate_line
         template_line = line
         #
         # template_file
         m_temp = pattern_template_begin.search( data[begin_index :] )
         assert m_temp != None
         template_file = m_temp.group(1).strip()
         #
         # line
         m_line = xrst.pattern['line'].search( data[begin_index :] )
         assert m_line
         line = m_line.group(1)
   #
   # extra
   if page_name != None :
      extra += f'page = {page_name}\n'
   if file_name :
      extra += f'file = {file_name}\n'
   if line != None :
      extra += f'line = {line}\n'
   if template_file != None :
      extra += f'template_file = {template_file}\n'
      extra += f'template_line = {template_line}\n'
   #
   # breakpoint()
   sys.exit('xrst: Error\n' + msg + extra)
