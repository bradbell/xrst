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

   .. code-block:: py

      def factorial(n) :
         if n == 1 :
            return 1
         return n * factorial(n-1)

#. This is the first line of the next list item.

.. meta::
   :keywords: lists

.. index:: lists

.. _list_example@Lists:

Lists
*****
The file below demonstrates using xrst commands in a list item.

.. _list_example@This Example File:

This Example File
*****************

.. literalinclude:: ../../example/list.py
   :language: py
