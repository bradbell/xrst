.. include:: xrst_preamble.rst

.. _child_list_example:

!!!!!!!!!!!!!!!!!!
child_list_example
!!!!!!!!!!!!!!!!!!

xrst input file: ``sphinx/test_in/child_list.xrst``

.. meta::
   :keywords: child_list_example, example, child_list, command

.. index:: child_list_example, example, child_list, command

.. _@child_list_example:

Example child_list Command
###########################
.. contents::
   :local:

.. meta::
   :keywords: this, example, file

.. index:: this, example, file

.. _child_list_example@this_example_file:

This Example File
*****************
The source code for this example is indented similar to the
:ref:`@indent_exam` :

.. literalinclude:: ../../sphinx/test_in/child_list.xrst
    :language: rst

.. meta::
   :keywords: children.py, file

.. index:: children.py, file

.. _child_list_example@children.py_file:

children.py File
****************
see :ref:`child_example_one@this_example_file`
in the child_example_one section.

.. meta::
   :keywords: child, link, children.py

.. index:: child, link, children.py

.. _child_list_example@child_link_children.py:

Child Link children.py
**********************

-  :ref:`@child_example_one`
-  :ref:`@child_example_two`

.. toctree::
   :maxdepth: 1
   :hidden:

   child_example_one
   child_example_two
