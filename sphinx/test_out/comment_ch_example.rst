.. include:: xrst_preamble.rst

.. _comment_ch_example:

!!!!!!!!!!!!!!!!!!
comment_ch_example
!!!!!!!!!!!!!!!!!!

xrst input file: ``example/comment_ch.py``

.. meta::
   :keywords: comment_ch_example, comment, character, command, example

.. index:: comment_ch_example, comment, character, command, example

.. _@comment_ch_example:

Comment Character Command Example
#################################
.. contents::
   :local:

.. meta::
   :keywords: discussion

.. index:: discussion

.. _comment_ch_example@discussion:

Discussion
**********
The ``#`` at the beginning of a line,
and space directly after it, are removed.
The remaining text lines up with the first line in the
function definition below:

.. code-block:: py

    def factorial(n) :
        if n == 1 :
            return 1
        return n * factorial(n-1)

.. meta::
   :keywords: this, example, file

.. index:: this, example, file

.. _comment_ch_example@this_example_file:

This Example File
*****************
The file below demonstrates the use of ``xrst_comment_ch`` :

.. literalinclude:: ../../example/comment_ch.py
    :language: py
