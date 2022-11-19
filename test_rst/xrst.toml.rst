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
If a key has a default value, it is used when the key is not present,
All of the directories mentioned below are relative to the directory
where this file is located.

.. contents::
   :local:

.. meta::
   :keywords: output_directory

.. index:: output_directory

.. _xrst.toml@output_directory:

output_directory
****************
The default value for this key is
::

  { 'html' : 'html' , 'pdf' : 'pdf' }

The value is a dictionary that maps the :ref:`run_xrst@target` to the
directory where the final output is stored. Note that the possible values
for *target* are ``'html'`` and ``'pdf'`` and that the default
uses the same name for the output directory.

.. _xrst.toml@output_directory@Example:

Example
=======

.. literalinclude:: ../xrst.toml
   :lines: 36-37
   :language: toml

.. meta::
   :keywords: rst_directory

.. index:: rst_directory

.. _xrst.toml@rst_directory:

rst_directory
*************
The default value for this key is ``'rst'`` .
The value is a string specifying the
directory where xrst writes the rst files it extracts from the source code.
For each :ref:`begin_cmd@page_name` , the file

|space| *rst_directory*\ /\ *page_name*\ ``.rst``

is the RST file for the corresponding page. There is one exception
to this rule. If *page_name* ends with ``.rst``, the extra ``.rst``
is not added at the end.

.. _xrst.toml@rst_directory@Example:

Example
=======

.. literalinclude:: ../xrst.toml
   :lines: 56-56
   :language: toml

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

.. literalinclude:: ../xrst.toml
   :lines: 120-135
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

.. literalinclude:: ../xrst.toml
   :lines: 139-154
   :language: toml

.. meta::
   :keywords: not_in_index

.. index:: not_in_index

.. _xrst.toml@not_in_index:

not_in_index
************
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

.. _xrst.toml@not_in_index@Example:

Example
=======

.. literalinclude:: ../xrst.toml
   :lines: 158-182
   :language: toml
