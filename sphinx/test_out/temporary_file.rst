.. include:: xrst_preamble.rst

.. _temporary_file:

!!!!!!!!!!!!!!
temporary_file
!!!!!!!!!!!!!!

xrst input file: ``xrst/temporary_file.py``

.. meta::
   :keywords: temporary_file, write, temporary, rst, page

.. index:: temporary_file, write, temporary, rst, page

.. _temporary_file-0:

Write the temporary RST file for a page
#######################################

.. contents::
   :local:

.. meta::
   :keywords: rst_line

.. index:: rst_line

.. _temporary_file@rst_line:

rst_line
********
is an int version of the :ref:`run_xrst@rst_line`
argument to the xrst program (with None represented by zero).

.. meta::
   :keywords: pseudo_heading

.. index:: pseudo_heading

.. _temporary_file@pseudo_heading:

pseudo_heading
**************
is the :ref:`process_headings@Returns@pseudo_heading` for this page.
It is placed before all the other headings in this page.
A label is added just before the pseudo heading that
links to it using the page name.

.. meta::
   :keywords: file_in

.. index:: file_in

.. _temporary_file@file_in:

file_in
*******
is the name of the xrst input file for this page.

.. meta::
   :keywords: tmp_dir

.. index:: tmp_dir

.. _temporary_file@tmp_dir:

tmp_dir
*******
is the directory where the output file will be saved.

.. meta::
   :keywords: page_name

.. index:: page_name

.. _temporary_file@page_name:

page_name
*********
is the name of this page.  The output file is tmp_dir/page_name.rst.

.. meta::
   :keywords: data_in

.. index:: data_in

.. _temporary_file@data_in:

data_in
*******
is the data for this page with all the xrst commands converted to
their sphinx RST values, except the \\n{xrst_page_number} command.
The following is added to this data before writing it to the output file:

#. The preamble is included at the beginning.
#. The pseudo heading and its label are added next.
#. The name of the input file file_in is displayed next.
#. More than 2 lines with only tabs or space are converted to 2 empty lines.
#. Empty lines at the end are removed
#. The line numbers are removed.
#. The text ``\{xrst_`` is replaced by ``{xrst_`` .
#. if rst_line > 0, a mapping from RST line numbers to file_in line numbers
   is included at the end.

.. literalinclude:: ../../xrst/temporary_file.py
   :lines: 61-73
   :language: py
