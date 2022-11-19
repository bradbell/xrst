.. include:: xrst_preamble.rst

.. _get_started:

!!!!!!!!!!!
get_started
!!!!!!!!!!!

xrst input file: ``example/get_started.xrst``

.. meta::
   :keywords: get_started, page, title:, getting, started

.. index:: get_started, page, title:, getting, started

.. _get_started-title:

Page Title: Getting Started
###########################

#. Use pip as follows to install xrst::

      pip install --index-url https://test.pypi.org/simple/ xrst

#. Create an empty directory and make it your current working directory.

#. Create a file called ``get_started.xrst`` in the working directory with the
   contents of this example file (see below).

#. Create a directory called ``sphinx`` below the working directory.

#. Execute the following command::

      xrst get_started.xrst

#. Use your web browser to open the file ``sphinx/html/index.html`` .
   This location is relative to your working directory.

.. contents::
   :local:

.. meta::
   :keywords: heading:, links, page

.. index:: heading:, links, page

.. _get_started@Heading\: Links to this Page:

Heading: Links to this Page
***************************

- :ref:`get_started`

- :ref:`get_started-title`

- :ref:`get_started@Heading: Links to this Page`

- :ref:`get_started@Heading: This Example File`

.. meta::
   :keywords: heading:

.. index:: heading:

.. _get_started@Heading\: This Example File:

Heading: This Example File
**************************
The file below demonstrates the use of ``xrst_begin`` and ``xrst_end`` :

.. literalinclude:: ../example/get_started.xrst
   :language: rst
