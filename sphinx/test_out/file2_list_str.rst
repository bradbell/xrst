.. include:: xrst_preamble.rst

.. _file2_list_str:

!!!!!!!!!!!!!!
file2_list_str
!!!!!!!!!!!!!!

xrst input file: ``xrst/file2_list_str.py``

.. meta::
   :keywords: file2_list_str, convert, lines, in, list, strings

.. index:: file2_list_str, convert, lines, in, list, strings

.. _file2_list_str-title:

Convert lines in a file to a list of strings
############################################

.. contents::
   :local:

.. meta::
   :keywords: file_name

.. index:: file_name

.. _file2_list_str@file_name:

file_name
*********
is the name of the file that we are converting.

.. meta::
   :keywords: list_str

.. index:: list_str

.. _file2_list_str@list_str:

list_str
********
the return value is a list of str, one for each line of the file.

#. Lines that begin with the # character are not included.
#. Leading and trailing spaces ' ', tabs '\t', and the newline '\n'
   are not included.
#. Empty lines, after step 2, are not included.

.. literalinclude:: ../../xrst/file2_list_str.py
   :lines: 28-33
   :language: py
