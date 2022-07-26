#! /usr/bin/env python3
# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
#
import sys
import re
import os
#
# usage
usage = \
'''
usage: update_xsrst.py operation file_in file_out

operation: is one of the following: dot2atsign
file_in:   is the name of the file we are updating.
file_out:  is the name of the updated file. It can be the samle as file_in.

dot2atsign:
Change the '.' to '@' character in all text of the form :ref:`text` and
text of the form (at the betinning of a line) .. _text:

'''
#
# pattern
pattern        = dict()
pattern['ref'] = re.compile( r'(:ref:`[^`]*)\.' )
#
# abort
def abort(msg) :
    msg = '\nupdate_xstst.py: ' + msg
    sys.exit(msg)
#
# dot2atsign
def dot2atsign(data_in) :
    # data_out
    data_out = data_in
    #
    # m_ref
    m_ref    = pattern['ref'].search(data_out)
    while m_ref :
        # data_out
        data_out = pattern['ref'].sub(r'\1@', data_out)
        #
        # m_ref
        m_ref  = pattern['ref'].search(data_out, m_ref.start() )
    #
    return data_out
#
# main
def main() :
    if( len(sys.argv) != 4 ) :
        print(usage)
    #
    # operation_dict
    operation_dict = {
        'dot2atsign' : dot2atsign,
    }
    #
    # operation
    operation = sys.argv[1]
    if operation not in operation_dict :
        msg  = f'operation = {operation} is not a valid operation'
        abort(msg)
    #
    # file_in,
    file_in = sys.argv[2]
    if not os.path.isfile(file_in) :
        msg = f'file_in = {file_in} is not an existing file'
        abort(msg)
    #
    # file_out
    file_out = sys.argv[3]
    #
    # file_data
    file_ptr   = open(file_in, 'r')
    file_data  = file_ptr.read()
    file_ptr.close()
    #
    # file_out
    file_data = operation_dict[operation](file_data)
    #
    # file_out
    file_ptr = open(file_out, 'w')
    file_ptr.write(file_data)
    file_ptr.close()
#
main()
print('update_xsrst.py: OK')
sys.exit(0)
