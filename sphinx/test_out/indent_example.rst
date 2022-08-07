.. include:: xrst_preamble.rst

.. _indent_example:

!!!!!!!!!!!!!!
indent_example
!!!!!!!!!!!!!!

xrst input file: ``sphinx/test_in/indent.py``

.. meta::
   :keywords: indent_example, indent, example

.. index:: indent_example, indent, example

.. _@indent_example:

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
   :keywords: this, example, file

.. index:: this, example, file

.. _indent_example@this_example_file:

This Example File
*****************

.. literalinclude:: ../../sphinx/test_in/indent.py
    :language: py
