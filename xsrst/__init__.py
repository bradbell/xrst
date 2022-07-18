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
# This dictionary is does not change from its inital settings in this file
pattern = dict()
#
# line
# These line numbers are added to the input by add_line_number
pattern['line'] = re.compile(r'\{xsrst_line ([0-9]+)@')
#
# BEGIN_SORT_THIS_LINE_PLUS_1
from .add_line_numbers       import add_line_numbers
from .check_section_name     import check_section_name
from .create_spell_checker   import create_spell_checker
from .newline_indices        import newline_indices
from .remove_line_numbers    import remove_line_numbers
from .replace_section_number import replace_section_number
from .system_exit            import system_exit
from .table_of_contents      import table_of_contents
# END_SORT_THIS_LINE_MINUS_1
