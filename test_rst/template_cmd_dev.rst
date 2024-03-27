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
   :lines: 152-155,311-312
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
   :keywords: page_file

.. index:: page_file

.. _template_cmd_dev@page_file:

page_file
*********
is the name of the file, for this page, where the begin command appears.
This is used for error reporting .

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
Each xrst template command is expanded and
xrst.add_line_numbers is used to add line numbers corresponding to the
template file.
In addition, the following text is added at the beginning and end of the
expansion:

| |tab| @ ``{xrst_template_begin`` @ *template_file* @ *page_line* @ ``}`` @
| |tab| @ ``{xrst_template_end}`` @

where *page_line* is the line where the line number in *page_file*
where the template command appeared. There is no white space between
the tokens above.
