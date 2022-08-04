.. include:: xrst_preamble.rst

.. _file_exam:

!!!!!!!!!
file_exam
!!!!!!!!!

xrst input file: ``sphinx/test_in/file.cpp``

.. meta::
   :keywords: file_exam, file, example

.. index:: file_exam, file, example

.. _@file_exam:

File Example
############
.. contents::
   :local:

.. literalinclude:: ../../sphinx/test_in/file.cpp
    :lines: 23-59
    :language: cpp

.. csv-table::
    :header: "Child", "Title"
    :widths: 20, 80

    "file_res", :ref:`@file_res`

.. toctree::
   :maxdepth: 1
   :hidden:

   file_res
