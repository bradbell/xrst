.. include:: xrst_preamble.rst

.. _literal_cmd_dev:

!!!!!!!!!!!!!!!
literal_cmd_dev
!!!!!!!!!!!!!!!

xrst input file: ``xrst/literal_command.py``

.. meta::
   :keywords: literal_cmd_dev, process, literal, commands, in, page

.. index:: literal_cmd_dev, process, literal, commands, in, page

.. _literal_cmd_dev-title:

Process the literal commands in a page
######################################

.. contents::
   :local:

.. meta::
   :keywords: arguments

.. index:: arguments

.. _literal_cmd_dev@Arguments:

Arguments
*********

.. meta::
   :keywords: data_in

.. index:: data_in

.. _literal_cmd_dev@Arguments@data_in:

data_in
=======
is the data for a page before the
:ref:`literal commands <literal_cmd>` have been removed.

.. meta::
   :keywords: file_name

.. index:: file_name

.. _literal_cmd_dev@Arguments@file_name:

file_name
=========
is the name of the file that this data comes from. This is used
for error reporting and for the display file (when the display file
is not included in the command).

.. meta::
   :keywords: page_name

.. index:: page_name

.. _literal_cmd_dev@Arguments@page_name:

page_name
=========
is the name of the page that this data is in. This is only used
for error reporting.

.. meta::
   :keywords: rst_dir

.. index:: rst_dir

.. _literal_cmd_dev@Arguments@rst_dir:

rst_dir
=======
is the directory, relative to the current working directory,
where xrst will place the final rst files.

.. meta::
   :keywords: returns

.. index:: returns

.. _literal_cmd_dev@Returns:

Returns
*******

.. meta::
   :keywords: data_out

.. index:: data_out

.. _literal_cmd_dev@Returns@data_out:

data_out
========
Each xrst literal command is converted to its corresponding sphinx commands.

.. literalinclude:: ../xrst/literal_command.py
   :lines: 160-164
   :language: py

.. literalinclude:: ../xrst/literal_command.py
   :lines: 314-316
   :language: py