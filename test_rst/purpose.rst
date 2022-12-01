.. include:: xrst_preamble.rst

.. _purpose-name:

!!!!!!!
purpose
!!!!!!!

xrst input file: ``user/user.xrst``

.. meta::
   :keywords: purpose, need, xrst

.. index:: purpose, need, xrst

.. _purpose-title:

The Need for xrst
#################

This is a sphinx wrapper that provides the features listed below.
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
#. Makes it easy to put documentation in source code comments,
   even when multiple computer languages are used by one package;
   e.g., see :ref:`comment_ch_cmd-name` .
#. Multiple pages can be specified in one
   input file and one page can be the parent for the
   other pages in the same file; see :ref:`begin_cmd-name` .
#. One can build subsets of the documentation; e.g., user, developer,
   examples. Pages for different subsets can be in the
   same input file; see :ref:`run_xrst@group_list`.
#. Words in each heading are automatically included in the
   index in a way that can be configured;
   see :ref:`toml_file@not_in_index` .
   These words are also automatically included as html keyword meta data.
#. Includes a spell checker with special words at two levels;
   :ref:`spell_cmd-name` for the page level
   and :ref:`toml_file@project_dictionary` at the project level.
   The spell checker catches double word errors.
#. Makes it easy to include source code that executes
   directly below the current location; see :ref:`code_cmd-name` .
#. Source code can also be included from any location and any file;
   see :ref:`literal_cmd-name`.
   This uses tokens in source code, not line numbers,
   to signify start and stop of the inclusion.
   This makes it easy to move things, like function prototypes,
   to different places in the documentation.
#. It is possible to document a feature using one language
   and implement the feature using a different language; e.g.,
   see :ref:`suspend_example-name` .
#. The rst file name is used as an abbreviated title
   in the navigation bar. This makes the navigation bar more useful
   while also having long descriptive titles attached to each page.
#. Each page (rst file) has a contents tree for its headings
   that is separate from the contents tree for the pages. This makes it
   easier to move pages to different places in the pages contents tree.
#. Automatically generates labels for linking to a heading in any page.
   These labels are designed with changing documentation in mind; e.g.,
   in this documentation the text
   ``:ref:`heading_links@Labels@Discussion``
   generates a link to :ref:`heading_links@Labels@Discussion`,
   which discusses these labels.
