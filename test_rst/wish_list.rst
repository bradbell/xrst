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
The following is a wish list for future improvements to ``run_xrst``:

.. contents::
   :local:

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

.. meta::
   :keywords: search

.. index:: search

.. _wish_list@Search:

Search
******
It would be nice for a search to display all of the index words for each
web page that matches the search.
