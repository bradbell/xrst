.. _purpose-name:

!!!!!!!
purpose
!!!!!!!

.. meta::
   :keywords: purpose, motivation

.. index:: purpose, motivation

.. _purpose-title:

Motivation
##########

This is a sphinx wrapper that provides the features listed below.
It was motivated by cases like the GNU Scientific library,
which is not written in python, uses sphinx, and has its documentation
in separate files from the corresponding source code; see `gsl doc`_ .
It provides a system that extracts rst documentation files from any source code
language and has some of the benefits of doxygen and autodoc without
some of the drawbacks.

.. _gsl doc: https://git.savannah.gnu.org/cgit/gsl.git/tree/doc

.. contents::
   :local:

.. meta::
   :keywords: features

.. index:: features

.. _purpose@Features:

Features
********
One can consider some of the xrst features listed below as a wish list for sphinx:

#. Makes it easy to put documentation in source code comments,
   even when multiple computer languages are used by one package;
   e.g., see :ref:`comment_ch_cmd-name` .
#. Multiple pages can be specified in one
   input file and one page can be the parent for the
   other pages in the same file; see :ref:`begin_cmd-name` .
#. One can build subsets of the documentation; e.g., user, developer,
   examples. Pages for different subsets can be in the
   same input file; see :ref:`run_xrst@group_list`.
#. For each page, the rst file name is used as an abbreviated title
   in the navigation bar. This makes the navigation bar more useful
   while also having long descriptive titles attached to each page.
#. Sphinx error messages are translated from rst file and line number
   to the file and line number in corresponding xrst input file.
   In addition, :ref:`run_xrst@page_source` is the xrst input,
   not the extracted rst file.
#. The are two levels to the table of contents. Each entry at the
   first level is a page name or page title; e.g.,
   see the :ref:`xrst_table_of_contents-title` for this documentation.
   Each entry at the second level is a headings with in a page.
   The :ref:`run_xrst@local_toc` option can be used to display the second
   level for each page.
#. Words in each heading are automatically included in the
   index in a way that can be configured;
   see :ref:`config_file@not_in_index` .
   These words are also automatically included as html keyword meta data.
#. Includes a spell checker with special words at two levels;
   :ref:`spell_cmd-name` for the page level
   and :ref:`config_file@project_dictionary` at the project level.
   The spell checker catches double word errors.
#. It is easy to include source code that executes
   directly below the current location; see :ref:`code_cmd-name` .
#. Source code can also be included from any location in any file;
   see the discussion of how this is different than the
   :ref:`literal_cmd@literalinclude` directive.
#. It is possible to document a feature using one language
   and implement the feature, right next to the documentation,
   using a different language; e.g., see :ref:`suspend_example-name` .
#. Automatically generates labels for linking to a heading in any page.
   These labels are designed with changing documentation in mind; e.g.,
   in this documentation the text
   ``:ref:`heading_links@Labels@Discussion``
   generates a link to :ref:`heading_links@Labels@Discussion`,
   which discusses these labels in more detail.
#. The configuration file :ref:`config_file@html_theme_options` allows for
   multiple themes and the command line argument :ref:`run_xrst@html_theme`
   enable one to chose a theme without having to change the
   configuration file.
