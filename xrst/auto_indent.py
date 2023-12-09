# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-23 Bradley M. Bell
# ----------------------------------------------------------------------------
r"""
{xrst_begin auto_indent dev}

Automatic Indentation
#####################
Compute the indentation at the beginning of every line in *data* .
The characters that can be used to indent are spaces or tabs.
Lines that only have spaces and tabs are not included in this calculation.

Prototype
*********
{xrst_literal ,
   # BEGIN PROTOTYPE, # END PROTOTYPE
   # BEGIN RETURN, # END RETURN
}

data
****
is the data we are computing the indent for.
The text before the first new_line does not matter.
If you want to include this text, add a newline at the beginning of *data*.

file_name
*********
used for error reporting when *data* mixes spaces and tabs in
the indentation.

page_name
*********
used for error reporting when *data* mixes spaces and tabs in
the indentation.

indent
******
The return value *indent* is the automatically computed indent.
It will be a sequence of spaces or tabs but it will not mix
spaces and tabs.

{xrst_end auto_indent}
"""
import xrst
#
# BEGIN PROTOTYPE
def auto_indent(data, file_name, page_name) :
   assert type(data) == str
   assert type(file_name) == str
   assert type(page_name) == str
   # END PROTOTYPE
   #
   # len_data
   len_data   = len(data)
   #
   # newline_list
   newline_list = xrst.newline_indices(data)
   #
   # num_remove
   num_remove = len(data)
   for newline in newline_list :
      next_ = newline + 1
      if next_ < len_data and 0 < num_remove :
         ch = data[next_]
         while ch in ' \t' and next_ + 1 < len_data :
            next_ += 1
            ch     = data[next_]
         if ch not in ' \t\n' :
            num_remove = min(num_remove, next_ - newline - 1)
   #
   # check if there is no indent to remove
   if num_remove == 0 :
      return ''
   #
   # indent_ch
   line      = 0
   indent_ch = data[ newline_list[line] + 1 ]
   while indent_ch == '\n' :
      line += 1
      indent_ch = data[ newline_list[line] + 1 ]
   #
   # check for mixing spaces and tabs
   check_ch  = indent_ch + '\n'
   for newline in newline_list :
      next_ = newline + 1
      end   = min( len_data, next_ + num_remove )
      while next_ < end :
         if data[next_] not in check_ch :
            msg  = 'mixing both spaces and tabs for '
            msg += 'white space that indents this page.'
            xrst.system_exit(
               msg, file_name=file_name, page_name=page_name
            )
         next_ += 1
   #
   #
   # indent
   indent = num_remove * indent_ch
   #
   # BEGIN RETURN
   assert type(indent) == str
   return indent
   # END RETURN
