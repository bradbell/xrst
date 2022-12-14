# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
"""
{xrst_begin auto_file user}
{xrst_spell
   conf
   config
}

Automatically Generated Files
#############################
These files are located in the :ref:`config_file@directory@rst_directory` .
A new version of these files is created each time ``xrst`` is run.
The files in the ``rst`` subdirectory that do not change are not replaced.
(This reduces the amount of processing that sphinx needs to do.)

conf.py
*******
This is the sphinx configuration_ file.
It is the only file in the *rst_directory* directory that is
not an rst file.

.. _configuration:  http://www.sphinx-doc.org/en/master/config


xrst_root_doc.rst
*****************
This file is the top of the documentation tree
built by sphinx. It is one level above the first page in
:ref:`config_file@root_file`.

xrst_table_of_contents.rst
**************************
This file contains the table of contents for the last run of ``xrst``.
You can link to the corresponding page with the following command::

   :ref:`xrst_table_of_contents-title`

The result of this command in this documentation is
:ref:`xrst_table_of_contents-title` .

xrst_index.rst
**************
If :ref:`run_xrst@target` is html,
this file contains a link to the table of contents generated by sphinx.
To be specific:

   :ref:`link to index<genindex>`

The xrst_index.rst file is not created when target is tex.

{xrst_end auto_file}
"""
# ----------------------------------------------------------------------------
import re
import os
import toml
import xrst
#
# conf_py_general
conf_py_general = '''#
# General configuration
extensions = [
   'sphinx.ext.mathjax',
]
root_doc = 'xrst_root_doc'
'''
#
# ----------------------------------------------------------------------------
# {xrst_begin auto_file_dev dev}
# {xrst_spell
#     bool
#     conf
#     dict
#     dir
#     genindex
#     tmp
# }
# {xrst_comment_ch #}
#
# Create the automatically generated files
# ########################################
#
# conf_dict
# *********
# is a python dictionary representation of the configuration file.
#
# rst_dir
# =======
# we use *rst_dir* to denote *conf_dict* ['directory']['rst_directory'] .
#
# tmp_dir
# =======
# we use *tmp_dir* to denote *rst_dir*\ /tmp .
# This is the directory where xrst creates a temporary copy of *rst_dir* .
# These files are also automatically generated.
#
# html_theme
# **********
# The html_theme as on the xrst command line.
#
# target
# ******
# is html or tex
#
# all_page_info
# *************
# is a list with length equal to the number of pages.
# with the following key, value pairs (all the keys are strings):
#
# .. csv-table::
#     :header: key, value
#
#     page_name, (str) containing the name of this page.
#     page_title,  (str) containing the title for this page.
#     parent_page, (int) index in all_page_info for the parent of this page.
#     in_parent_file, (bool) is this page in same input file as its parent.
#
# root_page_list
# **************
# is a list of the root page names (one for each group) in the order
# they will appear in the table of contents.
#
# tmp_dir/xrst_table_of_contents.rst
# **********************************
# This file creates is the table of contents for the documentation.
# It has the label xrst_table_of_contents which can be used to link
# to this page.
#
# tmp_dir/xrst_index.rst
# **********************
# This file just contains a link to the genindex.rst file.
# It is (is not) included if target is html (tex).
#
# rst_dir/_sources
# ****************
# The sub-directory is used to store the replacement
# for the _sources directory. This contains the xrst sources that were used
# to create the rst files that sphinx used as sources.
# This is (is not) included if target is html (tex).
# If target is html, this sub-directory must exist and should be empty,
# before calling auto_file.
#
# rst_dir/conf.py
# ***************
# This is the configuration file used by sphinx to build the documentation.
#
# rst_dir/xrst_root_doc.rst
# *************************
# This is the root level in the sphinx documentation tree.
#
# {xrst_code py}
def auto_file(
   conf_dict, html_theme, target, all_page_info, root_page_list
   ) :
   assert type(conf_dict) == dict
   assert type(html_theme) == str
   assert type(target) == str
   assert type(all_page_info) == list
   assert type(root_page_list) == list
   # {xrst_code}
   # {xrst_end auto_file_dev}
   #
   # rst_dir
   rst_dir = conf_dict['directory']['rst_directory']
   #
   # tmp_dir
   tmp_dir = f'{rst_dir}/tmp'
   #
   # project_name
   project_name = conf_dict['project_name']['data']
   #
   # ------------------------------------------------------------------------
   # tmp_dir/xrst_table_of_contents.rst
   #
   # file_data
   file_data     = xrst.table_of_contents(
      tmp_dir, target, all_page_info, root_page_list
   )
   #
   # xrst_table_of_contents.rst
   file_out    = tmp_dir + '/' + 'xrst_table_of_contents.rst'
   file_obj    = open(file_out, 'w')
   file_obj.write(file_data)
   file_obj.close()
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
      file_obj    = open(file_out, 'w')
      file_obj.write(file_data)
      file_obj.close()
   # ------------------------------------------------------------------------
   # rst_dir/_sources
   if target == 'html' :
      #
      # file_in, file_daa
      file_in   = None
      file_data = None
      for info in all_page_info :
         if info['file_in'] != file_in :
            #
            # file_in, file_data
            file_in    = info['file_in']
            file_obj   = open(file_in, 'r')
            file_data  = file_obj.read()
            file_obj.close()
            #
            # newline_list
            newline_list = xrst.newline_indices(file_data)
         #
         # begin_index
         begin_line  = info['begin_line']
         assert 1 <= begin_line
         if begin_line == 1 :
            begin_index = 0
         else :
            assert begin_line < len(newline_list)
            begin_index = newline_list[begin_line-2] + 1
         #
         # end_index
         end_line  = info['end_line']
         assert end_line - 1 <= len(newline_list)
         if end_line - 1 == len(newline_list) :
            end_index = len(file_data)
         else :
            end_index = newline_list[end_line-1] + 1
         #
         # page_data
         page_data  = f'lines {begin_line}-{end_line} of file: {file_in}\n\n'
         page_data += file_data[begin_index : end_index]
         #
         # file_out
         page_name = info['page_name']
         file_out  = rst_dir + '/_sources/' + page_name
         if not page_name.endswith('.rst') :
            file_out += '.rst'
         file_out += '.txt'
         file_obj = open(file_out, 'w')
         file_obj.write(page_data)
         file_obj.close()
   # ------------------------------------------------------------------------
   # rst_dir/conf.py
   #
   # html_theme_options
   if html_theme not in conf_dict['html_theme_options'] :
      html_theme_options = None
   else :
      html_theme_options = conf_dict['html_theme_options'][html_theme]
      html_theme_optiosn = str( html_theme_options )
      assert '"' not in html_theme_options
   #
   # conf_py
   conf_py  = '# This file was automatically generated by xrst\n'
   conf_py += '#\n'
   conf_py += '# Project information\n'
   conf_py += f"project = '{project_name}'\n"
   conf_py +=  "author = ''\n"
   conf_py += conf_py_general
   conf_py += f'html_theme = "{html_theme}"\n'
   if html_theme_options != None :
      conf_py += f'html_theme_options = {html_theme_options}\n'
   #
   # rst_epilog, rst_prolog, latex_macro
   rst_epilog  = conf_dict['include_all']['rst_epilog']
   rst_prolog  = conf_dict['include_all']['rst_prolog']
   latex_macro = conf_dict['include_all']['latex_macro']
   #
   # rst_prolog
   if target == 'html' and len(latex_macro) != 0 :
      if rst_prolog != '' :
         rst_prolog += '\n\n'
      rst_prolog += '.. rst-class:: hidden\n\n'
      for macro in latex_macro :
         rst_prolog += 3 * ' ' + f':math:`{macro}`\n'
   #
   # conf_py
   if rst_epilog != '' :
      conf_py += '#\n'
      conf_py += f"rst_epilog = r'''\n"
      conf_py += rst_epilog
      conf_py += "'''\n"
   if rst_prolog != '' :
      conf_py += '#\n'
      conf_py += f"rst_prolog = r'''\n"
      conf_py += rst_prolog
      conf_py += "'''\n"
   if len( latex_macro ) != 0 :
      conf_py += '#\n'
      conf_py += '# Latex used when sphinx builds tex\n'
      conf_py += 'latex_elements = {\n'
      conf_py += 3 * ' ' + "'preamble' : r'''\n"
      for macro in latex_macro :
         conf_py += 3 * ' ' + macro + '\n'
      conf_py +=  3 * ' ' +"'''\n"
      conf_py += '}\n'
   #
   # rst_dir/conf.py
   file_out    = rst_dir + '/conf.py'
   file_obj    = open(file_out, 'w')
   file_obj.write(conf_py)
   file_obj.close()
   # ------------------------------------------------------------------------
   # rst_dir/xrst_root_doc.rst
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
   # xrst_root_doc.rst
   file_name    = rst_dir + '/xrst_root_doc.rst'
   file_obj     = open(file_name, 'w')
   file_obj.write(file_data)
   file_obj.close()
