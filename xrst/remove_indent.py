# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-23 Bradley M. Bell
# ----------------------------------------------------------------------------
r"""
{xrst_begin indent user}

Indentation
###########
If there are a number of spaces (or tabs) before
all of the xrst documentation for a page,
those characters are not included in the xrst output.
This enables one to indent the
xrst so it is grouped with the proper code block in the source.
An error message will result if
you use mix tabs and spaces for the indentation.

Example
*******
:ref:`indent_example-name`, and
:ref:`comment_ch_example@Indent`.

{xrst_end indent}
"""
import re
import xrst
# {xrst_begin remove_indent dev}
# {xrst_comment_ch #}
#
# Remove indentation for a page
# #############################
#
# Prototype
# *********
# {xrst_literal ,
#  # BEGIN PROTOTYPE, # END PROTOTYPE
#  # BEGIN RETURN, # END RETURN
# }
#
# data_in
# *******
# is the data for this page.
#
# file_name
# *********
# is the input that this page appears in (used for error reporting).
#
# page_name
# *********
# is the name of this page (used for error reporting).
#
# data_out
# ********
# is a copy of data_in with the indentation for this section removed.
#
# {xrst_end remove_indent}
# BEGIN PROTOTYPE
def remove_indent(data_in, file_name, page_name) :
   assert type(data_in) == str
   assert type(file_name) == str
   assert type(page_name) == str
   # END PROTOTYPE
   #
   # indent
   indent = xrst.auto_indent(data_in, file_name, page_name)
   #
   # data_out
   pattern  = re.compile( r'\n' + indent )
   data_out = pattern.sub('\n', data_in)
   #
   # BEGIN RETURN
   assert type(data_out) == str
   return data_out
   # END RETURN
