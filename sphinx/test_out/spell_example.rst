.. include:: xrst_preamble.rst

.. _spell_example:

!!!!!!!!!!!!!
spell_example
!!!!!!!!!!!!!

xrst input file: ``example/spell.py``

.. meta::
   :keywords: spell_example, spell, command, example

.. index:: spell_example, spell, command, example

.. _@spell_example:

Spell Command Example
#####################
.. contents::
   :local:

.. meta::
   :keywords: text

.. index:: text

.. _spell_example@text:

Text
****
The word ``iterable`` is not in the dictionary,
so we have included it in the special words for this section.

.. meta::
   :keywords: spelling, file

.. index:: spelling, file

.. _spell_example@spelling_file:

Spelling File
*************
The word ``xrst`` is included by the
:ref:`run_xrst@sphinx_dir@spelling` file
and hence need not be in the special words for this section.

.. meta::
   :keywords: math

.. index:: math

.. _spell_example@math:

Math
****
Words that are preceded by a backslash; e.g., latex commands,
are automatically included as correct spelling.

.. math::

    z = \cos( \theta ) + {\rm i} \sin( \theta )

.. meta::
   :keywords: double, words

.. index:: double, words

.. _spell_example@double_words:

Double Words
************
It is consider an error to have only white space between
two occurrences of the same word; e.g.,
no no would be an error if there
were not two occurrences of :code:`no` next to each other in the
spelling command for this section.

.. meta::
   :keywords: this, example, file

.. index:: this, example, file

.. _spell_example@this_example_file:

This Example File
*****************

.. literalinclude:: ../../example/spell.py
    :language: py
