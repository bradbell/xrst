# -----------------------------------------------------------------------------
#                      xrst: Extract Sphinx RST Files
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
# group(0): preceeding character or empty + the command.
# group(1); preceeding character or empty
# group(2): begin or begin_parent
# group(3): the page name (without leading or trailing spaces or tabs)
# group(4): the group name (with leading and trailing spaces and tabs)
pattern['begin'] = re.compile(
   r'(^|[^\\]){xrst_(begin|begin_parent)[ \t]+([^ \t}]*)([^}]*)}'
)
#
# pattern['toc']
# Patterns for the toc_hidden, toc_list, and toc_table commands.
# group(0): preceeding character + the command.
# group(1): command name; i.e., hidden, list, or table
# group(2): the rest of the command that comes after the command name.
#        This is a list of file names with one name per line.
#        The } at the end of the command is not included.
#        This pattern may be empty.
# If you change this pattern, check pattern_toc in process_children.py
pattern['toc']   = re.compile(
   r'[^\\]{xrst_toc_(hidden|list|table)([^}]*)}'
)
#
# pattern['code']
# Pattern for code command.
# group(0): the entire line for the command (newline at front).
# group(1): the characters before the language argument including white space
# group(2): on possiblity for group(1)
# group(3): other possibility for group(1)
# group(4): the language argument which is emtpy (just white space)
#        for the second code command in each pair.
# group(5): the line number for this line; see pattern['line'] above.
pattern['code'] = re.compile(
   r'((\n{xrst_code *)|(\n[^\n]*[^\n\\]\{xrst_code *))' +
   r'([^}]*)}[^\n]*({xrst_line [0-9]+@)'
)
#
# pattern['comment_ch']
# Pattern for comment_ch command
# group(0): empty or character before comamnd + the command
# group(1): is the character (matched as any number of not space, tab or }
pattern['comment_ch'] = re.compile(
      r'(^|[^\\])\{xrst_comment_ch\s+([^} \t]*)\s*}'
)
#
# pattern['end']
# Pattern for end command
# group(0): preeeding character + white space + the command.
# group(1): the page name.
pattern['end'] = re.compile( r'[^\\]{xrst_end\s+([^}]*)}' )
#
#
# pattern['line']
# Pattern for line numbers are added to the input by add_line_number
# group(0): the line command.
# group(1): the line_number.
pattern['line'] = re.compile( r'{xrst_line ([0-9]+)@' )
#
# pattern['literal_0']
# xrst_literal with no arguments
# group(0): preceeding newline + white space + the command.
# group(1): line number where } at end of command appears
#
# pattern['literal_1']
# xrst_literal wth display_file
# group(0): preceeding newline + white space + the command.
# group(1): the line number where this command starts
# group(2): the display file
# group(3): line number where display file appears
# group(4): line number where } at end of command appears
#
# pattern['literal_2']
# xrst_literal with start, stop
# group(0): preceeding newline + white space + the command.
# group(1): the line number where this command starts
# group(2): the start text + surrounding white space
# group(3): line number where start text appears
# group(4): the stop text + surrounding white space
# group(5): the line number where stop text appears
# group(6): line number where } at end of command appears
#
# pattern['literal_3']
# xrst_literal with start, stop, display_file
# group(0): preceeding character + the command.
# group(1): the line number where this command starts
# group(2): the display file
# group(3): line number where display file appears
# group(4): the start text + surrounding white space
# group(5): line number where start text appears
# group(6): the stop text + surrounding white space
# group(7): the line number where stop text appears
# group(8): line number where } at end of command appears
#
arg = r'([^{]*){xrst_line ([0-9]+)@\n'
lin = r'[ \t]*{xrst_line ([0-9]+)@\n'
pattern['literal_0'] = re.compile(
   r'[^\\]{xrst_literal}' + lin
)
pattern['literal_1']  = re.compile(
   r'[^\\]{xrst_literal' + lin + arg + r'[ \t]*}' + lin
)
pattern['literal_2']  = re.compile(
   r'[^\\]{xrst_literal' + lin + arg + arg + r'[ \t]*}' + lin
)
pattern['literal_3']  = re.compile(
   r'[^\\]{xrst_literal' + lin + arg + arg + arg + r'[ \t]*}' + lin
)
