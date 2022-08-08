.. include:: xrst_preamble.rst

.. _code_example:

!!!!!!!!!!!!
code_example
!!!!!!!!!!!!

xrst input file: ``example/code.py``

.. meta::
   :keywords: code_example, code

.. index:: code_example, code

.. _@code_example:

Code Command Example
####################
.. contents::
   :local:

.. meta::
   :keywords: factorial

.. index:: factorial

.. _code_example@factorial:

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

.. _code_example@this_example_file:

This Example File
*****************

.. literalinclude:: ../../example/code.py
    :language: py
