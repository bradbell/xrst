# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
"""
{xrst_begin auto_file user}
{xrst_spell
   conf
   dir
}

Automatically Generated Files
#############################
These files are located in the *sphinx_dir* ``/rst`` directory; see
:ref:`run_xrst@sphinx_dir`.
A new version of these files is created each time ``xrst`` is run.
The files in the ``rst`` subdirectory that do not change are not replaced.
(This reduces the amount of processing that sphinx needs to do.)

conf.py
*******
This is the sphinx configuration_ file.
It is the only file in the *sphinx_dir* ``/rst`` directory that is
not an rst file.

.. _configuration:  http://www.sphinx-doc.org/en/master/config


index.rst
*********
This file is the root level in the documentation tree
built by sphinx. It is one level above the first page in
:ref:`run_xrst@root_file`.

xrst_table_of_contents.rst
**************************
This file contains the table of contents for the last run of ``xrst``.
You can link to the corresponding page with the following command::

   :ref:`@xrst_table_of_contents`

The result of this command in this documentation is
:ref:`@xrst_table_of_contents` .

xrst_index.rst
**************
If :ref:`run_xrst@target` is html,
this file contains a link to the table of contents generated by sphinx.
To be specific::

   :ref:`link to index<gen_index>`

This file is not created when target is pdf.

xrst_preamble.rst
*****************
If :ref:`run_xrst@sphinx_dir@preamble.rst` does not exist,
this file is empty.
Otherwise this file is a copy of the
:ref:`run_xrst@sphinx_dir@preamble.rst` file.
If the
:ref:`run_xrst@target` argument is
``pdf``, the latex macros have been removed.

{xrst_end auto_file}
"""
# ----------------------------------------------------------------------------
import re
import os
import xrst
#
# conf_py_general
conf_py_general = '''#
# General configuration
extensions = [
   'sphinx.ext.mathjax',
   'sphinx_rtd_theme',
]
'''
#
# conf_py_theme
conf_py_theme = '''#
# Theme
html_theme = '@html_theme@'
#
if html_theme == 'sphinx_rtd_theme' :
   html_theme_options = {
      'navigation_depth' : -1   ,
      'titles_only'      : True ,
   }
if html_theme == 'sphinx_book_theme' :
   html_theme_options = {
      'show_toc_level' : 4
   }
# furo theme uses default options
'''
#
#
# pattern_macro
# Note that each macro pattern match may overlap the previous match
# by the \n at the beginning and end of the pattern.
pattern_macro = r'\n[ \t]*:math:`(\\newcommand\{[^`]*\})`[ \t]*\n'
pattern_macro = re.compile(pattern_macro)
#
def preamble_macros(sphinx_dir) :
   #
   # file_name
   file_name = sphinx_dir + '/preamble.rst'
   if not os.path.isfile(file_name) :
      return list()
   #
   # file_data
   file_ptr  = open(file_name, 'r')
   file_data = file_ptr.read()
   file_ptr.close()
   #
   # m_macro
   m_macro = pattern_macro.search(file_data)
   #
   # macro_list
   macro_list = list()
   while m_macro :
      #
      # macro_list
      macro = m_macro.group(1)
      macro_list.append(macro)
      #
      # m_macro
      m_macro = pattern_macro.search(file_data, m_macro.end() - 1)
   #
   return macro_list
# ----------------------------------------------------------------------------
#
# Create the automatically generated files
#
# html_theme:
# The html_theme as on the xrst command line.
#
# sphinx_dir:
# is the name of xrst command line line argument *sphinx_dir*.
#
# tmp_dir:
# is the name of the directory where xrst creates a temporary copy of
# the sphinx_dir/rst directory. We need not add a comment that these files
# are automatically generated because all files in sphinx_dir/rst are.
#
# target:
# is html or pdf
#
# sinfo_list:
# is a list with length equal to the number of pages.
# The value page[page_index] is a dictionary for this seciton
# with the following key, value pairs (all the keys are strings:
# key            value
# page_name   a str continaing the name of this page.
# page_title  a str containing the title for this page.
# parent_page an int index in sinfo_list for the parent of this page.
# in_parent_file is this page in same input file as its parent.
#
# root_page_list:
# is a list of the root page names (one for each group) in the order
# they will appear in the table of contents.
#
# tmp_dir/xrst_table_of_contents.rst
# This file creates is the table of contents for the documentation.
# It has the lable xrst_table_of_contents which can be used to link
# to this page.
#
# tmp_dir/xrst_preamble.rst
# This is a copy of the sphinx_dir/preamble.rst file. If target is
# pdf (html) the latex macros are (are not) removed.
#
# tmp_dir/xrst_index.rst
# This file just contians a link to the genindex.rst file.
# It is (is not) included if target is html (pdf).
#
# sphinx_dir/rst/conf.py
# This is the configuration file used by sphinx to build the docuementation.
#
# sphinx_dir/rst/index.rst
# This is the root level in the sphinx documentation tree.
#
def auto_file(
   html_theme, sphinx_dir, tmp_dir, target, sinfo_list, root_page_list
   ) :
   assert type(html_theme) == str
   assert type(sphinx_dir) == str
   assert type(tmp_dir) == str
   assert type(target) == str
   assert type(sinfo_list) == list
   assert type(root_page_list) == list
   #
   # project_name
   project_name = sinfo_list[0]['file_in']
   index   = project_name.rfind('/')
   if 0 <= index and index + 1 < len(project_name) :
      project_name = project_name[index + 1 :]
   index   = project_name.rfind('.')
   if 0 < index :
      project_name = project_name[: index ]
   #
   # ------------------------------------------------------------------------
   # tmp_dir/xrst_table_of_contents.rst
   #
   # file_data
   file_data = '.. |space| unicode:: 0xA0\n'
   #
   # file_data
   level         = 1
   count         = list()
   page_index = 0
   file_data  += xrst.table_of_contents(
      tmp_dir, target, sinfo_list, root_page_list
   )
   #
   # xrst_table_of_contents.rst
   file_out    = tmp_dir + '/' + 'xrst_table_of_contents.rst'
   file_ptr    = open(file_out, 'w')
   file_ptr.write(file_data)
   file_ptr.close()
   #
   # ------------------------------------------------------------------------
   # tmp_dir/xrst_index.rst
   if target == 'html' :
      #
      # file_data
      file_data  = 'Index\n'
      file_data += '#####\n'
      file_data += ':ref:`link to index<genindex>`'
      #
      # xrst_index.rst
      file_out    = tmp_dir + '/' + 'xrst_index.rst'
      file_ptr    = open(file_out, 'w')
      file_ptr.write(file_data)
      file_ptr.close()
   # ------------------------------------------------------------------------
   # sphinx_dir/conf.py
   #
   # conf_py_theme
   theme_temp = conf_py_theme.replace('@html_theme@', html_theme)
   #
   # conf_py
   conf_py  = '# This file was automatically generated by xrst\n'
   conf_py += '#\n'
   conf_py += '# Project information\n'
   conf_py += f"project = '{project_name}'\n"
   conf_py +=  "author = ''\n"
   conf_py += conf_py_general
   conf_py += theme_temp
   conf_py += '#\n'
   conf_py += '# Latex used when sphinx builds  pdf\n'
   conf_py += 'latex_elements = {\n'
   conf_py += "    'preamble' :\n"
   conf_py += "    r'\\renewcommand{\\thepage}{{\\hspace{-1em}}} ' + \n"
   conf_py += "    r'\\renewcommand{\\thesubpage}{{\\hspace{-1em}}} ' + \n"
   conf_py += "    r'\\renewcommand{\\thesubsubpage}{{\\hspace{-1em}}}'"
   #
   # latex
   latex = ''
   macro_list = preamble_macros(sphinx_dir)
   for macro in macro_list :
      latex += ' + \n'
      latex += "    r'" + macro + "'"
   #
   # conf_py
   conf_py += latex + '\n}\n'
   #
   # sphinx_dir/conf.py
   file_out    = sphinx_dir + '/rst/conf.py'
   file_ptr    = open(file_out, 'w')
   file_ptr.write(conf_py)
   file_ptr.close()
   # ------------------------------------------------------------------------
   # tmp_dir/xrst_preamble.rst
   #
   # file_data
   file_name = sphinx_dir + '/preamble.rst'
   if not os.path.isfile( file_name ) :
      file_data = ''
   else :
      file_ptr  = open(file_name, 'r')
      file_data = file_ptr.read()
      file_ptr.close()
   #
   if target == 'pdf' :
      # remove the latex macros
      #
      # m_macro
      m_macro = pattern_macro.search(file_data)
      while m_macro :
         #
         # file_data
         before = file_data[0 : m_macro.start() ]
         after  = file_data[m_macro.end() - 1 : ]
         file_data = before + after
         #
         # m_macro
         m_macro = pattern_macro.search(file_data)
   #
   # pattern
   # check for and remove an empty .. rst-class hidden block.
   pattern = r'\n..[ \t]*rst-class:: hidden[ \t]*\n[ \t\n]*\n([^ \t\n]|$)'
   m_obj   = re.search(pattern, file_data)
   if m_obj :
      before    = file_data[ : m_obj.start() + 1]
      after     = file_data[ m_obj.end() - 1 : ]
      file_data = before + after
   #
   # tmp_dir/xrstt_preamble.rst
   file_out    = tmp_dir + '/' + 'xrst_preamble.rst'
   file_ptr    = open(file_out, 'w')
   file_ptr.write(file_data)
   file_ptr.close()
   # ------------------------------------------------------------------------
   # sphinx_dir/rst/index.rst
   #
   # file_data
   file_data  = '.. comment This file was automatically generated by xrst\n\n'
   file_data += project_name + '\n'
   file_data += len(project_name) * '#'
   file_data += '\n\n'
   file_data += '.. toctree::\n'
   file_data += '   :maxdepth: 1\n'
   file_data += '\n'
   file_data += '   xrst_table_of_contents\n'
   for page_name in root_page_list :
      file_data += '   ' + page_name + '\n'
   if target == 'html' :
      file_data += '   xrst_index\n'
   #
   # index.rst
   file_name    = sphinx_dir + '/rst/index.rst'
   file_ptr     = open(file_name, 'w')
   file_ptr.write(file_data)
   file_ptr.close()
