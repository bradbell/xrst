.. include:: xrst_preamble.rst

.. _replace_page_number:

!!!!!!!!!!!!!!!!!!!
replace_page_number
!!!!!!!!!!!!!!!!!!!

xrst input file: ``xrst/replace_page_number.py``

.. meta::
   :keywords: replace_page_number, replace, page, number, commands

.. index:: replace_page_number, replace, page, number, commands

.. _replace_page_number-title:

Replace page number commands
############################

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
   :keywords: page_number

.. index:: page_number

.. _replace_page_number@Arguments@page_number:

page_number
===========
This is a page number that is placed infront of the heading text.
This may be empty; i.e., the replacement text is the empty string.
The underline (and overline if present) are extended by the number of
characters added to the heading text.

.. meta::
   :keywords: page_name

.. index:: page_name

.. _replace_page_number@Arguments@page_name:

page_name
=========
name of this page (only used to report errors).

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
the return data_out is the data after replacement. The page number is
added (see above) and the command is removed.

.. literalinclude:: ../xrst/replace_page_number.py
   :lines: 52-54
   :language: py

.. literalinclude:: ../xrst/replace_page_number.py
   :lines: 141-143
   :language: py
