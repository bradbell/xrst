.. include:: xrst_preamble.rst

.. _xrst.toml:

!!!!!!!!!
xrst.toml
!!!!!!!!!

xrst input file: ``xrst.toml``

.. meta::
   :keywords: xrst.toml, configuration, xrst

.. index:: xrst.toml, configuration, xrst

.. _xrst.toml-title:

Configuration File for xrst
###########################
This toml file represents a python dictionary that configures xrst.
All of its keys are strings.

.. contents::
   :local:

.. meta::
   :keywords: preamble

.. index:: preamble

.. _xrst.toml@preamble:

preamble
********
If this key is present, its value is a string representation of the
preamble.rst file.
This file is included at the beginning of every page.
It should only define things, it should not generate any output.
The Latex macros in this file can be used by any page.
There must be one macro definition per line and each such line must match the
following python regular expression:

   ``\n[ \t]*:math:`\\newcommand\{[^`]*\}`[ \t]*``

.. _xrst.toml@preamble@Example:

Example
=======

.. literalinclude:: ../../xrst.toml
   :lines: 79-94
   :language: toml

.. meta::
   :keywords: project_dictionary

.. index:: project_dictionary

.. _xrst.toml@project_dictionary:

project_dictionary
******************
If this key is present, the value is a list of strings.
Each string contains a newline separated list of words.
Leading and trailing white space is not part of each word.
These special words are not considered spelling errors this entire project.
Special words, for a particular page, are specified using the
:ref:`spell command<spell_cmd>`.

.. _xrst.toml@project_dictionary@Example:

Example
=======

.. literalinclude:: ../../xrst.toml
   :lines: 98-113
   :language: toml

.. meta::
   :keywords: not_keyword

.. index:: not_keyword

.. _xrst.toml@not_keyword:

not_keyword
***********
If this key is present, the value is a list of strings.
Each string  contains a newline separated list of patterns.
Leading and trailing white space is not part of each pattern.
These are python regular expression patterns for heading tokens
that are not included in the index.
A heading token is any sequence of non white space characters
with upper case letters converted to lower case.
For example, a heading might contain the token ``The`` but you
might not want to include ``the`` as a entry in the :ref:`genindex`.
In this case you could have a line containing just ``the`` .
For another example, you might want to exclude all tokens that are
integer numbers.
In this case you could have a line containing just ``[0-9]*`` .

.. _xrst.toml@not_keyword@Example:

Example
=======

.. literalinclude:: ../../xrst.toml
   :lines: 117-141
   :language: toml
