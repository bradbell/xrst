.. include:: ../preamble.rst

!!!!!!!!!
wish_list
!!!!!!!!!

.. meta::
   :keywords: wish_list, wish, list

.. index:: wish_list, wish, list

.. _wish_list:

Wish List
#########
.. contents::
   :local:

The following is a wish list for future improvements to ``xsrst.py``:

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
   :keywords: relative, file, names

.. index:: relative, file, names

.. _wish_list@relative_file_names:

Relative File Names
*******************
Make all file names relative to the directory where the
:ref:`xsrst.py@command_line_arguments@root_file` is located.

.. meta::
   :keywords: git, repository

.. index:: git, repository

.. _wish_list@git_repository:

Git Repository
**************
Remove the need for xsrst.py to be executed from the top directory
of a git repository.

.. meta::
   :keywords: link, to, section, name

.. index:: link, to, section, name

.. _wish_list@link_to_section_name:

Link to Section Name
********************
Currently, when you link to an entire section, you get the section title
displayed for the link.
It would be good to have a separate anchor that displays the section name;
e.g., ``:ref:section_name`` would display the section name and
``:ref:title@section_name`` would display the section title.

.. meta::
   :keywords: subset, documentation

.. index:: subset, documentation

.. _wish_list@subset_documentation:

Subset Documentation
********************
Have a way to specify subsets of the documentation by a group name.
For example ``{xsrst_begin`` `section_name group_1 group_2}` would say that
this documentation should be included if `group_1` or `group_2`
is specified by the ``xsrst`` command line.
If not groups were specified, all groups would be included.

.. meta::
   :keywords: spelling

.. index:: spelling

.. _wish_list@spelling:

Spelling
********
Add a command that automatically fixes spelling warnings by changing
the :ref:`spell_cmd` in input sections. This is usefull when
pyspellchecker changes, when the
:ref:`xsrst.py@command_line_arguments@spelling` file changes,
and when xsrst.py automatically ignores more words.

.. meta::
   :keywords: tabs

.. index:: tabs

.. _wish_list@tabs:

Tabs
****
Tabs in a code blocks get expanded to 8 spaces; see stackoverflow_.
It would be nice to have a way to control the size of tabs in the code blocks
displayed by :ref:`code_cmd` and :ref:`file_cmd`.
Perhaps it would be good to support tabs as a method for
indenting xsrst input sections.

.. meta::
   :keywords: module

.. index:: module

.. _wish_list@module:

Module
******
Convert the program into a python module and provide a pip distribution for it.
It would at least be nice for cppad_py to install the ``xsrst.py`` program
so that users would not have to copy it to a directory in
their execution path.

----

xsrst input file: ``doc.xsrst``
