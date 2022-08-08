.. include:: xrst_preamble.rst

.. _code_cmd:

!!!!!!!!
code_cmd
!!!!!!!!

xrst input file: ``xrst/code_command.py``

.. meta::
   :keywords: code_cmd, code

.. index:: code_cmd, code

.. _@code_cmd:

Code Command
############
.. contents::
   :local:

.. _code_cmd@syntax:

Syntax
******
- ``{xrst_code`` *language* :code:`}`
- ``{xrst_code}``

.. _code_cmd@purpose:

Purpose
*******
A code block, directly below in the current input file, begins with
a line containing the *language* included version of the command above.
This has the following advantage over sphinx code block:

1. One can begin and end comments, without the comment delimiters being
   displayed.
2. You choose a language so that the proper highlighting is done.
3. You do not need to indent the code block.

.. meta::
   :keywords: requirements

.. index:: requirements

.. _code_cmd@requirements:

Requirements
************
Each code command ends with
a line containing the second version of the command; i.e., ``{xrst_code}``.
Hence there must be an even number of code commands.
If the back quote character \` appears before or after the ``{xrst_code``,
it is not a command but rather normal input text. This is useful when
referring to this command in documentation.

.. meta::
   :keywords: language

.. index:: language

.. _code_cmd@language:

language
********
A *language* is a non-empty sequence of non-space the characters.
It is used to determine the source code language
for highlighting the code block.

.. meta::
   :keywords: rest, line

.. index:: rest, line

.. _code_cmd@rest_of_line:

Rest of Line
************
Other characters on the same line as a code command
are not included in the xrst output.
This enables one to begin or end a comment block
without having the comment characters in the xrst output.

.. meta::
   :keywords: spell, checking

.. index:: spell, checking

.. _code_cmd@spell_checking:

Spell Checking
**************
Code blocks as usually small and
spell checking is done for these code blocks.
(Spell checking is not done for code blocks included using the
:ref:`file command<file_cmd>` .)

.. _code_cmd@example:

Example
*******
:ref:`code_example`
