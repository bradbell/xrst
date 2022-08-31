# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
"""
{xrst_begin child_example_one}

First Child
###########
This page is the first child in this file.
This file does not contain a begin parent command,
so all its pages are children of the page that includes this file.

Link to Second Child
********************
:ref:`child_example_two`

This Example File
*****************
{xrst_literal}

{xrst_end child_example_one}
"""
# ----------------------------------------------------------------------------
"""
{xrst_begin child_example_two}

Page Child
#############
This page is the second child in this file.

Link to First Child
*******************
:ref:`child_example_one`

{xrst_end child_example_two}
"""
