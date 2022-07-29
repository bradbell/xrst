# -----------------------------------------------------------------------------
#                      xrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xrst_begin file_cmd}

File Command
############

Syntax
******

| ``{xrst_file``
| |tab| *start*
| |tab| *stop*
| :code:`}`
|
| ``{xrst_file``
| |tab| *start*
| |tab| *stop*
| |tab| *display_file*
| :code:`}`

Purpose
*******
A code block, from any where in any file,
can be included by the command above at the
:ref:`beginning of a line<run_xrst@notation@beginning_of_a_line>`.

White Space
***********
Leading and trailing white space is not included in
*start*, *stop* or *display_file*.
The new line character separates these tokens.

display_file
************
If *display_file* is not in the syntax,
the code block is in the current input file.
Otherwise, the code block is in *display_file*.
The file name *display_file* is relative to the directory
where :ref:`xrst<run_xrst>` is executed.
This may seem verbose, but it makes it easier to write scripts
that move files and automatically change references to them.

start
*****
The code block starts with the line following the occurrence
of the text *start* in *display_file*.
If this is the same as the file containing the command,
the text *start* will not match any text in the command.
There must be one and only one occurrence of *start* in *display_file*,
not counting the command itself when the files are the same.

stop
****
The code block ends with the line before the occurrence
of the text *start* in *display_file*.
If this is the same as the file containing the command,
the text *stop* will not match any text in the command.
There must be one and only one occurrence of *stop* in *display_file*,
not counting the command itself when the files are the same.

Spell Checking
**************
Spell checking is **not** done for these code blocks.


Example
*******
{xrst_child_list
   sphinx/test_in/file.cpp
}

{xrst_end file_cmd}
"""
# ----------------------------------------------------------------------------
import os
import xrst
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
# rst_dir:
# is the directory, relative to the current working directory,
# where xrst will place the final rst files.
#
# data_out:
# Each xrst file command is convertd to its corresponding sphinx commands.
#
# data_out =
def file_command(data_in, file_name, section_name, rst_dir) :
    assert type(data_in) == str
    assert type(file_name) == str
    assert type(section_name) == str
    assert type(rst_dir) == str
    #
    assert xrst.pattern['file_2'].groups == 6
    assert xrst.pattern['file_3'].groups == 8
    #
    # data_out
    data_out = data_in
    #
    # key
    for key in [ 'file_2', 'file_3' ] :
        #
        m_file  = xrst.pattern[key].search(data_out)
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
            start_line, stop_line = xrst.start_stop_file(
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
            depth    = rst_dir.count('/') + 1
            work_dir = depth * '../'
            cmd      = f'.. literalinclude:: {work_dir}{display_file}\n'
            cmd     += 4 * ' ' + f':lines: {start_line}-{stop_line}\n'
            #
            # Add language to literalinclude, sphinx seems to be brain
            # dead and does not do this automatically.
            index = display_file.rfind('.')
            if 0 <= index and index + 1 < len(display_file) :
                extension = display_file[index + 1 :]
                if extension == 'xrst' :
                    extension = 'rst'
                elif extension == 'hpp' :
                    extension = 'cpp' # pygments does not recognize hpp ?
                cmd += 4 * ' ' + f':language: {extension}\n'
            cmd = '\n' + cmd + '\n'
            if m_file.start() > 0 :
                if data_out[m_file.start() - 1] != '\n' :
                    cmd = '\n' + cmd
            #
            # data_out
            data_tmp  = data_out[: m_file.start() ]
            data_tmp += cmd
            data_tmp += '\n' + data_out[ m_file.end() : ]
            data_out  = data_tmp
            #
            # m_file
            m_file  = xrst.pattern[key].search(data_out)
            #
    return data_out
