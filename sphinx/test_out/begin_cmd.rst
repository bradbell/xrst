.. include:: xrst_preamble.rst

.. _begin_cmd:

!!!!!!!!!
begin_cmd
!!!!!!!!!

xrst input file: ``xrst/get_file_info.py``

.. meta::
   :keywords: begin_cmd, begin, end, commands

.. index:: begin_cmd, begin, end, commands

.. _@begin_cmd:

Begin and End Commands
######################
.. contents::
   :local:

.. _begin_cmd@syntax:

Syntax
******
- ``{xrst_begin_parent`` *page_name* *group_name* :code:`}`
- ``{xrst_begin``        *page_name* *group_name* :code:`}`
- ``{xrst_end``          *page_name* :code:`}`

.. meta::
   :keywords: page

.. index:: page

.. _begin_cmd@page:

Page
*******
The start (end) of a page of the input file is indicated by a
begin (end) command.

.. meta::
   :keywords: page_name

.. index:: page_name

.. _begin_cmd@page_name:

page_name
************
The *page_name* is a non-empty sequence of the following characters:
period ``.``, underbar ``_``, the letters a-z, and decimal digits 0-9.
It can not begin with the characters ``xrst_``.
A link is included in the index under the page name
to the first heading the page.
The page name is also added to the html keyword meta data.

.. meta::
   :keywords: group_name

.. index:: group_name

.. _begin_cmd@group_name:

group_name
**********
This is the group that this page belongs to; see
:ref:`run_xrst@group_list`.
If *group_name* is empty, this page is part of the empty group.
Note that it is the group name and not the group that is empty.

.. meta::
   :keywords: output

.. index:: output

.. _begin_cmd@output_file:

Output File
***********
The output file corresponding to *page_name* is

| |tab| *sphinx_dir*\ ``/xrst/``\ *page_name*\ ``.rst``

see :ref:`sphinx_dir<run_xrst@sphinx_dir>`

.. meta::
   :keywords: parent, page

.. index:: parent, page

.. _begin_cmd@parent_page:

Parent Page
**************
The following conditions hold for each *group_name*:

#. There can be at most one begin parent command in an input file.
#. If there is a begin parent command, it must be the first begin command
   in the file and there must be other pages in the file.
#. The other pages are children of the parent page.
#. The parent page is a child
   of the page that included this file using a
   :ref:`toc command<toc_cmd>`.
#. If there is no begin parent command in an input file,
   all the pages in the file are children
   of the page that included this file using a
   :ref:`toc command<toc_cmd>`.

Note that there can be more than one begin parent command in a file if
they have different group names. Also note that pages are only children
of pages that have the same group name.
