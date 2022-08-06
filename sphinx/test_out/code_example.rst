.. include:: xrst_preamble.rst

.. _code_example:

!!!!!!!!!!!!
code_example
!!!!!!!!!!!!

xrst input file: ``sphinx/test_in/code.py``

.. meta::
   :keywords: code_example, code, command, example

.. index:: code_example, code, command, example

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
   :keywords: this, example, file

.. index:: this, example, file

.. _code_example@this_example_file:

This Example File
*****************

.. literalinclude:: ../../sphinx/test_in/code.py
    :language: py
