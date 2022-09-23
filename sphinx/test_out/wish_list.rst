.. include:: xrst_preamble.rst

.. _wish_list:

!!!!!!!!!
wish_list
!!!!!!!!!

xrst input file: ``xrst.xrst``

.. meta::
   :keywords: wish_list, wish, list

.. index:: wish_list, wish, list

.. _wish_list-0:

Wish List
#########
.. contents::
   :local:

The following is a wish list for future improvements to ``run_xrst``:

.. _stackoverflow: https://stackoverflow.com/questions/1686837/
   sphinx-documentation-tool-set-tab-width-in-output

.. meta::
   :keywords: xrst_page_number

.. index:: xrst_page_number

.. _wish_list@xrst_page_number:

xrst_page_number
****************
Putting a backslash in front { ``xrst_page_number`` } does not work because
the backslash is removed before the command is interpreted. This should
be fixed.

.. meta::
   :keywords: tabs

.. index:: tabs

.. _wish_list@Tabs:

Tabs
****
Tabs in xrst input is not tested because
tabs in a code blocks get expanded to 8 spaces; see stackoverflow_.
Perhaps we should add a command line option that sets the tab stops,
convert the tabs to spaces when a file is read,
and not include tabs in any of the processing after that.

.. meta::
   :keywords: path

.. index:: path

.. _wish_list@Path:

Path
****
It would be nice to have a way, in sphinx, to make file names relative
to the directory where the :ref:`run_xrst@root_file` is located
so it would be the same as for xrst commands.

.. meta::
   :keywords: configuration

.. index:: configuration

.. _wish_list@Configuration:

Configuration
*************
It would be nice to have a *sphinx_dir* ``/conf.toml`` file that
could be used for more complicated cases that can be handled by the
command line arguments.

.. meta::
   :keywords: sphinx, error, messages

.. index:: sphinx, error, messages

.. _wish_list@Sphinx Error Messages:

Sphinx Error Messages
*********************
It would be nice to have a way to translate sphinx error messages
to the corresponding xrst input file and line number.

.. meta::
   :keywords: developer, documentation

.. index:: developer, documentation

.. _wish_list@Developer Documentation:

Developer Documentation
***********************
Now that xrst has a :ref:`run_xrst@group_list` option,
it would be nice to convert the developer documentation
to xrst with a group name that does not get included when
building the user documentation; e.g. ``devel`` .

.. meta::
   :keywords: search

.. index:: search

.. _wish_list@Search:

Search
******
It would be nice for a search to display all of the index words for each
web page that matches the search.
