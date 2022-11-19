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
``xrst`` ( ``--version`` |  *root_file* )
[ ``--replace_spell_commands`` ]
[ ``--rst_line_numbers`` ]
[ ``--html`` *html_theme* ]
[ ``--group`` *group_list* ]
[ ``--target`` *target* ]
[ ``--output`` *output_dir* ]


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
to the :ref:`xrst.toml@project_dictionary` or when there is an update
of the pyspellchecker_ package (which is used to do the spell checking).
If this option is present,
none of the output files are created; e.g., the \*.rst and \*.html files.

.. _pyspellchecker: https://pypi.org/project/pyspellchecker

rst_line_numbers
****************
Normally sphinx error and warning messages are reported using line numbers
in the xrst source code files.
If this option is present, these messages are reported
using the line numbers in the RST files created by xrst.
This may be helpful if you have an error or warning for a sphinx command
and it does not make sense using source code line numbers.
It is also helpful for determining if a line number error is due to
sphinx or xrst.


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
The examples commands below assume you have cloned the
`xrst git repository <https://github.com/bradbell/xrst>`_
and it is your current working directory.


#. The xrst examples use the empty group
   and their documentation can be built using

      ``xrst xrst.xrst --group ,``

#. The xrst user documentation uses the empty and user groups
   and its documentation can be built using

      ``xrst xrst.xrst --group ,user``

#. The xrst developer documentation uses the empty, user, and dev
   groups and its documentation can be built using

      ``xrst xrst.xrst --group ,user,dev``


target
******
The optional command line argument *target* must be ``html`` or ``pdf``.
It specifies the type of type output you plan to generate using sphinx.
The default value for *target* is ``html`` .

output_dir
**********
The optional command line argument *output_dir* is a directory relative to
of the directory where *root_file* is located.
If *target* is ``html``, the html files are placed in this directory.
If *target* is ``pdf``, the output file is

| *output_dir*\ ``/latex/``\ *project_name*\ ``.pdf``

see :ref:`run_xrst@root_file@project_name` .
The default value for *output_dir* is *output_dir* ``/html`` .

Other Generated Files
=====================
See :ref:`auto_file-title` for the other files generated by ``xrst`` in the
:ref:`xrst.toml@rst_directory` .


{xrst_end run_xrst}
"""
# ---------------------------------------------------------------------------
# imports
# ---------------------------------------------------------------------------
import sys
import re
import os
import toml
import string
import spellchecker
import shutil
import filecmp
import argparse
import subprocess
# ---------------------------------------------------------------------------
def system_command(
      command                    ,
      page_name2line_pair = None ,
      page_name2file_in   = None ,
) :
   assert type(command) == str
   if type(page_name2line_pair) == dict :
      assert type(page_name2file_in) == dict
   #
   # subprocess.run, stderr
   print(command)
   command = command.split(' ')
   result = subprocess.run(command, capture_output = True)
   stderr = result.stderr.decode('utf-8')
   ok     =  result.returncode == 0 and stderr == ''
   if ok :
      return
   if page_name2line_pair == None :
      message  = f'system command failed: stderr = \n{stderr}'
      sys.exit(message)
   #
   # pattern_error
   pattern_error = re.compile( r'.*/rst/([a-z0-9_.]+).rst:([0-9]+):' )
   #
   # message
   message = ''
   #
   # error
   stderr_list = stderr.split('\n')
   for error in stderr_list :
      #
      # m_rst_error
      m_rst_error = pattern_error.search(error)
      if m_rst_error == None :
            if error != '' :
               # This should not happen
               # breakpoint()
               pass
      else :
         #
         # page_name
         page_name = m_rst_error.group(1)
         if not page_name in page_name2line_pair :
            assert page_name == 'xrst_table_of_contents'
         else :
            #
            # rst_line
            rst_line  = int( m_rst_error.group(2) )
            #
            # file_in, line_pair
            file_in   = page_name2file_in[page_name]
            line_pair = page_name2line_pair[page_name]
            #
            # n_pair
            n_pair = len(line_pair)
            #
            # index
            index  = 0
            while index < n_pair and line_pair[index][0] < rst_line :
                  index += 1
            #
            # line_before, line_after
            if index == n_pair :
               line_before = str( line_pair[n_pair-1][1] )
               line_after  = '?'
            elif line_pair[index][0] == rst_line :
               line_before = line_pair[index][1]
               line_after  = line_pair[index][1]
            elif 0 == index :
               line_before = '?'
               line_after  = line_pair[index][1]
            else :
               line_before = line_pair[index-1][1]
               line_after  = line_pair[index][1]
            #
            # error
            msg   = error[ m_rst_error.end()  : ]
            if line_before == line_after :
               error = f'{file_in}:{line_before}:{msg}'
            else :
               error = f'{file_in}:{line_before}-{line_after}:{msg}'
      #
      # message
      message += '\n' + error
   #
   sys.exit(message)
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
version = '2022.11.19'
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
   parser.add_argument('--rst_line_numbers', action='store_true',
      help='report sphinx erros and warnings using rst file line numbers'
   )
   parser.add_argument(
      '--html', metavar='html_theme', default='sphinx_rtd_theme',
      help='sphinx html_theme that is used to display web pages',
      choices=[ 'furo', 'sphinx_rtd_theme', 'sphinx_book_theme' ]
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
      '(default: html)'
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
   # rst_line_numbers
   rst_line_numbers = arguments.rst_line_numbers
   #
   # html_theme
   html_theme = arguments.html
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
   # output_dir
   output_dir = arguments.output
   if output_dir == None :
      output_dir = 'html'
   #
   # toml_dict
   toml_file  = 'xrst.toml'
   if not os.path.isfile( toml_file ) :
      toml_dict = dict()
   else :
      file_ptr  = open(toml_file, 'r')
      file_data = file_ptr.read()
      toml_dict = toml.loads(file_data)
   #
   # rst_directory
   if 'rst_directory' in toml_dict :
      rst_directory = toml_dict['rst_directory']
   else :
      rst_directory = 'rst'
   if rst_directory[0] == '/' :
      msg  = 'rst_directory = ' + rst_directory + '\n'
      msg += 'must be a path relative to current workding directory'
      xrst.system_exit(msg)
   if 0 <= rst_directory.find('../') :
      msg  = 'rst_directory = ' + rst_directory + '\n'
      msg += 'cannot contain ../'
      xrst.system_exit(msg)

   #
   if not os.path.isdir(rst_directory) :
      os.mkdir(rst_directory)
   #
   # tmp_dir
   tmp_dir = rst_directory + '/tmp'
   if os.path.isdir(tmp_dir) :
      shutil.rmtree(tmp_dir)
   os.mkdir(tmp_dir)
   #
   # spell_checker
   spell_list  = list()
   if 'project_dictionary' in toml_dict :
      for entry in toml_dict['project_dictionary'] :
         if not type(entry) == str :
            msg  = 'xrst.toml: project_dictionary '
            msg += 'the following entry is not a string\n'
            msg += str(entry)
            xrst.system_exit(msg)
         word_list = entry.split('\n')
         for word in word_list :
            word = word.strip(' \t')
            spell_list.append(word)
   spell_checker = xrst.create_spell_checker(spell_list)
   #
   # not_keyword_list
   not_keyword_list = list()
   if 'not_keyword' in toml_dict :
      for entry in toml_dict['not_keyword'] :
         if not type(entry) == str :
            msg  = 'xrst.toml: not_keyword '
            msg += 'the following entry is not a string\n'
            msg += str(entry)
            xrst.system_exit(msg)
         pattern_list = entry.split('\n')
         for pattern in pattern_list :
            pattern = pattern.strip(' \t')
            not_keyword_list.append( re.compile(pattern) )
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
   # page_name2line_pair, page_name2file_in
   # Each rst page name has a corresponding input file and mapping from
   # rst file line nubmers to input file line numbers.
   page_name2line_pair = dict()
   page_name2file_in   = dict()
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
         # pop first element of stack so that order in pdf file and
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
            if sinfo_file_in[0]['is_parent'] :
               n_page = 1
            else :
               n_page = len( sinfo_file_in )
            for i_page in range( n_page ) :
               page_name = sinfo_file_in[i_page]['page_name']
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
               rst_directory,
            )
            # ------------------------------------------------------------
            # literal command
            page_data = xrst.literal_command(
               page_data,
               file_in,
               page_name,
               rst_directory,
            )
            # ------------------------------------------------------------
            # process headings
            #
            # pseudo_heading, pinfo_list
            page_data, page_title, pseudo_heading = \
            xrst.process_headings(
               html_theme,
               page_data,
               file_in,
               page_name,
               not_keyword_list,
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
            #
            # line_pair and file tmp_dir/page_name.rst
            line_pair = xrst.temporary_file(
               pseudo_heading,
               file_in,
               tmp_dir,
               page_name,
               page_data,
            )
            #
            # page_name2line_pair, page_name2file_in
            page_name2line_pair[page_name] = line_pair
            page_name2file_in[page_name]   = file_in
   #
   # replace_spell
   if replace_spell_commands :
      xrst.replace_spell(tmp_dir)
      #
      # tmp_dir
      # reset tmp_dir because rmtree is such a dangerous command
      tmp_dir = f'{rst_directory}/tmp'
      shutil.rmtree(tmp_dir)
      print('xrst --replace_spell_commands: OK')
      return
   #
   # auto_file
   xrst.auto_file(
      toml_dict, html_theme, target, pinfo_list, root_page_list
   )
   #
   # -------------------------------------------------------------------------
   #
   # rst_directory/*.rst
   tmp_list = os.listdir(tmp_dir)
   rst_list = os.listdir(rst_directory)
   for name in tmp_list :
      src = f'{tmp_dir}/{name}'
      des = f'{rst_directory}/{name}'
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
               os.remove( f'{rst_directory}/{name}' )
   #
   # tmp_dir
   # reset tmp_dir because rmtree is such a dangerous command
   tmp_dir = f'{rst_directory}/tmp'
   shutil.rmtree(tmp_dir)
   # -------------------------------------------------------------------------
   if target == 'html' :
      command = f'sphinx-build -b html {rst_directory} {output_dir}'
      if rst_line_numbers :
         system_command(command)
      else :
         system_command(command, page_name2line_pair, page_name2file_in)
   else :
      assert target == 'pdf'
      #
      latex_dir = f'{output_dir}/latex'
      command = f'sphinx-build -b latex {rst_directory} {latex_dir}'
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
