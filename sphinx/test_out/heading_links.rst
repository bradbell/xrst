.. include:: xrst_preamble.rst

!!!!!!!!!!!!!
heading_links
!!!!!!!!!!!!!

.. toctree::
   :maxdepth: 1
   :hidden:

   heading_exam

.. meta::
   :keywords: heading_links, heading, links

.. index:: heading_links, heading, links

.. _heading_links:

Heading Links
#############
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
is automatically used
as a label for linking the title for a section; i.e., the
following two inputs will link to the title for *section_name*:

1.  ``:ref:``\ \` *section_name*\ \`
2.  ``:ref:``\ \`*linking_text*\ ``<``\ *section_name*\ ``>``\ \`

The *linking_text* in the second syntax is the text the user sees.
The linking text for the first syntax is the title for the Section,
not the *section_name* (which is used as an abbreviated title).

.. meta::
   :keywords: other, levels

.. index:: other, levels

.. _heading_links@labels@other_levels:

Other Levels
============
The label for linking a heading that is not at the first level is the label
for the heading directly above it plus an at sign character :code:`@`,
plus a lower case version of the heading with spaces and at signs converted to
underbars :code:`_`. For example, the label for the heading for this
paragraph is

|tab| ``run_xrst@links_to_headings@other_levels``

This may seem verbose, but it helps keep the links up to date.
If a heading changes, all the links to that heading, and all the headings
below it,  will break.
This identifies the links that should be checked
to make sure they are still valid.
Note that one uses the *section_name* ``run_xrst``
and not the title ``extract_sphinx_rst``.

.. meta::
   :keywords: example

.. index:: example

.. _heading_links@example:

Example
*******

The :ref:`heading_exam` section contains an example using these links.

----

xrst input file: ``xrst/process_headings.py``
