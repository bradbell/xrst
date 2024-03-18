.. _template_cmd_dev-name:

!!!!!!!!!!!!!!!!
template_cmd_dev
!!!!!!!!!!!!!!!!

.. meta::
   :keywords: template_cmd_dev, expand, template, commands, in, page

.. index:: template_cmd_dev, expand, template, commands, in, page

.. _template_cmd_dev-title:

Expand the template commands in a page
######################################

.. contents::
   :local:

.. meta::
   :keywords: prototype

.. index:: prototype

.. _template_cmd_dev@Prototype:

Prototype
*********

.. literalinclude:: ../../xrst/template_command.py
   :lines: 139-142,274-275
   :language: py

.. meta::
   :keywords: restrictions

.. index:: restrictions

.. _template_cmd_dev@Restrictions:

Restrictions
************
The template expansion must come before processing any other commands
except for the following:
begin, end, comment_ch, indent, suspend, resume, spell, template.

.. meta::
   :keywords: data_in

.. index:: data_in

.. _template_cmd_dev@data_in:

data_in
*******
is the data for a page before the
:ref:`template commands <template_cmd-name>` have been expanded.

.. meta::
   :keywords: file_name

.. index:: file_name

.. _template_cmd_dev@file_name:

file_name
*********
is the name of the file that this data comes from. This is used
for error reporting and for the display file (when the display file
is not included in the command).

.. meta::
   :keywords: page_name

.. index:: page_name

.. _template_cmd_dev@page_name:

page_name
*********
is the name of the page that this data is in. This is only used
for error reporting.

.. meta::
   :keywords: data_out

.. index:: data_out

.. _template_cmd_dev@data_out:

data_out
********
Each xrst template command is expanded.
