.. include:: xrst_preamble.rst

.. _remove_line_numbers:

!!!!!!!!!!!!!!!!!!!
remove_line_numbers
!!!!!!!!!!!!!!!!!!!

xrst input file: ``xrst/remove_line_numbers.py``

.. meta::
   :keywords: remove_line_numbers, remove, number, numbers

.. index:: remove_line_numbers, remove, number, numbers

.. _remove_line_numbers-title:

Remove the number numbers
#########################

.. contents::
   :local:

.. meta::
   :keywords: arguments

.. index:: arguments

.. _remove_line_numbers@Arguments:

Arguments
*********

.. meta::
   :keywords: data_in

.. index:: data_in

.. _remove_line_numbers@Arguments@data_in:

data_in
=======
is a string with line number markers added by :ref:`add_line_numbers` .
These lines number markers have the form:

    ``{xrst_line`` *line_number* ``@`` .

.. meta::
   :keywords: returns

.. index:: returns

.. _remove_line_numbers@Returns:

Returns
*******

.. meta::
   :keywords: data_out

.. index:: data_out

.. _remove_line_numbers@Returns@data_out:

data_out
========
The return data_out is a copy of data_in with the
line number markers removed.

.. meta::
   :keywords: line_pair

.. index:: line_pair

.. _remove_line_numbers@Returns@line_pair:

line_pair
=========
The second return line_pair is a list of two element tuples.

-   The first element is the line number in data_out corresponding to
    the line number marker that was removed.
    These line numbers, in data_out, do not count
    lines that only contain ``{xrst_page_number}`` .

-   The second element is the *line_number*, in the line number marker,
    that was removed.

.. literalinclude:: ../../xrst/remove_line_numbers.py
   :lines: 49-50
   :language: py

.. literalinclude:: ../../xrst/remove_line_numbers.py
   :lines: 107-114
   :language: py
