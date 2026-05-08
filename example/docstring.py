'''
This is doctring documentation for the module corresponding to this file.
'''
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-26 Bradley M. Bell
# ----------------------------------------------------------------------------
r'''
{xrst_begin docstring_example}

Docstring Example
#################

Python Docstring
****************
This example demonstrates using a python docstring to document a function.
It does not have any xrst commands in the docstring, just an extra colon, :,
at the beginning and end to enable the literal command find the docstring.
This avoids having xrst commands in the corresponding python help output.
See :ref:`indent_example@Python Docstring`
for an example where the xrst input is indented and
the xrst commands are in the docstring.

factorial
*********
{xrst_literal ,
    """:, :"""
}

This Example File
*****************
{xrst_literal}

{xrst_end docstring_example}
'''
def factorial(n) :
    r""":
    This function returns the product 1 * 2 * ... * n
    :"""
    if n == 1 :
        return 1
    return n * factorial(n-1)
