# -----------------------------------------------------------------------------
#                      xrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xrst_begin auto_file}

Automatically Generated Files
#############################
These files are located in the directory
created automatically each time :ref:`xrst<run_xrst>` is run.
They are located in the
:ref:`run_xrst@command_line_arguments@sphinx_dir` directory:


rst/xrst_table_contents.rst
***************************
This file contains the table of contents for the last run of ``xrst``.


{xrst_end auto_file}
"""
# Create the automatically generated files in tmp_dir/rst
# (which end up in sphinx_dir/rst)
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
# Is the file creates with the table of contents.
# It has the lable xrst_table_of_contents which can be used to link
# to this section.
#
# ----------------------------------------------------------------------------
import xrst
#
#
def auto_file(tmp_dir, target, sinfo_list) :
    #
    # xrst_table_of_contents
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
