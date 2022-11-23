.. include:: xrst_preamble.rst

.. _configure_example:

!!!!!!!!!!!!!!!!!
configure_example
!!!!!!!!!!!!!!!!!

xrst input file: ``example/configure.xrst``

.. meta::
   :keywords: configure_example, using, toml, configure

.. index:: configure_example, using, toml, configure

.. _configure_example-title:

Example Using TOML Configure File
#################################

.. contents::
   :local:

.. meta::
   :keywords: preamble

.. index:: preamble

.. _configure_example@preamble:

preamble
********

.. meta::
   :keywords: rst_substitution

.. index:: rst_substitution

.. _configure_example@preamble@rst_substitution:

rst_substitution
================
|tab| This line is indented using ``|tab|``
which is defined as an rst_substitution.

.. meta::
   :keywords: latex_macro

.. index:: latex_macro

.. _configure_example@preamble@latex_macro:

latex_macro
===========
:math:`f : \B{R}^n \rightarrow \B{R}^m`
This line uses ``\B`` which is defined as a latex_macro.

.. meta::
   :keywords: toml

.. index:: toml

.. _configure_example@Example TOML File:

Example TOML File
*****************

.. literalinclude:: ../xrst.toml
   :language: toml

.. _configure_example@This Example File:

This Example File
*****************

.. literalinclude:: ../example/configure.xrst
   :language: rst
