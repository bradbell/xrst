# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
def factorial(n) :
   """
   {xrst_begin indent_example}
   {xrst_spell
      docstring
   }

   Indent Example
   ##############

   Discussion
   **********
   The file below demonstrates indenting an entire xrst page.
   Note that underling headings works even though it is indented.

   Python Docstring
   ****************
   This example is the python docstring for the factorial function
   defined in this file, but it is documenting indentation instead
   of the function.

   This Example File
   *****************
   {xrst_literal}

   {xrst_end indent_example}
   """
   if n == 1 :
      return 1
   return n * factorial(n-1)
