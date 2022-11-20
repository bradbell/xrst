# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
import sys
import os
import xrst
# {xrst_begin system_exit dev}
# {xrst_spell
#     msg
#     obj
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
   root_directory = os.getcwd()
   extra          = f'\nroot_directory = {root_directory}\n'
   #
   if page_name :
      extra += f'page = {page_name}\n'
   if file_name :
      extra += f'file = {file_name}\n'
   if m_obj :
      match_line  = xrst.pattern['line'].search( data[m_obj.start() :] )
      assert match_line
      line = match_line.group(1)
   if line != None :
      extra += f'line = {line}\n'
   #
   # breakpoint()
   sys.exit('xrst: Error\n' + msg + extra)
