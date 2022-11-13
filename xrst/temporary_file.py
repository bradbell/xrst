# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
import re
import xrst
pattern_line_number = re.compile( r'\n[ \t]*{xrst_line [0-9]+@' )
pattern_newline_3   = re.compile( r'(\n[ \t]*){2,}\n' )
# ----------------------------------------------------------------------------
# {xrst_begin temporary_file dev}
# {xrst_spell
#     dir
#     file file
#     tmp
# }
# {xrst_comment_ch #}
#
# Write the temporary RST file for a page
# #######################################
#
# rst_line
# ********
# is an int version of the :ref:`run_xrst@rst_line`
# argument to the xrst program (with None represented by zero).
#
# pseudo_heading
# **************
# is the :ref:`process_headings@Returns@pseudo_heading` for this page.
# It is placed before all the other headings in this page.
# A label is added just before the pseudo heading that
# links to it using the page name.
#
# file_in
# *******
# is the name of the xrst input file for this page.
#
# tmp_dir
# *******
# is the directory where the output file will be saved.
#
# page_name
# *********
# is the name of this page.
#
# file_out
# ********
# The temporary file written by the routine, *file_out* , is
# tmp_dir/page_name.rst.
#
# data_in
# *******
# is the data for this page with all the xrst commands converted to
# their sphinx RST values, except the \\n{xrst_page_number} command.
# The following is added to this data before writing it to the output file:
#
# #. The preamble is included at the beginning.
# #. The pseudo heading and its label are added next.
# #. The name of the input file file_in is displayed next.
# #. More than 2 lines with only tabs or space are converted to 2 empty lines.
# #. Empty lines at the end are removed
# #. The line numbers are removed.
# #. The text ``\\{xrst_`` is replaced by ``\{xrst_`` .
# #. if rst_line > 0, a mapping from RST line numbers to file_in line numbers
#    is included at the end.
#
# line_pair
# *********
# This is the value returned by ``temporary_file`` .
# For each *index*, *line_pair* [ *index* ] is the a pair of line numbers.
#
# -   The first number in a pair is a line number in *file_out*
#     These line numbers to not count `{xrst_page_number}` lines
#     because they are removed before the final rst output is created.
#
# -   The second number in a pair is the corresponding line number in *file_in*
#
# -   The first (second) line number is increasing (no-decreasing)
#     with respect to *index* .
#
# {xrst_code py}
# line_pair =
def temporary_file(
   rst_line,
   pseudo_heading,
   file_in,
   tmp_dir,
   page_name,
   data_in,
) :
   assert type(rst_line) == int
   assert type(pseudo_heading) == str
   assert type(file_in) == str
   assert type(page_name) == str
   assert type(data_in) == str
   # {xrst_code}
   #
   # {xrst_literal
   #  BEGIN_RETURN
   #  END_RETURN
   # }
   # {xrst_end temporary_file}
   #
   # label
   # label that displays page name (which is text in pseudo heading)
   label = f'.. _{page_name}:\n\n'
   #
   # before
   # start output by including preamble and then pesudo_heading
   before  = '.. include:: xrst_preamble.rst\n\n'
   before += label
   before += pseudo_heading
   before += f'xrst input file: ``{file_in}``\n\n'
   #
   # data_out
   data_out = before + data_in
   #
   # data_out
   # Convert three or more sequential emtpty lines to two empty lines.
   data_out = pattern_line_number.sub('\n', data_out)
   data_out = pattern_newline_3.sub('\n\n', data_out)
   #
   # data_out
   # remove empty lines at the end
   while data_out[-2 :] == '\n\n' :
      data_out = data_out[: -1]
   #
   # data_out
   # The last step removing line numbers. This is done last for two reasons:
   # 1. So mapping from output to input line number is correct.
   # 2. We are no longer able to give line numbers for errors after this.
   data_out, line_pair = xrst.remove_line_numbers(data_out)
   #
   # data_out
   data_out = data_out.replace( r'\{xrst_', '{xrst_' )
   #
   # after
   # If line number increment is non-zero, include mapping from
   # rst file line number to xrst file line number
   if rst_line > 0 :
      after  = '\n.. csv--targetable:: Line Number Mapping\n'
      after += 4 * ' ' + ':header: rst file, xrst input\n'
      after += 4 * ' ' + ':widths: 10, 10\n\n'
      previous_line = None
      for pair in line_pair :
         if previous_line is None :
            after        += f'    {pair[0]}, {pair[1]}\n'
            previous_line = pair[1]
         elif pair[1] - previous_line >= rst_line :
            after         += f'    {pair[0]}, {pair[1]}\n'
            previous_line = pair[1]
      #
      data_out = data_out + after
   #
   # file_out
   if page_name.endswith('.rst') :
      file_out = tmp_dir + '/' + page_name
   else :
      file_out = tmp_dir + '/' + page_name + '.rst'
   file_ptr = open(file_out, 'w')
   file_ptr.write(data_out)
   file_ptr.close()
   #
   # BEGIN_RETURN
   assert type(line_pair) == list
   assert type( line_pair[0] ) == tuple
   assert len( line_pair[0] ) == 2
   assert type( line_pair[0][0] ) == int
   assert type( line_pair[0][1] ) == int
   return line_pair
   # END_RETURN
