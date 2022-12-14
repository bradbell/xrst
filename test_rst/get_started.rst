.. _get_started-name:

!!!!!!!!!!!
get_started
!!!!!!!!!!!

.. meta::
   :keywords: get_started, page, title:, getting, started

.. index:: get_started, page, title:, getting, started

.. _get_started-title:

Page Title: Getting Started
###########################

.. contents::
   :local:

.. meta::
   :keywords: heading:, steps

.. index:: heading:, steps

.. _get_started@Heading\: Steps:

Heading: Steps
**************

#. Use pip as follows to install xrst::

      pip install --index-url https://test.pypi.org/simple/ xrst

#. Create an empty directory and make it your current working directory.

#. Create a file called ``project.xrst`` in the working directory with the
   contents of this example file
   (project.xrst is the default root level input file).

#. Create an empty file called ``xrst.toml``
   in the working directory
   (xrst.toml is the default configure file).

#. Execute the following command::

      xrst

#. Use your web browser to open the file ``html/index.html`` .
   This location is relative to your working directory.

#. You should have gotten a warning that none of the input_files commands
   succeeded. You can fix this by putting the text below text in your
   xrst.toml file and then re-executing the xrst command::

      [input_files]
      data = [ [] ]

.. meta::
   :keywords: heading:, links, page

.. index:: heading:, links, page

.. _get_started@Heading\: Links to this Page:

Heading: Links to this Page
***************************

- :ref:`get_started-name`

- :ref:`get_started-title`

- :ref:`get_started@Heading: Steps`

- :ref:`get_started@Heading: Links to this Page`

- :ref:`get_started@Heading: This Example File`

.. meta::
   :keywords: heading:

.. index:: heading:

.. _get_started@Heading\: This Example File:

Heading: This Example File
**************************
The file below demonstrates the use of
``xrst_begin``,  ``xrst_end``, ``xrst_spell``, and heading references :

.. literalinclude:: ../../example/get_started.xrst
   :language: rst
