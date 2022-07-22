# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
import os
import xsrst
#
# Process the file commands in a section.
#
# data_in:
# is the data for a section before the file commands have been removed.
#
# file_name:
# is the name of the file that this data comes from. This is used
# for error reporting and for the display file (when the display file
# is not incuded in the command).
#
# section_name:
# is the name of the section that this data is in. This is only used
# for error reporting.
#
# data_out:
# Each file command is convertd to the following format
#   {xsrst__file display_file start_line stop_line}
# In addition, there is a newline just before and after the text above.
# display_file: is the name of the file that is displayed by this command.
# start_line:  line number of first line to dislay
# stop_line:   line number of last line to dislay
#
# data_out =
def file_command(data_in, file_name, section_name) :
    assert xsrst.pattern['file_2'].groups == 6
    assert xsrst.pattern['file_3'].groups == 8
    #
    # data_out
    data_out = data_in
    #
    # key
    for key in [ 'file_2', 'file_3' ] :
        #
        m_file  = xsrst.pattern[key].search(data_out)
        while m_file != None :
            #
            # cmd_line
            cmd_start_line = int( m_file.group(1) )
            if key == 'file_2' :
                cmd_stop_line = int( m_file.group(6) )
            else :
                cmd_stop_line = int( m_file.group(8) )
            cmd_line = (cmd_start_line, cmd_stop_line)
            #
            # start_text
            start_text = m_file.group(2).strip()
            #
            # stop_text
            stop_text = m_file.group(4) .strip()
            #
            # display_file
            if key == 'file_2' :
                display_file = file_name
            else :
                display_file = m_file.group(6).strip()
                same_file   = os.path.samefile(display_file, file_name)
                if same_file :
                    display_file = file_name
            #
            # start_line, stop_line
            start_line, stop_line = xsrst.start_stop_file(
                section_name = section_name,
                file_cmd     = file_name,
                display_file = display_file,
                cmd_line     = cmd_line,
                start_text   = start_text,
                stop_text    = stop_text
            )
            #
            # locations in display_file
            start_line  = start_line + 1
            stop_line   = stop_line  - 1
            #
            # beginning of lines with command in it
            begin_line = m_file.start();
            #
            # end of lines with command in it
            end_line = m_file.end();
            #
            # cmd
            # converted version of the command, use two underbars so does
            # not match pattern['file_2'] or pattern['file_3'].
            cmd  = f'xsrst__file {display_file} {start_line} {stop_line} '
            cmd  = '\n{' + cmd  + '}\n'
            #
            # data_out
            data_tmp  = data_out[: m_file.start() ]
            data_tmp += cmd
            data_tmp += '\n' + data_out[ m_file.end() : ]
            data_out  = data_tmp
            #
            # m_file
            m_file  = xsrst.pattern[key].search(data_out)
            #
    return data_out
