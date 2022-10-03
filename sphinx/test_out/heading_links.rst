.. include:: xrst_preamble.rst

.. _heading_links:

!!!!!!!!!!!!!
heading_links
!!!!!!!!!!!!!

xrst input file: ``xrst/process_headings.py``

.. meta::
   :keywords: heading_links, heading, cross, reference, links

.. index:: heading_links, heading, cross, reference, links

.. _heading_links-0:

Heading Cross Reference Links
#############################

.. contents::
   :local:

.. meta::
   :keywords: index

.. index:: index

.. _heading_links@Index:

Index
*****
For each word in a heading,
a link is included in the index from the word to the heading.
In addition, each word is added to the html keyword meta data
next to the page heading.

.. meta::
   :keywords: labels

.. index:: labels

.. _heading_links@Labels:

Labels
******
A cross reference label is defined for linking
from anywhere to a heading. The details of how to use
these labels are described below.

.. meta::
   :keywords: level, zero

.. index:: level, zero

.. _heading_links@Labels@Level Zero:

Level Zero
==========
Each :ref:`page<begin_cmd@page>` can have only one header at
the first level which is a title for the page.
The :ref:`page_name<begin_cmd@page_name>`
is automatically used as a label for a link that displays the
page name or page title. To be specific,
the first input below will display the page name as the linking text,
the second will display the page title as the linking text.

1. ``:ref:`` \` *page_name* \`
2. ``:ref:`` \` *page_name* ``-0`` \`

You can also explicitly choose the linking text; e.g.

3. ``:ref:`` \` *linking_text* ``<`` *page_name* ``>`` \`

.. meta::
   :keywords: other, levels

.. index:: other, levels

.. _heading_links@Labels@Other Levels:

Other Levels
============
The label for linking a heading that is not at the first level is the label
for the heading directly above it plus an at sign character :code:`@`,
plus the conversion for this heading.
These labels do not begin with ``@``.

.. meta::
   :keywords: conversion:

.. index:: conversion:

.. _heading_links@Labels@Conversion_:

Conversion:
===========
The conversion of a heading to a label changes the at sign ``@``
and colon ``:`` to underbars ``_``.

For example, the label for the heading above is

|tab| ``heading_links@Labels@Conversion_``

.. meta::
   :keywords: discussion

.. index:: discussion

.. _heading_links@Labels@Discussion:

Discussion
==========
1. Note that at the first level one uses the *page_name* and not the
   title; e.g., in the example above one uses ``heading_links``
   and not ``Heading Cross Reference Links`` .
2. The ``@`` and not ``.`` character is used to separate levels
   because the ``.`` character is often used in titles and
   page names; e.g. :ref:`auto_file@conf.py`.
3. Specifying all the levels for a heading may seem verbose,
   but it avoids ambiguity when the same heading appears twice in one page;
   e.g the heading Example might appears multiple times in different context.
   This also helps keep the links up to date.
   If a heading changes, all the links to that heading, and all the
   headings below it,  will break.  This identifies the links that should be
   checked to make sure they are still valid.

.. _heading_links@Example:

Example
*******
:ref:`heading_example`
