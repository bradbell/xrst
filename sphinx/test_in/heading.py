# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xsrst_begin_parent heading_exam}

Heading Example
###############

Child File
**********
{xsrst_file
    # BEGIN_SRC
    # END_SRC
}


Example Heading
***************
The example heading below (Child Sections) is a heading for the
:ref:`child_cmd@syntax@child_table` for this section:

Child Sections
**************

{xsrst_end heading_exam}
"""
# ----------------------------------------------------------------------------
# BEGIN_SRC
"""
{xsrst_begin heading_res}

Heading Result
##############
The label for this heading is the section name ``heading_res``.

Second Level
************
The label for this heading is ``heading_res.second_level``.

Third Level
===========
The label for this heading is ``heading_res.second_level.third_level``.

Another Second Level
********************
The label for this heading is ``heading_res.another_second_level``.

Third Level
===========
The label for this heading is
``heading_res.another_second_level.third_level``.

Links
*****
These links would also work from any other section because the
:ref:`section_name<begin_cmd@section_name>`
(which is ``heading_res`` in this case)
is included at the beginning of the target for the link:

1. :ref:`heading_res`
2. :ref:`heading_res@second_level`
3. :ref:`heading_res@second_level@third_level`
4. :ref:`heading_res@another_second_level`
5. :ref:`heading_res@another_second_level@third_level`

:ref:`heading_exam`

{xsrst_end heading_res}
"""
# END_SRC
