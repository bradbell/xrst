.. include:: xrst_preamble.rst

.. _run_xrst:

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
``xrst`` ( ``--version`` |  *toml_path* )
[ ``--replace_spell_commands`` ]
[ ``--rst_line_numbers`` ]
[ ``--html`` *html_theme* ]
[ ``--group`` *group_list* ]
[ ``--target`` *target* ]

.. meta::
   :keywords: version

.. index:: version

.. _run_xrst@version:

version
*******
If ``--version`` is present on the command line, there are no other arguments
and the version of xrst is printed. Otherwise *toml_path* is a required
argument.

.. meta::
   :keywords: toml_path

.. index:: toml_path

.. _run_xrst@toml_path:

toml_path
*********
The command line argument *toml_path* is the path to the
:ref:`toml_file` for this project.
This can be an absolute path or
relative to the directory where :ref:`xrst<run_xrst>` is executed.
For each group name in the *group_list*
there must be at least one xrst page in corresponding
:ref:`toml_file@root_file` .

.. meta::
   :keywords: root_directory

.. index:: root_directory

.. _run_xrst@toml_path@root_directory:

root_directory
==============
All of the xrst file references are relative to the directory where
the *toml_file* is located.

.. meta::
   :keywords: replace_spell_commands

.. index:: replace_spell_commands

.. _run_xrst@replace_spell_commands:

replace_spell_commands
**********************
If this option is present on the command line, the source code
:ref:`spell commands<spell_cmd>` a replaced in such a way that the
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
It is also helpful for determining if a line number error is due to
sphinx or xrst.

.. meta::
   :keywords: html_theme

.. index:: html_theme

.. _run_xrst@html_theme:

html_theme
**********
This the html_theme_ that is used.
The possible values (so far) are;
``furo``, ``sphinx_rtd_theme`` .
The default value for *html_theme* is ``sphinx_rtd_theme`` .

.. _html_theme: https://sphinx-themes.org/

The ``sphinx_rtd_theme`` theme includes a local table of contents for the
headers at the top of each page.
The other themes include this information in the right side bar.

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

#. The xrst examples use the empty group
   and their documentation can be built using

      ``xrst xrst.xrst --group ,``

#. The xrst user documentation uses the empty and user groups
   and its documentation can be built using

      ``xrst xrst.xrst --group ,user``

#. The xrst developer documentation uses the empty, user, and dev
   groups and its documentation can be built using

      ``xrst xrst.xrst --group ,user,dev``

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
   :keywords: other, generated, files

.. index:: other, generated, files

.. _run_xrst@target@Other Generated Files:

Other Generated Files
=====================
See :ref:`auto_file-title` for the other files generated by ``xrst`` in the
:ref:`toml_file@rst_directory` .
