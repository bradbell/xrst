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
   :keywords: template

.. index:: template

.. _wish_list@Template Command:

Template Command
****************
It would be nice to have a command that included an xrst file with replacement.
Perhaps

| ``{xrst_template``
| |tab| *file_name* *del*
| |tab| *pattern* *del* *replace*
| |tab| *pattern* *del* *replace*
| ...
| ``}``

We should report the following when an error that occurs in the
template expansion:

#. The line number of the template command.
#. The line number in the template file and its *file_name*.

.. meta::
   :keywords: spell, checking

.. index:: spell, checking

.. _wish_list@Spell Checking:

Spell Checking
**************
Spell checking not require a special word for any valid role names; .e.g,
the following text should not require a special spelling entry for ``samp``
::

   :samp:`print 1+{variable}`

.. meta::
   :keywords: testing

.. index:: testing

.. _wish_list@Testing:

Testing
*******
Use github actions to test xrst on multiple systems.
Note that tox and pytest are used to test xrst in different versions
of python. The following is the tox.ini file for xrst:

.. literalinclude:: ../../tox.ini
   :language: ini

.. meta::
   :keywords: theme

.. index:: theme

.. _wish_list@Theme:

Theme
*****
It would be nice to have better
:ref:`config_file@html_theme_options@Default` options for more themes
so that they work will with xrst.

.. meta::
   :keywords: sphinx_rtd_theme

.. index:: sphinx_rtd_theme

.. _wish_list@Theme@sphinx_rtd_theme:

sphinx_rtd_theme
================
It would be nice if there were a way to make this theme use more
horizontal space (currently xrst tires to modify its output to do this).

.. meta::
   :keywords: sphinx_book_theme

.. index:: sphinx_book_theme

.. _wish_list@Theme@sphinx_book_theme:

sphinx_book_theme
=================
It would be nice if the sphinx_book_theme did not use the full
width of the display for tables; see issue-807_  .

.. _issue-807: https://github.com/executablebooks/sphinx-book-theme/issues/807

.. meta::
   :keywords: search

.. index:: search

.. _wish_list@Search:

Search
******
It would be nice if we could make the sphinx search act like the xrst
:ref:`xrst_search-name` (so we would not need two searches) .

.. meta::
   :keywords: rst, names

.. index:: rst, names

.. _wish_list@RST Command File Names:

RST Command File Names
**********************
It would be nice if all commands in the rst files used file names
were automatically mapped so they were relative to the
:ref:`config_file@directory@project_directory` .
If this were the case, one would not need the
:ref:`dir command<dir_cmd-title>` .
In addition, the file names should not be checked for spelling
(this is already true for the ``ref`` role).

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
