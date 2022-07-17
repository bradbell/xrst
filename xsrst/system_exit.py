# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
# add file name, section name, and line number to a message in a system exit
# msg:    error message
# fname:  file name
# sname:  section name
# match:  match object inticating where in data the error is detected
# data:   is the input data that was matched when match is not None
# line:   is the error line number when match is None
#
import sys
import xsrst
def system_exit(msg, fname=None, sname=None, match=None, data=None, line=None) :
    assert type(msg)   == str
    assert type(fname) == str or fname == None
    assert type(sname) == str or sname == None
    assert type(line)  in [ int, str ] or line == None

    if match :
        assert type(data) == str
    #
    extra = ''
    if sname :
        extra += 'section = ' + sname
    if fname :
        if extra != '' :
            extra += ', '
        extra += 'file = ' + fname
    if match :
        assert fname != None
        assert data != None
        assert line == None
        match_line  = xsrst.pattern_line.search( data[match.start() :] )
        assert match_line
        line = match_line.group(1)
    if line != None :
        if extra != '' :
            extra += ', '
        extra += 'line = ' + str(line)
    if extra != '' :
        msg += '\n' + extra
    sys.exit('\n' + msg)
