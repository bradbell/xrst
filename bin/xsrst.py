#! /usr/bin/env python3
# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xsrst_begin xsrst_py}
{xsrst_spell
    rtd
    cd
    underbars
    conf
    toctree
    stackoverflow
    pyspellchecker
    cmd
    cppad
    dir
    cmake
}

Extract Sphinx RST
##################


.. The indentation examples are included by the child_cmd section.

{xsrst_children
    xsrst/get_file_info.py
    xsrst/child_commands.py
    xsrst/spell_command.py
    xsrst/suspend_command.py
    xsrst/code_command.py
    xsrst/file_command.py
    xsrst/remove_comment_ch.py
    sphinx/test_in/heading.py
    sphinx/test_in/indent.py
    sphinx/configure.xsrst
}

Syntax
******
-   ``xsrst.py`` *target* *root_file* *sphinx_dir* *spelling* *keyword*
-   ``xsrst.py`` *target* *root_file* *sphinx_dir* *spelling* *keyword*
    *line_increment*

Purpose
*******
This is a pseudo sphinx extension that provides the following features:

#.  The file name for each section is also an abbreviated title used
    in the navigation bar and for linking to the section. This makes the
    navigation bar more useful while also having long descriptive titles.
    It also makes cross reference linking from other sections easier.
#.  Enables documentation in the comments for source code
    even when multiple computer languages are used for one package.
    Allows the documentation for one section to span multiple locations
    in the source code; see :ref:`suspend command<suspend_cmd>`.
#.  Allows for multiple sections (rst output files) to be specified by one
    input file. In addition, one section can be the parent for the
    other sections in a file.
#.  Generates the table of contents from the specification
    of which files are included; see :ref:`child commands<child_cmd>`.
    Generates a jump table to the headings for each section
    so that the navigation bar need not include this information.
#.  Includes a configurable :ref:`spell checker<spell_cmd>` and
    :ref:`index<genindex>`.
    Words in each heading are automatically included in the index.
#.  Makes it easy to include source code, that also executes, from
    directly below the :ref:`code command<code_cmd>` or from
    a different location in a :ref:`file<file_cmd>`.
    Uses tokens in the source, not line numbers in the source,
    to signify start and stop of inclusion from a file.

Requirements
************
-   ``pip install --user pyspellchecker``
-   ``pip install --user sphinx``
-   ``pip install --user sphinx-rtd-theme``
-   The directory *cmake_install_prefix*\ ``/bin`` must be in your execution
    path where *cmake_install_prefix* is the prefix used to instal cppad_py.

Notation
********

White Space
===========
We define white space to be a sequence of space characters; e.g.,
tabs are not consider white space by xsrst.

Beginning of a Line
===================
We say that a string *text* is a the beginning of a line if
only white space, or nothing, comes before *text* in the line.

Command Line Arguments
**********************

target
======
The command line argument *target* must be ``html`` or ``pdf`` and
specifies the type of type output you plan to generate using sphinx.
If *target* is ``html`` you can generate the sphinx output using
the following command in the *sphinx_dir* directory:
{xsrst_code sh}
    make html
{xsrst_code}
If *target* is ``pdf``, you can use the following commands:
{xsrst_code sh}
    sed -i preamble.rst -e '/BEGIN_LATEX_MACROS/,/END_LATEX_MACROS/d'
    sphinx-build -b latex . _build/latex
    git checkout preamble.rst
    cd _build/latex
    sed -i cppad_py.tex -e 's|\\chapter{|\\paragraph{|'
    make cppad_py.pdf
{xsrst_code}

root_file
=========
The command line argument *root_file* is the name of a file,
relative to the top git repository directory.

sphinx_dir
==========
The command line argument *sphinx_dir* is a sub-directory,
of the top git repository directory.
The  files ``conf.py``, ``preamble.rst``, *spelling*, and *keyword*
files are located in this directory.
The file ``index.rst`` in this directory will be overwritten
each time ``xsrst.py`` is run.
The sub-directory *sphinx_dir* :code:`/xsrst` is managed by ``xsrst`` .
All the ``.rst`` files in *sphinx_dir* :code:`/xsrst`
were extracted from the source code and correspond to
last time that ``xsrst.py`` was executed.
Files that do not change are not updated (to speed up the processing).

Example Configuration Files
---------------------------
..  csv-table::
    :header: file name, description
    :widths: 20, 80

        conf.py,        :ref:`conf_py`
        preamble.rst,   :ref:`preamble_rst`
        keyword,        :ref:`keyword`
        spelling,       :ref:`spelling`

conf.py
-------
The sphinx configuration file.

preamble.rst
------------
An rst file that is automatically included at the beginning of every section.
This file should only define things, it should not generate any output.


spelling
========
The command line argument *spelling* is the name of a file,
relative to the *sphinx_dir* directory.
This file contains a list of words
that the spell checker will consider correct for all sections
(it can be an empty file).
A line that begins with :code:`#` is a comment (not included in the list).
The words are one per line and
leading and trailing white space in a word are ignored.
Special words, for a particular section, are specified using the
:ref:`spell command<spell_cmd>`.

keyword
=======
The command line argument *keyword* is the name of a file,
relative to the *sphinx_dir* directory.
This file contains a list of python regular expressions for heading tokens
that should not be included in the index (it can be an empty file).
A heading token is any sequence of non space or new line characters
with upper case letters converted to lower case.
For example, a heading might contain the token ``The`` but you
might not want to include ``the`` as a entry in the :ref:`genindex`.
In this case you could have a line containing just ``the`` in *keyword*.
For another example, you might want to exclude all tokens that are numbers.
In this case you could have a line containing just ``[0-9]*`` in *keyword*.
The regular expressions are one per line and
leading and trailing spaces are ignored.
A line that begins with :code:`#` is a comment
(not included in the list of python regular expressions).

line_increment
==============
This optional argument helps find the source of errors reported by sphinx.
If the argument *line_increment* is present,
a table is generated at the end of each output file.
This table maps line numbers in the output file to
line numbers in the corresponding xsrst input file.
The argument *line_increment* is a positive integer specifying the minimum
difference between xsrst input line numbers for entries in the table.
The value ``1`` will give the maximum resolution.
For example, the sphinx warning

| |tab| ... ``/xsrst/children_exam.rst:30: WARNING:`` ...

corresponds to line number 30 in the file ``children_exam.rst``.
The table at the bottom of that file maps line numbers in
``children_exam.rst`` to line numbers in the corresponding xsrst input file.

Table of Contents
*****************

toctree
=======
The sphinx ``toctree`` directives are automatically generated
for sections.

Parent Section
==============
A single input file may contain multiple
:ref:`sections<begin_cmd.section>`.
The first of these sections may use a
:ref:`parent begin<begin_cmd.parent_section>` command.
In this case, the other sections in the file are children of this section
and this section is a child of the section containing the
:ref:`child command<child_cmd>` that included this file.

If there is no begin parent command in a file,
all the sections in the file are children of the section containing the
child command that included the file.

Links to Headings
*****************
- For each word in a heading,
  a link is included in the index from the word to the heading.

- Each word in a heading is added to the html keyword meta data.

- A cross reference label is defined for linking
  from anywhere to a heading. The details of how to use
  these labels are described below.

- Headings can also be used to help find links to children
  of the current section; see the heading
  :ref:`xsrst_py.links_to_headings.children` below.

First Level
===========
Each :ref:`section<begin_cmd.section>` can have only one header at
the first level which is a title for the section.
The :ref:`section_name<begin_cmd.section_name>`
is automatically used
as a label for linking the title for a section; i.e., the
following two inputs will link to the title for *section_name*:

1.  ``:ref:``\ \` *section_name*\ \`
2.  ``:ref:``\ \`*linking_text*\ ``<``\ *section_name*\ ``>``\ \`

The *linking_text* in the second syntax is the text the user sees.
The linking text for the first syntax is the title for the Section,
not the *section_name* (which is used as an abbreviated title).

Other.Levels
============
The label for linking a heading that is not at the first level is the label
for the heading directly above it plus a period character :code:`.`,
plus a lower case version of the heading with spaces and periods converted to
underbars :code:`_`. For example, the label for the heading for this
paragraph is

|tab| ``xsrst_py.links_to_headings.other_levels``

This may seem verbose, but it helps keep the links up to date.
If a heading changes, all the links to that heading, and all the headings
below it,  will break.
This identifies the links that should be checked
to make sure they are still valid.
Note that one uses the *section_name* ``xsrst_py``
and not the title ``extract_sphinx_rst``.

Children
========
If a xsrst input file has a
:ref:`parent section<xsrst_py.table_of_contents.parent_section>`
the other sections in the file are children of the parent.

- If a section has a :ref:`child link or list command<child_cmd>`
  links to all the children of the section are placed where the
  child link command is located.
- If a section has a :ref:`children command<child_cmd>`
  no automatic links to the children of the current section are generated.
- Otherwise, the links to the children of a section are placed
  at the end of the section.

You can place a heading directly before the links to make them easier to find.

Example
=======
:ref:`heading_exam`

Indentation
***********
If there are a number of spaces before
all of the xsrst documentation for a section,
those characters are not included in the xsrst output.
This enables one to indent the
xsrst so it is grouped with the proper code block in the source.
An error message will result if
you use tabs in the indentation.

Example
=======
- :ref:`indent_exam`

Wish List
*********
The following is a wish list for future improvements to ``xsrst.py``:

.. _stackoverflow: https://stackoverflow.com/questions/1686837/
   sphinx-documentation-tool-set-tab-width-in-output

Standard Indent
===============
Change the number of spaces corresponding to a tab from 4 to 3 characters.
This better aligns wih usage in sphinx rst files and saves output columns.

Dot in Section Name
===================
Change the character used in the link to separate levels from dot ``.``
to colon ``:`` so that dot can be used in section names.

Relative File Names
===================
Make all file names relative to the directory where the
:ref:`xsrst_py.command_line_arguments.root_file` is located.

Git Repository
==============
Remove the need for xsrst.py to be executed from the top directory
of a git repository.

Link to Section Name
====================
Currently, when you link to an entire section, you get the section title
displayed for the link.
It would be good to have a separate anchor that displays the section name;
e.g., ``:ref:section_name`` would display the section name and
``:ref:title@section_name`` would display the section title.

Subset Documentation
====================
Have a way to specify subsets of the documentation by a group name.
For example ``{xsrst_begin`` `section_name group_1 group_2}` would say that
this documentation should be included if `group_1` or `group_2`
is specified by the ``xsrst`` command line.
If not groups were specified, all groups would be included.

Spelling
========
Add a command that automatically fixes spelling warnings by changing
the :ref:`spell_cmd` in input sections. This is usefull when
pyspellchecker changes, when the
:ref:`xsrst_py.command_line_arguments.spelling` file changes,
and when xsrst.py automatically ignores more words.

Tabs
====
Tabs in a code blocks get expanded to 8 spaces; see stackoverflow_.
It would be nice to have a way to control the size of tabs in the code blocks
displayed by :ref:`code_cmd` and :ref:`file_cmd`.
Perhaps it would be good to support tabs as a method for
indenting xsrst input sections.

Module
======
Convert the program into a python module and provide a pip distribution for it.
It would at least be nice for cppad_py to install the ``xsrst.py`` program
so that users would not have to copy it to a directory in
their execution path.


.. All the children of this section are commands except for heading_exam.

Commands
********
- :ref:`begin_cmd`
- :ref:`child_cmd`
- :ref:`spell_cmd`
- :ref:`suspend_cmd`
- :ref:`code_cmd`
- :ref:`file_cmd`
- :ref:`comment_ch_cmd`

{xsrst_end xsrst_py}
"""
# ---------------------------------------------------------------------------
# imports
# ---------------------------------------------------------------------------
import sys
import re
import os
import pdb
import string
import spellchecker
import shutil
import filecmp
#
# sys.path
# used so that we can test before installing
if( os.getcwd().endswith('/xsrst.git') ) :
    if( os.path.isdir('xsrst') ) :
        sys.path.insert(0, os.getcwd() )
#
import xsrst
# ---------------------------------------------------------------------------
# functions
# ---------------------------------------------------------------------------
# Compute output corresponding to a section.
# This finishes all the xsrst processing that has been delayed to this point
# with the exception of {xsrst_section_number}. The section number is computed
# after all the sections have been output and replaced during the
# table_of_contents computation.
def compute_output(
    file_in,
    section_data,
    list_children,
    pseudo_heading,
    section_name,
    line_increment,
) :
    # split section data into lines
    newline_list = xsrst.newline_indices(section_data)
    #
    # start output by including preamble
    rst_output = '.. include:: ../preamble.rst\n\n'
    #
    # put pseudo heading next
    rst_output += pseudo_heading
    #
    # put hidden toctree next
    if len(list_children) > 0  :
        rst_output += '.. toctree::\n'
        rst_output += '   :maxdepth: 1\n'
        rst_output += '   :hidden:\n\n'
        for child in list_children :
            rst_output += '   ' + child + '\n'
        rst_output += '\n'
    #
    # now output the section data
    startline         = 0
    previous_empty    = True
    has_child_command = False
    for newline in newline_list :
        line  = section_data[startline : newline + 1]
        # commands that delay some processing to this point
        children_command       = line.startswith('{xsrst_children')
        child_list_command     = line.startswith('{xsrst_child_list')
        child_table_command    = line.startswith('{xsrst_child_table')
        if children_command or child_list_command or child_table_command:
            assert not has_child_command
            assert len(list_children) > 0
            has_child_command = True
            #
            if child_list_command:
                rst_output += '\n'
                for child in list_children :
                    rst_output += '-  :ref:`' + child + '`\n'
                rst_output += '\n'
            previous_empty = True
            if child_table_command:
                rst_output += '.. csv-table::\n'
                rst_output += '    :header:  "Child", "Title"\n'
                rst_output += '    :widths: 20, 80\n\n'
                for child in list_children :
                    rst_output += '    "' + child + '"'
                    rst_output += ', :ref:`' + child + '`\n'
                rst_output += '\n'
            previous_empty = True
        else :
            m_obj = xsrst.pattern['line'].search(line)
            if m_obj :
                empty_line = m_obj.start() == 0
            else :
                if len( line.strip(' \t') ) == 0 :
                    empty_line = True
                else :
                    empty_line = False
            if empty_line :
                    line = '\n'
            #
            if line != '\n' :
                rst_output += line
            elif not previous_empty :
                rst_output += line
            #
            previous_empty = line == '\n'
        startline = newline + 1
    #
    # The last step in converting xsrst commands is removing line numbers
    # (done last so mapping from output to input line number is correct)
    rst_output, line_pair = xsrst.remove_line_numbers(rst_output)
    # -----------------------------------------------------------------------
    if not previous_empty :
        rst_output += '\n'
    #
    # If there is no child command in this section, automatically generate
    # links to the child sections at the end of the section.
    if len(list_children) > 0 and not has_child_command :
        rst_output += '.. csv-table::\n'
        rst_output += '    :header: "Child", "Title"\n'
        rst_output += '    :widths: 20, 80\n\n'
        for child in list_children :
            rst_output += '    "' + child + '"'
            rst_output += ', :ref:`' + child + '`\n'
        rst_output += '\n'
    #
    # sphinx transition
    rst_output += '----\n\n'
    rst_output += f'xsrst input file: ``{file_in}``\n'
    #
    if line_increment > 0 :
        rst_output += '\n.. csv-table:: Line Number Mapping\n'
        rst_output += 4 * ' ' + ':header: rst file, xsrst input\n'
        rst_output += 4 * ' ' + ':widths: 10, 10\n\n'
        previous_line = None
        for pair in line_pair :
            if previous_line is None :
                rst_output   += f'    {pair[0]}, {pair[1]}\n'
                previous_line = pair[1]
            elif pair[1] - previous_line >= line_increment :
                rst_output   += f'    {pair[0]}, {pair[1]}\n'
                previous_line = pair[1]
    #
    return rst_output
# -----------------------------------------------------------------------------
# write file corresponding to a section
def write_file(
    tmp_dir,
    section_name,
    rst_output,
) :
    # open output file
    file_out = tmp_dir + '/' + section_name + '.rst'
    file_ptr = open(file_out, 'w')
    file_ptr.write(rst_output)
    file_ptr.close()
# =============================================================================
# main program
# =============================================================================
def main() :
    # check working directory
    if not os.path.isdir('.git') :
        msg = 'must be executed from to top directory for a git repository'
        xsrst.system_exit(msg)
    #
    # check number of command line arguments
    if len(sys.argv) != 6 and len(sys.argv) != 7 :
        usage  = 'bin/xsrst.py target root_file sphinx_dir spelling keyword'
        usage += ' [line_increment]'
        xsrst.system_exit(usage)
    #
    # target
    target = sys.argv[1]
    if target != 'html' and target != 'pdf' :
        msg  = 'target = ' + target + '\n'
        msg += 'is not "html" or "pdf"'
        xsrst.system_exit(msg)
    #
    # root_file
    root_file = sys.argv[2]
    if not os.path.isfile(root_file) :
        msg  = 'root_file = ' + root_file + '\n'
        msg += 'is not a file'
        xsrst.system_exit(msg)
    #
    # sphinx_dir
    sphinx_dir      = sys.argv[3]
    if not os.path.isdir(sphinx_dir) :
        msg  = 'sphinx_dir = ' + sphinx_dir + '\n'
        msg += 'is a vlid directory path'
        xsrst.system_exit(msg)
    if sphinx_dir[0] == '/' :
        msg  = 'sphinx_dir = ' + sphinx_dir + '\n'
        msg += 'must be a path relative to current workding directory'
        xsrst.system_exit(msg)
    if 0 <= sphinx_dir.find('../') :
        msg  = 'sphinx_dir = ' + sphinx_dir + '\n'
        msg += 'cannot contain ../'
        xsrst.system_exit(msg)
    #
    # spelling
    spelling   = sys.argv[4]
    spell_path = sphinx_dir + '/' + spelling
    if not os.path.isfile(spell_path) :
        msg  = 'sphinx_dir/spelling = ' + spell_path + '\n'
        msg += 'is not a file'
        xsrst.system_exit(msg)
    #
    # keyword
    keyword      = sys.argv[5]
    keyword_path = sphinx_dir + '/' + keyword
    if not os.path.isfile(keyword_path) :
        msg  = 'sphinx_dir/keyword = ' + keyword_path + '\n'
        msg += 'is not a file'
        xsrst.system_exit(msg)
    #
    # line_increment
    if len(sys.argv) == 6 :
        line_increment = 0
    else :
        line_increment = int(sys.argv[6])
        if line_increment < 1 :
            msg += 'line_increment is not a positive integer'
            xsrst.system_exit(msg)
    #
    # conf.y
    file_path = sphinx_dir + '/conf.py'
    if not os.path.isfile( file_path ) :
        msg  = 'can not find the file conf.py\n'
        msg += 'in sphinx_dir = ' + sphinx_dir
        xsrst.system_exit(msg)
    #
    # xsrist_dir
    xsrst_dir = sphinx_dir + '/xsrst'
    if not os.path.isdir(xsrst_dir) :
        os.mkdir(xsrst_dir)
    #
    # tmp_dir
    tmp_dir = xsrst_dir + '/tmp'
    if os.path.isdir(tmp_dir) :
        shutil.rmtree(tmp_dir)
    os.mkdir(tmp_dir)
    #
    # spell_checker
    spell_list           = xsrst.file2_list_str(spell_path)
    spell_checker        = xsrst.create_spell_checker(spell_list)
    #
    # index_list
    index_list = list()
    for regexp in xsrst.file2_list_str(keyword_path) :
        index_list.append( re.compile( regexp ) )
    # -----------------------------------------------------------------------
    # pattern
    # -----------------------------------------------------------------------
    pattern = dict()
    #
    # regular expressions corresponding to xsrst commands
    pattern['suspend'] = re.compile( r'\n[ \t]*\{xsrst_suspend\}' )
    pattern['resume']  = re.compile( r'\n[ \t]*\{xsrst_resume\}' )
    # -------------------------------------------------------------------------
    # process each file in the list
    section_info     = list()
    file_info_stack  = list()
    file_info_done   = list()
    info = {
        'file_in'        : root_file,
        'parent_file'    : None,
        'parent_section' : None,
    }
    file_info_stack.append(info)
    while 0 < len(file_info_stack) :
        # pop first element is stack so that order in pdf file and
        # table of contents is correct
        info  = file_info_stack.pop(0)
        #
        for info_tmp in file_info_done :
            if info_tmp['file_in'] == info['file_in'] :
                msg  = 'The file ' + info['file_in'] + ' is included twice\n'
                msg += 'Once in ' + info_tmp['parent_file'] + '\n'
                msg += 'and again in ' + info['parent_file'] + '\n'
                xsrst.system_exit(msg)
        file_info_done.append(info)
        #
        file_in              = info['file_in']
        parent_file          = info['parent_file']
        parent_file_section  = info['parent_section']
        assert os.path.isfile(file_in)
        #
        # get xsrst docuemntation in this file
        this_file_info = xsrst.get_file_info(
            section_info,
            file_in,
        )
        #
        # determine index of parent section for this file
        this_file_parent_section_index = None
        for i in range( len(this_file_info) ) :
            if this_file_info[i]['is_parent'] :
                this_file_parent_section_index = len(section_info) + i
        #
        # add this files sections to section_info
        for i_file in range( len(this_file_info) ) :
            # ----------------------------------------------------------------
            # section_name, section_data
            section_name = this_file_info[i_file]['section_name']
            section_data = this_file_info[i_file]['section_data']
            is_parent    = this_file_info[i_file]['is_parent']
            if is_parent or this_file_parent_section_index is None :
                parent_section = parent_file_section
            else :
                parent_section = this_file_parent_section_index
            #
            section_info.append( {
                'section_name'   : section_name,
                'file_in'        : file_in,
                'parent_section' : parent_section
            } )
            # ----------------------------------------------------------------
            # process spell commands
            # do after suspend and before other commands to help ignore
            # sections of text that do not need spell checking
            section_data = xsrst.spell_command(
                section_data,
                file_in,
                section_name,
                spell_checker,
            )
            # ----------------------------------------------------------------
            # process child command
            section_data, child_file, child_section = xsrst.child_commands(
                section_data,
                file_in,
                section_name,
            )
            section_index = len(section_info) - 1
            for file_tmp in child_file :
                file_info_stack.append( {
                    'file_in'        : file_tmp,
                    'parent_file'    : file_in,
                    'parent_section' : section_index,
                } )
            # ----------------------------------------------------------------
            # process code commands
            section_data = xsrst.code_command(
                section_data,
                file_in,
                section_name,
            )
            # ---------------------------------------------------------------
            # file command: convert start and stop to line numbers
            section_data = xsrst.file_command(
                section_data,
                file_in,
                section_name,
                xsrst_dir,
            )
            # ---------------------------------------------------------------
            # add labels and indices corresponding to headings
            section_data, section_title, pseudo_heading = \
            xsrst.process_headings(
                section_data,
                file_in,
                section_name,
                index_list,
            )
            # section title is used by table_of_contents
            section_info[section_index]['section_title'] = section_title
            # ----------------------------------------------------------------
            # list_children
            # first section in each file may need to add to child list
            list_children = list()
            if is_parent :
                for i in range( len(this_file_info) ) :
                    if i != i_file :
                        list_children.append(this_file_info[i]['section_name'])
            list_children = list_children + child_section
            # ---------------------------------------------------------------
            rst_output = compute_output(
                file_in,
                section_data,
                list_children,
                pseudo_heading,
                section_name,
                line_increment,
            )
            # ---------------------------------------------------------------
            write_file(
                tmp_dir,
                section_name,
                rst_output,
            )
    # -------------------------------------------------------------------------
    # xstst_automatic.rst
    output_data = '.. include:: ../preamble.rst\n'
    #
    if target == 'pdf' :
        # The top level heading is not included in pdf output
        output_data += '\n'
        output_data += 'Dummy Heading\n'
        output_data += '#############\n'
    #
    # Table of Contents
    level         = 1
    count         = list()
    section_index = 0
    output_data  += xsrst.table_of_contents(
        tmp_dir, target, section_info, level, count, section_index
    )
    if target == 'html' :
        # Link to Index
        output_data += '\n'
        output_data += 'Link to Index\n'
        output_data += '*************\n'
        output_data += '* :ref:`genindex`\n'
    #
    file_out    = tmp_dir + '/' + 'xsrst_automatic.rst'
    file_ptr    = open(file_out, 'w')
    file_ptr.write(output_data)
    file_ptr.close()
    # -------------------------------------------------------------------------
    # section_info[0] corresponds to the root section
    assert section_info[0]['file_in'] == root_file
    assert section_info[0]['parent_section'] is None
    section_name = section_info[0]['section_name']
    #
    # index.rst
    index_file   = sphinx_dir + '/index.rst'
    file_ptr     = open(index_file, 'w')
    output_data  = section_name.upper() + '\n'
    output_data += len(section_name) * '#' + '\n\n'
    output_data += '.. comment '
    output_data += 'This file was automatically generated by xsrst.py\n\n'
    output_data += '.. toctree::\n'
    output_data += '   xsrst/xsrst_automatic\n'
    output_data += '   xsrst/' + section_name + '\n'
    file_ptr.write(output_data)
    file_ptr.close()
    #
    # -------------------------------------------------------------------------
    # overwrite xsrst files that have changed and then remove temporary files
    tmp_list   = os.listdir(tmp_dir)
    xsrst_list = os.listdir(xsrst_dir)
    for name in tmp_list :
        src = tmp_dir + '/' + name
        des = xsrst_dir + '/' + name
        if name.endswith('.rst') :
            if name not in xsrst_list :
               shutil.copyfile(src, des)
            else :
                if not filecmp.cmp(src, des, shallow=False) :
                    os.replace(src, des)
    for name in xsrst_list :
        if name.endswith('.rst') :
            if name not in tmp_list :
                os.remove( xsrst_dir + '/' + name )
    # reset tmp_dir becasue rmtree is such a dangerous command
    tmp_dir = xsrst_dir + '/tmp'
    shutil.rmtree(tmp_dir)
    # -------------------------------------------------------------------------
main()
print('xsrst.py: OK')
sys.exit(0)
