# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
"""
{xrst_begin auto_file user}
{xrst_spell
   conf
   config
   macros
}

Automatically Generated Files
#############################
These files are located in the :ref:`toml_file@rst_directory` .
A new version of these files is created each time ``xrst`` is run.
The files in the ``rst`` subdirectory that do not change are not replaced.
(This reduces the amount of processing that sphinx needs to do.)

conf.py
*******
This is the sphinx configuration_ file.
It is the only file in the *rst_directory* directory that is
not an rst file.

.. _configuration:  http://www.sphinx-doc.org/en/master/config


index.rst
*********
This file is the top of the documentation tree
built by sphinx. It is one level above the first page in
:ref:`toml_file@root_file`.

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
To be specific::

   :ref:`link to index<gen_index>`

This file is not created when target is pdf.

xrst_preamble.rst
*****************
If :ref:`toml_file@preamble` does not exist,
this file is empty.
Otherwise this file is a copy of the string corresponding to preamble.
If the
:ref:`run_xrst@target` argument is
``pdf``, the latex macros have been removed.

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
#     macros
#     pinfo
#     tmp
#     toml
# }
# {xrst_comment_ch #}
#
# Create the automatically generated files
# ########################################
#
# toml_dict
# *********
# is a python dictionary representation of the xrst.toml file.
# (It is empty if there is no such file).
#
# rst_dir
# =======
# we use *rst_dir* to denote *toml_dict* ['rst_directory']['data'] .
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
# is html or pdf
#
# pinfo_list
# **********
# is a list with length equal to the number of pages.
# The value page[page_index] is a dictionary for this page
# with the following key, value pairs (all the keys are strings):
#
# .. csv-table::
#     :header: key, value
#
#     page_name, (str) containing the name of this page.
#     page_title,  (str) containing the title for this page.
#     parent_page, (int) index in pinfo_list for the parent of this page.
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
# tmp_dir/xrst_preamble.rst
# *************************
# The data in :ref:`toml_file@preamble` is placed in this file.
# If target is html (pdf) the latex macros are (are not) included.
#
# tmp_dir/xrst_index.rst
# **********************
# This file just contains a link to the genindex.rst file.
# It is (is not) included if target is html (pdf).
#
# rst_dir/conf.py
# ***************
# This is the configuration file used by sphinx to build the documentation.
#
# rst_dir/index.rst
# *****************
# This is the root level in the sphinx documentation tree.
#
# {xrst_code py}
def auto_file(
   toml_dict, html_theme, target, pinfo_list, root_page_list
   ) :
   assert type(toml_dict) == dict
   assert type(html_theme) == str
   assert type(target) == str
   assert type(pinfo_list) == list
   assert type(root_page_list) == list
   # {xrst_code}
   # {xrst_end auto_file_dev}
   #
   # rst_dir
   rst_dir = toml_dict['rst_directory']['data']
   #
   # tmp_dir
   tmp_dir = f'{rst_dir}/tmp'
   #
   # project_name
   project_name = toml_dict['project_name']['data']
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
      tmp_dir, target, pinfo_list, root_page_list
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
   # rst_dir/conf.py
   #
   # html_theme_options
   if html_theme not in toml_dict['html_theme_options'] :
      html_theme_options = None
   else :
      html_theme_options = toml_dict['html_theme_options'][html_theme]
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
   # latex_macro
   latex_macro  = toml_dict['preamble']['latex_macro']
   #
   # conf_py
   if len( latex_macro ) != 0 :
      conf_py += '#\n'
      conf_py += '# Latex used when sphinx builds  pdf\n'
      conf_py += 'latex_elements = {\n'
      conf_py += 3 * ' ' + "'preamble' : r'''\n"
      for macro in latex_macro :
         conf_py += 3 * ' ' + macro + '\n'
      conf_py +=  3 * ' ' +"'''\n"
      conf_py += '}\n'
   #
   # rst_dir/conf.py
   file_out    = rst_dir + '/conf.py'
   file_ptr    = open(file_out, 'w')
   file_ptr.write(conf_py)
   file_ptr.close()
   # ------------------------------------------------------------------------
   # tmp_dir/xrst_preamble.rst
   #
   # rst_substitution, latex_macro
   rst_substitution = toml_dict['preamble']['rst_substitution']
   latex_macro      = toml_dict['preamble']['latex_macro']
   #
   # file_data
   if len(rst_substitution) + len(latex_macro) == 0 :
      file_data = ''
   else :
      file_data  = '.. comment: xrst_preamble.rst\n\n'
      file_data += rst_substitution
      if target == 'html' and latex_macro != '' :
         file_data += '\n\n'
         file_data += '.. rst-class:: hidden\n\n'
         for macro in latex_macro :
            file_data += 3 * ' ' + f':math:`{macro}`\n'
   #
   # tmp_dir/xrst_preamble.rst
   file_out    = tmp_dir + '/' + 'xrst_preamble.rst'
   file_ptr    = open(file_out, 'w')
   file_ptr.write(file_data)
   file_ptr.close()
   # ------------------------------------------------------------------------
   # rst_dir/index.rst
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
   file_name    = rst_dir + '/index.rst'
   file_ptr     = open(file_name, 'w')
   file_ptr.write(file_data)
   file_ptr.close()
