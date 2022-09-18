# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
"""
{xrst_begin list_example}

Example using Commands in a List
################################

Code Command
************
#. The ``\{xrst_code py}`` cannot be on the first line of a list item.
   {xrst_code py}"""
   def factorial(n) :
      if n == 1 :
         return 1
      return n * factorial(n-1)
   """{xrst_code}
#. This is the first line of the next list item.

Lists
*****
The file below demonstrates using xrst commands in a list item.

This Example File
*****************
{xrst_literal}

{xrst_end list_example}
"""
