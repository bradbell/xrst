# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
import re
import xrst
# {xrst_begin check_page_name dev}
# {xrst_spell
#     obj
#     underbar
# }
# {xrst_comment_ch #}
#
# Check the rules for a page name
# ###############################
#
# page_name
# *********
# The page_name appears in *m_obj* in one of the following ways
# #. \{xrst_begin_parent page_name user}
# #. \{xrst_begin page_name user}
# #. \{xrst_end page_name}
#
# The valid characters in a page name are [a-z], [0-9], period and underbar.
# A page name cannot begin with ``xrst_`` . If *page_name* does not follow
# these rules, a message is printed and the program exits.
#
# file_name
# *********
# is the name of the original input file that data appears in
# (used for error reporting).
#
# m_obj
# *****
# is the match object corresponding to *page_name*
#
# data
# ****
# is that data that was searched to get the match object.
#
# {xrst_code py}
def check_page_name(page_name, file_name, m_obj, data) :
   assert type(page_name) == str
   assert type(file_name) == str
   assert m_obj
   assert type(data) == str
   # {xrst_code}
   # {xrst_end check_page_name}
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
