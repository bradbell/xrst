.. include:: xrst_preamble.rst

.. _create_spell_checker:

!!!!!!!!!!!!!!!!!!!!
create_spell_checker
!!!!!!!!!!!!!!!!!!!!

xrst input file: ``xrst/create_spell_checker.py``

.. meta::
   :keywords: create_spell_checker, create, pyspellchecker, object

.. index:: create_spell_checker, create, pyspellchecker, object

.. _create_spell_checker-0:

Create a pyspellchecker object
##############################
.. contents::
   :local:

.. meta::
   :keywords: local_words

.. index:: local_words

.. _create_spell_checker@local_words:

local_words
***********
a list of words that get added to the dictionary for this spell checker.
No need to add single letter words because they are considered correct
by spell_command routine.

.. meta::
   :keywords: spell_checker

.. index:: spell_checker

.. _create_spell_checker@spell_checker:

spell_checker
*************
The return spell_checker is a pyspellchecker spell checking object.

.. literalinclude:: ../../xrst/create_spell_checker.py
   :lines: 26-30
   :language: py
