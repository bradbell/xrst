.. include:: xrst_preamble.rst

.. _begin_cmd:

!!!!!!!!!
begin_cmd
!!!!!!!!!

xrst input file: ``xrst/get_file_info.py``

.. meta::
   :keywords: begin_cmd, begin, end, commands

.. index:: begin_cmd, begin, end, commands

.. _@begin_cmd:

Begin and End Commands
######################
.. contents::
   :local:

.. _begin_cmd@syntax:

Syntax
******
- ``{xrst_begin_parent`` *section_name* *group_name* :code:`}`
- ``{xrst_begin``        *section_name* *group_name* :code:`}`
- ``{xrst_end``          *section_name* :code:`}`

.. meta::
   :keywords: section

.. index:: section

.. _begin_cmd@section:

Section
*******
The start (end) of a section of the input file is indicated by a
begin (end) command.
The line containing the command
can only have spaces and tabs before the command.

.. meta::
   :keywords: section_name

.. index:: section_name

.. _begin_cmd@section_name:

section_name
************
The *section_name* is a non-empty sequence of the following characters:
period ``.``, underbar ``_``, the letters a-z, and decimal digits 0-9.
It can not begin with the characters ``xrst_``.
A link is included in the index under the section name
to the first heading the section.
The section name is also added to the html keyword meta data.

.. meta::
   :keywords: group_name

.. index:: group_name

.. _begin_cmd@group_name:

group_name
**********
This is the group that this section belongs to; see
:ref:`run_xrst@group_list`.
If *group_name* is empty, this section is part of the empty group.
Note that it is the group name and not the group that is empty.

.. meta::
   :keywords: output

.. index:: output

.. _begin_cmd@output_file:

Output File
***********
The output file corresponding to *section_name* is

| |tab| *sphinx_dir*\ ``/xrst/``\ *section_name*\ ``.rst``

see :ref:`sphinx_dir<run_xrst@sphinx_dir>`

.. meta::
   :keywords: parent, section

.. index:: parent, section

.. _begin_cmd@parent_section:

Parent Section
**************
The following conditions hold for each *group_name*:

#.  There can be at most one begin parent command in an input file.
#.  If there is a begin parent command, it must be the first begin command
    in the file and there must be other sections in the file.
#.  The other sections are children of the parent section.
#.  The parent section is a child
    of the section that included this file using a
    :ref:`child command<child_cmd>`.
#.  If there is no begin parent command in an input file,
    all the sections in the file are children
    of the section that included this file using a
    :ref:`child command<child_cmd>`.

Note that there can be more than one begin parent command in a file if
they have different group names. Also note that sections are only children
of sections that have the same group name.
