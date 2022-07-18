#! /usr/bin/env python3
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
# find corresponding line number in the input file
pattern['line'] = re.compile(r'\{xsrst_line ([0-9]+)@')
#
from .check_section_name     import check_section_name
from .replace_section_number import replace_section_number
from .system_exit            import system_exit
