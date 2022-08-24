# -----------------------------------------------------------------------------
#                      xrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xrst_begin heading_example}

Title Heading for This Section
##############################
The label for the section title is the ``@``
character followed by the section name; i.e., ``@heading_example``.
The label ``heading_example`` displays ``heading_example``
instead of the section title.

Second Level
************
The label for this heading is ``heading_example@second_level``.

Third Level
===========
The label for this heading is ``heading_example@second_level@third_level``.

Another Second Level
********************
The label for this heading is ``heading_example@another_second_level``.

Third Level
===========
The label for this heading is
``heading_example@another_second_level@third_level``.

x
=
A heading can have just one character.
The label for this heading is
``heading_example@another_second_level@x``.

Links
*****
These links would also work from any other section because the section name
(``heading_example`` in this case)
is included at the beginning of the target for the link:

#. :ref:`@heading_example`
#. :ref:`heading_example@second_level`
#. :ref:`heading_example@second_level@third_level`
#. :ref:`heading_example@another_second_level`
#. :ref:`heading_example@another_second_level@third_level`
#. :ref:`heading_example@another_second_level@x`

Linking Headings Using :ref:
****************************
The file below demonstrates linking to headings using ``:ref:`` .

This Example File
*****************
{xrst_literal}

{xrst_end heading_example}
"""
