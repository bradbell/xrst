.. include:: xrst_preamble.rst

.. _code_cmd:

!!!!!!!!
code_cmd
!!!!!!!!

xrst input file: ``xrst/code_command.py``

.. meta::
   :keywords: code_cmd, code

.. index:: code_cmd, code

.. _code_cmd-0:

Code Command
############

.. contents::
   :local:

.. _code_cmd@Syntax:

Syntax
******
- ``{xrst_code`` *language* :code:`}`
- ``{xrst_code}``

.. _code_cmd@Purpose:

Purpose
*******
A code block, directly below in the current input file, begins (ends) with
a code command that contains *language* (not containing *language*).
Lines containing the code commands are not included in the rst output.
One can use these lines to end and begin comments so that the
code also executes.
If this is not useful, one can instead use a sphinx code-block directive.

.. meta::
   :keywords: requirements

.. index:: requirements

.. _code_cmd@Requirements:

Requirements
************
Each code section ends with
a line containing the second version of the command; i.e., ``{xrst_code}``.
Hence there must be an even number of code commands.

.. meta::
   :keywords: language

.. index:: language

.. _code_cmd@language:

language
********
A *language* is a non-empty sequence of lower case letters.
It determines the language for highlighting the code block.

.. meta::
   :keywords: rest, line

.. index:: rest, line

.. _code_cmd@Rest of Line:

Rest of Line
************
Other characters on the same line as a code commands
are not included in the xrst output.
This enables one to begin or end a comment block
without having the comment characters in the xrst output.

.. meta::
   :keywords: spell, checking

.. index:: spell, checking

.. _code_cmd@Spell Checking:

Spell Checking
**************
Code blocks as usually small and
spell checking is done for these code blocks.
You can turn off this spell checking by putting
:ref:`spell_cmd@spell_off` before and :ref:`spell_cmd@spell_on` after
a code block.
Spell checking is not done for code blocks included using the
:ref:`literal command<literal_cmd>` .

.. _code_cmd@Example:

Example
*******
:ref:`code_example`
