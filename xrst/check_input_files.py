# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# -----------------------------------------------------------------------------
import re
import sys
import dismod_at
# -----------------------------------------------------------------------------
# {xrst_begin check_input_files dev}
# {xrst_spell
#     conf
#     dict
#     fullmatch
# }
# {xrst_comment_ch #}
#
# Check That Expected xrst Input Files Are Included
# #################################################
#
# conf_dict
# *********
# is a python dictionary representation of the configuration file.
#
# group_name
# **********
# is the name of the group that we are checking
#
# toc_file_set
# ************
# is the set of files that were included by toc commands starting
# at the root file for this group.
# A warning is printed if a file has a begin command for this group
# and it is not in *toc_file_set*.
#
# Syntax
# ******
# {xrst_code py}
def check_input_files(conf_dict, group_name, toc_file_set) :
   #
   assert type(conf_dict) == dict
   assert type(group_name) == str
   assert type(toc_file_set) == set
   #
   assert group_name != ''
   p_group_name = re.compile( r'[a-z]+' )
   assert p_group_name.fullmatch( group_name )
   # {xrst_code}
   # {xrst_end check_input_files}
   #
   # input_files
   input_files = conf_dict['input_files']['data']
   if len(input_files) == 0 :
      return
   #
   # file_list
   result  = dismod_at.system_command_prc(
      command       = input_files,
      print_command = True,
      return_stdout = True,
      return_stderr = True,
   )
   if result.returncode != 0 :
      msg += 'warning: source comamd specified in configure file failed\n'
      msg += result.stderr
      sys.stderr.write(msg)
      return
   file_list = result.stdout.split()
   #
   # p_empty
   p_empty  = r'(^|[^\\])\{xrst_(begin|begin_parent)[ \t]+([^ \t}]*)[ \t]*}'
   p_empty  = re.compile(p_empty)
   #
   # p_non_empty
   p_non_empty  = r'(^|[^\\])\{xrst_(begin|begin_parent)[ \t]+([^ \t}]*)[ \t]+'
   p_non_empty += group_name
   p_non_empty += r'[ \t]*}'
   p_non_empty  = re.compile( p_non_empty )
   #
   # group_file_set
   group_file_set = set()
   #
   # warning_count
   warning_count = 0
   #
   # file_name
   for file_name in file_list :
      if warning_count < 10 :
         #
         # file_data
         file_obj     = open(file_name, 'r')
         file_data    = file_obj.read()
         file_obj.close()
         #
         # m_non_empty
         m_non_empty = p_non_empty.search( file_data )
         if m_non_empty != None :
            if file_name not in toc_file_set :
               msg  = 'warning: file = ' + file_name + ' '
               msg += 'has a page with group_name = ' + group_name + '\n'
               msg += '         but it is not in any xrst_toc commands '
               msg += 'starting at the root_file for this group\n'
               sys.stderr.write(msg)
               warning_count += 1
         #
         # m_empty
         elif group_name == 'default' :
            m_empty = p_empty.search( file_data )
            if m_empty != None :
               if file_name not in toc_file_set :
                  msg  = 'warning: file = ' + file_name + ' '
                  msg += 'has a page with the empty group_name\n'
                  msg += '         but it is not in any xrst_toc commands '
                  msg += 'starting at the root_file for the default group\n'
                  sys.stderr.write(msg)
                  warning_count += 1
            #
            if warning_count == 10 :
               msg+= f'Surpressing this warning after {warning_count} files.\n'
               sys.stderr.write(msg)
