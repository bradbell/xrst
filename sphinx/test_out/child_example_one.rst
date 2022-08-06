.. include:: xrst_preamble.rst

.. _child_example_one:

!!!!!!!!!!!!!!!!!
child_example_one
!!!!!!!!!!!!!!!!!

xrst input file: ``sphinx/test_in/children.py``

.. meta::
   :keywords: child_example_one, first, child

.. index:: child_example_one, first, child

.. _@child_example_one:

First Child
###########
.. contents::
   :local:

This section is the first child in this file.
This file does not contain a begin parent command,
so all its sections are children of the section that includes this file.

.. meta::
   :keywords: link, to, second, child

.. index:: link, to, second, child

.. _child_example_one@link_to_second_child:

Link to Second Child
********************
:ref:`child_example_two`

.. meta::
   :keywords: this, example, file

.. index:: this, example, file

.. _child_example_one@this_example_file:

This Example File
*****************

.. literalinclude:: ../../sphinx/test_in/children.py
    :language: py
