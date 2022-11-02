.. include:: xrst_preamble.rst

.. _test_example:

!!!!!!!!!!!!
test_example
!!!!!!!!!!!!

xrst input file: ``example/test.py``

.. meta::
   :keywords: test_example, test, special, conditions

.. index:: test_example, test, special, conditions

.. _test_example-title:

Test Special Conditions
#######################

.. contents::
   :local:

.. meta::
   :keywords: code, in, list

.. index:: code, in, list

.. _test_example@Code Command in List:

Code Command in List
********************
#. The ``{xrst_code py}`` cannot be on the first line of a list item.

   .. literalinclude:: ../../example/test.py
      :lines: 17-20
      :language: py

#. This is the second item for this list

.. meta::
   :keywords: no, newline, at, end

.. index:: no, newline, at, end

.. _test_example@No Newline at End of File:

No Newline at End of File
*************************
This example file does not have a newline at the end.

.. _test_example@This Example File:

This Example File
*****************

.. literalinclude:: ../../example/test.py
   :language: py
