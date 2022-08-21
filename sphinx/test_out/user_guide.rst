.. include:: xrst_preamble.rst

.. _user_guide:

!!!!!!!!!!
user_guide
!!!!!!!!!!

xrst input file: ``xrst.xrst``

.. meta::
   :keywords: user_guide, extract, sphinx, rst, files

.. index:: user_guide, extract, sphinx, rst, files

.. _@user_guide:

Extract Sphinx RST Files
########################
.. contents::
   :local:

.. meta::
   :keywords: version

.. index:: version

.. _user_guide@version_2022.8.20:

Version 2022.8.20
******************

.. meta::
   :keywords: git, repository

.. index:: git, repository

.. _user_guide@git_repository:

Git Repository
**************
https://github.com/bradbell/xrst

.. meta::
   :keywords: pip, install

.. index:: pip, install

.. _user_guide@pip_install:

Pip Install
***********
-   ``pip install --index-url https://test.pypi.org/simple/ xrst``

.. meta::
   :keywords: run, program

.. index:: run, program

.. _user_guide@run_program:

Run Program
***********
:ref:`@run_xrst`

.. _user_guide@purpose:

Purpose
*******
This is a pseudo sphinx extension that provides the features listed below.
It was motivated by cases like the GNU Scientific library,
which is not written in python, uses sphinx, and has its documentation
in separate files from the corresponding source code; see `gsl doc`_ .

.. _gsl doc: https://git.savannah.gnu.org/cgit/gsl.git/tree/doc

#.  The rst file name is used as an abbreviated title
    in the navigation bar. This makes the navigation bar more useful
    while also having long descriptive titles.
#.  Each section (rst file) has a contents tree for its headings
    that is separate from the contents tree for the sections. This makes it
    easy to move sections to different places in the sections contents tree.
#.  Puts a jump table to headings that is a contents tree at the top of each
    section because the navigation bar does not include this information.
#.  Makes it easy to put documentation in source code comments
    when multiple computer languages are used by one package;
    e.g., see :ref:`comment_ch_cmd` .
#.  Allows the documentation for one section to span multiple locations
    in source code; see :ref:`suspend_cmd`.
#.  Allows for multiple sections to be specified by one
    input file. One section can be the parent for the
    other sections in the same file; see :ref:`begin_cmd` .
#.  Allows one to build subsets of the documentation; e.g., user, developer,
    examples. Sections for different subsets can be in the
    same input file; see :ref:`run_xrst@group_list`.
#.  Unlike doxygen and autodoc, xrst organizes  the contents tree
    for sections using commands that include files;
    see :ref:`child_cmd`. This enables one to group functions or classes
    into one section of the documentation.
#.  Includes a configurable spell checker; see
    :ref:`spell_cmd` and :ref:`run_xrst@sphinx_dir@spelling` .
    The spell checker catches double word errors.
#.  Words in each heading are automatically included in the
    keyword index in a way that can be configured;
    see :ref:`run_xrst@sphinx_dir@keyword` .
#.  Makes it easy to include source code that executes
    directly below the current location; see :ref:`code_cmd` .
#.  Source code can also be included from any location and any file;
    see :ref:`file_cmd`.
    This uses tokens in source code, not line numbers,
    to signify start and stop of the inclusion.
    This makes it easy to move things, like function prototypes,
    to different places in the documentation.
#.  Automatically generates labels for linking to a heading in any section.
    These labels are designed with changing documentation in mind; e.g.,
    in this documentation the text
    ``:ref:`heading_links@labels@discussion``
    generates the following link (which discusses these labels)
    :ref:`heading_links@labels@discussion`.

.. meta::
   :keywords: contents

.. index:: contents

.. _user_guide@contents:

Contents
********

-  :ref:`@run_xrst`
-  :ref:`@commands`
-  :ref:`@automatic`

.. toctree::
   :maxdepth: 1
   :hidden:

   run_xrst
   commands
   automatic
