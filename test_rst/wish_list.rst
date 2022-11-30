.. include:: xrst_preamble.rst

.. _wish_list-name:

!!!!!!!!!
wish_list
!!!!!!!!!

xrst input file: ``user/wish_list.xrst``

.. meta::
   :keywords: wish_list, wish, list

.. index:: wish_list, wish, list

.. _wish_list-title:

Wish List
#########
The following is a wish list for future improvements to ``run_xrst``:

.. _stackoverflow: https://stackoverflow.com/questions/1686837/
   sphinx-documentation-tool-set-tab-width-in-output

.. contents::
   :local:

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
to the :ref:`toml_file@directory@project_directory` .

.. meta::
   :keywords: sphinx, error, messages

.. index:: sphinx, error, messages

.. _wish_list@Sphinx Error Messages:

Sphinx Error Messages
*********************
It would be nice to have a way to translate sphinx error messages
to the corresponding xrst input file and line number.

.. meta::
   :keywords: search

.. index:: search

.. _wish_list@Search:

Search
******
It would be nice for a search to display all of the index words for each
web page that matches the search.
