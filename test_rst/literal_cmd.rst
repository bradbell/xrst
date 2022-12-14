.. _literal_cmd-name:

!!!!!!!!!!!
literal_cmd
!!!!!!!!!!!

.. meta::
   :keywords: literal_cmd, literal

.. index:: literal_cmd, literal

.. _literal_cmd-title:

Literal Command
###############

.. contents::
   :local:

.. _literal_cmd@Syntax:

Syntax
******

-  ``{xrst_literal}``

-  | ``{xrst_literal``
   |     *display_file*
   | :code:`}`

-  | ``{xrst_literal``
   |     *start*
   |     *stop*
   | :code:`}`

-  | ``{xrst_literal``
   |     *display_file*
   |     *start*
   |     *stop*
   | :code:`}`

.. _literal_cmd@Purpose:

Purpose
*******
A code block, from any where in any file,
can be included by the command above.

.. meta::
   :keywords: white, space

.. index:: white, space

.. _literal_cmd@White Space:

White Space
***********
Leading and trailing white space is not included in
*start*, *stop* or *display_file*.
The new line character separates these tokens.
The line containing the ``}`` must have nothing but white space after it.

.. meta::
   :keywords: display_file

.. index:: display_file

.. _literal_cmd@display_file:

display_file
************
If *display_file* is not in the syntax,
the code block is in the current input file.
Otherwise, the code block is in *display_file*.
The file name *display_file* is relative to the
:ref:`config_file@directory@project_directory` .

1. This may seem verbose, but it makes it easier to write scripts
   that move files and automatically change references to them.
2. Note that if you use the sphinx ``literalinclude`` directive,
   the corresponding file name will be relative to the
   :ref:`config_file@directory@rst_directory` , which is a path relative
   to the project_directory.

.. meta::
   :keywords: no, start, or, stop

.. index:: no, start, or, stop

.. _literal_cmd@No start or stop:

No start or stop
****************
In the case where there is no *start* or *stop*,
the entire display file is displayed.
In the case of the ``{xrst_literal}`` syntax,
the entire current input file is displayed.

.. meta::
   :keywords: start

.. index:: start

.. _literal_cmd@start:

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

.. _literal_cmd@stop:

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

.. _literal_cmd@Spell Checking:

Spell Checking
**************
Spell checking is **not** done for these code blocks.

.. _literal_cmd@Example:

Example
*******
see :ref:`literal_example-name` .
