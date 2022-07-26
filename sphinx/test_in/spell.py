# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xsrst_begin_parent spell_exam}

Spell Example
#############

{xsrst_file
    # BEGIN_SRC
    # END_SRC
}

{xsrst_end spell_exam}
"""
# ----------------------------------------------------------------------------
# BEGIN_SRC
"""
{xsrst_begin spell_res}
{xsrst_spell
    iterable
    no no
}


Spell Result
############

Text
****
The word ``iterable`` is not in the dictionary,
so we have included it in the special words for this section.

Spelling File
*************
The word ``xsrst`` is included by the
:ref:`spelling<xsrst.py@command_line_arguments@spelling>` file
and hence need not be in the special words for this section.

Math
****
Words that are preceded by a backslash; e.g., latex commands,
are automatically included as correct spelling.

.. math::

    z = \cos( \theta ) + {\rm i} \sin( \theta )

Double Words
************
It is consider an error to have only white space between
two occurrences of the same word; e.g.,
no no would be an error if there
were not two occurrences of :code:`no` next to each other in the
spelling command for this section.

:ref:`spell_exam`

{xsrst_end spell_res}
"""
# END_SRC
