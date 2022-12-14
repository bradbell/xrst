.. _create_spell_checker-name:

!!!!!!!!!!!!!!!!!!!!
create_spell_checker
!!!!!!!!!!!!!!!!!!!!

.. meta::
   :keywords: create_spell_checker, create, pyspellchecker, object

.. index:: create_spell_checker, create, pyspellchecker, object

.. _create_spell_checker-title:

Create a pyspellchecker object
##############################

.. contents::
   :local:

.. meta::
   :keywords: arguments

.. index:: arguments

.. _create_spell_checker@Arguments:

Arguments
*********

.. meta::
   :keywords: local_words

.. index:: local_words

.. _create_spell_checker@Arguments@local_words:

local_words
===========
a list of words that get added to the dictionary for this spell checker.
No need to add single letter words because they are considered correct
by spell_command routine.

.. meta::
   :keywords: returns

.. index:: returns

.. _create_spell_checker@Returns:

Returns
*******

.. meta::
   :keywords: spell_checker

.. index:: spell_checker

.. _create_spell_checker@Returns@spell_checker:

spell_checker
=============
The return spell_checker is a pyspellchecker spell checking object.

.. literalinclude:: ../../xrst/create_spell_checker.py
   :lines: 32-35
   :language: py

.. literalinclude:: ../../xrst/create_spell_checker.py
   :lines: 143-143
   :language: py
