.. include:: xrst_preamble.rst

.. _newline_indices:

!!!!!!!!!!!!!!!
newline_indices
!!!!!!!!!!!!!!!

xrst input file: ``xrst/newline_indices.py``

.. meta::
   :keywords: newline_indices, find, index, all, newlines, in, string

.. index:: newline_indices, find, index, all, newlines, in, string

.. _newline_indices-0:

Find index of all the newlines in a string
##########################################
.. contents::
   :local:

.. meta::
   :keywords: data

.. index:: data

.. _newline_indices@data:

data
****
The string we are searching for newlines.

.. meta::
   :keywords: newline_list

.. index:: newline_list

.. _newline_indices@newline_list:

newline_list
************
The return newline_list is the list of indices in data that
represent all of the newlines; i.e. '\n'.

.. literalinclude:: ../../xrst/newline_indices.py
   :lines: 25-29
   :language: py
