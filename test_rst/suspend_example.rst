.. include:: xrst_preamble.rst

.. _suspend_example:

!!!!!!!!!!!!!!!
suspend_example
!!!!!!!!!!!!!!!

xrst input file: ``example/suspend.py``

.. meta::
   :keywords: suspend_example, suspend

.. index:: suspend_example, suspend

.. _suspend_example-title:

Suspend Command Example
#######################
This example was taken from the xrst configure file documentation.
It displays a default value using toml file format and
implements this default using python that is not in the documentation.

.. contents::
   :local:

.. meta::
   :keywords: output_directory

.. index:: output_directory

.. _suspend_example@output_directory:

output_directory
****************
The value corresponding to this key is a dictionary that maps the
*target* command line argument to
the directory where the final output is stored .
The default value for this key is

.. literalinclude:: ../example/suspend.py
   :lines: 24-25
   :language: toml

Note that the possible values
for *target* are ``'html'`` and ``'pdf'`` and that the default
uses the same name for the output directory.

.. _suspend_example@This Example File:

This Example File
*****************

.. literalinclude:: ../example/suspend.py
   :language: py
