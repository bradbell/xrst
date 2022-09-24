.. include:: xrst_preamble.rst

.. _table_of_contents:

!!!!!!!!!!!!!!!!!
table_of_contents
!!!!!!!!!!!!!!!!!

xrst input file: ``xrst/table_of_contents.py``

.. meta::
   :keywords: table_of_contents, create, table, contents

.. index:: table_of_contents, create, table, contents

.. _table_of_contents-0:

Create the table of contents
############################
.. contents::
   :local:

and replace the '{xrst_page_number}' for all pages in pinfo_list.

.. meta::
   :keywords: arguments

.. index:: arguments

.. _table_of_contents@Arguments:

Arguments
*********

.. meta::
   :keywords: tmp_dir

.. index:: tmp_dir

.. _table_of_contents@Arguments@tmp_dir:

tmp_dir
=======
is the temporary directory whre the rst files are written.

.. meta::
   :keywords: target

.. index:: target

.. _table_of_contents@Arguments@target:

target
======
is either 'html' or 'pdf'.

 #. If target is 'pdf',  in the file
    tmp_dir/page_name.rst the text { ``xrst_page_number`` }
    is replaced by the page number which includes the counter for each level.
 #. If target is 'html', { ``xrst_page_number`` } is removed with not
    replacement.

.. meta::
   :keywords: pinfo_list

.. index:: pinfo_list

.. _table_of_contents@Arguments@pinfo_list:

pinfo_list
==========
is a list with length equal to the number of pages.
The value pinfo_list[page_index] is a dictionary for this page
with the following key, value pairs (all the keys are strings):

..  csv-table::
    :header: key, value, type

    page_name, contains the name of this page, str
    page_title,  contains the title for this page, str
    parent_page, index in pinfo_list for the parent of this page, int
    in_parent_file, is this page in same input file as its parent, bool

.. meta::
   :keywords: root_page_list

.. index:: root_page_list

.. _table_of_contents@Arguments@root_page_list:

root_page_list
==============
is a list of strings containing the root page name for each group.
The order of the root page names determine the order of the groups
int the table of contents.

.. meta::
   :keywords: returns

.. index:: returns

.. _table_of_contents@Returns:

Returns
*******

.. meta::
   :keywords: content

.. index:: content

.. _table_of_contents@Returns@content:

content
=======
The return content is the table of contents entries for all the pages.
The title Table of Contents and the label xrst_table_of_contents
are placed at the beginning of the of content.

.. literalinclude:: ../../xrst/table_of_contents.py
   :lines: 209-218
   :language: py

.. literalinclude:: ../../xrst/table_of_contents.py
   :lines: 249-250
   :language: py
