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
These files are located in the directory
created automatically each time :ref:`xrst<run_xrst>` is run.
They are located in the
:ref:`run_xrst@command_line_arguments@sphinx_dir` directory:


rst/xrst_table_contents.rst
***************************
This file contains the table of contents for the last run of ``xrst``.

conf.py
*******
This is the sphinx configuration_ file.

.. _configuration:  http://www.sphinx-doc.org/en/master/config




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
def preamble_macros(sphinx_dir) :
    #
    # pattern
    pattern = r'\n[ \t]*:math:`(\\newcommand\{[^`]*\})`[ \t]*\n'
    pattern = re.compile(pattern)
    #
    # file_data
    file_name = sphinx_dir + '/preamble.rst'
    file_ptr  = open(file_name, 'r')
    file_data = file_ptr.read()
    file_ptr.close()
    #
    # m_math
    m_math = pattern.search(file_data)
    #
    # macro_list
    macro_list = list()
    while m_math :
        #
        # macro_list
        macro = m_math.group(1)
        macro_list.append(macro)
        #
        # m_math
        m_math = pattern.search(file_data, m_math.end() - 1)
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
# sphinx_dir/conf.py
# This is the configuration file used by sphinx to build the docuementation.
#
def auto_file(sphinx_dir, tmp_dir, target, sinfo_list) :
    #
    # rst/xrst_table_of_contents.rst
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
    # conf_pu
    conf_py += latex + '\n}\n'
    #
    file_out    = sphinx_dir + '/' + 'conf.py'
    file_ptr    = open(file_out, 'w')
    file_ptr.write(conf_py)
    file_ptr.close()
