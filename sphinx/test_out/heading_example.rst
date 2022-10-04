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
The label for the page title is the page name followed by ``-0``.
For example, the label ``heading_example-0`` displays
``The Page Title is Level Zero`` as the linking text.
(The label ``heading_example`` displays ``heading_example``
as the linking text.)

.. contents::
   :local:

.. meta::
   :keywords: level, one

.. index:: level, one

.. _heading_example@Level One:

Level One
*********
The label for this heading is ``heading_example@Level One``.

.. meta::
   :keywords: level, two

.. index:: level, two

.. _heading_example@Level One@Level Two:

Level Two
=========
The label for this heading is ``heading_example@Level One@Level Two``.

.. meta::
   :keywords: another, level, one

.. index:: another, level, one

.. _heading_example@Another Level One:

Another Level One
*****************
The label for this heading is ``heading_example@Another Level One``.

.. meta::
   :keywords: level, two\_

.. index:: level, two\_

.. _heading_example@Another Level One@Level Two\_:

Level Two\_
===========
The label for this heading is
``heading_example@Another Level One@Level Two_``.
Note that the backslash in the heading keeps ``Two_``
from being interpreted as a link.
Also note that the backslash does not appear in the
display of the heading or in the corresponding label.

.. meta::
   :keywords: x

.. index:: x

.. _heading_example@Another Level One@x:

x
=
A heading can have just one character.
The label for this heading is
``heading_example@Another Level One@x``.

.. meta::
   :keywords: links

.. index:: links

.. _heading_example@Links:

Links
*****
These links would also work from any other page because the page name
(``heading_example`` in this case)
is included at the beginning of the target for the link:

#. :ref:`heading_example`
#. :ref:`heading_example-0`
#. :ref:`heading_example@Level One`
#. :ref:`heading_example@Level One@Level Two`
#. :ref:`heading_example@Another Level One`
#. :ref:`heading_example@Another Level One@Level Two_`
#. :ref:`heading_example@Another Level One@x`

.. meta::
   :keywords: linking, headings, using, :ref:

.. index:: linking, headings, using, :ref:

.. _heading_example@Linking Headings Using :ref\::

Linking Headings Using :ref:
****************************
The file below demonstrates linking to headings using ``:ref:`` .

.. _heading_example@This Example File:

This Example File
*****************

.. literalinclude:: ../../example/heading.py
   :language: py
