# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
# {xrst_begin file2_list_str dev}
# {xrst_spell
#     len
#     newline
# }
# {xrst_comment_ch #}
#
# Convert lines in a file to a list of strings
# ############################################
#
# file_name
# *********
# is the name of the file that we are converting.
#
# list_str
# ********
# the return value is a list of str, one for each line of the file.
#
# #. Lines that begin with the # character are not included.
# #. Leading and trailing spaces ' ', tabs '\t', and the newline '\n'
#    are not included.
# #. Empty lines, after step 2, are not included.
#
# {xrst_code py}
# list_str =
def file2_list_str(file_name) :
   assert type(file_name) == str
   # assert type(list_str) == list
   # if len(list_str) > 0 :
   #    assert type( list_str[0] ) == str
   # {xrst_code}
   # {xrst_end file2_list_str}
   file_ptr  = open(file_name, 'r')
   list_str  = list()
   for line in file_ptr :
      if not line.startswith('#') :
         line = line.strip(' \t\n')
         if not line == '' :
            list_str.append(line)
   file_ptr.close()
   return list_str
