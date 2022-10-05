#! /usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
"""
{xrst_begin run_xrst user}
{xrst_spell
   dir
   furo
   pyspellchecker
   rtd
   xrst xrst
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
*******
If ``--version`` is present on the command line, there are no other arguments
and the version of xrst is printed. Otherwise *root_file* is a required
argument.

root_file
*********
The command line argument *root_file* is the name of a file
containing the root page for the documentation tree.
This can be an absolute path or
relative to the directory where :ref:`xrst<run_xrst>` is executed.
There must be at least one page in *root_file* that has each
:ref:`begin_cmd@group_name` in the *group_list*.

project_name
============
The base part of *root_file*, without directories or file extension,
is used as the sphinx project name.

replace_spell_commands
**********************
If this option is present on the command line, the source code
:ref:`spell commands<spell_cmd>` a replaced in such a way that the
there will be no spelling warnings during future processing by xrst.
This is useful when there are no spelling warnings before a change
to the :ref:`run_xrst@sphinx_dir@spelling` file or an update
of the pyspellchecker_ package (which is used to do the spell checking).
If this option is present,
none of the output files are created; e.g., the \*.rst and \*.html files.

.. _pyspellchecker: https://pypi.org/project/pyspellchecker

html_theme
**********
This the html_theme_ that is used.
The possible values (so far) are;
``furo``, ``sphinx_rtd_theme`` .
The default value for *html_theme* is ``sphinx_rtd_theme`` .

.. _html_theme: https://sphinx-themes.org/

The ``sphinx_rtd_theme`` theme includes a local table of contents for the
headers at the top of each page.
The other themes include this information in the right side bar.


rst_line
********
This option helps find the source of errors reported by sphinx.
If *rst_line* is (is not) present,
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
It is possible to select one or more groups of pages
to include in the output using this optional argument.

#. The *group_list* is a comma separated list of
   :ref:`group names<begin_cmd@group_name>`.
#. If *group_list* begins or ends with a comma, the empty group is included
   along with the other groups specified by *group_list*.
   Note that it is the group name and not the group that is empty.
#. The order of the groups determines their order in the resulting output.
#. The default value for *group_list* is ``,`` .

The xrst examples are a subset of its user documentation
and its user documentation is a subset of its developer documentation.
For each command, the same source code file provides both the
user and developer documentation. In addition, the developer documentation
has links to the user documentation and the user documentation has links
to the examples.

Example
=======

#. The xrst examples use the empty group name
   and their documentation can be built using

   | xrst xrst.xrst --group ,

#. The xrst user documentation uses the empty, user, and app group names
   and its documentation can be built using

   | xrst xrst.xrst --group ,user,app

#. The xrst developer documentation uses the empty, user, app, and dev
   group names and its documentation can be built using

   | xrst xrst.xrst --group ,user,app,dev


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
If it exists, it is included at the beginning of every page.
It should only define things, it should not generate any output.
For example, :ref:`preamble.rst-0`.
The Latex macros in this file can be used by any page.
There must be one macro definition per line and each such line must match the
following python regular expression:

   ``\n[ \t]*:math:`\\newcommand\{[^`]*\}`[ \t]*``

Example
-------
:ref:`preamble.rst-0`

spelling
========
The file *sphinx_dir* ``/spelling`` can be create by the user.
If it exists, it contains a list of words
that the spell checker will consider correct for all pages.
A line that begins with :code:`#` is a comment (not included in the list).
The words are one per line and
leading and trailing white space in a word are ignored.
For example; see :ref:`spelling-0`.
Special words, for a particular page, are specified using the
:ref:`spell command<spell_cmd>`.

Example
-------
:ref:`spelling-0`

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
For example; see :ref:`keyword-0`.

Example
-------
:ref:`keyword-0`

Page RST Files
==============
The directory *sphinx_dir*\ :code:`/rst` is managed by ``xrst`` .
It contains all the rst files that were extracted from the source code,
and correspond to last time that ``xrst`` was executed.
For each :ref:`begin_cmd@page_name`, the file

|space| *sphinx_dir*\ ``/xrst/``\ *page_name*\ ``.rst``

Is the RST file for the corresponding page. There is one exception
to this rule. If *page_name* ends with ``.rst``, the extra ``.rst``
is not added at the end.

Other Generated Files
=====================
See :ref:`auto_file-0` for the other files generated by ``xrst`` in the
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
def fix_latex(latex_dir, project_name) :
   assert type(latex_dir) == str
   assert type(project_name) == str
   #
   # file_name
   file_name = f'{latex_dir}/{project_name}.tex'
   #
   # file_data
   file_ptr  = open(file_name, 'r')
   file_data = file_ptr.read()
   file_ptr.close()
   #
   # file_data
   pattern   = re.compile( r'\n\\section{' )
   file_data = pattern.sub( r'\n\\section*{', file_data)
   #
   # file_data
   pattern   = re.compile( r'\n\\subsection{' )
   file_data = pattern.sub( r'\n\\subsection*{', file_data)
   #
   # file_data
   pattern   = re.compile( r'\n\\subsubsection{' )
   file_data = pattern.sub( r'\n\\subsubsection*{', file_data)
   #
   # file_name
   file_ptr  = open(file_name, 'w')
   file_ptr.write(file_data)
   file_ptr.close()
   #
   return
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
version = '2022.10.5'
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
      help='file that contains root page (not required for --version'
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
   # pinfo_list
   # This list accumulates over all the group names
   pinfo_list       = list()
   #
   # root_page_list
   # Each group has a root secion (in root_file) at the top if its tree.
   root_page_list = list()
   #
   # group_name
   for group_name in group_list :
      #
      # finfo_stack, finfo_done
      # This information is by file, not page
      finfo_stack      = list()
      finfo_done       = list()
      finfo = {
         'file_in'        : root_local,
         'parent_file'    : None,
         'parent_page' : None,
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
         parent_file_page  = finfo['parent_page']
         assert os.path.isfile(file_in)
         #
         # get xrst docuemntation in this file
         sinfo_file_in = xrst.get_file_info(
            pinfo_list,
            group_name,
            parent_file,
            file_in,
         )
         #
         # root_page_list
         if finfo['parent_file'] == None :
            assert file_in == root_local
            page_name = sinfo_file_in[0]['page_name']
            root_page_list.append(page_name)
         #
         # parent_page_file_in
         # index in pinfo_list of parent page for this file
         parent_page_file_in = None
         if sinfo_file_in[0]['is_parent'] :
            parent_page_file_in = len(pinfo_list)
         #
         # add this files pages to pinfo_list
         for i_page in range( len(sinfo_file_in) ) :
            # ------------------------------------------------------------
            # page_name, page_data, is_parent
            page_name = sinfo_file_in[i_page]['page_name']
            page_data = sinfo_file_in[i_page]['page_data']
            is_parent    = sinfo_file_in[i_page]['is_parent']
            is_child     = sinfo_file_in[i_page]['is_child']
            #
            # parent_page
            if is_parent or parent_page_file_in is None :
               parent_page = parent_file_page
            else :
               parent_page = parent_page_file_in
            #
            # pinfo_list
            pinfo_list.append( {
               'page_name'      : page_name,
               'file_in'        : file_in,
               'parent_page'    : parent_page,
               'in_parent_file' : is_child,
            } )
            # -------------------------------------------------------------
            # comment_command
            page_data = xrst.comment_command(page_data)
            # -------------------------------------------------------------
            # spell_command
            # do after suspend and before other commands to help ignore
            # pages of text that do not need spell checking
            page_data = xrst.spell_command(
               tmp_dir,
               page_data,
               file_in,
               page_name,
               spell_checker,
            )
            # -------------------------------------------------------------
            # toc commands
            page_data, child_file, child_page_list = \
               xrst.toc_commands(
                  page_data,
                  file_in,
                  page_name,
                  group_name,
            )
            #
            # page_index, finfo_stack
            page_index = len(pinfo_list) - 1
            for file_tmp in child_file :
               finfo_stack.append( {
                  'file_in'        : file_tmp,
                  'parent_file'    : file_in,
                  'parent_page' : page_index,
               } )
            # ------------------------------------------------------------
            # code commands
            page_data = xrst.code_command(
               page_data,
               file_in,
               page_name,
               rst_dir,
            )
            # ------------------------------------------------------------
            # literal command
            page_data = xrst.literal_command(
               page_data,
               file_in,
               page_name,
               rst_dir,
            )
            # ------------------------------------------------------------
            # process headings
            # add labels and indices corresponding to headings
            page_data, page_title, pseudo_heading = \
            xrst.process_headings(
               html_theme,
               page_data,
               file_in,
               page_name,
               keyword_list,
            )
            # pinfo_list
            # page title is used by table_of_contents
            pinfo_list[page_index]['page_title'] = page_title
            # -------------------------------------------------------------
            # list_children
            # page_name for each of the children of the current page
            list_children = child_page_list
            if is_parent :
               for i in range( len(sinfo_file_in) ) :
                  if i != i_page :
                     list_children.append(
                        sinfo_file_in[i]['page_name']
                     )
            # -------------------------------------------------------------
            # process children
            # want this as late as possible to toctree at end of input
            page_data = xrst.process_children(
               page_name,
               page_data,
               list_children,
            )
            # -------------------------------------------------------------
            # write temporary file
            xrst.temporary_file(
               rst_line,
               pseudo_heading,
               file_in,
               tmp_dir,
               page_name,
               page_data,
            )
   #
   # replace_spell
   if replace_spell_commands :
      xrst.replace_spell(tmp_dir)
      #
      # tmp_dir
      # reset tmp_dir because rmtree is such a dangerous command
      tmp_dir = f'{rst_dir}/tmp'
      shutil.rmtree(tmp_dir)
      print('xrst --replace_spell_commands: OK')
      return
   #
   # auto_file
   xrst.auto_file(
      html_theme, sphinx_dir, tmp_dir, target, pinfo_list, root_page_list
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
            if name != 'index.rst' :
               os.remove( f'{rst_dir}/{name}' )
   #
   # tmp_dir
   # reset tmp_dir because rmtree is such a dangerous command
   tmp_dir = f'{rst_dir}/tmp'
   shutil.rmtree(tmp_dir)
   # -------------------------------------------------------------------------
   if target == 'html' :
      command = f'sphinx-build -b html {sphinx_dir}/rst {output_dir}'
      system_command(command)
   else :
      assert target == 'pdf'
      #
      latex_dir = f'{output_dir}/latex'
      command = f'sphinx-build -b latex {sphinx_dir}/rst {latex_dir}'
      system_command(command)
      #
      # latex_dir/project_name.tex
      fix_latex(latex_dir, project_name)
      #
      command = f'make -C {latex_dir} {project_name}.pdf'
      system_command(command)
   # -------------------------------------------------------------------------
   # output_dir/_static/css/theme.css
   # see https://stackoverflow.com/questions/23211695/
   #  modifying-content-width-of-the-sphinx-theme-read-the-docs
   if html_theme == 'sphinx_rtd_theme' and target == 'html' :
      pattern = dict()
      pattern['content'] = re.compile(
         r'([.]wy-nav-content[{][^}]*;max-width):[^;]*;'
      )
      pattern['sidebar'] = re.compile(
         r'([.]wy-nav-side[{][^}]*;width):[^;]*;'
      )
      pattern['search'] = re.compile(
         r'([.]wy-side-nav-search[{][^}]*;width):[^;]*;'
      )
      new_value = { 'content':'100%', 'sidebar':'250px', 'search':'250px' }
      file_name = f'{output_dir}/_static/css/theme.css'
      try :
         file_obj  = open(file_name, 'r')
         ok        = True
      except :
         ok        = False
      if ok :
         data_in   = file_obj.read()
         file_obj.close()
         match     = dict()
         for key in pattern :
            match[key] = pattern[key].search(data_in)
            ok         = match[key] != None
      if ok :
         for key in pattern :
            match[key] = pattern[key].search(data_in, match[key].end())
            ok        = match[key] == None
      if ok :
         data_out = data_in
         for key in pattern :
            data_tmp  = data_out
            value     = new_value[key]
            data_out  = pattern[key].sub( f'\\1:{value};', data_tmp)
            ok        = data_out != data_tmp
      if not ok :
         msg       = 'warning: cannot modify widths in sphinx_rtd_theme\n'
         sys.stderr.write(msg)
      else :
         file_obj  = open(file_name, 'w')
         file_obj.write(data_out)
         file_obj.close()
   # -------------------------------------------------------------------------
   print('xrst: OK')
