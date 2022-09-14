# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
"""
{xrst_begin heading_example}

The Page Title is Level Zero
############################
The label for the page title is the page name followed by ``-0``.
For example, the label ``heading_example-0`` displays
``The Page Title is Level Zero`` as the linking text.
(The label ``heading_example`` displays ``heading_example``
as the linking text.)

Level One
*********
The label for this heading is ``heading_example@level_one``.

Level Two
=========
The label for this heading is ``heading_example@level_one@level_two``.

Another Level One
*****************
The label for this heading is ``heading_example@another_level_one``.

Level Two
=========
The label for this heading is
``heading_example@another_level_one@level_two``.

x
=
A heading can have just one character.
The label for this heading is
``heading_example@another_level_one@x``.

Links
*****
These links would also work from any other page because the page name
(``heading_example`` in this case)
is included at the beginning of the target for the link:

#. :ref:`heading_example`
#. :ref:`heading_example-0`
#. :ref:`heading_example@level_one`
#. :ref:`heading_example@level_one@level_two`
#. :ref:`heading_example@another_level_one`
#. :ref:`heading_example@another_level_one@level_two`
#. :ref:`heading_example@another_level_one@x`

Linking Headings Using :ref:
****************************
The file below demonstrates linking to headings using ``:ref:`` .

This Example File
*****************
{xrst_literal}

{xrst_end heading_example}
"""
