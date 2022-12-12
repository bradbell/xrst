.. _check_input_files-name:

!!!!!!!!!!!!!!!!!
check_input_files
!!!!!!!!!!!!!!!!!

xrst input file: ``xrst/check_input_files.py``

.. meta::
   :keywords: check_input_files, check, expected, xrst, input, files, are, included

.. index:: check_input_files, check, expected, xrst, input, files, are, included

.. _check_input_files-title:

Check That Expected xrst Input Files Are Included
#################################################

.. contents::
   :local:

.. meta::
   :keywords: conf_dict

.. index:: conf_dict

.. _check_input_files@conf_dict:

conf_dict
*********
is a python dictionary representation of the configuration file.

.. meta::
   :keywords: group_name

.. index:: group_name

.. _check_input_files@group_name:

group_name
**********
is the name of the group that we are checking

.. meta::
   :keywords: toc_file_set

.. index:: toc_file_set

.. _check_input_files@toc_file_set:

toc_file_set
************
is the set of files that were included by toc commands starting
at the root file for this group.
A warning is printed if a file has a begin command for this group
and it is not in *toc_file_set*.

.. _check_input_files@Syntax:

Syntax
******

.. literalinclude:: ../../xrst/check_input_files.py
   :lines: 37-45
   :language: py
