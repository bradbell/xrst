.. include:: xrst_preamble.rst

.. _start_stop_file-name:

!!!!!!!!!!!!!!!
start_stop_file
!!!!!!!!!!!!!!!

xrst input file: ``xrst/start_stop_file.py``

.. meta::
   :keywords: start_stop_file, convert, literal, start,, stop, from, text, line, numbers

.. index:: start_stop_file, convert, literal, start,, stop, from, text, line, numbers

.. _start_stop_file-title:

Convert literal command start, stop from text to line numbers
#############################################################

.. contents::
   :local:

.. meta::
   :keywords: arguments

.. index:: arguments

.. _start_stop_file@Arguments:

Arguments
*********

.. meta::
   :keywords: file_cmd

.. index:: file_cmd

.. _start_stop_file@Arguments@file_cmd:

file_cmd
========
is the name of the file where the xrst_literal command appears.

.. meta::
   :keywords: page_name

.. index:: page_name

.. _start_stop_file@Arguments@page_name:

page_name
=========
is the name of the page where the xrst_literal command appears.

.. meta::
   :keywords: display_file

.. index:: display_file

.. _start_stop_file@Arguments@display_file:

display_file
============
is the name of the file that we are displaying. If it is not the same as
file_cmd, then it must have appeared in the xrst_literal command.

.. meta::
   :keywords: cmd_line

.. index:: cmd_line

.. _start_stop_file@Arguments@cmd_line:

cmd_line
========
If file_cmd is equal to display_file, the lines of the file
between line numbers cmd_line[0] and cmd_line[1] inclusive
are in the xrst_literal command and are excluded from the search.

.. meta::
   :keywords: start_text

.. index:: start_text

.. _start_stop_file@Arguments@start_text:

start_text
==========
is the starting text. There must be one and only one copy of this text in the
file (not counting the excluded text). This text has no newlines and cannot
be empty.  If not, an the error is reported and the program stops.

.. meta::
   :keywords: stop_text

.. index:: stop_text

.. _start_stop_file@Arguments@stop_text:

stop_text
=========
is the stopping text. There must be one and only one copy of this text in the
file (not counting the excluded text). This text has no newlines and cannot
be empty.  Furthermore, the stopping text must come after the end of the
starting text. If not, an the error is reported and the program stops.

.. meta::
   :keywords: returns

.. index:: returns

.. _start_stop_file@Returns:

Returns
*******

.. meta::
   :keywords: start_line

.. index:: start_line

.. _start_stop_file@Returns@start_line:

start_line
==========
is the line number where start_text appears.

.. meta::
   :keywords: stop_line

.. index:: stop_line

.. _start_stop_file@Returns@stop_line:

stop_line
=========
is the line number where stop_text appears.

.. literalinclude:: ../xrst/start_stop_file.py
   :lines: 62-77
   :language: py

.. literalinclude:: ../xrst/start_stop_file.py
   :lines: 159-162
   :language: py
