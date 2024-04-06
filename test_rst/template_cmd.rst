.. _template_cmd-name:

!!!!!!!!!!!!
template_cmd
!!!!!!!!!!!!

.. meta::
   :keywords: template_cmd,template,command,syntax,input,file,rst,include,white,space,separator,template_file,match,replace,end,example

.. index:: template_cmd, template

.. _template_cmd-title:

Template Command
################

.. contents::
   :local:

.. _template_cmd@Syntax:

Syntax
******
| ``{xrst_template`` *separator*
| |tab| *template_file*
| |tab| *match_1* *separator* *replace_1*
| |tab| *match_2* *separator* *replace_2*
| |tab| ...
| ``}``

.. index:: input

.. _template_cmd@Input File:

Input File
**********
During the expansion of a template command,
the current input file is its *template_file* .
Otherwise, the current input file is the current :ref:`begin_cmd@Page File` .

.. index:: rst, include

.. _template_cmd@Rst Include:

Rst Include
***********
A similar sphinx include directive, in the context of xrst, is:

| |tab| .. include {xrst_dir *file_name* }

see :ref:`dir_cmd-name` .
The template command differs form the include directive in the following ways:

#. The template command allows for text replacement
   during the include so that *template_file* is like function or macro.

#. Errors and warnings in a template expansion will include both
   the line in the template file and the line where it is used.
   Errors and warnings in a sphinx include only report the
   line number in the include file.

#. xrst commands in *template_file* ( *file_name* )
   will get interpreted (will not get interpreted).

.. index:: white, space

.. _template_cmd@White Space:

White Space
***********
The newline character separates the lines of input above
and excluded from white space in the discussion below..

.. index:: separator

.. _template_cmd@separator:

separator
*********
The *separator* argument is a single character that separates
matches from their replacements.
Leading and trailing white space around *separator* is ignored.

.. index:: template_file

.. _template_cmd@template_file:

template_file
*************
is the name of the template file.
Leading and trailing white space around *template_file* is ignored
and *template_file* cannot contain the ``@`` character.
It is different for a normal xrst input file because it cannot have
any of the following xrst commands in a template expansion:

:ref:`begin or end <begin_cmd-name>` ,
:ref:`comment character <comment_ch_cmd-name>` ,
:ref:`indent<indent_cmd-name>` ,
:ref:`spell<spell_cmd-name>` ,
:ref:`template <template_cmd-name>` .

.. index:: match

.. _template_cmd@match:

match
*****
Each occurrence of a match in the template file gets replaced.
Leading and trailing white space around *match* is ignored.

.. index:: replace

.. _template_cmd@replace:

replace
*******
For each match, the corresponding replacement is used in its place.
Leading and trailing white space around *replace* is ignored.

.. index:: end

.. _template_cmd@Command End:

Command End
***********
The first occurrence of a right brace ``}`` ,
directly after a newline ,
terminates the template command.

.. _template_cmd@Example:

Example
*******
:ref:`template_example-name`
