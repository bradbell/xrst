.. include:: xrst_preamble.rst

.. _file_example:

!!!!!!!!!!!!
file_example
!!!!!!!!!!!!

xrst input file: ``sphinx/test_in/file.cpp``

.. meta::
   :keywords: file_example, file, command, example

.. index:: file_example, file, command, example

.. _@file_example:

File Command Example
####################
.. contents::
   :local:

.. meta::
   :keywords: this, example, file

.. index:: this, example, file

.. _file_example@this_example_file:

This Example File
*****************

.. literalinclude:: ../../sphinx/test_in/file.cpp
    :language: cpp

.. csv-table::
    :header: "Child", "Title"
    :widths: 20, 80

    "file_start_stop", :ref:`@file_start_stop`

.. toctree::
   :maxdepth: 1
   :hidden:

   file_start_stop
