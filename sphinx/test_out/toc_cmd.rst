.. include:: xrst_preamble.rst

.. _toc_cmd:

!!!!!!!
toc_cmd
!!!!!!!

xrst input file: ``xrst/toc_commands.py``

.. meta::
   :keywords: toc_cmd, table, children, commands

.. index:: toc_cmd, table, children, commands

.. _@toc_cmd:

Table of Children Commands
##########################
.. contents::
   :local:

.. _toc_cmd@syntax:

Syntax
******

.. meta::
   :keywords: hidden

.. index:: hidden

.. _toc_cmd@syntax@hidden:

hidden
======
| ``{xrst_toc_hidden``
|   *file_1*
|   ...
|   *file_n*
| :code:`}`

.. meta::
   :keywords: list

.. index:: list

.. _toc_cmd@syntax@list:

list
====
| ``{xrst_toc_list``
|   *file_1*
|   ...
|   *file_n*
| :code:`}`

.. meta::
   :keywords: table

.. index:: table

.. _toc_cmd@syntax@table:

table
=====
| ``{xrst_toc_table``
|   *file_1*
|   ...
|   *file_n*
| :code:`}`

.. meta::
   :keywords: table, contents

.. index:: table, contents

.. _toc_cmd@table_of_contents:

Table of Contents
*****************
These commands specify the section that are children
of the current section; i.e., sections that are at the
next level in the table of contents.

.. meta::
   :keywords: names

.. index:: names

.. _toc_cmd@file_names:

File Names
**********
A new line character must precede and follow each
of the file names *file_1* ... *file_n*.
Leading and trailing white space is not included in the names
The file names are  relative to the directory where
:ref:`run_xrst@root_file` is located.
This may seem verbose, but it makes it easier to write scripts
that move files and automatically change references to them.

.. meta::
   :keywords: children

.. index:: children

.. _toc_cmd@children:

Children
********
Each of the files may contain multiple :ref:`sections<begin_cmd@section>`.
The first of these sections may use a
:ref:`parent begin<begin_cmd@parent_section>` command.

#. The first section in a file is always a child of the
   section where the toc command appears..

#. If the first section in a file is a begin parent section,
   the other sections in the file are children of the frist section.
   Hence the other sections are grand children of the section
   where the begin toc command appears.

#. If there is no begin parent command in a file,
   all the sections in the file are children of the
   section where the toc command appears.

#. If the first section in a file is a begin parent section,
   and there is also a toc command in this section,
   links to the toc command children come first and then links to
   the children that are other sections in the same file.

.. meta::
   :keywords: child, links

.. index:: child, links

.. _toc_cmd@child_links:

Child Links
***********
#. The toc_list syntax generates links to the children that
   display the title for each section.
   The toc_table syntax generates links to the children that
   display both the section name and section tile.

#. If a section has a toc_list or toc_table command,
   links to all the children of the section are placed where the
   toc command is located.
   You can place a heading directly before the these commands
   to make the links easier to find.

#. If a section uses the hidden syntax,
   no automatic links to the children of the current section are generated.

#. If a section does not have a toc command,
   and it has a begin parent command,
   links to the children of the section are placed at the end of the section.

.. meta::
   :keywords: toctree

.. index:: toctree

.. _toc_cmd@toctree:

toctree
*******
This command replaces the sphinx ``toctree`` directive.
A ``toctree`` directive is automatically generated and includes each
section that is a child of the current section.

.. _toc_cmd@example:

Example
*******
:ref:`toc_list_example`
