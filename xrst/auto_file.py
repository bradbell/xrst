# -----------------------------------------------------------------------------
#                      xrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xrst_begin auto_file}
{xrst_spell
    conf
}

Automatically Generated Files
#############################
These files are located in the
:ref:`run_xrst@command_line_arguments@sphinx_dir` directory.
A new version of these files is created each time ``xrst`` is run.
The files in the ``rst`` subdirectory that do not change are not replaced.


conf.py
*******
This is the sphinx configuration_ file.

.. _configuration:  http://www.sphinx-doc.org/en/master/config

rst/xrst_table_contents.rst
***************************
This file contains the table of contents for the last run of ``xrst``.
You can link to the corresponding section with the following command:

```
:ref:`xrst_table_of_contents`
```

The result of this command in this documentation is
:ref:`xrst_table_of_contents` .

rst/xrst_preamble.rst
*********************
This is a copy of the
:ref:`run_xrst@command_line_arguments@preamble.rst` file.
If the
:ref:`run_xrst@command_line_arguments@target` argument is
``pdf``, the latex macros have been removed.

{xrst_end auto_file}
"""
# ----------------------------------------------------------------------------
import re
import xrst
#
# conf_py_general
conf_py_general = '''#
# General configuration
extensions = [
    'sphinx.ext.mathjax',
    'sphinx_rtd_theme',
]
exclude_patterns = [
    'test_out',
    'preamble.rst',
]
'''
#
# conf_py_theme
conf_py_theme = '''#
# Theme
html_theme = 'sphinx_rtd_theme'
#
if html_theme == 'sphinx_rtd_theme' :
    html_theme_options = {
        'navigation_depth' : -1   ,
        'titles_only'      : True ,
    }
elif html_theme == 'insipid' :
    html_theme_options = {
        'strip_section_numbers' : True,
        'nosidebar'             : True,
        'body_centered'         : False,
        'body_max_width'        : '70em',
        'breadcrumbs'           : True,
    }
else :
    assert False
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
    #
    # file_data
    file_name = sphinx_dir + '/preamble.rst'
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
# Create the automatically generated files in tmp_dir/rst
# (which end up in sphinx_dir/rst)
#
# sphinx_dir:
# is the name of xrst command line line argument *sphinx_dir*.
#
# tmp_dir:
# is the name of the directory where xrst creates a temporary copy of
# the sphinx_dir/rst directory.
#
# target:
# is html or pdf
#
# sinfo_list:
# is a list with length equal to the number of sections.
# The value section[section_index] is a dictionary for this seciton
# with the following key, value pairs (all the keys are strings:
# key            value
# section_name   a str continaing the name of this section.
# section_title  a str containing the title for this section.
# parent_section an int index in section_info for the parent of this section.
# in_parent_file is this section in same input file as its parent.
#
# tmp_dir/xsrst_table_of_contents.rst
# This file creates is the table of contents for the documentation.
# It has the lable xrst_table_of_contents which can be used to link
# to this section.
#
# tmp_dir/xsrst_preamble.rst
# This is a copy of the sphinx_dir/preamble.rst file. If target is
# pdf (html) the latex macros are (are not) removed.
#
# sphinx_dir/conf.py
# This is the configuration file used by sphinx to build the docuementation.
#
#
def auto_file(sphinx_dir, tmp_dir, target, sinfo_list) :
    # ------------------------------------------------------------------------
    # tmp_dir/xrst_table_of_contents.rst
    output_data = '.. include:: ../preamble.rst\n'
    #
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
    file_out    = tmp_dir + '/' + 'xrst_table_of_contents.rst'
    file_ptr    = open(file_out, 'w')
    file_ptr.write(output_data)
    file_ptr.close()
    # ------------------------------------------------------------------------
    # sphinx_dir/conf.py
    #
    # conf_py
    project = sinfo_list[0]['section_name']
    conf_py  = '# Project information\n'
    conf_py += f"project = '{project}'\n"
    conf_py += conf_py_general
    conf_py += conf_py_theme
    conf_py += '#\n'
    conf_py += '# Latex used when sphinx builds  pdf\n'
    conf_py += 'latex_elements = {\n'
    conf_py += "    'preamble' :\n"
    conf_py += "    r'\\renewcommand{\\thesection}{{\\hspace{-1em}}} ' + \n"
    conf_py += "    r'\\renewcommand{\\thesubsection}{{\\hspace{-1em}}} ' + \n"
    conf_py += "    r'\\renewcommand{\\thesubsubsection}{{\\hspace{-1em}}}'"
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
    file_out    = sphinx_dir + '/' + 'conf.py'
    file_ptr    = open(file_out, 'w')
    file_ptr.write(conf_py)
    file_ptr.close()
    # ------------------------------------------------------------------------
    # tmp_dir/xrst_preamble.rst
    #
    # file_data
    file_name = sphinx_dir + '/preamble.rst'
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
            after  = file_data[m_macro.end() - 1 ]
            file_data = before + after
            #
            # m_macro
            m_macro = pattern_macro.search(file_data, m_end() - 1)
    #
    # tmp_dir/xrstt_preamble.rst
    file_out    = tmp_dir + '/' + 'xrst_preamble.rst'
    file_ptr    = open(file_out, 'w')
    file_ptr.write(file_data)
    file_ptr.close()
    # ------------------------------------------------------------------------
