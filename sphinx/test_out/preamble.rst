.. include:: xrst_preamble.rst

.. _preamble.rst:

!!!!!!!!!!!!
preamble.rst
!!!!!!!!!!!!

xrst input file: ``example/configure.xrst``

.. meta::
   :keywords: preamble.rst, preamble.rst

.. index:: preamble.rst, preamble.rst

.. _preamble.rst-title:

The preamble.rst Example File
#############################

.. contents::
   :local:

.. meta::
   :keywords: substitution

.. index:: substitution

.. _preamble.rst@Substitution:

Substitution
************
The example preamble defines ``|tab|`` so that the input:

``|tab| indented line``

generates the output:

|tab| indented line

.. meta::
   :keywords: latex, macro

.. index:: latex, macro

.. _preamble.rst@Latex Macro:

Latex Macro
***********
The example preamble defines ``\B`` and ``\R`` so that the input:

``:math:` f : \B{R} \rightarrow \B{R} \; \R{by} \; f(x) = x^2`` `````

generates the output:

:math:`f : \B{R} \rightarrow \B{R} \; \R{by} \; f(x) = x^2`

.. _preamble.rst@Example File:

Example File
************

.. literalinclude:: ../../sphinx/preamble.rst
   :language: rst
