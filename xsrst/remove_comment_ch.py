# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
# Removes the beginning of line comment character from file data.
#
# Comment Character:
# The comment character is specified by {xsrst_comment_ch ch} where ch
# is a single character after leading and trailing white space is removed.
#
# data_in:
# is the original data in this file as one disk. Line numbers may, or may not
# have been added.
#
# file_name:
# is the name of this file (used for error reporting).
#
# data_out:
# is a copy of data_in with occurences of the comment character at the
# beginning of each line removed. If there is a space directly after the
# comment character, it is also removed.
#
import re
import xsrst
def remove_comment_ch(data_in, file_name) :
    assert type(data_in) == str
    assert type(file_name) == str
    #
    # m_obj
    pattern = re.compile(r'{xsrst_comment_ch\s+([^}])\s*\}')
    m_obj   = pattern.search(data_in)
    #
    # data_out
    if not m_obj :
        data_out = data_in
    else :
        #
        # comment_ch
        comment_ch = m_obj.group(1)
        if comment_ch == ']' :
            line = data_in[: m_obj.start() ].count('\n') + 1
            msg  = 'Cannot use "]" as charaxter in comment_ch command\n'
            xsrst.system_exit(msg, fname=file_name, line=line)
        #
        # m_obj
        data_rest  = data_in[ m_obj.end() : ]
        m_rest     = pattern.search(data_rest)
        if m_rest :
            line = data_in[: m_obj.end() + m_rest.start() ].count('\n') + 1
            msg = 'There are multiple comment_ch commands in this file'
            xsrst.system_exit(msg, fname=file_name, line=line)
        #
        # data_out
        pattern  = re.compile( r'\n[' + comment_ch + r'] ?' )
        data_out = pattern.sub(r'\n', data_in)
    return data_out
