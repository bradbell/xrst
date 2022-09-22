# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
"""
{xrst_begin list_example}
{xrst_spell
   csv
}
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
#. This is the second item for this list

RST Directive
*************
#. This list demonstrates using an rst directive in a list
   .. csv_table::

      a11, a12
      a21, a22

#. This is the second item for this list



This Example File
*****************
{xrst_literal}

{xrst_end list_example}
"""
