.. include:: xrst_preamble.rst

.. _heading_links:

!!!!!!!!!!!!!
heading_links
!!!!!!!!!!!!!

xrst input file: ``xrst/process_headings.py``

.. meta::
   :keywords: heading_links, heading, cross, reference, links

.. index:: heading_links, heading, cross, reference, links

.. _heading_links-title:

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
page name or page title.

.. meta::
   :keywords: page_name

.. index:: page_name

.. _heading_links@Labels@Level Zero@page_name:

page_name
---------
The input below will display the page name as the linking text:

  ``:ref:`` \` *page_name* \`

.. meta::
   :keywords: page_title

.. index:: page_title

.. _heading_links@Labels@Level Zero@page_title:

page_title
----------
The input below will display the page title as the linking text:

    ``:ref:`` \` *page_name* ``-title`` \`

.. meta::
   :keywords: linking, text

.. index:: linking, text

.. _heading_links@Labels@Level Zero@Linking Text:

Linking Text
------------
You can also explicitly choose the linking text using:

   ``:ref:`` \` *linking_text* ``<`` *page_name* ``>`` \`

.. meta::
   :keywords: other, levels

.. index:: other, levels

.. _heading_links@Labels@Other Levels:

Other Levels
============
The label for linking a heading that is not at level zero is the label
for the heading directly above it plus an at sign character :code:`@`,
plus the conversion for this heading.
These labels use the *page_name*
(not *page_name* ``-title`` ) for level zero.

.. meta::
   :keywords: heading@to@label

.. index:: heading@to@label

.. _heading_links@Labels@Heading_To_Label:

Heading@To@Label
================
The conversion of a heading to a label
removes all backslashes ``\`` and changes at signs ``@``
to underbars ``_``.

For example, the label for the heading above is

   :ref:`heading_links@Labels@Heading_To_Label
   <heading_links@Labels@Heading_To_Label>`

The label corresponding to a header is used to reference the heading
using the ``:ref:`` role.

.. meta::
   :keywords: label, anchor

.. index:: label, anchor

.. _heading_links@Labels@Label To Anchor:

Label To Anchor
===============
There is a further conversion to create the
HTML anchor corresponding to a label.  To be specific:

1. The anchor is converted to lower case.
2. The page name is removed.
3. Characters that are not letters or decimal digits are converted to dashes.
4. Multiple dashes are converted to one dash.
5. The beginning of the anchor is trimmed until a letter is reached.
6. The end of the anchor is trimmed until a letter or digit is reached.

If for one page, these anchors are not unique, xrst reports an error.

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
3. Including all the levels above a heading in its label may seem verbose,
   but it avoids ambiguity when the same heading appears twice in one page;
   e.g the heading Example might appears multiple times in different context.
   This also helps keep the links up to date.
   If a heading changes, all the links to that heading, and all the
   headings below it,  will break.  This identifies the links that should be
   checked to make sure they are still valid.
4. It is an error for two headings have the same HTML anchor.
   This makes the html links to a heading valid as long as its label
   does not change. This is useful when posting the answer to a questions
   using a link to a particular heading.

.. _heading_links@Example:

Example
*******
:ref:`heading_example`
