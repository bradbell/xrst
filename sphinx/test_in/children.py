# -----------------------------------------------------------------------------
#                      xrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
# BEGIN_FILE
"""
{xrst_begin children_exam user}

Children Example
################
This file does not contain a begin parent command,
so all its sections are children of the section that includes it.

Other Section
*************
The :ref:`link<children_other>` goes to the other section in this file.

This File
*********
{xrst_file
    # BEGIN_FILE
    # END_FILE
}

{xrst_end children_exam}
"""
# ----------------------------------------------------------------------------
"""
{xrst_begin children_other user}

Other Child
###########
This is the other child section in
:ref:`this file<children_exam@this_file>`.


{xrst_end children_other}
"""
# END_FILE
