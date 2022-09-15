.. include:: xrst_preamble.rst

.. _toc_list_example:

!!!!!!!!!!!!!!!!
toc_list_example
!!!!!!!!!!!!!!!!

xrst input file: ``example/toc_list.xrst``

.. meta::
   :keywords: toc_list_example, toc_list

.. index:: toc_list_example, toc_list

.. _toc_list_example-0:

toc_list Command Example
########################
.. contents::
   :local:

.. meta::
   :keywords: children.py

.. index:: children.py

.. _toc_list_example@children.py File:

children.py File
****************
see :ref:`child_example_one@This Example File`
in the child_example_one page.

.. meta::
   :keywords: toc_list

.. index:: toc_list

.. _toc_list_example@toc_list Command:

toc_list Command
****************

-  :ref:`child_example_one-0`
-  :ref:`child_example_two-0`

.. meta::
   :keywords: xrst_toc_list

.. index:: xrst_toc_list

.. _toc_list_example@xrst_toc_list:

xrst_toc_list
*************
The file below demonstrates the use of ``xrst_toc_list`` .

.. _toc_list_example@This Example File:

This Example File
*****************

.. literalinclude:: ../../example/toc_list.xrst
   :language: rst

.. toctree::
   :maxdepth: 1
   :hidden:

   child_example_one
   child_example_two
