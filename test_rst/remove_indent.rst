.. _remove_indent-name:

!!!!!!!!!!!!!
remove_indent
!!!!!!!!!!!!!

.. meta::
   :keywords: remove_indent, remove, indentation, page

.. index:: remove_indent, remove, indentation, page

.. _remove_indent-title:

Remove indentation for a page
#############################

.. contents::
   :local:

.. meta::
   :keywords: prototype

.. index:: prototype

.. _remove_indent@Prototype:

Prototype
*********

.. literalinclude:: ../../xrst/remove_indent.py
   :lines: 58-61,72-73
   :language: py

.. meta::
   :keywords: data_in

.. index:: data_in

.. _remove_indent@data_in:

data_in
*******
is the data for this page.

.. meta::
   :keywords: file_name

.. index:: file_name

.. _remove_indent@file_name:

file_name
*********
is the input that this page appears in (used for error reporting).

.. meta::
   :keywords: page_name

.. index:: page_name

.. _remove_indent@page_name:

page_name
*********
is the name of this page (used for error reporting).

.. meta::
   :keywords: data_out

.. index:: data_out

.. _remove_indent@data_out:

data_out
********
is a copy of data_in with the indentation for this section removed.
