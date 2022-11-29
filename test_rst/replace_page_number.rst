.. include:: xrst_preamble.rst

.. _replace_page_number-name:

!!!!!!!!!!!!!!!!!!!
replace_page_number
!!!!!!!!!!!!!!!!!!!

xrst input file: ``xrst/replace_page_number.py``

.. meta::
   :keywords: replace_page_number, if, pdf,, add, page, number, name, title

.. index:: replace_page_number, if, pdf,, add, page, number, name, title

.. _replace_page_number-title:

If PDF, Add Page Number and Name to Title
#########################################

.. contents::
   :local:

.. meta::
   :keywords: arguments

.. index:: arguments

.. _replace_page_number@Arguments:

Arguments
*********

.. meta::
   :keywords: data_in

.. index:: data_in

.. _replace_page_number@Arguments@data_in:

data_in
=======
data for this page before replacement.

 #. data_in must contain '\\n{xrst_page_number}'
    which is referred to as the command below.
 #. The page title must come directly after the command
    and start with a newline.
 #. The page title may have an rst overline directly before the
    heading text and must have an underline directly after it.
 #. If both an overline and underline follow, they must be equal.

.. meta::
   :keywords: target

.. index:: target

.. _replace_page_number@Arguments@target:

target
======
if *target* is ``html`` , the command is removed and no other action
is taken. Otherwise, the *page_number* following by the *page_name* is
added at the font of the title for this page.
The underline (and overline if present) are extended by the number of
characters added to the title.

.. meta::
   :keywords: page_number

.. index:: page_number

.. _replace_page_number@Arguments@page_number:

page_number
===========
This is a page number that identifies this page in the table of contents.

.. meta::
   :keywords: page_name

.. index:: page_name

.. _replace_page_number@Arguments@page_name:

page_name
=========
This is the name of the page.

.. meta::
   :keywords: returns

.. index:: returns

.. _replace_page_number@Returns:

Returns
*******

.. meta::
   :keywords: data_out

.. index:: data_out

.. _replace_page_number@Returns@data_out:

data_out
========
the return data_out is the data after replacement.

.. literalinclude:: ../xrst/replace_page_number.py
   :lines: 56-60
   :language: py

.. literalinclude:: ../xrst/replace_page_number.py
   :lines: 148-150
   :language: py
