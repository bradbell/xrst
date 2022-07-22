# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
import re
import xsrst
#
# Remove text specified by suspend / resume pairs.
#
# data_in
# is the data for this section.
#
# file_name
# is the input file corresponding to this section.
#
# section_name
# is the name of this section.
#
# data_out
# The return data_out is a copy of data_in except that the text between
# and including each suspend / resume pair has been removed.
#
# data_out =
def suspend_command(data_in, file_name, section_name) :
    assert type(data_in) == str
    assert type(file_name) == str
    assert type(section_name) == str
    #
    # data_out
    data_out = data_in
    #
    # pattern_suspend, pattern_resume
    pattern_suspend = re.compile( r'\n[ \t]*\{xsrst_suspend\}' )
    pattern_resume  = re.compile( r'\n[ \t]*\{xsrst_resume\}' )
    #
    # m_suspend
    m_suspend       = pattern_suspend.search(data_out)
    while m_suspend != None :
        # suspend_start, suspend_end, data_rest
        suspend_start = m_suspend.start()
        suspend_end   = m_suspend.end()
        data_rest     = data_out[ suspend_end : ]
        #
        # m_resume
        m_resume      = pattern_resume.search(data_rest)
        if m_resume == None :
            msg  = 'There is a suspend command without a '
            msg += 'corresponding resume commannd.'
            xsrst.system_exit(msg,
                file_name=file_name,
                section_name=section_name,
                m_obj=m_suspend,
                data=data_out
            )
        #
        # m_obj
        m_obj = pattern_suspend.search(data_rest)
        if m_obj != None :
            if m_obj.start() < m_resume.start() :
                msg  = 'There are two suspend commands without a '
                msg += 'resume command between them.'
                xsrst.system_exit(msg,
                    file_name=file_name,
                    section_name=section_name,
                    m_obj=m_obj,
                    data=data_rest
                )
        resume_end = m_resume.end() + suspend_end
        data_rest  = data_out[ resume_end :]
        data_out   = data_out[: suspend_start] + data_rest
        #
        # redo match_suppend so relative to new data_out
        m_suspend = pattern_suspend.search(data_out)
    return data_out
