# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
# Check that a section name abides by its rules. If not, report error and exit.
#
# section_name:
# The string section_name appears at the begnning of a line, not counting
# white space, in one of the following cases:
# 1. {xsrst_begin_parent section_name}
# 2. {xsrst_begin section_name}
# 3. {xsrst_end section_name}
# The valid characters in a seciton name are [a-z], [0-9], and underbar.
# A section name cannot begin with xsrst_. If seciton_name does not follow the
# rules in the previous sentence, a message is printed and the program exits.
#
# fname:
# is the name of the original input file that data appears in.
#
# m_obj:
# is the match object correpsonding to finding the section name
#
# data:
# is that data that was searched to detect the match object.
#
import re
import xsrst
def check_section_name(section_name, fname, m_obj, data) :
    m = re.search('[a-z0-9_]+', section_name)
    if m.group(0) != section_name :
        msg  = 'section_name after xsrst_begin must be non-empty'
        msg += '\nand only contain following characters: a-z, 0-9, _'
        xsrst.system_exit(msg,
            fname=fname, m_obj=m_obj, data=data
        )
    if section_name.startswith('xsrst_') :
        # section name xsrst_py is used to document this program
        if section_name != 'xsrst_py' :
            msg = 'section_name cannot start with xsrst_'
            xsrst.system_exit(msg,
                fname=fname, m_obj=m_obj, data=data
            )
