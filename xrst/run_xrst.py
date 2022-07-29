#! /usr/bin/env python3
# -----------------------------------------------------------------------------
#                      xrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xrst_begin run_xrst}
{xrst_spell
    cd
    conf
    dir
    mv
}

Run Extract Sphinx RST And Sphinx
#################################



Syntax
******
-   ``xrst`` *target* *root_file* *sphinx_dir* *spelling* *keyword*
    [ *line_increment* ]


Notation
********

White Space
===========
We define white space to be a sequence of space characters; e.g.,
tabs are not consider white space by xrst.

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

Run Sphinx
----------
If *target* is ``html`` you can generate the sphinx output using
the following command:

|space|   ``sphinx-build -b html`` *sphinx_dir* *html_dir*

where *html_dir* is the directory where the html files are written,
see below for the meaning of *sphinx_dir*.
If *target* is ``pdf``, you can use the following commands:
{xrst_code sh}
cd sphinx_dir
sed -i.bak preamble.rst -e '/BEGIN_LATEX_MACROS/,/END_LATEX_MACROS/d'
sphinx-build -b latex . latex
mv preamble.rst.bak preamble.rst
cd latex
sed -i xrst.tex -e 's|\\chapter{|\\paragraph{|'
make xrst.pdf
{xrst_code}

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
each time ``run_xrst`` executes.
The sub-directory *sphinx_dir* :code:`/xrst` is managed by ``xrst`` .
All the ``.rst`` files in *sphinx_dir* :code:`/xrst`
were extracted from the source code and correspond to
last time that ``run_xrst`` was executed.
Files that do not change are not updated (to speed up the processing).

conf.py
-------
The sphinx configuration file; e.g., :ref:`conf.py`.

preamble.rst
------------
An rst file that is automatically included at the beginning of every section.
This file should only define things, it should not generate any output.
For example, :ref:`preamble_rst`.


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
For example; see :ref:`spelling`.
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
For example; see :ref:`keyword`.

line_increment
==============
This optional argument helps find the source of errors reported by sphinx.
If the argument *line_increment* is present,
a table is generated at the end of each output file.
This table maps line numbers in the output file to
line numbers in the corresponding xrst input file.
The argument *line_increment* is a positive integer specifying the minimum
difference between xrst input line numbers for entries in the table.
The value ``1`` will give the maximum resolution.
For example, the sphinx warning

| |tab| ... ``/xrst/children_exam.rst:30: WARNING:`` ...

corresponds to line number 30 in the file ``children_exam.rst``.
The table at the bottom of that file maps line numbers in
``children_exam.rst`` to line numbers in the corresponding xrst input file.

{xrst_end run_xrst}
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
if( os.getcwd().endswith('/xrst.git') ) :
    if( os.path.isdir('xrst') ) :
        sys.path.insert(0, os.getcwd() )
#
import xrst
def run_xrst() :
    # check working directory
    if not os.path.isdir('.git') :
        msg = 'must be executed from to top directory for a git repository'
        xrst.system_exit(msg)
    #
    # check number of command line arguments
    if len(sys.argv) != 6 and len(sys.argv) != 7 :
        usage  = 'python -m xrst target root_file sphinx_dir spelling keyword'
        usage += ' [line_increment]'
        xrst.system_exit(usage)
    #
    # target
    target = sys.argv[1]
    if target != 'html' and target != 'pdf' :
        msg  = 'target = ' + target + '\n'
        msg += 'is not "html" or "pdf"'
        xrst.system_exit(msg)
    #
    # root_file
    root_file = sys.argv[2]
    if not os.path.isfile(root_file) :
        msg  = 'root_file = ' + root_file + '\n'
        msg += 'is not a file'
        xrst.system_exit(msg)
    #
    # sphinx_dir
    sphinx_dir      = sys.argv[3]
    if not os.path.isdir(sphinx_dir) :
        msg  = 'sphinx_dir = ' + sphinx_dir + '\n'
        msg += 'is a vlid directory path'
        xrst.system_exit(msg)
    if sphinx_dir[0] == '/' :
        msg  = 'sphinx_dir = ' + sphinx_dir + '\n'
        msg += 'must be a path relative to current workding directory'
        xrst.system_exit(msg)
    if 0 <= sphinx_dir.find('../') :
        msg  = 'sphinx_dir = ' + sphinx_dir + '\n'
        msg += 'cannot contain ../'
        xrst.system_exit(msg)
    #
    # spelling
    spelling   = sys.argv[4]
    spell_path = sphinx_dir + '/' + spelling
    if not os.path.isfile(spell_path) :
        msg  = 'sphinx_dir/spelling = ' + spell_path + '\n'
        msg += 'is not a file'
        xrst.system_exit(msg)
    #
    # keyword
    keyword      = sys.argv[5]
    keyword_path = sphinx_dir + '/' + keyword
    if not os.path.isfile(keyword_path) :
        msg  = 'sphinx_dir/keyword = ' + keyword_path + '\n'
        msg += 'is not a file'
        xrst.system_exit(msg)
    #
    # line_increment
    if len(sys.argv) == 6 :
        line_increment = 0
    else :
        line_increment = int(sys.argv[6])
        if line_increment < 1 :
            msg += 'line_increment is not a positive integer'
            xrst.system_exit(msg)
    #
    # conf.y
    file_path = sphinx_dir + '/conf.py'
    if not os.path.isfile( file_path ) :
        msg  = 'can not find the file conf.py\n'
        msg += 'in sphinx_dir = ' + sphinx_dir
        xrst.system_exit(msg)
    #
    # xsrist_dir
    xrst_dir = sphinx_dir + '/xrst'
    if not os.path.isdir(xrst_dir) :
        os.mkdir(xrst_dir)
    #
    # tmp_dir
    tmp_dir = xrst_dir + '/tmp'
    if os.path.isdir(tmp_dir) :
        shutil.rmtree(tmp_dir)
    os.mkdir(tmp_dir)
    #
    # spell_checker
    spell_list           = xrst.file2_list_str(spell_path)
    spell_checker        = xrst.create_spell_checker(spell_list)
    #
    # index_list
    index_list = list()
    for regexp in xrst.file2_list_str(keyword_path) :
        index_list.append( re.compile( regexp ) )
    # -----------------------------------------------------------------------
    # pattern
    # -----------------------------------------------------------------------
    pattern = dict()
    #
    # regular expressions corresponding to xrst commands
    pattern['suspend'] = re.compile( r'\n[ \t]*\{xrst_suspend\}' )
    pattern['resume']  = re.compile( r'\n[ \t]*\{xrst_resume\}' )
    # -------------------------------------------------------------------------
    # process each file in the list
    sinfo_list       = list()
    finfo_stack      = list()
    finfo_done       = list()
    finfo = {
        'file_in'        : root_file,
        'parent_file'    : None,
        'parent_section' : None,
    }
    finfo_stack.append(finfo)
    while 0 < len(finfo_stack) :
        # pop first element is stack so that order in pdf file and
        # table of contents is correct
        finfo  = finfo_stack.pop(0)
        #
        for finfo_tmp in finfo_done :
            if finfo_tmp['file_in'] == finfo['file_in'] :
                msg  = 'The file ' + finfo['file_in'] + ' is included twice\n'
                msg += 'Once in ' + finfo_tmp['parent_file'] + '\n'
                msg += 'and again in ' + finfo['parent_file'] + '\n'
                xrst.system_exit(msg)
        finfo_done.append(finfo)
        #
        file_in              = finfo['file_in']
        parent_file          = finfo['parent_file']
        parent_file_section  = finfo['parent_section']
        assert os.path.isfile(file_in)
        #
        # get xrst docuemntation in this file
        sinfo_file_in = xrst.get_file_info(
            sinfo_list,
            file_in,
        )
        #
        # parent_section_file_in
        # index in sinfo_list of parent section for this file
        parent_section_file_in = None
        if sinfo_file_in[0]['is_parent'] :
            parent_section_file_in = len(sinfo_list)
        #
        # add this files sections to sinfo_list
        for i_section in range( len(sinfo_file_in) ) :
            # ----------------------------------------------------------------
            # section_name, section_data, is_parent
            section_name = sinfo_file_in[i_section]['section_name']
            section_data = sinfo_file_in[i_section]['section_data']
            is_parent    = sinfo_file_in[i_section]['is_parent']
            is_child     = sinfo_file_in[i_section]['is_child']
            #
            # parent_section
            if is_parent or parent_section_file_in is None :
                parent_section = parent_file_section
            else :
                parent_section = parent_section_file_in
            #
            # sinfo_list
            sinfo_list.append( {
                'section_name'   : section_name,
                'file_in'        : file_in,
                'parent_section' : parent_section,
                'in_parent_file' : is_child,
            } )
            # ----------------------------------------------------------------
            # spell_command
            # do after suspend and before other commands to help ignore
            # sections of text that do not need spell checking
            section_data = xrst.spell_command(
                section_data,
                file_in,
                section_name,
                spell_checker,
            )
            # ----------------------------------------------------------------
            # child commands
            section_data, child_file, child_section_list = xrst.child_commands(
                section_data,
                file_in,
                section_name,
            )
            #
            # section_index, finfo_stack
            section_index = len(sinfo_list) - 1
            for file_tmp in child_file :
                finfo_stack.append( {
                    'file_in'        : file_tmp,
                    'parent_file'    : file_in,
                    'parent_section' : section_index,
                } )
            # ----------------------------------------------------------------
            # code commands
            section_data = xrst.code_command(
                section_data,
                file_in,
                section_name,
            )
            # ---------------------------------------------------------------
            # file command
            section_data = xrst.file_command(
                section_data,
                file_in,
                section_name,
                xrst_dir,
            )
            # ---------------------------------------------------------------
            # process headings
            # add labels and indices corresponding to headings
            section_data, section_title, pseudo_heading = \
            xrst.process_headings(
                section_data,
                file_in,
                section_name,
                index_list,
            )
            # section title is used by table_of_contents
            sinfo_list[section_index]['section_title'] = section_title
            # ----------------------------------------------------------------
            # list_children
            # section_name for each of the children of the current section
            list_children = child_section_list
            if is_parent :
                for i in range( len(sinfo_file_in) ) :
                    if i != i_section :
                        list_children.append(sinfo_file_in[i]['section_name'])
            # ---------------------------------------------------------------
            # process children
            section_data = xrst.process_children(
                section_name,
                section_data,
                list_children,
            )
            # ---------------------------------------------------------------
            # write temporary file
            xrst.temporary_file(
                line_increment,
                pseudo_heading,
                file_in,
                tmp_dir,
                section_name,
                section_data,
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
    output_data  += xrst.table_of_contents(
        tmp_dir, target, sinfo_list, level, count, section_index
    )
    if target == 'html' :
        # Link to Index
        output_data += '\n'
        output_data += 'Link to Index\n'
        output_data += '*************\n'
        output_data += '* :ref:`genindex`\n'
    #
    file_out    = tmp_dir + '/' + 'xrst_automatic.rst'
    file_ptr    = open(file_out, 'w')
    file_ptr.write(output_data)
    file_ptr.close()
    # -------------------------------------------------------------------------
    # sinfo_list[0] corresponds to the root section
    assert sinfo_list[0]['file_in'] == root_file
    assert sinfo_list[0]['parent_section'] is None
    section_name = sinfo_list[0]['section_name']
    #
    # index.rst
    index_file   = sphinx_dir + '/index.rst'
    file_ptr     = open(index_file, 'w')
    output_data  = section_name.upper() + '\n'
    output_data += len(section_name) * '#' + '\n\n'
    output_data += '.. comment '
    output_data += 'This file was automatically generated by xrst\n\n'
    output_data += '.. toctree::\n'
    output_data += '   xrst/xrst_automatic\n'
    output_data += '   xrst/' + section_name + '\n'
    file_ptr.write(output_data)
    file_ptr.close()
    #
    # -------------------------------------------------------------------------
    # overwrite xrst files that have changed and then remove temporary files
    tmp_list   = os.listdir(tmp_dir)
    xrst_list = os.listdir(xrst_dir)
    for name in tmp_list :
        src = tmp_dir + '/' + name
        des = xrst_dir + '/' + name
        if name.endswith('.rst') :
            if name not in xrst_list :
               shutil.copyfile(src, des)
            else :
                if not filecmp.cmp(src, des, shallow=False) :
                    os.replace(src, des)
    for name in xrst_list :
        if name.endswith('.rst') :
            if name not in tmp_list :
                os.remove( xrst_dir + '/' + name )
    # reset tmp_dir becasue rmtree is such a dangerous command
    tmp_dir = xrst_dir + '/tmp'
    shutil.rmtree(tmp_dir)
    # -------------------------------------------------------------------------
    print('xrst: OK')