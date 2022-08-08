.. include:: xrst_preamble.rst

.. _spell_cmd:

!!!!!!!!!
spell_cmd
!!!!!!!!!

xrst input file: ``xrst/spell_command.py``

.. meta::
   :keywords: spell_cmd, spell

.. index:: spell_cmd, spell

.. _@spell_cmd:

Spell Command
#############
.. contents::
   :local:

.. _spell_cmd@syntax:

Syntax
******
``{xrst_spell`` *word_1* ...  *word_n* :code:`}`

Here *word_1*, ..., *word_n* is the special word list for this section.
In the syntax above the list of words is all in one line.
They could be on different lines which helps when displaying
the difference between  versions of the corresponding file.
Each word is a sequence of letters.
Upper case letters start a new word (even when preceded by a letter).
You need not include latex commands in special word list because
words with a backslash directly before them are not include in spell checking.

.. _spell_cmd@purpose:

Purpose
*******
You can specify a special list of words
(not normally considered correct spelling)
for the current section using the command above.
The line starting the command
can only have spaces and tabs before the command.

.. meta::
   :keywords: spelling

.. index:: spelling

.. _spell_cmd@spelling:

spelling
********
The list of words in
:ref:`spelling<run_xrst@sphinx_dir@spelling>`
are considered correct spellings for all sections.
The latex commands corresponding to the letters in the greek alphabet
are automatically added to this list.

.. meta::
   :keywords: capital, letters

.. index:: capital, letters

.. _spell_cmd@capital_letters:

Capital Letters
***************
The case of the first letter does not matter when checking spelling;
e.g., if ``abcd`` is *word_1* then ``Abcd`` will be considered a valid word.
Each capital letter starts a new word; e.g., `CamelCase` is considered to
be the two words 'camel' and 'case'.
Single letter words are always correct and not included in the
special word list; e.g., the word list entry ``CppAD`` is the same as ``Cpp``.

.. meta::
   :keywords: double, words

.. index:: double, words

.. _spell_cmd@double_words:

Double Words
************
It is considered an error to have only white space between two occurrences
of the same word. You can make an exception for this by entering
the same word twice (next to each other) in the special word list.

.. _spell_cmd@example:

Example
*******
:ref:`spell_example`
