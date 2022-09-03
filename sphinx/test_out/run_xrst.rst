.. include:: xrst_preamble.rst

.. _run_xrst:

!!!!!!!!
run_xrst
!!!!!!!!

xrst input file: ``xrst/run_xrst.py``

.. meta::
   :keywords: run_xrst, run, extract, sphinx, rst, sphinx

.. index:: run_xrst, run, extract, sphinx, rst, sphinx

.. _@run_xrst:

Run Extract Sphinx RST And Sphinx
#################################
.. contents::
   :local:

.. _run_xrst@syntax:

Syntax
******
-  ``xrst`` ( --version |  *root_file* )
   [ ``--replace_spell_commands`` ]
   [ ``--html`` *html_theme* ]
   [ ``--rst`` *rst_line* ]
   [ ``--group`` *group_list* ]
   [ ``--target`` *target* ]
   [ ``--output`` *output_dir* ]
   [ ``--sphinx`` *sphinx_dir* ]

.. meta::
   :keywords: version

.. index:: version

.. _run_xrst@version:

version
*******
If ``--version`` is present on the command line, there are no other arguments
and the version of xrst is printed. Otherwise *root_file* is a required
argument.

.. meta::
   :keywords: root_file

.. index:: root_file

.. _run_xrst@root_file:

root_file
*********
The command line argument *root_file* is the name of a file
containing the root page for the documentation tree.
This can be an absolute path or
relative to the directory where :ref:`xrst<run_xrst>` is executed.
There must be at least one page in *root_file* that has each
:ref:`begin_cmd@group_name` in the *group_list*.

.. meta::
   :keywords: project_name

.. index:: project_name

.. _run_xrst@root_file@project_name:

project_name
============
The base part of *root_file*, without directories or file extension,
is used as the sphinx project name.

.. meta::
   :keywords: replace_spell_commands

.. index:: replace_spell_commands

.. _run_xrst@replace_spell_commands:

replace_spell_commands
**********************
If this command is present on the command line, the source code
:ref:`spell commands<spell_cmd>` a replaced in such a way that the
there will be no spelling warnings during future processing by xrst.
This useful when there are no spelling warnings before a change
to the :ref:`run_xrst@sphinx_dir@spelling` file or an update
of the pyspellchecker_ package (which is used to do the spell checking).

.. _pyspellchecker: https://pypi.org/project/pyspellchecker

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
   :keywords: rst_line

.. index:: rst_line

.. _run_xrst@rst_line:

rst_line
********
This optional argument helps find the source of errors reported by sphinx.
If the argument *rst_line* is (is not) present,
a table is (is not) generated at the end of each output file.
This table maps line numbers in the rst output files to
line numbers in the corresponding xrst input file.
The argument *rst_line* is a positive integer specifying the minimum
difference between xrst input line numbers for entries in the table.
The value ``1`` will give the maximum resolution.
For example, the sphinx warning

| |tab| ... ``/xrst/children_exam.rst:30: WARNING:`` ...

corresponds to line number 30 in the file ``children_exam.rst``.
The table at the bottom of that file maps line numbers in
``children_exam.rst`` to line numbers in the corresponding xrst input file.

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
#. If *group_list* begins or ends with a comma, the empty group is included
   along with the other groups specified by *group_list*.
   Note that it is the group name and not the group that is empty.
#. The order of the groups determines their order in the resulting output.
#. The default value for *group_list* is ``,`` .

One use case for this is where the user documentation is a subset of the
developer documentation. This enables the developer documentation to
easily link to the specific paragraphs in the user documentation.
It also enables the same source code file to provide both the developer
and user documentation for the actions it provides.

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
The optional command line argument *sphinx_dir* is a directory relative to
of the directory where *root_file* is located.
If *target* is ``html``, the html files are placed in this directory.
If *target* is ``pdf``, the output file is

| *output_dir*\ ``/latex/``\ *project_name*\ ``.pdf``

see :ref:`run_xrst@root_file@project_name` .
The default value for *output_dir* is *sphinx_dir* ``/html`` .

.. meta::
   :keywords: sphinx_dir

.. index:: sphinx_dir

.. _run_xrst@sphinx_dir:

sphinx_dir
**********
The optional command line argument *sphinx_dir* is a directory relative to
of the directory where *root_file* is located.
This directory contains the optional configuration files (described below)
and the files generated by ``xrst`` .
The default value for *sphinx_dir* is ``sphinx`` .

.. meta::
   :keywords: preamble.rst

.. index:: preamble.rst

.. _run_xrst@sphinx_dir@preamble.rst:

preamble.rst
============
The file *sphinx_dir* ``/preamble.rst`` can be create by the user.
If it exists, it is included at the beginning of every page.
It should only define things, it should not generate any output.
For example, :ref:`@preamble.rst`.
The Latex macros in this file can be used by any page.
There must be one macro definition per line and each such line must match the
following python regular expression:

   ``\n[ \t]*:math:`\\newcommand\{[^`]*\}`[ \t]*``

.. _run_xrst@sphinx_dir@preamble.rst@example:

Example
-------
:ref:`@preamble.rst`

.. meta::
   :keywords: spelling

.. index:: spelling

.. _run_xrst@sphinx_dir@spelling:

spelling
========
The file *sphinx_dir* ``/spelling`` can be create by the user.
If it exists, it contains a list of words
that the spell checker will consider correct for all pages.
A line that begins with :code:`#` is a comment (not included in the list).
The words are one per line and
leading and trailing white space in a word are ignored.
For example; see :ref:`@spelling`.
Special words, for a particular page, are specified using the
:ref:`spell command<spell_cmd>`.

.. _run_xrst@sphinx_dir@spelling@example:

Example
-------
:ref:`@spelling`

.. meta::
   :keywords: keyword

.. index:: keyword

.. _run_xrst@sphinx_dir@keyword:

keyword
=======
The file *sphinx_dir* ``/keyword`` can be create by the user.
If it exists, it contains a list of
python regular expressions for heading tokens
that are not included in the index.
A heading token is any sequence of non space or new line characters
with upper case letters converted to lower case.
For example, a heading might contain the token ``The`` but you
might not want to include ``the`` as a entry in the :ref:`genindex`.
In this case you could have a line containing just ``the`` in *keyword*.
For another example, you might want to exclude all tokens that are numbers.
In this case you could have a line containing just ``[0-9]*`` in *keyword*.
The regular expressions are one per line and
leading and trailing spaces are ignored.
A line that begins with :code:`#` is a comment
(not included in the list of python regular expressions).
For example; see :ref:`@keyword`.

.. _run_xrst@sphinx_dir@keyword@example:

Example
-------
:ref:`@keyword`

.. meta::
   :keywords: page, rst, files

.. index:: page, rst, files

.. _run_xrst@sphinx_dir@page_rst_files:

Page RST Files
==============
The directory *sphinx_dir*\ :code:`/rst` is managed by ``xrst`` .
It contains all the rst files that were extracted from the source code,
and correspond to last time that ``xrst`` was executed.
For each :ref:`begin_cmd@page_name`, the file

|space| *sphinx_dir*\ ``/xrst/``\ *page_name*\ ``.rst``

Is the RST file for the corresponding page. There is one exception
to this rule. If *page_name* ends with ``.rst``, the extra ``.rst``
is not added at the end.

.. meta::
   :keywords: other, generated, files

.. index:: other, generated, files

.. _run_xrst@sphinx_dir@other_generated_files:

Other Generated Files
=====================
See :ref:`@auto_file` for the other files generated by ``xrst`` in the
*sphinx_dir* directory.
