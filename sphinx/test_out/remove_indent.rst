.. include:: xrst_preamble.rst

.. _remove_indent:

!!!!!!!!!!!!!
remove_indent
!!!!!!!!!!!!!

xrst input file: ``xrst/remove_indent.py``

.. meta::
   :keywords: remove_indent, remove, indentation, page

.. index:: remove_indent, remove, indentation, page

.. _remove_indent-0:

Remove indentation for a page
#############################
.. contents::
   :local:

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

.. meta::
   :keywords: indent

.. index:: indent

.. _remove_indent@indent:

indent
******
is the white space that was removed from each line (except for empty lines)

.. literalinclude:: ../../xrst/remove_indent.py
   :lines: 53-59
   :language: py
