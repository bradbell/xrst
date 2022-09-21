# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
#
# {xrst_begin comment_example}
# {xrst_comment_ch #}
#
# Comment Command Example
# #######################
# This sentence has an inline comment {xrst_comment This comment is inline}.
# This sentence has a multiple line comment directly after it.
# {xrst_comment
#     This comment spans multiple lines
# }
# The multiple line comment is directly before this sentence.
#
# Factorial
# *********
# {xrst_code r}
factorial <- function(n)
{  if( n == 0 )
      return(1)
   else
      return( n * factorial(n-1) )
}
# {xrst_code}
#
# xrst_comment
# ************
# The file below demonstrates the use of ``xrst_comment`` .
#
# This Example File
# *****************
# {xrst_literal}
#
# {xrst_end comment_example}
