.. include:: xrst_preamble.rst

.. _comment_cmd_dev:

!!!!!!!!!!!!!!!
comment_cmd_dev
!!!!!!!!!!!!!!!

xrst input file: ``xrst/comment_command.py``

.. meta::
   :keywords: comment_cmd_dev, remove, all, comment, commands

.. index:: comment_cmd_dev, remove, all, comment, commands

.. _comment_cmd_dev-0:

Remove all comment commands
###########################
.. contents::
   :local:

.. meta::
   :keywords: data_in

.. index:: data_in

.. _comment_cmd_dev@data_in:

data_in
*******
is the data for this page.

.. meta::
   :keywords: data_out

.. index:: data_out

.. _comment_cmd_dev@data_out:

data_out
********
The return data_out is a copy of data_in except that the comment
commands have been removed.

.. literalinclude:: ../../xrst/comment_command.py
   :lines: 51-54
   :language: py
