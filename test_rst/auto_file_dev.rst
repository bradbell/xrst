.. include:: xrst_preamble.rst

.. _auto_file_dev-name:

!!!!!!!!!!!!!
auto_file_dev
!!!!!!!!!!!!!

xrst input file: ``xrst/auto_file.py``

.. meta::
   :keywords: auto_file_dev, create, automatically, generated, files

.. index:: auto_file_dev, create, automatically, generated, files

.. _auto_file_dev-title:

Create the automatically generated files
########################################

.. contents::
   :local:

.. meta::
   :keywords: toml_dict

.. index:: toml_dict

.. _auto_file_dev@toml_dict:

toml_dict
*********
is a python dictionary representation of the xrst.toml file.
(It is empty if there is no such file).

.. meta::
   :keywords: rst_dir

.. index:: rst_dir

.. _auto_file_dev@toml_dict@rst_dir:

rst_dir
=======
we use *rst_dir* to denote *toml_dict* ['directory']['rst_directory'] .

.. meta::
   :keywords: tmp_dir

.. index:: tmp_dir

.. _auto_file_dev@toml_dict@tmp_dir:

tmp_dir
=======
we use *tmp_dir* to denote *rst_dir*\ /tmp .
This is the directory where xrst creates a temporary copy of *rst_dir* .
These files are also automatically generated.

.. meta::
   :keywords: html_theme

.. index:: html_theme

.. _auto_file_dev@html_theme:

html_theme
**********
The html_theme as on the xrst command line.

.. meta::
   :keywords: target

.. index:: target

.. _auto_file_dev@target:

target
******
is html or pdf

.. meta::
   :keywords: pinfo_list

.. index:: pinfo_list

.. _auto_file_dev@pinfo_list:

pinfo_list
**********
is a list with length equal to the number of pages.
The value page[page_index] is a dictionary for this page
with the following key, value pairs (all the keys are strings):

.. csv-table::
    :header: key, value

    page_name, (str) containing the name of this page.
    page_title,  (str) containing the title for this page.
    parent_page, (int) index in pinfo_list for the parent of this page.
    in_parent_file, (bool) is this page in same input file as its parent.

.. meta::
   :keywords: root_page_list

.. index:: root_page_list

.. _auto_file_dev@root_page_list:

root_page_list
**************
is a list of the root page names (one for each group) in the order
they will appear in the table of contents.

.. meta::
   :keywords: tmp_dir/xrst_table_of_contents.rst

.. index:: tmp_dir/xrst_table_of_contents.rst

.. _auto_file_dev@tmp_dir/xrst_table_of_contents.rst:

tmp_dir/xrst_table_of_contents.rst
**********************************
This file creates is the table of contents for the documentation.
It has the label xrst_table_of_contents which can be used to link
to this page.

.. meta::
   :keywords: tmp_dir/xrst_preamble.rst

.. index:: tmp_dir/xrst_preamble.rst

.. _auto_file_dev@tmp_dir/xrst_preamble.rst:

tmp_dir/xrst_preamble.rst
*************************
The data in :ref:`toml_file@preamble` is placed in this file.
If target is html (pdf) the latex macros are (are not) included.

.. meta::
   :keywords: tmp_dir/xrst_index.rst

.. index:: tmp_dir/xrst_index.rst

.. _auto_file_dev@tmp_dir/xrst_index.rst:

tmp_dir/xrst_index.rst
**********************
This file just contains a link to the genindex.rst file.
It is (is not) included if target is html (pdf).

.. meta::
   :keywords: rst_dir/conf.py

.. index:: rst_dir/conf.py

.. _auto_file_dev@rst_dir/conf.py:

rst_dir/conf.py
***************
This is the configuration file used by sphinx to build the documentation.

.. meta::
   :keywords: rst_dir/index.rst

.. index:: rst_dir/index.rst

.. _auto_file_dev@rst_dir/index.rst:

rst_dir/index.rst
*****************
This is the root level in the sphinx documentation tree.

.. literalinclude:: ../../xrst/auto_file.py
   :lines: 161-168
   :language: py
