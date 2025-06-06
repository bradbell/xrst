# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-25 Bradley M. Bell
# ----------------------------------------------------------------------------
r"""
{xrst_begin auto_file user}
{xrst_spell
   conf
   js
}

Automatically Generated Files
#############################

#. These files are located in the :ref:`config_file@directory@rst_directory` .
#. A new version of these files is created each time ``xrst`` is run.
#. The files in the ``rst`` subdirectory that do not change are not replaced.
   (This reduces the amount of processing that sphinx needs to do.)
#. All these files have the ``.rst`` extension with the exception of
   conf.py and xrst_search.js .


conf.py
*******
This is the sphinx configuration_ file.
It is the only file in the *rst_directory* directory that is
not an rst file.

.. _configuration:  https://www.sphinx-doc.org/en/master/usage/configuration.html


xrst_root_doc.rst
*****************
This file is the top of the documentation tree
built by sphinx. It is one level above the first page in
:ref:`config_file@root_file`.

xrst_contents.rst
*****************
This file contains the table of contents for the last run of ``xrst``.
You can link to the corresponding
page name :ref:`xrst_contents-name`
or page title :ref:`xrst_contents-title`
with the following commands::

   :ref:`xrst_contents-name`
   :ref:`xrst_contents-title`

xrst_index.rst
**************
If :ref:`run_xrst@target` is html,
this file contains a link to the table of contents generated by sphinx.
You can link to the corresponding page name or page title
with the following commands::

   :ref:`xrst_index-name`
   :ref:`xrst_index-title`

The xrst_index.rst file is not created when target is tex.

xrst_search.rst
***************
If :ref:`run_xrst@target` is html,
this file contains the xrst search utility for the last run of ``xrst``.
A link to this search utility appears at top left side of each web page.
You can place a link to this page name or page title
using the following commands::

   :ref:`xrst_search-title`
   :ref:`xrst_search-name`

This page tile will start with the :ref:`config_file@project_name`
(which for this documentation is ``xrst`` ).
The xrst_search.rst file is not created when target is tex.

xrst_search.js
**************
This file is used by xrst_search.rst.


{xrst_end auto_file}
"""
# ----------------------------------------------------------------------------
import re
import os
import xrst
#
# conf_py_constant
conf_py_constant = '''#
# General configuration
extensions = [
   'sphinx.ext.mathjax',
   'sphinx_copybutton',
]
root_doc = 'xrst_root_doc'
#
# This does not seem to work so run_xrst.py copies xrst_search.js after
# target directory directory is created.
# html_js_files = [ 'xrst_search.js', ]
#
'''
#
# xrst_index_rst
xrst_index_rst=r'''.. _xrst_index-name:

!!!!!
index
!!!!!

.. _xrst_index-title:

Link To Index Page
##################
:ref:`Link to index <genindex>`

'''
#
#
# xrst_search_rst_template
# Do not start with a newine because it will get removed from
# test_rst/xrst_search.rst during the check for invisible white space.
xrst_search_rst_template = r'''.. _xrst_search-name:

!!!!!!
search
!!!!!!

.. _xrst_search-title:

{XRST_SEARCH_TITLE}

.. raw:: html

   <noscript><h1>
   This search utility requires Javascript to be enabled
   and Javascript is disabled in your browser.
   </h1></noscript>
   <form name='search'>
   <p><table>
      Keywords include the page name, and words in the title or headings.
      Enter Keywords separated by spaces to reduce the match count:
      <tr><td>
         Keywords
      </td><td>
         Match
      </td><tr><td>
         <input
            type='text'
            name='keywords'
            onkeydown='update_match()'
            size='50'
         ></input>
      </td><td>
         <input
            type='text'
            name='match'
            size=5
         ></input>
      </td></tr>
   </table></p>
   <p><table>
      Selecting a page name or ttle below will go to that page:
      <tr><td>
         Page Name
      </td><td>
         Page Title
      </td></tr>
      <tr><td>
         <textarea
            name='name_match'
            rows='20'
            cols='15'
            onclick='select_match(this)'
            ondblclick='goto_match(this)'
            onkeydown='page_or_title_entry(this)'
         ></textarea>
      </td><td>
         <textarea
            name='title_match'
            rows='20'
            cols='50'
            onclick='select_match(this)'
            ondblclick='goto_match(this)'
            onkeydown='page_or_title_entry(this)'
         ></textarea>
      </td></tr>
   </table></p>
   </form>
   <script type='text/javascript' src='xrst_search.js'>
   </script>
'''
#
# xrst_search_js_constant
xrst_search_js_constant = r'''
var max_match_display_global  = 100;
var keywords_length_global    = -1;
var match2page_name_global    = [];
Initialize();
//
// initialize
function Initialize()
{  update_match();
   document.search.keywords.focus()
}
// update_match
function update_match()
{
   // keywords_value, keywords_length_global
   var keywords_value = document.search.keywords.value;
   if( keywords_value.length == keywords_length_global )
      return;
   keywords_lenght_global = keywords_value.length;
   //
   // keyword_list, n_keyword
   var keyword_list = keywords_value.match(/\S+/g);
   var n_keyword    = 0;
   if( keyword_list != null )
      n_keyword = keyword_list.length;
   //
   // pattern
   var pattern = new Array(n_keyword);
   for(var j = 0; j < n_keyword; j++)
      pattern[j] = new RegExp(keyword_list[j], 'i')
   //
   // name_match, title_match, match2page_name_global, count_match
   var count_match = 0;
   var name_match  = '';
   var title_match = '';
   var n_page      = all_page_info_global.length;
   for(i = 0; i < n_page; i++)
   {
      var match = true;
      for(j = 0; j < n_keyword; j++)
      {  flag  = pattern[j].test( all_page_info_global[i].keywords );
         match = match && flag;
      }
      if( match )
      {
         if( count_match < max_match_display_global )
         {  var name    = all_page_info_global[i].page_name;
            var title   = all_page_info_global[i].page_title;
            name_match  = name_match   + name  + '\n';
            title_match = title_match + title + '\n';
            match2page_name_global[count_match] = name;
         }
         count_match = count_match + 1;
      }
   }
   //
   // document.search.match
   document.search.match.value    = count_match;
   document.search.match.readOnly = true;
   document.search.match.setAttribute('wrap', 'off');
   //
   // document.search.name_match
   document.search.name_match.value    = name_match;
   document.search.name_match.readOnly = false;
   document.search.name_match.setAttribute('wrap', 'off');
   //
   // document.search.title_match
   document.search.title_match.value    = title_match;
   document.search.title_match.readOnly = false;
   document.search.title_match.setAttribute('wrap', 'off');
}
// select_match
function select_match(textarea)
{  // start_pos
   var start_select = textarea.value.substring(0, textarea.selectionStart);
   var start_pos    = Math.max(0, start_select.lastIndexOf('\n') + 1);
   //
   // end_pos
   var length       = textarea.length;
   var end_select   = textarea.value.substring(textarea.selectionEnd, length);
   var end_pos      = textarea.selectionEnd + end_select.indexOf('\n');
   //
   // textarea
   textarea.selectionStart = start_pos;
   textarea.selectionEnd   = end_pos;
}
// goto_match
function goto_match(textarea)
{  var start_select = textarea.value.substring(0, textarea.selectionStart);
   var match_index  = start_select.split('\n').length - 1;
   var page_name    = match2page_name_global[match_index];

   //
   parent.location  = page_name + '.html'
}
// page_or_title_entry()
function page_or_title_entry(textarea)
{  alert( 'Only use single or double click below Page Name and Page Title');
   parent.location  = 'xrst_search.html'
}
'''
#
# ----------------------------------------------------------------------------
# {xrst_begin auto_file_dev dev}
# {xrst_spell
#     conf
#     genindex
#     js
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
# link_timeout
# ************
# The link_timeout determine by the xrst command line.
#
# html_theme
# **********
# The html_theme determined by the xrst command line.
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
#     keywords, (str) space separated list of index entries for this page.
#     file_in, (str) name of the input file for this page
#     begin_line, (int) line number where begin command is for this page
#     end_line, (int) line number where end command is for this page
#     template_list, (list of str) name of template files used by this page
#
# root_page_list
# **************
# is a list of the root page names (one for each group) in the order
# they will appear in the table of contents.
#
# tmp_dir/xrst_contents.rst
# *************************
# This file creates is the table of contents for the documentation.
# It has the label xrst_contents which can be used to link
# to this page.
#
# tmp_dir/xrst_index.rst
# **********************
# This file just contains a link to the genindex.rst file.
# It is (is not) included if target is html (tex).
#
# tmp_dir/xrst_search.rst
# ***********************
# This file contains the xrst search utility.
# It is (is not) included if target is html (tex).
#
# tmp_dir/xrst_search.js
# **********************
# This file contains the java script used by xrst_search.rst.
# It is (is not) included if target is html (tex).
#
# tmp_dir/xrst_root_doc.rst
# *************************
# This is the root level in the sphinx documentation tree.
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
#
# Prototype
# *********
# {xrst_literal
#  # BEGIN_DEF
#  # END_DEF
#  }
#
# {xrst_end auto_file_dev}
#
# BEGIN_DEF
def auto_file(
   conf_dict, link_timeout, html_theme, target, all_page_info, root_page_list
   ) :
   assert type(conf_dict) == dict
   assert type(html_theme) == str
   assert type(target) == str
   assert type(all_page_info) == list
   assert type(root_page_list) == list
   # END_DEF
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
   # tmp_dir/xrst_contents.rst
   #
   # file_data
   file_data     = xrst.table_of_contents(
      tmp_dir, target, all_page_info, root_page_list
   )
   #
   # xrst_contents.rst
   file_out    = tmp_dir + '/' + 'xrst_contents.rst'
   file_obj    = open(file_out, 'w')
   file_obj.write(file_data)
   file_obj.close()
   #
   # ------------------------------------------------------------------------
   # tmp_dir/xrst_index.rst
   if target == 'html' :
      #
      # file_data
      file_data  = xrst_index_rst
      #
      # xrst_index.rst
      file_out    = tmp_dir + '/' + 'xrst_index.rst'
      file_obj    = open(file_out, 'w')
      file_obj.write(file_data)
      file_obj.close()
   #
   # ------------------------------------------------------------------------
   # tmp_dir/xrst_search.rst
   # tmp_dir/xrst_search.js
   if target == 'html' :
      #
      # xrst_search.rst
      file_data   = xrst_search_rst_template
      pattern     = '{XRST_SEARCH_TITLE}'
      line        = f'{project_name} Keyword Search'
      replace     = line + '\n' + len(line) * '*'
      file_data   = re.sub(pattern, replace, file_data)
      file_out    = tmp_dir + '/' + 'xrst_search.rst'
      file_obj    = open(file_out, 'w')
      file_obj.write(file_data)
      file_obj.close()
      #
      # xrst_search.js
      file_data = 'var all_page_info_global = [\n{\n'
      for index, page in enumerate( all_page_info ) :
         for key in [ 'page_name', 'page_title', 'keywords' ] :
            value      = page[key]
            value      = value.replace("'", '"')
            if key == 'keywords' :
               file_data += f"'{key}' : ' {value} '"
            else :
               file_data += f"'{key}' : '{value}'"
               file_data += ',\n'
         if index == len( all_page_info ) - 1 :
            file_data += '\n}\n];'
         else :
            file_data += '\n},{\n'
      file_data  += xrst_search_js_constant
      file_out    = tmp_dir + '/' + 'xrst_search.js'
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
         title     = f'lines {begin_line}-{end_line} of file: {file_in}'
         dash_line = len(title) * '-'
         title     = f'{dash_line}\n{title}\n{dash_line}\n\n'
         page_data = title + file_data[begin_index : end_index]
         #
         # file_out
         page_name = info['page_name']
         file_out  = rst_dir + '/_sources/' + page_name
         if not page_name.endswith('.rst') :
            file_out += '.rst'
         file_out += '.txt'
         file_obj = open(file_out, 'w')
         file_obj.write(page_data)
         for temp_file in info['template_list'] :
            file_temp  = open(temp_file, 'r')
            data_temp = file_temp.read()
            file_temp.close()
            title     = f'xrst template file: {temp_file}'
            dash_line = len(title) * '-'
            title     = f'\n{dash_line}\n{title}\n{dash_line}\n\n'
            data_temp = title + data_temp
            file_obj.write(data_temp)
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
   conf_py += conf_py_constant
   conf_py += f'linkcheck_timeout = {link_timeout}\n'
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
   # tmp_dir/xrst_root_doc.rst
   #
   # file_data
   file_data  = '.. comment This file was automatically generated by xrst\n\n'
   file_data += project_name + '\n'
   file_data += len(project_name) * '#'
   file_data += '\n\n'
   file_data += '.. toctree::\n'
   file_data += 3 * ' ' + ':maxdepth: 1\n'
   file_data += '\n'
   if target == 'html' :
      file_data += 3 * ' ' + 'xrst_search\n'
      file_data += 3 * ' ' + 'xrst_index\n'
   file_data += 3 * ' ' + 'xrst_contents\n'
   for page_name in root_page_list :
      file_data += 3 * ' ' + '' + page_name + '\n'
   #
   # xrst_root_doc.rst
   file_name    = tmp_dir + '/xrst_root_doc.rst'
   file_obj     = open(file_name, 'w')
   file_obj.write(file_data)
   file_obj.close()
