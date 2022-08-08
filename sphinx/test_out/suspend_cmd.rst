.. include:: xrst_preamble.rst

.. _suspend_cmd:

!!!!!!!!!!!
suspend_cmd
!!!!!!!!!!!

xrst input file: ``xrst/suspend_command.py``

.. meta::
   :keywords: suspend_cmd, suspend, resume, commands

.. index:: suspend_cmd, suspend, resume, commands

.. _@suspend_cmd:

Suspend and Resume Commands
###########################
.. contents::
   :local:

.. _suspend_cmd@syntax:

Syntax
******
- ``{xrst_suspend}``
- ``{xrst_resume}``

.. _suspend_cmd@purpose:

Purpose
*******
It is possible to suspend (resume) the xrst extraction during a section.
One begins (ends) the suspension with a line that only contains spaces,
tabs and a suspend command (resume command).
Note that this will also suspend all other xrst processing; e.g.,
spell checking.

.. _suspend_cmd@example:

Example
*******
:ref:`suspend_example`
