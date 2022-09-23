.. include:: xrst_preamble.rst

.. _replace_spell:

!!!!!!!!!!!!!
replace_spell
!!!!!!!!!!!!!

xrst input file: ``xrst/replace_spell.py``

.. meta::
   :keywords: replace_spell, replace, spelling, commands

.. index:: replace_spell, replace, spelling, commands

.. _replace_spell-0:

Replace spelling commands
#########################
.. contents::
   :local:

.. meta::
   :keywords: tmp_dir

.. index:: tmp_dir

.. _replace_spell@tmp_dir:

tmp_dir
*******
is the directory where spell.toml is located

.. meta::
   :keywords: spell.toml

.. index:: spell.toml

.. _replace_spell@tmp_dir@spell.toml:

spell.toml
==========
The file tmp_dir/spell.toml contains the following information:
For each file that was included in the documentation,
for each page in that file::

    [file_name.page_name]
    begin_line  = integer line number for the begin command
    start_spell = integer line number where the spell command starts
    end_spell   = integer line number where the spell command ends
    unknown     = array of strings (words) that are not in dictionary

#.  file_name and page_name are strings.
#.  file_name is relative to the directory where the
    :ref:`run_xrst@root_file` is located.
#.  Descriptions to the left (right) of the equal signs are literal text
    (replaced by their values).
#.  Line numbers start at one and are for the specified file.
#.  The line number zero is used for start_spell and end_spell when
    there is no spell command for this page.
#.  The spell start and end lines do not overlap the begin line.

.. literalinclude:: ../../xrst/replace_spell.py
   :lines: 45-46
   :language: py
