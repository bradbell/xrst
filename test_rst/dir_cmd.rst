.. _dir_cmd-name:

!!!!!!!
dir_cmd
!!!!!!!

.. meta::
   :keywords: dir_cmd, convert, name, from, project, directory, rst, directory

.. index:: dir_cmd, convert, name, from, project, directory, rst, directory

.. _dir_cmd-title:

Convert a File Name From Project Directory to RST Directory
###########################################################

.. contents::
   :local:

.. _dir_cmd@Syntax:

Syntax
******
``{xrst_dir`` *file_name* ``}``

.. _dir_cmd@Purpose:

Purpose
*******
This command converts a file name relative to the
:ref:`config_file@directory@project_directory` to be relative to the
:ref:`config_file@directory@rst_directory` so it can be used by
sphinx commands.

.. meta::
   :keywords: file_name

.. index:: file_name

.. _dir_cmd@file_name:

file_name
*********
Is a file name relative to the project directory.
The entire command gets replaced by a name for the same file
relative to the rst directory.
Leading and trailing white space in *file_name* is ignored.

.. _dir_cmd@Example:

Example
*******
:ref:`dir_example-name`
