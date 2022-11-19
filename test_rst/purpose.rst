.. include:: xrst_preamble.rst

.. _purpose:

!!!!!!!
purpose
!!!!!!!

xrst input file: ``xrst.xrst``

.. meta::
   :keywords: purpose, need, xrst

.. index:: purpose, need, xrst

.. _purpose-title:

The Need for xrst
#################

This is a pseudo sphinx extension that provides the features listed below.
It was motivated by cases like the GNU Scientific library,
which is not written in python, uses sphinx, and has its documentation
in separate files from the corresponding source code; see `gsl doc`_ .
It provides a system that extracts documentation from any source code
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
#. Makes it easy to put documentation in source code comments
   when multiple computer languages are used by one package;
   e.g., see :ref:`comment_ch_cmd` .
#. Multiple pages can be specified in one
   input file and one page can be the parent for the
   other pages in the same file; see :ref:`begin_cmd` .
#. One can build subsets of the documentation; e.g., user, developer,
   examples. Pages for different subsets can be in the
   same input file; see :ref:`run_xrst@group_list`.
#. Documentation for one page can span multiple locations
   in source code; see :ref:`suspend_cmd`.
#. Organizes the contents tree
   for pages using commands that include files;
   see :ref:`toc_cmd`. This enables one to group multiple functions or classes
   into one page of the documentation.
#. Words in each heading are automatically included in the
   index in a way that can be configured;
   see :ref:`xrst.toml@not_in_index` .
#. Includes a configurable spell checker; see
   :ref:`spell_cmd` and :ref:`xrst.toml@project_dictionary` .
   The spell checker catches double word errors.
#. Makes it easy to include source code that executes
   directly below the current location; see :ref:`code_cmd` .
#. Source code can also be included from any location and any file;
   see :ref:`literal_cmd`.
   This uses tokens in source code, not line numbers,
   to signify start and stop of the inclusion.
   This makes it easy to move things, like function prototypes,
   to different places in the documentation.
#. The rst file name is used as an abbreviated title
   in the navigation bar. This makes the navigation bar more useful
   while also having long descriptive titles.
#. Each page (rst file) has a contents tree for its headings
   that is separate from the contents tree for the pages. This makes it
   easier to move pages to different places in the pages contents tree.
#. Automatically generates labels for linking to a heading in any page.
   These labels are designed with changing documentation in mind; e.g.,
   in this documentation the text
   ``:ref:`heading_links@Labels@Discussion``
   generates a link to :ref:`heading_links@Labels@Discussion`,
   which discusses these labels.