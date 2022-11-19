.. include:: xrst_preamble.rst

.. _check_page_name:

!!!!!!!!!!!!!!!
check_page_name
!!!!!!!!!!!!!!!

xrst input file: ``xrst/check_page_name.py``

.. meta::
   :keywords: check_page_name, check, rules, page, name

.. index:: check_page_name, check, rules, page, name

.. _check_page_name-title:

Check the rules for a page name
###############################

.. contents::
   :local:

.. meta::
   :keywords: page_name

.. index:: page_name

.. _check_page_name@page_name:

page_name
*********
The page_name appears in *m_obj* in one of the following ways
#. {xrst_begin_parent page_name user}
#. {xrst_begin page_name user}
#. {xrst_end page_name}

The valid characters in a page name are [a-z], [0-9], period and underbar.
A page name cannot begin with ``xrst_`` . If *page_name* does not follow
these rules, a message is printed and the program exits.

.. meta::
   :keywords: file_name

.. index:: file_name

.. _check_page_name@file_name:

file_name
*********
is the name of the original input file that data appears in
(used for error reporting).

.. meta::
   :keywords: m_obj

.. index:: m_obj

.. _check_page_name@m_obj:

m_obj
*****
is the match object corresponding to *page_name*

.. meta::
   :keywords: data

.. index:: data

.. _check_page_name@data:

data
****
is that data that was searched to get the match object.

.. literalinclude:: ../xrst/check_page_name.py
   :lines: 41-45
   :language: py
