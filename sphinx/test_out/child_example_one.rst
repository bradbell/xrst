.. include:: xrst_preamble.rst

.. _child_example_one:

!!!!!!!!!!!!!!!!!
child_example_one
!!!!!!!!!!!!!!!!!

xrst input file: ``example/children.xrst``

.. meta::
   :keywords: child_example_one, first, child

.. index:: child_example_one, first, child

.. _child_example_one-0:

First Child
###########
This page is the first child in this file.
This file does not contain a begin parent command,
so all its pages are children of the page that includes this file.

.. contents::
   :local:

.. meta::
   :keywords: link, second, child

.. index:: link, second, child

.. _child_example_one@Link to Second Child:

Link to Second Child
********************
:ref:`child_example_two`

.. _child_example_one@This Example File:

This Example File
*****************

.. literalinclude:: ../../example/children.xrst
   :language: rst
