.. include:: xrst_preamble.rst

.. _code_example:

!!!!!!!!!!!!
code_example
!!!!!!!!!!!!

xrst input file: ``example/code.py``

.. meta::
   :keywords: code_example, code

.. index:: code_example, code

.. _code_example-0:

Code Command Example
####################
.. contents::
   :local:

.. meta::
   :keywords: factorial

.. index:: factorial

.. _code_example@Factorial:

Factorial
*********

.. code-block:: py

   def factorial(n) :
      if n == 1 :
         return 1
      return n * factorial(n-1)

.. meta::
   :keywords: xrst_code

.. index:: xrst_code

.. _code_example@xrst_code:

xrst_code
*********
The file below demonstrates the use of ``xrst_code`` .

.. _code_example@This Example File:

This Example File
*****************

.. literalinclude:: ../../example/code.py
   :language: py
