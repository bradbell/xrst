.. include:: xrst_preamble.rst

.. _toml_file:

!!!!!!!!!
toml_file
!!!!!!!!!

xrst input file: ``xrst/get_toml_dict.py``

.. meta::
   :keywords: toml_file, configuration, xrst

.. index:: toml_file, configuration, xrst

.. _toml_file-title:

Configuration File for xrst
###########################
A toml file is used to configure xrst.
This file represents a python dictionary

#. Each key, in this dictionary,
   has a default value that is used when the key is not present
   in the toml file.
#. All of the keys are strings and all the values have the same type
   as its corresponding default.
   If a value is has components, all of the comments have the same
   type as the default components.
#. All of the directories mentioned below are relative to the
   :ref:`run_xrst@toml_path@project_directory`;
   i.e.; the directory where the toml file is located.

.. contents::
   :local:

.. meta::
   :keywords: project_name

.. index:: project_name

.. _toml_file@project_name:

project_name
************
The value corresponding to this key is a string specifying the
name of this project.
The default value for this key is

.. literalinclude:: ../xrst/get_toml_dict.py
   :lines: 36-36
   :language: toml

.. _toml_file@project_name@Example:

Example
=======

.. literalinclude:: ../xrst.toml
   :lines: 5-5
   :language: toml

.. meta::
   :keywords: root_file

.. index:: root_file

.. _toml_file@root_file:

root_file
*********
The value corresponding to this key is a dictionary that maps the
:ref:`group names <begin_cmd@group_name>`
to its top level xrst input file.
Note that multiple groups an use the same input file.
The default value for this key is

.. literalinclude:: ../xrst/get_toml_dict.py
   :lines: 55-55
   :language: toml

Note that ``default`` corresponds to the
:ref:`begin_cmd@group_name@Default Group` and ``project.xrst``
is the default root file.

.. _toml_file@root_file@Example:

Example
=======

.. literalinclude:: ../xrst.toml
   :lines: 9-11
   :language: toml

.. meta::
   :keywords: output_directory

.. index:: output_directory

.. _toml_file@output_directory:

output_directory
****************
The value corresponding to this key is a dictionary that maps the
:ref:`run_xrst@target` to the
directory where the final output is stored .
The default value for this key is

.. literalinclude:: ../xrst/get_toml_dict.py
   :lines: 76-79
   :language: toml

Note that the possible values
for *target* are ``'html'`` and ``'pdf'`` and that the default
uses the same name for the output directory.

.. _toml_file@output_directory@Example:

Example
=======

.. literalinclude:: ../xrst.toml
   :lines: 15-17
   :language: toml

.. meta::
   :keywords: rst_directory

.. index:: rst_directory

.. _toml_file@rst_directory:

rst_directory
*************
The value corresponding to this key is a string specifying the
directory where xrst writes the rst files it extracts from the source code.
For each :ref:`begin_cmd@page_name` , the file

|space| *rst_directory*\ /\ *page_name*\ ``.rst``

is the RST file for the corresponding page. There is one exception
to this rule. If *page_name* ends with ``.rst``, the extra ``.rst``
is not added at the end.
The default value for this key is

.. literalinclude:: ../xrst/get_toml_dict.py
   :lines: 106-106
   :language: toml

.. _toml_file@rst_directory@Example:

Example
=======

.. literalinclude:: ../xrst.toml
   :lines: 21-22
   :language: toml

.. meta::
   :keywords: preamble

.. index:: preamble

.. _toml_file@preamble:

preamble
********
The value corresponding to this key is a string specifying the
preamble.rst file.
This file is included at the beginning of every xrst output page.
It should only define things, it should not generate any output.
The Latex macros in this file can be used by any page.
There must be one macro definition per line and each such line must match the
following python regular expression:

   ``\n[ \t]*:math:`\\newcommand\{[^`]*\}`[ \t]*``

The default value for this key is

.. literalinclude:: ../xrst/get_toml_dict.py
   :lines: 131-131
   :language: toml

.. _toml_file@preamble@Example:

Example
=======

.. literalinclude:: ../xrst.toml
   :lines: 26-41
   :language: toml

.. meta::
   :keywords: project_dictionary

.. index:: project_dictionary

.. _toml_file@project_dictionary:

project_dictionary
******************
The value corresponding to this key is list of a strings.
Each string contains a newline separated list of words.
Leading and trailing white space is not part of each word.
These special words are not considered spelling errors for the entire project.
Special words, for a particular page, are specified using the
:ref:`spell command<spell_cmd>`.
The default value for this key is

.. literalinclude:: ../xrst/get_toml_dict.py
   :lines: 152-152
   :language: toml

.. _toml_file@project_dictionary@Example:

Example
=======

.. literalinclude:: ../xrst.toml
   :lines: 45-60
   :language: toml

.. meta::
   :keywords: not_in_index

.. index:: not_in_index

.. _toml_file@not_in_index:

not_in_index
************
The value corresponding to this key is list of a strings.
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
The default value for this key is

.. literalinclude:: ../xrst/get_toml_dict.py
   :lines: 180-180
   :language: toml

.. _toml_file@not_in_index@Example:

Example
=======

.. literalinclude:: ../xrst.toml
   :lines: 64-88
   :language: toml
