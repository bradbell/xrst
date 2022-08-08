.. include:: xrst_preamble.rst

.. _get_started:

!!!!!!!!!!!
get_started
!!!!!!!!!!!

xrst input file: ``example/get_started.xrst``

.. meta::
   :keywords: get_started, getting, started

.. index:: get_started, getting, started

.. _@get_started:

Getting Started
###############
.. contents::
   :local:

#.  Use pip as follows to install xrst::

        pip install --index-url https://test.pypi.org/simple/ xrst

#. Create an empty directory and make it your current working directory.

#. Create a file called ``get_started.xrst`` in the working directory with the
   contents of this example file (see below).

#. Create a directory called ``sphinx`` below the working directory.

#. Execute the following command::

    xrst get_started.xrst

#. Use your web browser to open the file ``sphinx/html/index.html`` .
   This location is relative to your workng directory.

.. _get_started@this_example_file:

This Example File
*****************
The file below demonstrates the use of ``xrst_begin`` and ``xrst_end`` :

.. literalinclude:: ../../example/get_started.xrst
    :language: rst
