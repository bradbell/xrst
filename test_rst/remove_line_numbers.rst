.. _remove_line_numbers-name:

!!!!!!!!!!!!!!!!!!!
remove_line_numbers
!!!!!!!!!!!!!!!!!!!

.. meta::
   :keywords: remove_line_numbers, remove, number, numbers

.. index:: remove_line_numbers, remove, number, numbers

.. _remove_line_numbers-title:

Remove the number numbers
#########################

.. contents::
   :local:

.. meta::
   :keywords: prototype

.. index:: prototype

.. _remove_line_numbers@Prototype:

Prototype
*********

.. literalinclude:: ../../xrst/remove_line_numbers.py
   :lines: 74-75,179-186
   :language: py

.. meta::
   :keywords: data_in

.. index:: data_in

.. _remove_line_numbers@data_in:

data_in
*******
is a string with line number markers added by :ref:`add_line_numbers-name` .
These lines number markers have the form:

    ``@xrst_line`` *line_number* ``@`` .

.. meta::
   :keywords: data_out

.. index:: data_out

.. _remove_line_numbers@data_out:

data_out
********
The return data_out is a copy of data_in with the
line number markers removed.

.. meta::
   :keywords: rst2xrst_list

.. index:: rst2xrst_list

.. _remove_line_numbers@rst2xrst_list:

rst2xrst_list
*************
The second return rst2xrst_list is a list of tuples.
Each tuple in the list has two or four elements.

.. meta::
   :keywords: first, tuple, element

.. index:: first, tuple, element

.. _remove_line_numbers@rst2xrst_list@First Tuple Element:

First Tuple Element
===================
is the line number in *data_out* corresponding to a line number marker
that was removed from *data_in* .
The lines in *data_out*  still contain the ``{xrst@before_title}`` commands
that were in *data_in*.
These are not included in the line number could (because they are
removed before writing its rst file).

.. meta::
   :keywords: second, tuple, element

.. index:: second, tuple, element

.. _remove_line_numbers@rst2xrst_list@Second Tuple Element:

Second Tuple Element
====================
The second tuple element is the line number in the file that contains
the begin command for this page.

.. meta::
   :keywords: third, tuple, element

.. index:: third, tuple, element

.. _remove_line_numbers@rst2xrst_list@Third Tuple Element:

Third Tuple Element
===================
This element is present If the current line in *data_out* is
part of a template expansion.
In this case, the third element is the template file name.

.. meta::
   :keywords: fourth, tuple, element

.. index:: fourth, tuple, element

.. _remove_line_numbers@rst2xrst_list@Fourth Tuple Element:

Fourth Tuple Element
====================
This element is present If the current line in *data_out* is
part of a template expansion.
In this case, the fourth element is the line in the template file.

.. meta::
   :keywords: fourthtuple, element

.. index:: fourthtuple, element

.. _remove_line_numbers@rst2xrst_list@FourthTuple Element:

FourthTuple Element
===================
If the current line in data_out corresponds to a template file,
this is the line number in the template file. Otherwise, it is None.
