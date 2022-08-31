# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
# {xrst_comment_ch #}
#
# {xrst_begin comment_ch_example}
  {xrst_spell
     ch
  }
#
# Comment Character Command Example
# #################################
#
# Discussion
# **********
# The ``#`` at the beginning of a line,
# and space directly after it, are removed.
# The remaining text lines up with the first line in the
# function definition below:
#
# {xrst_code py}
def factorial(n) :
   if n == 1 :
      return 1
   return n * factorial(n-1)
# {xrst_code}
#
# xrst_comment_ch
# ***************
# The file below demonstrates the use of ``xrst_comment_ch`` .
#
# This Example File
# *****************
# {xrst_literal}
#
# {xrst_end comment_ch_example}
