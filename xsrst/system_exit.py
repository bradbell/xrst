# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
# Add file name, section name, and line number to a message in a system exit
#
# msg:           error message
# file_name:     original input file that that data appeared in.
# section_name:  section name
# m_obj:         match object inticating where in data the error is detected
# data:          is the input data that was matched when m_obj is not None
# line:          is the error line number when m_obj is None
#
import sys
import xsrst
def system_exit(
    msg, file_name=None, section_name=None, m_obj=None, data=None, line=None
) :
    assert type(msg)   == str
    assert type(file_name) == str or file_name== None
    assert type(section_name) == str or section_name== None
    assert type(line)  in [ int, str ] or line == None
    #
    if m_obj :
        assert type(data) == str
    #
    extra = ''
    if section_name :
        extra += 'section = ' + section_name
    if file_name :
        if extra != '' :
            extra += ', '
        extra += 'file = ' + file_name
    if m_obj :
        assert file_name != None
        assert data != None
        assert line == None
        match_line  = xsrst.pattern['line'].search( data[m_obj.start() :] )
        assert match_line
        line = match_line.group(1)
    if line != None :
        if extra != '' :
            extra += ', '
        extra += 'line = ' + str(line)
    if extra != '' :
        msg += '\n' + extra
    sys.exit('\nxsrst: ' + msg)
