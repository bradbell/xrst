.. include:: xrst_preamble.rst

.. _code_cmd_dev:

!!!!!!!!!!!!
code_cmd_dev
!!!!!!!!!!!!

xrst input file: ``xrst/code_command.py``

.. meta::
   :keywords: code_cmd_dev, process, xrst, code, commands, page

.. index:: code_cmd_dev, process, xrst, code, commands, page

.. _code_cmd_dev-title:

Process the xrst code commands for a page
#########################################

.. contents::
   :local:

.. meta::
   :keywords: arguments

.. index:: arguments

.. _code_cmd_dev@Arguments:

Arguments
*********

.. meta::
   :keywords: data_in

.. index:: data_in

.. _code_cmd_dev@Arguments@data_in:

data_in
=======
is the data for the page before the
:ref:`code commands <code_cmd>` have been processed.

.. meta::
   :keywords: file_name

.. index:: file_name

.. _code_cmd_dev@Arguments@file_name:

file_name
=========
is the name of the file that this data comes from. This is only used
for error reporting.

.. meta::
   :keywords: page_name

.. index:: page_name

.. _code_cmd_dev@Arguments@page_name:

page_name
=========
is the name of the page that this data is in. This is only used
for error reporting.

.. meta::
   :keywords: rst_dir

.. index:: rst_dir

.. _code_cmd_dev@Arguments@rst_dir:

rst_dir
=======
is the directory, relative to the current working directory,
where xrst will place the final rst files.

.. meta::
   :keywords: returns

.. index:: returns

.. _code_cmd_dev@Returns:

Returns
*******

.. meta::
   :keywords: data_out

.. index:: data_out

.. _code_cmd_dev@Returns@data_out:

data_out
========
is a copy of data_in with the xrst code commands replaced by a corresponding
sphinx command.

.. literalinclude:: ../xrst/code_command.py
   :lines: 101-105
   :language: py

.. literalinclude:: ../xrst/code_command.py
   :lines: 214-215
   :language: py