.. _wish_list-name:

!!!!!!!!!
wish_list
!!!!!!!!!

.. meta::
   :keywords: wish_list, wish, list

.. index:: wish_list, wish, list

.. _wish_list-title:

Wish List
#########
The following is a wish list for future improvements to ``run_xrst``.
If you want to help with one of these, or some other aspect of xrst,
open an `xrst issue <https://github.com/bradbell/xrst/issues>`_ .

.. contents::
   :local:

.. meta::
   :keywords: testing

.. index:: testing

.. _wish_list@Testing:

Testing
*******
Use github actions to test xrst on multiple systems.
The script ``bin/check_xrst.sh`` will need to be modified so that
it can run in batch mode and fail when the results change.

.. meta::
   :keywords: theme

.. index:: theme

.. _wish_list@Theme:

Theme
*****
It would be nice to have better
:ref:`config_file@html_theme_options@Default` options more themes
so that they work will with xrst.

.. meta::
   :keywords: search

.. index:: search

.. _wish_list@Search:

Search
******
It would be nice for the search to only match pages that index
all of the words entered into the search box.
It would also be nice if each matching page had a list of all its index
words below the corresponding page name.
(In xrst, the :ref:`heading_links@Index` words are
all words that appear in headings in the page.)

.. meta::
   :keywords: path

.. index:: path

.. _wish_list@Path:

Path
****
It would be nice if all sphinx commands that used file names were automatically
mapped so they were relative to the
:ref:`config_file@directory@project_directory` .
If this were the case, one would not need the
:ref:`dir command<dir_cmd-title>` .

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

.. _stackoverflow: https://stackoverflow.com/questions/1686837/
   sphinx-documentation-tool-set-tab-width-in-output
