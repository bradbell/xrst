# -----------------------------------------------------------------------------
#                      xrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xrst_begin_parent code_exam user}

Code Example
############

{xrst_file
    # BEGIN_SRC
    # END_SRC
}

{xrst_end code_exam}
"""
# ----------------------------------------------------------------------------
# BEGIN_SRC
"""
{xrst_begin code_res user}

Code Result
###########
{xrst_code py}"""
def factorial(n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)
"""{xrst_code}

:ref:`@code_exam`

{xrst_end code_res}
"""
# END_SRC
