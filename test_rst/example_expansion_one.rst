.. _example_expansion_one-name:

!!!!!!!!!!!!!!!!!!!!!
example_expansion_one
!!!!!!!!!!!!!!!!!!!!!

.. meta::
   :keywords: example_expansion_one, first, expansion

.. index:: example_expansion_one, first, expansion

.. _example_expansion_one-title:

First Expansion
###############

.. contents::
   :local:

.. meta::
   :keywords: expansion, number

.. index:: expansion, number

.. _example_expansion_one@Expansion Number:

Expansion Number
****************
This is expansion number one of the template file
``example/template_file.xrst`` .

.. meta::
   :keywords: spelling

.. index:: spelling

.. _example_expansion_one@Spelling:

Spelling
********
Template files can not have the following command:

   ``{xrst_spell *word_1* ... *word_n* ``}``

We therefore suggest that you surround the intended use of special words,
or double words, by
``{xrst_spell_off}`` and ``{xrst_spell_on}`` .
This is what is done in the following sentence:
Using 'myspecialword' and using 'double double' are OK here.

.. meta::
   :keywords: template

.. index:: template

.. _example_expansion_one@This Template File:

This Template File
******************

.. literalinclude:: ../../example/template_file.xrst
   :language: rst

.. meta::
   :keywords: template, usage

.. index:: template, usage

.. _example_expansion_one@This Template Usage:

This Template Usage
*******************

.. literalinclude:: ../../example/template.xrst
   :lines: 23-28
   :language: rst
