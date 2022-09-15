.. include:: xrst_preamble.rst

.. _indent_example:

!!!!!!!!!!!!!!
indent_example
!!!!!!!!!!!!!!

xrst input file: ``example/indent.py``

.. meta::
   :keywords: indent_example, indent

.. index:: indent_example, indent

.. _indent_example-0:

Indent Example
##############
.. contents::
   :local:

.. code-block:: py

   def factorial(n) :
      if n == 1 :
         return 1
      return n * factorial(n-1)

.. meta::
   :keywords: discussion

.. index:: discussion

.. _indent_example@Discussion:

Discussion
**********
The file below demonstrates indenting an entire xrst page.
Note that underling headings works even though it is indented.

.. _indent_example@This Example File:

This Example File
*****************

.. literalinclude:: ../../example/indent.py
   :language: py
