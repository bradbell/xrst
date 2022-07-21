# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
import re
# ----------------------------------------------------------------------------
# pattern
# This dictionary is does not change from its inital settings in this file
pattern = dict()
#
# pattern['line']
# These line numbers are added to the input by add_line_number
# match.group(0) is the entire line command.
# match.group(1) is the line_number.
pattern['line'] = re.compile( r'\{xsrst_line ([0-9]+)@' )
#
# pattern['begin']
# This pattern assume that remove_comment_ch has preprocessed the input
# match.group(0) is preceeding newline and white space plus the command.
# match.group(2) is begin or begin_parent
# match.group(3) is the section name.
pattern['begin'] = re.compile(
    r'(^|\n)[ \t]*\{xsrst_(begin|begin_parent)\s+([^}]*)\}'
)
# pattern['end']
# This pattern assume that remove_comment_ch has preprocessed the input
# match.group(0) is preceeding newline and white space plus the command.
# match.group(1) is the section name.
pattern['end'] = re.compile( r'\n[ \t]*\{xsrst_end\s+([^}]*)\}' )
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
# ----------------------------------------------------------------------------
# functions
#
# BEGIN_SORT_THIS_LINE_PLUS_1
from .add_line_numbers       import add_line_numbers
from .check_section_name     import check_section_name
from .child_commands         import child_commands
from .create_spell_checker   import create_spell_checker
from .file2_list_str         import file2_list_str
from .get_file_info          import get_file_info
from .isolate_code_command   import isolate_code_command
from .newline_indices        import newline_indices
from .remove_comment_ch      import remove_comment_ch
from .remove_indent          import remove_indent
from .remove_line_numbers    import remove_line_numbers
from .replace_section_number import replace_section_number
from .spell_command          import spell_command
from .start_stop_file        import start_stop_file
from .suspend_command        import suspend_command
from .system_exit            import system_exit
from .table_of_contents      import table_of_contents
# END_SORT_THIS_LINE_MINUS_1
