.. include:: xrst_preamble.rst

.. _remove_line_numbers:

!!!!!!!!!!!!!!!!!!!
remove_line_numbers
!!!!!!!!!!!!!!!!!!!

xrst input file: ``xrst/remove_line_numbers.py``

.. meta::
   :keywords: remove_line_numbers, remove, number, numbers

.. index:: remove_line_numbers, remove, number, numbers

.. _remove_line_numbers-0:

Remove the number numbers
#########################
.. contents::
   :local:

.. meta::
   :keywords: data_in

.. index:: data_in

.. _remove_line_numbers@data_in:

data_in
*******
is a string with line numbers added by :ref:`add_line_numbers` .
These have the form: ``{xrst_line`` *number* ``@`` .

.. meta::
   :keywords: data_out

.. index:: data_out

.. _remove_line_numbers@data_out:

data_out
********
The return data_out is a copy of data_in with the line numbers removed.

.. meta::
   :keywords: line_pair

.. index:: line_pair

.. _remove_line_numbers@line_pair:

line_pair
*********
The second return line_pair is a list of two element tuples.
The first element is the line number in data_out not counting the\n lines. The second element is the corresponding
line number that has been removed.

.. literalinclude:: ../../xrst/remove_line_numbers.py
   :lines: 36-43
   :language: py
