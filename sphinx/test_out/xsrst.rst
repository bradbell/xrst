.. include:: ../preamble.rst

!!!!!
xsrst
!!!!!

.. toctree::
   :maxdepth: 1
   :hidden:

   commands
   other_processing
   wish_list
   release_notes
   xsrst.py

.. meta::
   :keywords: xsrst, extract, sphinx, rst, files

.. index:: xsrst, extract, sphinx, rst, files

.. _xsrst:

Extract Sphinx RST Files
########################
.. contents::
   :local:

.. meta::
   :keywords: version, 2021.9.7

.. index:: version, 2021.9.7

.. _xsrst@version_2021.9.7:

Version 2021.9.7
******************

.. meta::
   :keywords: git, repository

.. index:: git, repository

.. _xsrst@git_repository:

Git Repository
**************
https://github.com/bradbell/xsrst

.. meta::
   :keywords: program

.. index:: program

.. _xsrst@program:

Program
********

:ref:`xsrst@py<xsrst.py>`

.. meta::
   :keywords: purpose

.. index:: purpose

.. _xsrst@purpose:

Purpose
*******
This is a pseudo sphinx extension that provides the following features:

#.  The rst file name for each section is also an abbreviated title used
    in the navigation bar and for linking to the section. This makes the
    navigation bar more useful while also having long descriptive titles.
    It also makes cross reference linking from other sections easier.
#.  Each section has its own table of contents (for its headings) that is
    separate from the table of contents for the sections. This makes it
    easy to move sections to different places in the over all structure.
#.  Enables documentation in the comments for source code
    when multiple computer languages are used for one package.
    Allows the documentation for one section to span multiple locations
    in the source code; see :ref:`suspend command<suspend_cmd>`.
#.  Allows for multiple sections (rst output files) to be specified by one
    input file. In addition, one section can be the parent for the
    other sections in a file.
#.  Generates the table of contents from the specification
    of which files are included; see :ref:`child commands<child_cmd>`.
    Generates a jump table to the headings for each section
    so that the navigation bar need not include this information.
#.  Includes a configurable :ref:`spell checker<spell_cmd>` and
    :ref:`index<genindex>`. The spell checker catches double word errors.
    Words in each heading are automatically included in the index.
#.  Makes it easy to include source code that also executes, from
    directly below the :ref:`code command<code_cmd>` or from
    a different location in a :ref:`file<file_cmd>`.
    This uses tokens in the source, not line numbers,
    to signify start and stop of inclusion from a file.

.. meta::
   :keywords: requirements

.. index:: requirements

.. _xsrst@requirements:

Requirements
************
-   ``pip install --user pyspellchecker``
-   ``pip install --user sphinx``
-   ``pip install --user sphinx-rtd-theme``

----

xsrst input file: ``doc.xsrst``
