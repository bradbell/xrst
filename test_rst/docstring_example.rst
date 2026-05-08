.. _docstring_example-name:

!!!!!!!!!!!!!!!!!
docstring_example
!!!!!!!!!!!!!!!!!

.. meta::
    :keywords: docstring_example,docstring,example,python,factorial,this,file

.. index:: docstring_example, docstring

.. _docstring_example-title:

Docstring Example
#################

.. contents::
    :local:

.. index:: python, docstring

.. _docstring_example@Python Docstring:

Python Docstring
****************
This example demonstrates using a python docstring to document a function.
It does not have any xrst commands in the docstring, just an extra colon, :,
at the beginning and end to enable the literal command find the docstring.
This avoids having xrst commands in the corresponding python help output.
See :ref:`indent_example@Python Docstring`
for an example where the xrst input is indented and
the xrst commands are in the docstring.

.. index:: factorial

.. _docstring_example@factorial:

factorial
*********

.. literalinclude:: ../../example/docstring.py
    :lines: 38-38
    :language: py

.. _docstring_example@This Example File:

This Example File
*****************

.. literalinclude:: ../../example/docstring.py
    :language: py
