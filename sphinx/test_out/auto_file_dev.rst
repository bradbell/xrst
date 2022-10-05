.. include:: xrst_preamble.rst

.. _auto_file_dev:

!!!!!!!!!!!!!
auto_file_dev
!!!!!!!!!!!!!

xrst input file: ``xrst/auto_file.py``

.. meta::
   :keywords: auto_file_dev, create, automatically, generated, files

.. index:: auto_file_dev, create, automatically, generated, files

.. _auto_file_dev-0:

Create the automatically generated files
########################################

.. contents::
   :local:

.. meta::
   :keywords: html_theme

.. index:: html_theme

.. _auto_file_dev@html_theme:

html_theme
**********
The html_theme as on the xrst command line.

.. meta::
   :keywords: sphinx_dir

.. index:: sphinx_dir

.. _auto_file_dev@sphinx_dir:

sphinx_dir
**********
is the name of xrst command line argument *sphinx_dir*.

.. meta::
   :keywords: tmp_dir

.. index:: tmp_dir

.. _auto_file_dev@tmp_dir:

tmp_dir
*******
is the name of the directory where xrst creates a temporary copy of
the sphinx_dir/rst directory. We need not add a comment that these files
are automatically generated because all files in sphinx_dir/rst are.

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
This is a copy of the sphinx_dir/preamble.rst file. If target is
pdf (html) the latex macros are (are not) removed.

.. meta::
   :keywords: tmp_dir/xrst_index.rst

.. index:: tmp_dir/xrst_index.rst

.. _auto_file_dev@tmp_dir/xrst_index.rst:

tmp_dir/xrst_index.rst
**********************
This file just contains a link to the genindex.rst file.
It is (is not) included if target is html (pdf).

.. meta::
   :keywords: sphinx_dir/rst/conf.py

.. index:: sphinx_dir/rst/conf.py

.. _auto_file_dev@sphinx_dir/rst/conf.py:

sphinx_dir/rst/conf.py
**********************
This is the configuration file used by sphinx to build the documentation.

.. meta::
   :keywords: sphinx_dir/rst/index.rst

.. index:: sphinx_dir/rst/index.rst

.. _auto_file_dev@sphinx_dir/rst/index.rst:

sphinx_dir/rst/index.rst
************************
This is the root level in the sphinx documentation tree.

.. literalinclude:: ../../xrst/auto_file.py
   :lines: 210-218
   :language: py
