.. include:: xrst_preamble.rst

.. _heading_example:

!!!!!!!!!!!!!!!
heading_example
!!!!!!!!!!!!!!!

xrst input file: ``example/heading.py``

.. meta::
   :keywords: heading_example, page, title, is, level, zero

.. index:: heading_example, page, title, is, level, zero

.. _heading_example-0:

The Page Title is Level Zero
############################
.. contents::
   :local:

The label for the page title is the page name followed by ``-0``.
For example, the label ``heading_example-0`` displays
``The Page Title is Level Zero`` as the linking text.
(The label ``heading_example`` displays ``heading_example``
as the linking text.)

.. meta::
   :keywords: level, one

.. index:: level, one

.. _heading_example@level_one:

Level One
*********
The label for this heading is ``heading_example@level_one``.

.. meta::
   :keywords: level, two

.. index:: level, two

.. _heading_example@level_one@level_two:

Level Two
=========
The label for this heading is ``heading_example@level_one@level_two``.

.. meta::
   :keywords: another, level, one

.. index:: another, level, one

.. _heading_example@another_level_one:

Another Level One
*****************
The label for this heading is ``heading_example@another_level_one``.

.. meta::
   :keywords: level, two

.. index:: level, two

.. _heading_example@another_level_one@level_two:

Level Two
=========
The label for this heading is
``heading_example@another_level_one@level_two``.

.. meta::
   :keywords: x

.. index:: x

.. _heading_example@another_level_one@x:

x
=
A heading can have just one character.
The label for this heading is
``heading_example@another_level_one@x``.

.. meta::
   :keywords: links

.. index:: links

.. _heading_example@links:

Links
*****
These links would also work from any other page because the page name
(``heading_example`` in this case)
is included at the beginning of the target for the link:

#. :ref:`heading_example`
#. :ref:`heading_example-0`
#. :ref:`heading_example@level_one`
#. :ref:`heading_example@level_one@level_two`
#. :ref:`heading_example@another_level_one`
#. :ref:`heading_example@another_level_one@level_two`
#. :ref:`heading_example@another_level_one@x`

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
