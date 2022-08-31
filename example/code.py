# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
"""
{xrst_begin code_example}

Code Command Example
####################

Factorial
*********
{xrst_code py}"""
def factorial(n) :
   if n == 1 :
      return 1
   return n * factorial(n-1)
"""{xrst_code}

xrst_code
*********
The file below demonstrates the use of ``xrst_code`` .

This Example File
*****************
{xrst_literal}

{xrst_end code_example}
"""
