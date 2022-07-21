# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
import re
#
# pattern
# This dictionary is does not change after its inital settings in this file
pattern = dict()
#
# pattern['begin']
# This pattern assume that remove_comment_ch has preprocessed the input
# match.group(0) is preceeding newline and white space plus the command.
# match.group(2) is begin or begin_parent
# match.group(3) is the section name.
pattern['begin'] = re.compile(
    r'(^|\n)[ \t]*\{xsrst_(begin|begin_parent)\s+([^}]*)\}'
)
#
# pattern['child']
# Patterns for the children, child_list, and child_table commands.
#
# match.group(1) is command name; i.e., children, child_list, or child_table
# match.group(2) is the rest of the command that comes after the command name.
#                This is a list of file names with one name per line.
#                The } at the end of the command is not included.
pattern['child']   = re.compile(
    r'\n[ \t]*\{xsrst_(children|child_list|child_table)([^}]*)\}'
)
#
# pattern['code']
# Pattern for entire line containing a code command.
# match.group(0) is the entire line for the command (whith newline at front).
# match.group(1) is the characters before the language argument including
#                white space
# match.group(2) is the language argument which is emtpy (just white space)
#                for the second code command in each pair.
# match.group(3) is the line number for this line; see pattern['line'] above.
pattern['code'] = re.compile(
    r'(\n[^\n`]*\{xsrst_code *)([^}]*)\}[^\n`]*(\{xsrst_line [0-9]+@)'
)
#
# pattern['end']
# This pattern assume that remove_comment_ch has preprocessed the input
# match.group(0) is preceeding newline and white space plus the command.
# match.group(1) is the section name.
pattern['end'] = re.compile( r'\n[ \t]*\{xsrst_end\s+([^}]*)\}' )
#
# pattern['line']
# These line numbers are added to the input by add_line_number
# match.group(0) is the entire line command.
# match.group(1) is the line_number.
pattern['line'] = re.compile( r'\{xsrst_line ([0-9]+)@' )
