#! /usr/bin/env python3
# -----------------------------------------------------------------------------
#                      xrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xrst_begin run_xrst user}
{xrst_spell
   dir
   furo
   pyspellchecker
   rtd
}

Run Extract Sphinx RST And Sphinx
#################################

Syntax
******
-  ``xrst`` ( --version |  *root_file* )
   [ ``--replace_spell_commands`` ]
   [ ``--html`` *html_theme* ]
   [ ``--rst`` *rst_line* ]
   [ ``--group`` *group_list* ]
   [ ``--target`` *target* ]
   [ ``--output`` *output_dir* ]
   [ ``--sphinx`` *sphinx_dir* ]

version
********
If ``--version`` is present on the command line, there are no other arguments
and the version of xrst is printed. Otherwise *root_file* is a required
argument.

root_file
*********
The command line argument *root_file* is the name of a file
containing the root section for the documentation tree.
This can be an absolute path or
relative to the directory where :ref:`xrst<run_xrst>` is executed.
There must be at least one section in *root_file* that has each
:ref:`begin_cmd@group_name` in the *group_list*.

project_name
============
The base part of *root_file*, without directories or file extension,
is used as the sphinx project name.

replace_spell_commands
**********************
If this command is present on the command line, the source code
:ref:`spell commands<spell_cmd>` a replaced in such a way that the
there will be no spelling warnings during future processing by xrst.
This useful when there are no spelling warnings before a change
to the :ref:`run_xrst@sphinx_dir@spelling` file or an update
of the pyspellchecker_ package (which is used to do the spell checking).

.. _pyspellchecker: https://pypi.org/project/pyspellchecker

html_theme
**********
This the html_theme_ that is used.
The possible values (so far) are;
``furo``, ``sphinx_rtd_theme`` .
The default value for *html_theme* is ``sphinx_rtd_theme`` .

.. _html_theme: https://sphinx-themes.org/

The ``sphinx_rtd_theme`` theme includes a local table of contents for the
headers at the top of each section.
The other themes include this information in the right side bar.


rst_line
********
This optional argument helps find the source of errors reported by sphinx.
If the argument *rst_line* is (is not) present,
a table is (is not) generated at the end of each output file.
This table maps line numbers in the rst output files to
line numbers in the corresponding xrst input file.
The argument *rst_line* is a positive integer specifying the minimum
difference between xrst input line numbers for entries in the table.
The value ``1`` will give the maximum resolution.
For example, the sphinx warning

| |tab| ... ``/xrst/children_exam.rst:30: WARNING:`` ...

corresponds to line number 30 in the file ``children_exam.rst``.
The table at the bottom of that file maps line numbers in
``children_exam.rst`` to line numbers in the corresponding xrst input file.

group_list
**********
It is possible to select one or more groups of sections
to include in the output using this optional argument.

#. The *group_list* is a comma separated list of
   :ref:`group names<begin_cmd@group_name>`.
#. If *group_list* begins or ends with a comma, the empty group is included
   along with the other groups specified by *group_list*.
   Note that it is the group name and not the group that is empty.
#. The order of the groups determines their order in the resulting output.
#. The default value for *group_list* is ``,`` .

One use case for this is where the user documentation is a subset of the
developer documentation. This enables the developer documentation to
easily link to the specific paragraphs in the user documentation.
It also enables the same source code file to provide both the developer
and user documentation for the actions it provides.

target
******
The optional command line argument *target* must be ``html`` or ``pdf``.
It specifies the type of type output you plan to generate using sphinx.
The default value for *target* is ``html`` .

output_dir
**********
The optional command line argument *sphinx_dir* is a directory relative to
of the directory where *root_file* is located.
If *target* is ``html``, the html files are placed in this directory.
If *target* is ``pdf``, the output file is

| *output_dir*\ ``/latex/``\ *project_name*\ ``.pdf``

see :ref:`run_xrst@root_file@project_name` .
The default value for *output_dir* is *sphinx_dir* ``/html`` .

sphinx_dir
**********
The optional command line argument *sphinx_dir* is a directory relative to
of the directory where *root_file* is located.
This directory contains the optional configuration files (described below)
and the files generated by ``xrst`` .
The default value for *sphinx_dir* is ``sphinx`` .

preamble.rst
============
The file *sphinx_dir* ``/preamble.rst`` can be create by the user.
If it exists, it is included at the beginning of every section.
It should only define things, it should not generate any output.
For example, :ref:`@preamble.rst`.
The Latex macros in this file can be used by any section.
There must be one macro definition per line and each such line must match the
following python regular expression:

   ``\n[ \t]*:math:`\\newcommand\{[^`]*\}`[ \t]*``

Example
-------
:ref:`@preamble.rst`

spelling
========
The file *sphinx_dir* ``/spelling`` can be create by the user.
If it exists, it contains a list of words
that the spell checker will consider correct for all sections.
A line that begins with :code:`#` is a comment (not included in the list).
The words are one per line and
leading and trailing white space in a word are ignored.
For example; see :ref:`@spelling`.
Special words, for a particular section, are specified using the
:ref:`spell command<spell_cmd>`.

Example
-------
:ref:`@spelling`

keyword
=======
The file *sphinx_dir* ``/keyword`` can be create by the user.
If it exists, it contains a list of
python regular expressions for heading tokens
that are not included in the index.
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
For example; see :ref:`@keyword`.

Example
-------
:ref:`@keyword`

Section RST Files
=================
The directory *sphinx_dir*\ :code:`/rst` is managed by ``xrst`` .
It contains all the rst files that were extracted from the source code,
and correspond to last time that ``xrst`` was executed.
For each :ref:`begin_cmd@section_name`, the file

|space| *sphinx_dir*\ ``/xrst/``\ *section_name*\ ``.rst``

Is the RST file for the corresponding section. There is one exception
to this rule. If *section_name* ends with ``.rst``, the extra ``.rst``
is not added at the end.

Other Generated Files
=====================
See :ref:`@auto_file` for the other files generated by ``xrst`` in the
*sphinx_dir* directory.


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
import argparse
import subprocess
# ---------------------------------------------------------------------------
def system_command(command) :
   print(command)
   command = command.split(' ')
   result = subprocess.run(command, capture_output = True)
   stderr = result.stderr.decode('utf-8')
   ok     =  result.returncode == 0 and stderr == ''
   if ok :
      return
   msg  = f'system command failed: stderr = \n{stderr}'
   sys.exit(msg)
# ---------------------------------------------------------------------------
# sys.path
# used so that we can test before installing
if( os.getcwd().endswith('/xrst.git') ) :
   if( os.path.isdir('xrst') ) :
      sys.path.insert(0, os.getcwd() )
#
import xrst
#
# version
# The script that updates version numbers expects version at begining of line
# and to have the value surrounded by single quotes.
version = '2022.8.29'
#
def run_xrst() :
   #
   # execution_directory
   execution_directory = os.getcwd()
   #
   # parser
   parser = argparse.ArgumentParser(
      prog='xrst', description='extract Sphinx RST files'
   )
   parser.add_argument('--version', action='store_true',
      help='just print version of xrst'
   )
   parser.add_argument('root_file', nargs='?', default=None,
      help='file that contains root section (not required for --version'
   )
   parser.add_argument('--replace_spell_commands', action='store_true',
      help='replace the xrst spell commands in source code files'
   )
   parser.add_argument(
      '--html', metavar='html_theme', default='sphinx_rtd_theme',
      help='sphinx html_theme that is used to display web pages',
      choices=[ 'furo', 'sphinx_rtd_theme', 'sphinx_book_theme' ]
   )
   parser.add_argument(
      '--rst', metavar='rst_line', type=int,
      help='increment in table that converts sphinx error messages'
   )
   parser.add_argument(
      '--group', metavar='group_list', default=',',
      help='comma separated list of groups to include (default: ,)'
   )
   parser.add_argument(
      '--target', metavar='target', choices=['html', 'pdf'], default='html',
      help='type of output files, choices are html or pdf (default: html)'
   )
   parser.add_argument(
      '--output', metavar='output_dir',
      help= 'directory containing the sphinx output files ' +
      '(default: sphinx_dir/html)'
   )
   parser.add_argument(
      '--sphinx', metavar='sphinx_dir', default='sphinx',
      help='directory containing configuration and xrst generated files ' +
      '(default: sphinx)'
   )
   #
   # arguments
   arguments = parser.parse_args()
   #
   if arguments.version :
      print(version)
      sys.exit(0)
   #
   # root_file
   # can not use system_exit until os.getcwd() returns root_directory
   root_file = arguments.root_file
   if root_file == None :
      msg  = 'xsrst: Error\n'
      msg += 'root_file is required when not using the --version option'
      sys.exit(msg)
   if not os.path.isfile(root_file) :
      msg  = 'xsrst: Error\n'
      msg += f'root_file = {root_file}\n'
      if root_file[0] == '/' :
         msg += 'is not a file\n'
      else :
         msg += f'is not a file relative to the execution directory\n'
         msg += execution_directory
      sys.exit(msg)
   #
   # root_directory
   index = root_file.rfind('/')
   if index < 0 :
      root_directory = '.'
   elif index == 0 :
      root_directory = '/'
   elif 0 < index :
      root_directory = root_file[: index]
   os.chdir(root_directory)
   #
   # replace_spell_commands
   replace_spell_commands = arguments.replace_spell_commands
   if replace_spell_commands :
      cwd      = os.getcwd()
      prompt   = '\nThe replace_spell_commands option will change some of \n'
      prompt  += 'the files read by xrst. Make sure that you have a backup\n'
      prompt  += f'of source files in {cwd}\n'
      prompt  += 'before contining this operation: continue [yes/no] ? '
      response = None
      while response not in [ 'yes', 'no' ]:
         response = input(prompt)
      if response != 'yes' :
         sys.exit('xrst: aborting replace_spell_commands')
   #
   # html_theme
   html_theme = arguments.html
   #
   # rst_line
   rst_line = arguments.rst
   if rst_line == None :
      rst_line = 0
   else :
      if rst_line < 1 :
         msg = 'rst_line is not a positive integer'
         xrst.system_exit(msg)
   #
   # group_list
   group_list = arguments.group
   if group_list == ',' :
      group_list = [ '' ]
   else :
      group_list = group_list.split(',')
   #
   # target
   target = arguments.target
   #
   # sphinx_dir
   sphinx_dir = arguments.sphinx
   if not os.path.isdir(sphinx_dir) :
      msg  = 'sphinx_dir = ' + sphinx_dir + '\n'
      msg += 'is a valid directory path'
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
   # output_dir
   output_dir = arguments.output
   if output_dir == None :
      output_dir = f'{sphinx_dir}/html'
   #
   # rst_dir
   rst_dir = sphinx_dir + '/rst'
   if not os.path.isdir(rst_dir) :
      os.mkdir(rst_dir)
   #
   # tmp_dir
   tmp_dir = rst_dir + '/tmp'
   if os.path.isdir(tmp_dir) :
      shutil.rmtree(tmp_dir)
   os.mkdir(tmp_dir)
   #
   # spell_checker
   spell_list  = list()
   spell_file  = sphinx_dir + '/spelling'
   if os.path.isfile( spell_file ) :
      spell_list  = xrst.file2_list_str(spell_file)
   spell_checker = xrst.create_spell_checker(spell_list)
   #
   # keyword_list
   keyword_list = list()
   keyword_file = sphinx_dir + '/keyword'
   if os.path.isfile( keyword_file ) :
      str_list = xrst.file2_list_str(keyword_file)
      for regexp in str_list :
         keyword_list.append( re.compile( regexp ) )
   # -------------------------------------------------------------------------
   #
   # root_local
   index = root_file.rfind('/')
   if index < 0 :
      root_local = root_file
   else :
      root_local = root_file[index + 1 :]
   #
   # project_name
   project_name = root_local
   index        = root_local.rfind('.')
   if 0 < index :
      project_name = root_local[: index]
   #
   # sinfo_list
   # This list accumulates over all the group names
   sinfo_list       = list()
   #
   # root_section_list
   # Each group has a root secion (in root_file) at the top if its tree.
   root_section_list = list()
   #
   # group_name
   for group_name in group_list :
      #
      # finfo_stack, finfo_done
      # This information is by file, not section
      finfo_stack      = list()
      finfo_done       = list()
      finfo = {
         'file_in'        : root_local,
         'parent_file'    : None,
         'parent_section' : None,
      }
      finfo_stack.append(finfo)
      #
      while 0 < len(finfo_stack) :
         # pop first element is stack so that order in pdf file and
         # table of contents is correct
         finfo  = finfo_stack.pop(0)
         #
         for finfo_tmp in finfo_done :
            if finfo_tmp['file_in'] == finfo['file_in'] :
               msg  = 'The file ' + finfo['file_in']
               msg += '\nis included twice with '
               msg += f'group_name = "{group_name}"\n'
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
            group_name,
            parent_file,
            file_in,
         )
         #
         # root_section_list
         if finfo['parent_file'] == None :
            assert file_in == root_local
            section_name = sinfo_file_in[0]['section_name']
            root_section_list.append(section_name)
         #
         # parent_section_file_in
         # index in sinfo_list of parent section for this file
         parent_section_file_in = None
         if sinfo_file_in[0]['is_parent'] :
            parent_section_file_in = len(sinfo_list)
         #
         # add this files sections to sinfo_list
         for i_section in range( len(sinfo_file_in) ) :
            # ------------------------------------------------------------
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
            # -------------------------------------------------------------
            # spell_command
            # do after suspend and before other commands to help ignore
            # sections of text that do not need spell checking
            section_data = xrst.spell_command(
               tmp_dir,
               section_data,
               file_in,
               section_name,
               spell_checker,
            )
            # -------------------------------------------------------------
            # toc commands
            section_data, child_file, child_section_list = \
               xrst.toc_commands(
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
            # ------------------------------------------------------------
            # code commands
            section_data = xrst.code_command(
               section_data,
               file_in,
               section_name,
            )
            # ------------------------------------------------------------
            # literal command
            section_data = xrst.literal_command(
               section_data,
               file_in,
               section_name,
               rst_dir,
            )
            # ------------------------------------------------------------
            # process headings
            # add labels and indices corresponding to headings
            section_data, section_title, pseudo_heading = \
            xrst.process_headings(
               html_theme,
               section_data,
               file_in,
               section_name,
               keyword_list,
            )
            # sinfo_list
            # section title is used by table_of_contents
            sinfo_list[section_index]['section_title'] = section_title
            # -------------------------------------------------------------
            # list_children
            # section_name for each of the children of the current section
            list_children = child_section_list
            if is_parent :
               for i in range( len(sinfo_file_in) ) :
                  if i != i_section :
                     list_children.append(
                        sinfo_file_in[i]['section_name']
                     )
            # -------------------------------------------------------------
            # process children
            # want this as late as possible to toctree at end of input
            section_data = xrst.process_children(
               section_name,
               section_data,
               list_children,
            )
            # -------------------------------------------------------------
            # write temporary file
            xrst.temporary_file(
               rst_line,
               pseudo_heading,
               file_in,
               tmp_dir,
               section_name,
               section_data,
            )
   #
   # auto_file
   xrst.auto_file(
      html_theme, sphinx_dir, tmp_dir, target, sinfo_list, root_section_list
   )
   #
   # -------------------------------------------------------------------------
   #
   # rst_dir/*.rst
   tmp_list = os.listdir(tmp_dir)
   rst_list = os.listdir(rst_dir)
   for name in tmp_list :
      src = f'{tmp_dir}/{name}'
      des = f'{rst_dir}/{name}'
      if name.endswith('.rst') :
         if name not in rst_list :
               shutil.copyfile(src, des)
         else :
            if not filecmp.cmp(src, des, shallow=False) :
               os.replace(src, des)
   for name in rst_list :
      if name.endswith('.rst') :
         if name not in tmp_list :
            os.remove( f'{rst_dir}/{name}' )
   #
   # replace_spell
   if replace_spell_commands :
      xrst.replace_spell(tmp_dir)
   #
   # tmp_dir
   # reset tmp_dir because rmtree is such a dangerous command
   tmp_dir = f'{rst_dir}/tmp'
   shutil.rmtree(tmp_dir)
   # -------------------------------------------------------------------------
   if target == 'html' :
      command = f'sphinx-build -b html {sphinx_dir} {output_dir}'
      system_command(command)
   else :
      assert target == 'pdf'
      #
      latex_dir = f'{output_dir}/latex'
      command = f'sphinx-build -b latex {sphinx_dir} {latex_dir}'
      system_command(command)
      #
      command = f'make -C {latex_dir} {project_name}.pdf'
      system_command(command)
   # -------------------------------------------------------------------------
   print('xrst: OK')
