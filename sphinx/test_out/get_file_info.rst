.. include:: xrst_preamble.rst

.. _get_file_info:

!!!!!!!!!!!!!
get_file_info
!!!!!!!!!!!!!

xrst input file: ``xrst/get_file_info.py``

.. meta::
   :keywords: get_file_info, get, information, all, pages, in

.. index:: get_file_info, get, information, all, pages, in

.. _get_file_info-0:

Get information for all pages in a file
#######################################

.. contents::
   :local:

.. meta::
   :keywords: arguments

.. index:: arguments

.. _get_file_info@Arguments:

Arguments
*********

.. meta::
   :keywords: page_info

.. index:: page_info

.. _get_file_info@Arguments@page_info:

page_info
=========
a list of with information for pages that came before this file.
For each list index, page_info[index] is a dict and
page_info[index]['page_name'] is an str
containing the name of a pager that came before this file.
This includes pages for all the groups that came before this group.

.. meta::
   :keywords: group_name

.. index:: group_name

.. _get_file_info@Arguments@group_name:

group_name
==========
We are only retrieving information for pages in this group.

.. meta::
   :keywords: parent_file

.. index:: parent_file

.. _get_file_info@Arguments@parent_file:

parent_file
===========
name of the file that included file_in.

.. meta::
   :keywords: file_in

.. index:: file_in

.. _get_file_info@Arguments@file_in:

file_in
=======
is the name of the file we are getting all the information for.

.. meta::
   :keywords: returns

.. index:: returns

.. _get_file_info@Returns:

Returns
*******

.. meta::
   :keywords: file_info

.. index:: file_info

.. _get_file_info@Returns@file_info:

file_info
=========
The value file_info is a list of dict. Each dict contains the information
for one page in this file. We use info below for one element of the list:

.. meta::
   :keywords: info['page_name']

.. index:: info['page_name']

.. _get_file_info@Returns@file_info@info['page_name']:

info['page_name']
-----------------
is an str containing the name of a page in this file.

.. meta::
   :keywords: info['page_data']

.. index:: info['page_data']

.. _get_file_info@Returns@file_info@info['page_data']:

info['page_data']
-----------------
is an str containing the data for this page.

 #. Line numbers have been added using :ref:`add_line_numbers` .
    This is the first operation done on a page and other operations
    assume that line numbers are present. They are removed near the end
    when the temporary file corresponding to a page is created.
 #. If present for this page, the comment character and possible space
    after have been removed.
 #. The xrst begin and end commands are not include in this data.
 #. The first (last) line number corresponds to the begin (end) command
 #. The suspend / resume commands and data between such pairs
    have been removed.
 #. If there is a common :ref`indent` for the entire page,
    it has been removed.

.. meta::
   :keywords: info['is_parent']

.. index:: info['is_parent']

.. _get_file_info@Returns@file_info@info['is_parent']:

info['is_parent']
-----------------
is true (false) if this is (is not) the parent page for the other
pages in this file. The parent page must be the first for this group,
and hence have index zero in file_info. In addition,
if there is a parent page, there must be at least one other page;
i.e., len(file_info) >= 2.

.. meta::
   :keywords: info['is_child']

.. index:: info['is_child']

.. _get_file_info@Returns@file_info@info['is_child']:

info['is_child']
----------------
is true (false) if this is (is not) a child of the first page in
this file.

.. literalinclude:: ../../xrst/get_file_info.py
   :lines: 154-165
   :language: py

.. literalinclude:: ../../xrst/get_file_info.py
   :lines: 370-373
   :language: py
