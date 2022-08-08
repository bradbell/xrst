.. include:: xrst_preamble.rst

.. _configure_example:

!!!!!!!!!!!!!!!!!
configure_example
!!!!!!!!!!!!!!!!!

xrst input file: ``example/configure.xrst``

.. meta::
   :keywords: configure_example, configuration, files

.. index:: configure_example, configuration, files

.. _@configure_example:

Example Configuration Files
###########################
.. contents::
   :local:

These files are used to configure xrst to build its documentation:

.. csv-table::
    :header:  "Child", "Title"
    :widths: 20, 80

    "spelling", :ref:`@spelling`
    "keyword", :ref:`@keyword`
    "preamble.rst", :ref:`@preamble.rst`

.. meta::
   :keywords: xrst_file

.. index:: xrst_file

.. _configure_example@xrst_file:

xrst_file
*********
The file below demonstrates the used of ``xrst_file`` .

.. meta::
   :keywords: xrst_begin_parent

.. index:: xrst_begin_parent

.. _configure_example@xrst_begin_parent:

xrst_begin_parent
*****************
The file below demonstrates the used of ``xrst_begin_parent`` .

.. _configure_example@this_example_file:

This Example File
*****************

.. literalinclude:: ../../example/configure.xrst
    :language: rst

.. toctree::
   :maxdepth: 1
   :hidden:

   spelling
   keyword
   preamble
