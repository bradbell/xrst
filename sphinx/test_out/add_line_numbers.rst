.. include:: xrst_preamble.rst

.. _add_line_numbers:

!!!!!!!!!!!!!!!!
add_line_numbers
!!!!!!!!!!!!!!!!

xrst input file: ``xrst/add_line_numbers.py``

.. meta::
   :keywords: add_line_numbers, add, line, numbers, data

.. index:: add_line_numbers, add, line, numbers, data

.. _add_line_numbers-0:

Add Line Numbers to File Data
#############################
.. contents::
   :local:

Add line numbers to a string in a way that is useful for reporting errors
(for modified versions of string) using line number in the original string.

.. meta::
   :keywords: data_in

.. index:: data_in

.. _add_line_numbers@data_in:

data_in
*******
The original string.  An empty line is a line with just spaces or tabs.
line_number is the number of newlines before a line plus one; i.e.,
the first line is number one.

.. meta::
   :keywords: data_out

.. index:: data_out

.. _add_line_numbers@data_out:

data_out
********
The return data_out is a modified version of data_in. The text

 | ``{xrst_line`` *line_number@*

is added at the end of each non-empty line.
Spaces and tabs in empty lines are removed (so they are truely empty).

.. literalinclude:: ../../xrst/add_line_numbers.py
   :lines: 37-40
   :language: py
