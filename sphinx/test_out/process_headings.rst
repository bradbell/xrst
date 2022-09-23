.. include:: xrst_preamble.rst

.. _process_headings:

!!!!!!!!!!!!!!!!
process_headings
!!!!!!!!!!!!!!!!

xrst input file: ``xrst/process_headings.py``

.. meta::
   :keywords: process_headings, add, labels, index, entries, headings

.. index:: process_headings, add, labels, index, entries, headings

.. _process_headings-0:

Add labels and index entries for headings
#########################################
.. contents::
   :local:

.. meta::
   :keywords: arguments

.. index:: arguments

.. _process_headings@Arguments:

Arguments
*********

.. meta::
   :keywords: html_theme

.. index:: html_theme

.. _process_headings@Arguments@html_theme:

html_theme
==========
is the xrst command line html_theme setting.

.. meta::
   :keywords: data_in

.. index:: data_in

.. _process_headings@Arguments@data_in:

data_in
=======
contains the data for a page before the headings are processed.

.. meta::
   :keywords: file_name

.. index:: file_name

.. _process_headings@Arguments@file_name:

file_name
=========
name of the file that contains the input data for this page.
This is only used for error reporting.

.. meta::
   :keywords: page_name

.. index:: page_name

.. _process_headings@Arguments@page_name:

page_name
=========
is the name of this page.

.. meta::
   :keywords: keyword_list

.. index:: keyword_list

.. _process_headings@Arguments@keyword_list:

keyword_list
============
is a list of compiled regular expressions. If pattern is in this list,
*word* is a lower case version of a word in the heading text, and
pattern.fullmatch( *word* ) returns a match, an index entry is not
generated for word.

.. meta::
   :keywords: returns

.. index:: returns

.. _process_headings@Returns:

Returns
*******

.. meta::
   :keywords: data_out

.. index:: data_out

.. _process_headings@Returns@data_out:

data_out
========
is a copy of data_in with the following extra command added:

 #. The index entries, and meta keyword entries (same as index),
    and the :ref:`heading_links@Labels` for this page.
 #. The command '{xrst_page_number}\n' is placed directly before the
    first heading for this page; i.e. its title.
    This is makes it easy to add the page number to the heading text.

.. meta::
   :keywords: page_title

.. index:: page_title

.. _process_headings@Returns@page_title:

page_title
==========
This is the heading text in the first heading for this page.
There can only be one heading at this level.

.. meta::
   :keywords: pseudo_heading

.. index:: pseudo_heading

.. _process_headings@Returns@pseudo_heading:

pseudo_heading
==============
This is an automatically generated heading for this page. It is intended
to come before the page_title heading.
It has three lines each terminated by a newline:

 1. an overline line
 2. heading text line for this page title
 3. an underline line

.. literalinclude:: ../../xrst/process_headings.py
   :lines: 151-158
   :language: py

.. literalinclude:: ../../xrst/process_headings.py
   :lines: 378-382
   :language: py
