# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xsrst_begin code_cmd}

Code Command
############

Syntax
******
- ``{xsrst_code`` *language* :code:`}`
- ``{xsrst_code}``

Purpose
*******
A code block, directly below in the current input file, begins with
a line containing the first version ( *language* included version)
of the command above.

Requirements
************
Each code command ends with
a line containing the second version of the command; i.e., ``{xsrst_code}``.
Hence there must be an even number of code commands.
If the back quote character \` appears before or after the ``{xsrst_code``,
it is not a command but rather normal input text. This is useful when
referring to this command in documentation.

language
********
A *language* is a non-empty sequence of non-space the characters.
It is used to determine the source code language
for highlighting the code block.

Rest of Line
************
Other characters on the same line as a code command
are not included in the xsrst output.
This enables one to begin or end a comment block
without having the comment characters in the xsrst output.

Spell Checking
**************
Code blocks as usually small and
spell checking is done for these code blocks.
(Spell checking is not done for code blocks included using the
:ref:`file command<file_cmd>` .)

Example
*******
{xsrst_child_list
   sphinx/test_in/code.py
}

{xsrst_end code_cmd}
"""
# ----------------------------------------------------------------------------
import xsrst
#
# Remove extra characters on same line as code commands.
#
# data_in:
# is the data for the section before the code commands have been isolated.
# Line numbers have been added to this data: see add_line_numbers.
#
# file_name:
# is the name of the file that this data comes from. This is only used
# for error reporting.
#
# section_name:
# is the name of the section that this data is in. This is only used
# for error reporting.
#
# data_out:
# is a copy of data_in with the code commands isloated. To be specific,
# for each line that contains a code command, the characters that are not
# part of the command (except for the line numbers) are removed.
#
# data_out =
def isolate_code_command(data_in, file_name, section_name) :
    assert type(data_in) == str
    assert type(file_name) == str
    assert type(section_name) == str
    #
    # data_out
    data_out = data_in
    #
    # m_begin
    m_begin = xsrst.pattern['code'].search(data_in)
    #
    if m_begin == None :
        return data_in
    #
    while m_begin != None :
        #
        # m_end
        start = m_begin.end()
        m_end = xsrst.pattern['code'].search(data_in, start)
        #
        # language
        language  = m_begin.group(2).strip()
        if language == '' :
            msg = 'missing language in first command of a code block pair'
            xsrst.system_exit(msg,
                file_name=file_name,
                section_name=section_name,
                m_obj=m_begin,
                data=data_out
            )
        for ch in language :
            if ch < 'a' or 'z' < ch :
                msg = 'code block language character not in a-z.'
                xsrst.system_exit(msg,
                    file_name=file_name,
                    section_name=section_name,
                    m_obj=m_begin,
                    data=data_out
                )
        #
        if m_end == None :
            msg = 'Start code command does not have a corresponding stop'
            xsrst.system_exit(msg,
                file_name=file_name,
                section_name=section_name,
                m_obj=m_begin,
                data=data_out
            )
        if m_end.group(2).strip() != '' :
            msg ='Stop code command has a non-empty language argument'
            xsrst.system_exit(msg,
                file_name=file_name,
                section_name=section_name,
                m_obj=m_end,
                data=section_rest
            )
        #
        # data_out
        # pygments does not recognize hpp so change it to cpp ?
        if language == 'hpp' :
            index = m_begin.start() + len(m_begin.group(1))
            assert data_out[index: index+2] == 'hpp'
            data_out[index] = 'c'
        #
        # m_begin
        start   = m_end.end()
        m_begin = xsrst.pattern['code'].search(data_in, start)
    #
    # data_out
    replace  = r'\n{xsrst_code \2}\3'
    data_out = xsrst.pattern['code'].sub(replace, data_in)
    #
    return data_out
