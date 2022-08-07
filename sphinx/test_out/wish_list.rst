.. include:: xrst_preamble.rst

.. _wish_list:

!!!!!!!!!
wish_list
!!!!!!!!!

xrst input file: ``xrst.xrst``

.. meta::
   :keywords: wish_list, wish, list

.. index:: wish_list, wish, list

.. _@wish_list:

Wish List
#########
.. contents::
   :local:

The following is a wish list for future improvements to ``run_xrst``:

.. _stackoverflow: https://stackoverflow.com/questions/1686837/
   sphinx-documentation-tool-set-tab-width-in-output

.. meta::
   :keywords: standard, indent

.. index:: standard, indent

.. _wish_list@standard_indent:

Standard Indent
***************
Change the number of spaces corresponding to a tab from 4 to 3 characters.
This better aligns wih usage in sphinx rst files and saves output columns.

.. meta::
   :keywords: subset, documentation

.. index:: subset, documentation

.. _wish_list@subset_documentation:

Subset Documentation
********************
Have a way to specify subsets of the documentation by a group name.
For example ``{xrst_begin`` `section_name group_1 group_2}` would say that
this documentation should be included if `group_1` or `group_2`
is specified by the ``xrst`` command line.
If not groups were specified, all groups would be included.

.. meta::
   :keywords: spelling

.. index:: spelling

.. _wish_list@spelling:

Spelling
********
Add a command that automatically fixes spelling warnings by changing
the :ref:`@spell_cmd` in input sections. This is usefull when
pyspellchecker changes, when the
:ref:`run_xrst@sphinx_dir@spelling` file changes,
and when run_xrst automatically ignores more words.

.. meta::
   :keywords: tabs

.. index:: tabs

.. _wish_list@tabs:

Tabs
****
Tabs in a code blocks get expanded to 8 spaces; see stackoverflow_.
It would be nice to have a way to control the size of tabs in the code blocks
displayed by :ref:`@code_cmd` and :ref:`@file_cmd`.
Perhaps it would be good to support tabs as a method for
indenting xrst input sections.
