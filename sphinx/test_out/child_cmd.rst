.. include:: xrst_preamble.rst

.. _child_cmd:

!!!!!!!!!
child_cmd
!!!!!!!!!

xrst input file: ``xrst/child_commands.py``

.. meta::
   :keywords: child_cmd, child, commands

.. index:: child_cmd, child, commands

.. _@child_cmd:

Child Commands
##############
.. contents::
   :local:

.. _child_cmd@syntax:

Syntax
******

.. meta::
   :keywords: children

.. index:: children

.. _child_cmd@syntax@children:

children
========
| ``{xrst_children``
|   *file_1*
|   ...
|   *file_n*
| :code:`}`

.. meta::
   :keywords: child_list

.. index:: child_list

.. _child_cmd@syntax@child_list:

child_list
==========
| ``{xrst_child_list``
|   *file_1*
|   ...
|   *file_n*
| :code:`}`

.. meta::
   :keywords: child_table

.. index:: child_table

.. _child_cmd@syntax@child_table:

child_table
===========
| ``{xrst_child_table``
|   *file_1*
|   ...
|   *file_n*
| :code:`}`

.. _child_cmd@purpose:

Purpose
*******
These commands specify the section that are children
of the current section.

.. meta::
   :keywords: names

.. index:: names

.. _child_cmd@file_names:

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

.. _child_cmd@children:

Children
********
Each of the files may contain multiple :ref:`sections<begin_cmd@section>`.
The first of these sections may use a
:ref:`parent begin<begin_cmd@parent_section>` command.

#.  The first section in a file is always a child of the
    section where the child command appears..

#.  If the first section in a file is a begin parent section,
    the other sections in the file are children of the frist section.
    Hence the other sections are grand children of the section
    where the begin child command appears.

#.  If there is no begin parent command in a file,
    all the sections in the file are children of the
    section where the child command appears.

#.  If the first section in a file is a begin parent section,
    and there is also a child command in this section,
    links to the child command children come first and then links to
    the children that are other sections in the same file.

.. meta::
   :keywords: child, links

.. index:: child, links

.. _child_cmd@child_links:

Child Links
***********
#.  The child_list syntax generates links to the children that
    display the title for each section.
    The child_table syntax generates links to the children that
    display both the section name and section tile.

#.  If a section has a child_list or child_table command,
    links to all the children of the section are placed where the
    child command is located.
    You can place a heading directly before the these commands
    to make the links easier to find.

#.  If a section uses the children syntax,
    no automatic links to the children of the current section are generated.

#.  If a section does not have a child command,
    and it has a begin parent command,
    links to the children of the section are placed at the end of the section.

.. meta::
   :keywords: table, contents,, toctree

.. index:: table, contents,, toctree

.. _child_cmd@table_of_contents,_toctree:

Table of Contents, toctree
**************************
A sphinx ``toctree`` directive is automatically generated for each
section that has children. This directive has the hidden attribute so that
one can control the links to the children using the syntax choices above.

.. _child_cmd@example:

Example
*******
:ref:`child_list_example`
