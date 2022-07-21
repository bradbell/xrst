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
# This dictionary contains compiled regular expressions.
# It does not change after its initial setting when this file is imported.
pattern = dict()
#
# pattern['begin']
# Pattern for the begin command.
# group(0): preceeding newline + white space + the command.
# group(2): begin or begin_parent
# group(3): the section name.
pattern['begin'] = re.compile(
    r'(^|\n)[ \t]*\{xsrst_(begin|begin_parent)\s+([^}]*)\}'
)
#
# pattern['child']
# Patterns for the children, child_list, and child_table commands.
# group(0): preceeding newline + white space + the command.
# group(1): command name; i.e., children, child_list, or child_table
# group(2): the rest of the command that comes after the command name.
#           This is a list of file names with one name per line.
#           The } at the end of the command is not included.
pattern['child']   = re.compile(
    r'\n[ \t]*\{xsrst_(children|child_list|child_table)([^}]*)\}'
)
#
# pattern['code']
# Pattern for code command.
# group(0): the entire line for the command (newline at front).
# group(1): the characters before the language argument including white space
# group(2): the language argument which is emtpy (just white space)
#           for the second code command in each pair.
# group(3): the line number for this line; see pattern['line'] above.
pattern['code'] = re.compile(
    r'(\n[^\n`]*\{xsrst_code *)([^}]*)\}[^\n`]*(\{xsrst_line [0-9]+@)'
)
#
# pattern['end']
# Pattern for end command
# group(0): preceeding newline + white space + the command.
# group(1): the section name.
pattern['end'] = re.compile( r'\n[ \t]*\{xsrst_end\s+([^}]*)\}' )
#
# pattern['file_2']
# Pattern for a file command that searches the from current input file.
# group(0): preceeding newline + white space + the command.
# group(1): the line number where this command starts
# group(2): the start text + surrounding white space
# group(3): line number where start text appears
# group(4): the stop text + surrounding white space
# group(5): the line number where stop text appears
# group(6): line number where } at end of command appears
#
# pattern['file_3']
# Pattern for a file command that search a specified file.
# group(0): preceeding newline + white space + the command.
# group(1): the line number where this command starts
# group(2): the start text + surrounding white space
# group(3): line number where start text appears
# group(4): the stop text + surrounding white space
# group(5): the line number where stop text appears
# group(6): the file that is searched
# group(7): line number where search file appears
# group(8): line number where } at end of command appears
#
arg = r'([^{]*)\{xsrst_line ([0-9]+)@\n'
lin = r'[ \t]*\{xsrst_line ([0-9]+)@\n'
pattern['file_2']  = re.compile(
    r'\n[ \t]*\{xsrst_file' + lin + arg + arg + r'[ \t]*\}' + lin
)
pattern['file_3']  = re.compile(
    r'\n[ \t]*\{xsrst_file' + lin + arg + arg + arg + r'[ \t]*\}' + lin
)
#
#
# pattern['line']
# Pattern for line numbers are added to the input by add_line_number
# group(0): the line command.
# group(1): the line_number.
pattern['line'] = re.compile( r'\{xsrst_line ([0-9]+)@' )
