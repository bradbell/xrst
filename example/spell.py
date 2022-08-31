# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
"""
{xrst_begin spell_example}
{xrst_spell
   iterable
   no no
}

Spell Command Example
#####################

Text
****
The word ``iterable`` is not in the dictionary,
so we have included it in the special words for this page.

Spelling File
*************
The word ``xrst`` is included by the spelling file used to build this
documentation and hence need not be in the special words for this page.

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
spelling command for this page.

xrst_spell
**********
The file below demonstrates the use of ``xrst_spell``

This Example File
*****************
{xrst_literal}

{xrst_end spell_example}
"""
