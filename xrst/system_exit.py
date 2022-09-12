# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
import sys
import os
import xrst
#
# Add file name, page name, and line number to a message in a system exit
#
# msg:        error message
# file_name:  original input file that that data appeared in.
# page_name:  page name
# m_obj:      match object indicating where in data the error is detected
# data:       is the input data that was matched when m_obj is not None
# line:       is the error line number when m_obj is None
#
def system_exit(
   msg, file_name=None, page_name=None, m_obj=None, data=None, line=None
) :
   assert type(msg)   == str
   assert type(file_name) == str or file_name== None
   assert type(page_name) == str or page_name== None
   assert type(line)  in [ int, str ] or line == None
   #
   if m_obj :
      assert type(data) == str
   #
   #
   # extra
   root_directory = os.getcwd()
   extra          = f'\nroot_directory = {root_directory}\n'
   #
   if page_name :
      extra += f'page = {page_name}\n'
   if file_name :
      extra += f'file = {file_name}\n'
   if m_obj :
      assert file_name != None
      assert data != None
      assert line == None
      match_line  = xrst.pattern['line'].search( data[m_obj.start() :] )
      assert match_line
      line = match_line.group(1)
   if line != None :
      extra += f'line = {line}\n'
   #
   sys.exit('xrst: Error\n' + msg + extra)
