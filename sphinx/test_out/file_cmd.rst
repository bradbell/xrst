.. include:: ../preamble.rst

!!!!!!!!
file_cmd
!!!!!!!!

.. toctree::
   :maxdepth: 1
   :hidden:

   file_exam

.. meta::
   :keywords: file_cmd, file, command

.. index:: file_cmd, file, command

.. _file_cmd:

File Command
############
.. contents::
   :local:

.. meta::
   :keywords: syntax

.. index:: syntax

.. _file_cmd@syntax:

Syntax
******

| ``{xrst_file``
| |tab| *start*
| |tab| *stop*
| :code:`}`
|
| ``{xrst_file``
| |tab| *start*
| |tab| *stop*
| |tab| *display_file*
| :code:`}`

.. meta::
   :keywords: purpose

.. index:: purpose

.. _file_cmd@purpose:

Purpose
*******
A code block, from any where in any file,
can be included by the command above at the
:ref:`beginning of a line<run_xrst@notation@beginning_of_a_line>`.

.. meta::
   :keywords: white, space

.. index:: white, space

.. _file_cmd@white_space:

White Space
***********
Leading and trailing white space is not included in
*start*, *stop* or *display_file*.
The new line character separates these tokens.

.. meta::
   :keywords: display_file

.. index:: display_file

.. _file_cmd@display_file:

display_file
************
If *display_file* is not in the syntax,
the code block is in the current input file.
Otherwise, the code block is in *display_file*.
The file name *display_file* is relative to the directory
where :ref:`xrst<run_xrst>` is executed.
This may seem verbose, but it makes it easier to write scripts
that move files and automatically change references to them.

.. meta::
   :keywords: start

.. index:: start

.. _file_cmd@start:

start
*****
The code block starts with the line following the occurrence
of the text *start* in *display_file*.
If this is the same as the file containing the command,
the text *start* will not match any text in the command.
There must be one and only one occurrence of *start* in *display_file*,
not counting the command itself when the files are the same.

.. meta::
   :keywords: stop

.. index:: stop

.. _file_cmd@stop:

stop
****
The code block ends with the line before the occurrence
of the text *start* in *display_file*.
If this is the same as the file containing the command,
the text *stop* will not match any text in the command.
There must be one and only one occurrence of *stop* in *display_file*,
not counting the command itself when the files are the same.

.. meta::
   :keywords: spell, checking

.. index:: spell, checking

.. _file_cmd@spell_checking:

Spell Checking
**************
Spell checking is **not** done for these code blocks.

.. meta::
   :keywords: example

.. index:: example

.. _file_cmd@example:

Example
*******

-  :ref:`file_exam`

----

xrst input file: ``xrst/file_command.py``
