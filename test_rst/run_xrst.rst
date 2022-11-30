.. include:: xrst_preamble.rst

.. _run_xrst-name:

!!!!!!!!
run_xrst
!!!!!!!!

xrst input file: ``xrst/run_xrst.py``

.. meta::
   :keywords: run_xrst, run, extract, sphinx, rst, sphinx

.. index:: run_xrst, run, extract, sphinx, rst, sphinx

.. _run_xrst-title:

Run Extract Sphinx RST And Sphinx
#################################

.. contents::
   :local:

.. _run_xrst@Syntax:

Syntax
******
| ``xrst`` \\
| |tab| [ ``--version`` ]
| |tab| [ ``--local_toc`` ]
| |tab| [ ``--toml_file``  *toml_file* ] \\
| |tab| [ ``--html_theme`` *html_theme* ] \\
| |tab| [ ``--group_list`` *group_list* ] \\
| |tab| [ ``--target``     *target* ]  \\
| |tab| [ ``--output_dir`` *output_dir* ] \\
| |tab| [ ``--replace_spell_commands`` ] \\
| |tab| [ ``--rst_line_numbers`` ] \\

.. meta::
   :keywords: version

.. index:: version

.. _run_xrst@version:

version
*******
If ``--version`` is present on the command line,
the version of xrst is printed and none of the other arguments matter.

.. meta::
   :keywords: local_toc

.. index:: local_toc

.. _run_xrst@local_toc:

local_toc
*********
If this option is present on the command line,
a table of contents for the Headings in the current page
is included at the top of every page.
The page name and page title are not in this table of contents.

Some :ref:`html themes<run_xrst@html_theme>` include this information
on a side bar; e.g. ``furo`` and ``sphinx_book_theme`` .

.. meta::
   :keywords: toml_file

.. index:: toml_file

.. _run_xrst@toml_file:

toml_file
*********
The command line argument *toml_file* specifies the location of the
:ref:`toml_file-name` for this project.
This can be an absolute path or
relative to the directory where :ref:`xrst<run_xrst-name>` is executed.

.. meta::
   :keywords: xrst.toml

.. index:: xrst.toml

.. _run_xrst@toml_file@xrst.toml:

xrst.toml
=========
If *toml_file* is not present on the command line,
the default value ``xrst.toml`` is used for *toml_file* .

.. meta::
   :keywords: html_theme

.. index:: html_theme

.. _run_xrst@html_theme:

html_theme
**********
This the html_theme_ that is used.
The default value for *html_theme* is ``furo`` .

.. _html_theme: https://sphinx-themes.org/

.. meta::
   :keywords: theme, choices

.. index:: theme, choices

.. _run_xrst@html_theme@Theme Choices:

Theme Choices
=============
The following is a list of some themes that work well with the
default settings in :ref:`toml_file@html_theme_options` .
If you have a theme together with html_theme_options
that work well with xrst,
please post an issue on github so that it can be added to the list below.

.. csv-table:: Sphinx Themes
   :header: name,  local_toc

   sphinx_rtd_theme,     yes
   furo,                 no
   sphinx_book_theme,    no
   pydata_sphinx_theme,  no
   piccolo_theme,        no

.. meta::
   :keywords: sphinx_rtd_theme

.. index:: sphinx_rtd_theme

.. _run_xrst@html_theme@sphinx_rtd_theme:

sphinx_rtd_theme
================
A special modification is make to this theme when *target* is html,
so that it displays wider than its normal limit.
This modification may be removed in the future.

.. meta::
   :keywords: group_list

.. index:: group_list

.. _run_xrst@group_list:

group_list
**********
It is possible to select one or more groups of pages
to include in the output using this optional argument.

#. The *group_list* is a comma separated list of
   :ref:`group names<begin_cmd@group_name>`.
#. The :ref:`begin_cmd@group_name@Default Group` is represented by
   the group name ``default`` .
#. The order of the groups determines their order in the resulting output.
#. The default value for *group_list* is ``default`` .

For each group name in the *group_list*
there must be at least one xrst page in corresponding
:ref:`toml_file@root_file` .

The xrst examples are a subset of its user documentation
and its user documentation is a subset of its developer documentation.
For each command, the same source code file provides both the
user and developer documentation. In addition, the developer documentation
has links to the user documentation and the user documentation has links
to the examples.

.. _run_xrst@group_list@Example:

Example
=======
The examples commands below assume you have cloned the
`xrst git repository <https://github.com/bradbell/xrst>`_
and it is your current working directory.

#. The xrst examples use the default group
   and their documentation can be built using

      ``xrst --group_list default``

#. The xrst user documentation uses the default and user groups
   and its documentation can be built using

      ``xrst --group_list default,user``

#. The xrst developer documentation uses the default, user, and dev
   groups and its documentation can be built using

      ``xrst xrst.xrst --group_list default,user,dev``

.. meta::
   :keywords: target

.. index:: target

.. _run_xrst@target:

target
******
The optional command line argument *target* must be ``html`` or ``pdf``.
It specifies the type of type output you plan to generate using sphinx.
The default value for *target* is ``html`` .

.. meta::
   :keywords: output_dir

.. index:: output_dir

.. _run_xrst@output_dir:

output_dir
**********
The target files are placed in this sub-directory of the
:ref:`toml_file@directory@project_directory` .
The default value for *output_dir* is ``html`` .

.. meta::
   :keywords: replace_spell_commands

.. index:: replace_spell_commands

.. _run_xrst@replace_spell_commands:

replace_spell_commands
**********************
If this option is present on the command line, the source code
:ref:`spell commands<spell_cmd-name>` a replaced in such a way that the
there will be no spelling warnings during future processing by xrst.
This is useful when there are no spelling warnings before a change
to the :ref:`toml_file@project_dictionary` or when there is an update
of the pyspellchecker_ package (which is used to do the spell checking).
If this option is present,
none of the output files are created; e.g., the \*.rst and \*.html files.

.. _pyspellchecker: https://pypi.org/project/pyspellchecker

.. meta::
   :keywords: rst_line_numbers

.. index:: rst_line_numbers

.. _run_xrst@rst_line_numbers:

rst_line_numbers
****************
Normally sphinx error and warning messages are reported using line numbers
in the xrst source code files.
If this option is present, these messages are reported
using the line numbers in the RST files created by xrst.
This may be helpful if you have an error or warning for a sphinx command
and it does not make sense using source code line numbers.
It is also helpful for determining if an incorrect line number is due to
sphinx or xrst.
