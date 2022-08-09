.. include:: xrst_preamble.rst

.. _heading_example:

!!!!!!!!!!!!!!!
heading_example
!!!!!!!!!!!!!!!

xrst input file: ``example/heading.py``

.. meta::
   :keywords: heading_example, title, heading, section

.. index:: heading_example, title, heading, section

.. _@heading_example:

Title Heading for This Section
##############################
.. contents::
   :local:

The label for the section title is the ``@``
character followed by the section name; i.e., ``@heading_example``.
The label ``heading_example`` displays ``heading_example``
instead of the section title.

.. meta::
   :keywords: second, level

.. index:: second, level

.. _heading_example@second_level:

Second Level
************
The label for this heading is ``heading_example.second_level``.

.. meta::
   :keywords: third, level

.. index:: third, level

.. _heading_example@second_level@third_level:

Third Level
===========
The label for this heading is ``heading_example.second_level.third_level``.

.. meta::
   :keywords: another, second, level

.. index:: another, second, level

.. _heading_example@another_second_level:

Another Second Level
********************
The label for this heading is ``heading_example.another_second_level``.

.. meta::
   :keywords: third, level

.. index:: third, level

.. _heading_example@another_second_level@third_level:

Third Level
===========
The label for this heading is
``heading_example.another_second_level.third_level``.

.. meta::
   :keywords: links

.. index:: links

.. _heading_example@links:

Links
*****
These links would also work from any other section because the section name
(``heading_example`` in this case)
is included at the beginning of the target for the link:

1. :ref:`@heading_example`
2. :ref:`heading_example@second_level`
3. :ref:`heading_example@second_level@third_level`
4. :ref:`heading_example@another_second_level`
5. :ref:`heading_example@another_second_level@third_level`

.. meta::
   :keywords: linking, headings, using, :ref:

.. index:: linking, headings, using, :ref:

.. _heading_example@linking_headings_using__ref_:

Linking Headings Using :ref:
****************************
The file below demonstrates linking to headings using ``:ref:`` .

.. _heading_example@this_example_file:

This Example File
*****************

.. literalinclude:: ../../example/heading.py
    :language: py
