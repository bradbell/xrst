.. include:: xrst_preamble.rst

.. _indent_example:

!!!!!!!!!!!!!!
indent_example
!!!!!!!!!!!!!!

xrst input file: ``example/indent.py``

.. meta::
   :keywords: indent_example, indent

.. index:: indent_example, indent

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
   :keywords: discussion

.. index:: discussion

.. _indent_example@discussion:

Discussion
**********
The file below demonstrates indenting an entire xrst section.
Note that underling headings works even though it is indented.

.. _indent_example@this_example_file:

This Example File
*****************

.. literalinclude:: ../../example/indent.py
    :language: py
