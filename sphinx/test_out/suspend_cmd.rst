.. include:: ../preamble.rst

!!!!!!!!!!!
suspend_cmd
!!!!!!!!!!!

.. toctree::
   :maxdepth: 1
   :hidden:

   suspend_exam

.. meta::
   :keywords: suspend_cmd, suspend, resume, commands

.. index:: suspend_cmd, suspend, resume, commands

.. _suspend_cmd:

Suspend and Resume Commands
###########################
.. contents::
   :local:

.. meta::
   :keywords: syntax

.. index:: syntax

.. _suspend_cmd.syntax:

Syntax
******
- ``{xsrst_suspend}``
- ``{xsrst_resume}``

.. meta::
   :keywords: purpose

.. index:: purpose

.. _suspend_cmd.purpose:

Purpose
*******
It is possible to suspend (resume) the xsrst extraction during a section.
One begins (ends) the suspension with a line that only contains spaces,
tabs and a suspend command (resume command).
Note that this will also suspend all other xsrst processing; e.g.,
spell checking.

.. meta::
   :keywords: example

.. index:: example

.. _suspend_cmd.example:

Example
*******

-  :ref:`suspend_exam`

----

xsrst input file: ``xsrst/suspend_command.py``
