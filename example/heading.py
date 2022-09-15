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
The label for this heading is ``heading_example@Level One``.

Level Two
=========
The label for this heading is ``heading_example@Level One@Level Two``.

Another Level One
*****************
The label for this heading is ``heading_example@Another Level One``.

Level Two
=========
The label for this heading is
``heading_example@Another Level One@Level Two``.

x
=
A heading can have just one character.
The label for this heading is
``heading_example@Another Level One@x``.

Links
*****
These links would also work from any other page because the page name
(``heading_example`` in this case)
is included at the beginning of the target for the link:

#. :ref:`heading_example`
#. :ref:`heading_example-0`
#. :ref:`heading_example@Level One`
#. :ref:`heading_example@Level One@Level Two`
#. :ref:`heading_example@Another Level One`
#. :ref:`heading_example@Another Level One@Level Two`
#. :ref:`heading_example@Another Level One@x`

Linking Headings Using :ref:
****************************
The file below demonstrates linking to headings using ``:ref:`` .

This Example File
*****************
{xrst_literal}

{xrst_end heading_example}
"""
