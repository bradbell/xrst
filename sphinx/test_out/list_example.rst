.. include:: xrst_preamble.rst

.. _list_example:

!!!!!!!!!!!!
list_example
!!!!!!!!!!!!

xrst input file: ``example/list.py``

.. meta::
   :keywords: list_example, using, commands, in, list

.. index:: list_example, using, commands, in, list

.. _list_example-0:

Example using Commands in a List
################################
.. contents::
   :local:

.. meta::
   :keywords: code

.. index:: code

.. _list_example@Code Command:

Code Command
************
#. The ``{xrst_code py}`` cannot be on the first line of a list item.

   .. literalinclude:: ../../example/list.py
      :lines: 16-19
      :language: py

#. This is the second item for this list

.. meta::
   :keywords: rst, directive

.. index:: rst, directive

.. _list_example@RST Directive:

RST Directive
*************
#. This list demonstrates using an rst directive in a list
   .. csv_table::

      a11, a12
      a21, a22

#. This is the second item for this list

.. _list_example@This Example File:

This Example File
*****************

.. literalinclude:: ../../example/list.py
   :language: py
