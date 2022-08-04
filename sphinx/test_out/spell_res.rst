.. include:: xrst_preamble.rst

.. _spell_res:

!!!!!!!!!
spell_res
!!!!!!!!!

xrst input file: ``sphinx/test_in/spell.py``

.. meta::
   :keywords: spell_res, spell, result

.. index:: spell_res, spell, result

.. _@spell_res:

Spell Result
############
.. contents::
   :local:

.. meta::
   :keywords: text

.. index:: text

.. _spell_res@text:

Text
****
The word ``iterable`` is not in the dictionary,
so we have included it in the special words for this section.

.. meta::
   :keywords: spelling, file

.. index:: spelling, file

.. _spell_res@spelling_file:

Spelling File
*************
The word ``xrst`` is included by the
:ref:`spelling<run_xrst@sphinx_dir@spelling>` file
and hence need not be in the special words for this section.

.. meta::
   :keywords: math

.. index:: math

.. _spell_res@math:

Math
****
Words that are preceded by a backslash; e.g., latex commands,
are automatically included as correct spelling.

.. math::

    z = \cos( \theta ) + {\rm i} \sin( \theta )

.. meta::
   :keywords: double, words

.. index:: double, words

.. _spell_res@double_words:

Double Words
************
It is consider an error to have only white space between
two occurrences of the same word; e.g.,
no no would be an error if there
were not two occurrences of :code:`no` next to each other in the
spelling command for this section.

:ref:`@spell_exam`

