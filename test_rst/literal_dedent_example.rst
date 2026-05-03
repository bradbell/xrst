.. _literal_dedent_example-name:

!!!!!!!!!!!!!!!!!!!!!!
literal_dedent_example
!!!!!!!!!!!!!!!!!!!!!!

.. meta::
    :keywords: literal_dedent_example,example,using,dedent,in,literal,command,without,where,does,not,match,matches,this,file

.. index:: literal_dedent_example, using, dedent, in, literal

.. _literal_dedent_example-title:

Example Using dedent in Literal Command
#######################################

.. contents::
    :local:

.. index:: without, dedent

.. _literal_dedent_example@Example Without dedent:

Example Without dedent
**********************
In this literal example the output lines are exactly as they appear
in the display file:

.. literalinclude:: ../../example/dedent.rs
    :lines: 43-44
    :language: rs

.. index:: where, dedent, does, not, match

.. _literal_dedent_example@Example Where dedent Does Not Match:

Example Where dedent Does Not Match
***********************************
In this literal example the leading spaces are removed:

.. literalinclude:: ../../example/dedent.rs
    :lines: 52-53
    :language: rs
    :dedent: 4

.. index:: where, dedent, matches

.. _literal_dedent_example@Example Where dedent Matches:

Example Where dedent Matches
****************************
In this literal example the leading spaces, the dedent characters,
and one space after the dedent characters are removed:

.. literalinclude:: ../../example/dedent.rs
    :lines: 61-62
    :language: rs
    :dedent: 8

.. _literal_dedent_example@This Example File:

This Example File
*****************

.. literalinclude:: ../../example/dedent.rs
    :language: rs
