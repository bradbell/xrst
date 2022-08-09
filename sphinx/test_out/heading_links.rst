.. include:: xrst_preamble.rst

.. _heading_links:

!!!!!!!!!!!!!
heading_links
!!!!!!!!!!!!!

xrst input file: ``xrst/process_headings.py``

.. meta::
   :keywords: heading_links, heading, cross, reference, links

.. index:: heading_links, heading, cross, reference, links

.. _@heading_links:

Heading Cross Reference Links
#############################
.. contents::
   :local:

.. meta::
   :keywords: index

.. index:: index

.. _heading_links@index:

Index
*****
For each word in a heading,
a link is included in the index from the word to the heading.
In addition, each word is added to the html keyword meta data
next to the section heading.

.. meta::
   :keywords: labels

.. index:: labels

.. _heading_links@labels:

Labels
******
A cross reference label is defined for linking
from anywhere to a heading. The details of how to use
these labels are described below.

.. meta::
   :keywords: first, level

.. index:: first, level

.. _heading_links@labels@first_level:

First Level
===========
Each :ref:`section<begin_cmd@section>` can have only one header at
the first level which is a title for the section.
The :ref:`section_name<begin_cmd@section_name>`
is automatically used as a label for a link that displays the
section name or section title. To be specific,
the first input below will display the section name as the linking text,
the second will display the section title as the linking text.

1.  ``:ref:``\ \` *section_name*\ \`
2.  ``:ref:``\ \` ``@``\ *section_name*\ \`

You can also explicitly choose the linking text; e.g.

3.  ``:ref:``\ \`*linking_text*\ ``<``\ *section_name*\ ``>``\ \`

.. meta::
   :keywords: other, levels

.. index:: other, levels

.. _heading_links@labels@other_levels:

Other Levels
============
The label for linking a heading that is not at the first level is the label
for the heading directly above it plus an at sign character :code:`@`,
plus the conversion for this heading.
These labels do not begin with ``@``.

.. meta::
   :keywords: conversion

.. index:: conversion

.. _heading_links@labels@conversion:

Conversion
==========
The conversion of a heading to a label does the following:

1.  Letters are converted to lower case.
2.  The following characters are converted to underbars ``_`` :
    space ,  at signs ``@``, and colon ``:`` .

For example, the label for the heading above is

|tab| ``heading_links@labels@conversion``

.. meta::
   :keywords: discussion

.. index:: discussion

.. _heading_links@labels@discussion:

Discussion
==========
1.  Note that at the first level one uses the *section_name*
    ( ``run_xrst`` in example above)
    and not the title ( ``extract_sphinx_rst`` in example above ).
2.  The ``@`` and not ``.`` character is used to separate levels
    because the ``.`` character is often used in titles and
    section names; e.g. :ref:`auto_file@conf.py`.
3.  Specifying all the levels for a heading may seem verbose,
    but it avoids ambiguity when the same heading appears twice in one section;
    e.g the heading Example might appears multiple times in different context.
4.  Specifying all the levels also helps keep the links up to date.
    If a heading changes, all the links to that heading, and all the
    headings below it,  will break.  This identifies the links that should be
    checked to make sure they are still valid.

.. _heading_links@example:

Example
*******
:ref:`heading_example`
