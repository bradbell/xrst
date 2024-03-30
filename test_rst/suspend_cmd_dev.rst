.. _suspend_cmd_dev-name:

!!!!!!!!!!!!!!!
suspend_cmd_dev
!!!!!!!!!!!!!!!

.. meta::
   :keywords: suspend_cmd_dev,remove,text,specified,by,suspend,/,resume,pairs,prototype,data_in,file_name,page_name,data_out

.. index:: suspend_cmd_dev, remove, text, specified, suspend, /, resume, pairs

.. _suspend_cmd_dev-title:

Remove text specified by suspend / resume pairs
###############################################

.. contents::
   :local:

.. index:: prototype

.. _suspend_cmd_dev@Prototype:

Prototype
*********

.. literalinclude:: ../../xrst/suspend_command.py
   :lines: 73-76,135-137
   :language: py

.. index:: data_in

.. _suspend_cmd_dev@data_in:

data_in
*******
is the data for this page.

.. index:: file_name

.. _suspend_cmd_dev@file_name:

file_name
*********
is the input file corresponding to this page.

.. index:: page_name

.. _suspend_cmd_dev@page_name:

page_name
*********
is the name of this page.

.. index:: data_out

.. _suspend_cmd_dev@data_out:

data_out
********
The return data_out is a copy of data_in except that the text between
and including each suspend / resume pair has been removed.
