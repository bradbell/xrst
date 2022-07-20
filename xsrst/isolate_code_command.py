# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
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
import xsrst
def isolate_code_command(data_in, file_name, section_name) :
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
