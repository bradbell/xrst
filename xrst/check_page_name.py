# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
import re
import xrst
#
# Check that a page name abides by its rules. If not, report error and exit.
#
# page_name:
# The string page_name appears at the begnning of a line, not counting
# white space, in one of the following cases:
# 1. {xrst_begin_parent page_name user}
# 2. {xrst_begin page_name user}
# 3. {xrst_end page_name}
# The valid characters in a seciton name are [a-z], [0-9], and underbar.
# A page name cannot begin with xrst_. If seciton_name does not follow the
# rules in the previous sentence, a message is printed and the program exits.
#
# file_name:
# is the name of the original input file that data appears in.
#
# m_obj:
# is the match object correpsonding to finding the page name
#
# data:
# is that data that was searched to detect the match object.
#
def check_page_name(page_name, file_name, m_obj, data) :
   assert type(page_name) == str
   assert type(file_name) == str
   assert m_obj
   assert type(data) == str
   #
   m_page_name = re.search('[._a-z0-9]+', page_name)
   if m_page_name.group(0) != page_name :
      msg  = f'in begin comamnd page_name = "{page_name}"'
      msg += '\nIt must be non-empty and only contain the following'
      msg += ' characters: ., _, a-z, 0-9'
      xrst.system_exit(msg,
         file_name=file_name, m_obj=m_obj, data=data
      )
   if page_name.startswith('xrst_') :
      msg = 'page_name cannot start with xrst_'
      xrst.system_exit(msg,
         file_name=file_name, m_obj=m_obj, data=data
      )
   if page_name == 'index' :
      msg = 'page_name cannot be index'
      xrst.system_exit(msg,
         file_name=file_name, m_obj=m_obj, data=data
      )
