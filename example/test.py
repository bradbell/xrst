# vim:nofixeol
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
"""
{xrst_begin testExample}
{xrst_spell
   underbar
   newline
}
Test Special Conditions
#######################

Camel Case
**********
This page name uses a capital letter, instead of an underbar,
to separate the words test and example.

Code Command in List
********************
#. The ``\{xrst_code py}`` cannot be on the first line of a list item.
   {xrst_code py}"""
   def factorial(n) :
      if n == 1 :
         return 1
      return n * factorial(n-1)
   """{xrst_code}
#. This is the second item for this list

No Newline at End of File
*************************
This example file does not have a newline at the end.

This Example File
*****************
{xrst_literal}

{xrst_end testExample}
"""