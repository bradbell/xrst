.. include:: xrst_preamble.rst

.. _heading_exam:

!!!!!!!!!!!!
heading_exam
!!!!!!!!!!!!

xrst input file: ``sphinx/test_in/heading.py``

.. meta::
   :keywords: heading_exam, heading, example

.. index:: heading_exam, heading, example

.. _@heading_exam:

Heading Example
###############
.. contents::
   :local:

.. meta::
   :keywords: child, file

.. index:: child, file

.. _heading_exam@child_file:

Child File
**********

.. literalinclude:: ../../sphinx/test_in/heading.py
    :lines: 34-74
    :language: py

.. meta::
   :keywords: example, heading

.. index:: example, heading

.. _heading_exam@example_heading:

Example Heading
***************
The example heading below (Child Sections) is a heading for the
:ref:`child_cmd@syntax@child_table` for this section:

.. meta::
   :keywords: child, sections

.. index:: child, sections

.. _heading_exam@child_sections:

Child Sections
**************

.. csv-table::
    :header: "Child", "Title"
    :widths: 20, 80

    "heading_res", :ref:`@heading_res`

.. toctree::
   :maxdepth: 1
   :hidden:

   heading_res

