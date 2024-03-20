.. _system_exit-name:

!!!!!!!!!!!
system_exit
!!!!!!!!!!!

.. meta::
   :keywords: system_exit, form, error, message, exit

.. index:: system_exit, form, error, message, exit

.. _system_exit-title:

Form error message and exit
###########################

.. contents::
   :local:

.. meta::
   :keywords: msg

.. index:: msg

.. _system_exit@msg:

msg
***
Reason for aborting xrst

.. meta::
   :keywords: file_name

.. index:: file_name

.. _system_exit@file_name:

file_name
*********
is the name of the file that contains the begin command for this page.
This is different from the current input file if we are processing
a template command.

.. meta::
   :keywords: page_name

.. index:: page_name

.. _system_exit@page_name:

page_name
*********
name of page that the error appeared in

.. meta::
   :keywords: m_obj

.. index:: m_obj

.. _system_exit@m_obj:

m_obj
*****
The error was detected in the values returned by this match object.

.. meta::
   :keywords: data

.. index:: data

.. _system_exit@data:

data
****
is the data that was searched to get the match object m_obj.

.. meta::
   :keywords: line

.. index:: line

.. _system_exit@line:

line
****
is the line number in the current input file where the error
was detected.

.. literalinclude:: ../../xrst/system_exit.py
   :lines: 52-61
   :language: py
