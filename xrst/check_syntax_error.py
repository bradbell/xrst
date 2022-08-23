# -----------------------------------------------------------------------------
#                      xrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
import re
import xrst
#
# Check for an xrst command that should have been removed and if not,
# report a syntax error.
#
# command_name:
# is the name of the xrst command; i.e., the following characters
# constitute a match for the command [^\\]{xrst_{command_name}[^z-a].
# where {command_name} is repalaced by the command name
#
# data:
# is the data for this section. This includes line numbers added by
# add_line_numbers.
#
# file_name:
# is the input that this section appears in (used for error reporting).
#
# section_name:
# is None or the name of this section (used for error reporting).
#
def check_syntax_error(command_name, data, file_name, section_name) :
   assert type(data) == str
   assert type(file_name) == str
   assert type(section_name) == str or section_name == None
   #
   pattern = r'[^\\]{xrst_' + command_name + r'[^a-z]'
   m_error = re.search(pattern, data)
   if m_error :
      msg = f'syntax error in xrst {command_name} command'
      xrst.system_exit(msg,
         file_name    = file_name ,
         section_name = section_name ,
         m_obj        = m_error ,
         data         = data ,
      )
   #
   return