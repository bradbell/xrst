.. include:: ../preamble.rst

!!!!!!!!
run_xrst
!!!!!!!!

.. meta::
   :keywords: run_xrst, run, extract, sphinx, rst

.. index:: run_xrst, run, extract, sphinx, rst

.. _run_xrst:

Run Extract Sphinx RST
######################
.. contents::
   :local:

.. meta::
   :keywords: syntax

.. index:: syntax

.. _run_xrst@syntax:

Syntax
******
-   ``xrst`` *target* *root_file* *sphinx_dir* *spelling* *keyword*
-   ``xrst`` *target* *root_file* *sphinx_dir* *spelling* *keyword*
    *line_increment*

.. meta::
   :keywords: notation

.. index:: notation

.. _run_xrst@notation:

Notation
********

.. meta::
   :keywords: white, space

.. index:: white, space

.. _run_xrst@notation@white_space:

White Space
===========
We define white space to be a sequence of space characters; e.g.,
tabs are not consider white space by xrst.

.. meta::
   :keywords: beginning, line

.. index:: beginning, line

.. _run_xrst@notation@beginning_of_a_line:

Beginning of a Line
===================
We say that a string *text* is a the beginning of a line if
only white space, or nothing, comes before *text* in the line.

.. meta::
   :keywords: command, line, arguments

.. index:: command, line, arguments

.. _run_xrst@command_line_arguments:

Command Line Arguments
**********************

.. meta::
   :keywords: target

.. index:: target

.. _run_xrst@command_line_arguments@target:

target
======
The command line argument *target* must be ``html`` or ``pdf`` and
specifies the type of type output you plan to generate using sphinx.
If *target* is ``html`` you can generate the sphinx output using
the following command in the *sphinx_dir* directory:

.. code-block:: sh

        make html

If *target* is ``pdf``, you can use the following commands:

.. code-block:: sh

        sed -i preamble.rst -e '/BEGIN_LATEX_MACROS/,/END_LATEX_MACROS/d'
        sphinx-build -b latex . _build/latex
        git checkout preamble.rst
        cd _build/latex
        sed -i cppad_py.tex -e 's|\\chapter{|\\paragraph{|'
        make cppad_py.pdf

.. meta::
   :keywords: root_file

.. index:: root_file

.. _run_xrst@command_line_arguments@root_file:

root_file
=========
The command line argument *root_file* is the name of a file,
relative to the top git repository directory.

.. meta::
   :keywords: sphinx_dir

.. index:: sphinx_dir

.. _run_xrst@command_line_arguments@sphinx_dir:

sphinx_dir
==========
The command line argument *sphinx_dir* is a sub-directory,
of the top git repository directory.
The  files ``conf.py``, ``preamble.rst``, *spelling*, and *keyword*
files are located in this directory.
The file ``index.rst`` in this directory will be overwritten
each time ``run_xrst`` executes.
The sub-directory *sphinx_dir* :code:`/xrst` is managed by ``xrst`` .
All the ``.rst`` files in *sphinx_dir* :code:`/xrst`
were extracted from the source code and correspond to
last time that ``run_xrst`` was executed.
Files that do not change are not updated (to speed up the processing).

.. meta::
   :keywords: conf.py

.. index:: conf.py

.. _run_xrst@command_line_arguments@sphinx_dir@conf.py:

conf.py
-------
The sphinx configuration file; e.g., :ref:`conf.py`.

.. meta::
   :keywords: preamble.rst

.. index:: preamble.rst

.. _run_xrst@command_line_arguments@sphinx_dir@preamble.rst:

preamble.rst
------------
An rst file that is automatically included at the beginning of every section.
This file should only define things, it should not generate any output.
For example, :ref:`preamble_rst`.

.. meta::
   :keywords: spelling

.. index:: spelling

.. _run_xrst@command_line_arguments@spelling:

spelling
========
The command line argument *spelling* is the name of a file,
relative to the *sphinx_dir* directory.
This file contains a list of words
that the spell checker will consider correct for all sections
(it can be an empty file).
A line that begins with :code:`#` is a comment (not included in the list).
The words are one per line and
leading and trailing white space in a word are ignored.
For example; see :ref:`spelling`.
Special words, for a particular section, are specified using the
:ref:`spell command<spell_cmd>`.

.. meta::
   :keywords: keyword

.. index:: keyword

.. _run_xrst@command_line_arguments@keyword:

keyword
=======
The command line argument *keyword* is the name of a file,
relative to the *sphinx_dir* directory.
This file contains a list of python regular expressions for heading tokens
that should not be included in the index (it can be an empty file).
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
For example; see :ref:`keyword`.

.. meta::
   :keywords: line_increment

.. index:: line_increment

.. _run_xrst@command_line_arguments@line_increment:

line_increment
==============
This optional argument helps find the source of errors reported by sphinx.
If the argument *line_increment* is present,
a table is generated at the end of each output file.
This table maps line numbers in the output file to
line numbers in the corresponding xrst input file.
The argument *line_increment* is a positive integer specifying the minimum
difference between xrst input line numbers for entries in the table.
The value ``1`` will give the maximum resolution.
For example, the sphinx warning

| |tab| ... ``/xrst/children_exam.rst:30: WARNING:`` ...

corresponds to line number 30 in the file ``children_exam.rst``.
The table at the bottom of that file maps line numbers in
``children_exam.rst`` to line numbers in the corresponding xrst input file.

----

xrst input file: ``xrst/run_xrst.py``
