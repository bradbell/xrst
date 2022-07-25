# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xsrst_begin suspend_cmd}

Suspend and Resume Commands
###########################

Syntax
******
- ``{xsrst_suspend}``
- ``{xsrst_resume}``

Purpose
*******
It is possible to suspend (resume) the xsrst extraction during a section.
One begins (ends) the suspension with a suspend command (resume command)
at the
:ref:`beginning of a line<xsrst_py.notation.beginning_of_a_line>`.
Note that this will also suspend all other xsrst processing; e.g.,
spell checking.

Example
*******
{xsrst_child_list
   sphinx/test_in/suspend.py
}

{xsrst_end suspend_cmd}
"""
# ----------------------------------------------------------------------------
import re
import xsrst
#
# pattern_suspend, pattern_resume
pattern_suspend = re.compile( r'\n[ \t]*\{xsrst_suspend\}' )
pattern_resume  = re.compile( r'\n[ \t]*\{xsrst_resume\}' )
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
    # m_suspend
    m_suspend  = pattern_suspend.search(data_out)
    while m_suspend != None :
        #
        # suspend_stat, suspend_end
        suspend_start = m_suspend.start()
        suspend_end   = m_suspend.end()
        #
        # m_resume
        m_resume      = pattern_resume.search(data_out, suspend_end)
        if m_resume == None :
            msg  = 'There is a suspend command without a '
            msg += 'corresponding resume commannd.'
            xsrst.system_exit(msg,
                file_name=file_name,
                section_name=section_name,
                m_obj=m_suspend,
                data=data_out
            )
        # resume_start, resume_end
        resume_start = m_resume.start()
        resume_end   = m_resume.end()
        #
        # m_obj
        m_obj = pattern_suspend.search(data_out, suspend_end)
        if m_obj != None :
            if m_obj.start() < resume_end :
                msg  = 'There are two suspend commands without a '
                msg += 'resume command between them.'
                xsrst.system_exit(msg,
                    file_name=file_name,
                    section_name=section_name,
                    m_obj=m_obj,
                    data=data_rest
                )
        #
        # data_out
        data_tmp  = data_out[: suspend_start]
        data_tmp += data_out[resume_end : ]
        data_out  = data_tmp
        #
        # m_suspend
        m_suspend = pattern_suspend.search(data_out)
    return data_out
