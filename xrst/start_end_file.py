# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-26 Bradley M. Bell
# ----------------------------------------------------------------------------
import xrst
import re
# ----------------------------------------------------------------------------
def number_dedent(display_data, dedent) :
    lines    = display_data.split('\n')
    n_dedent = None
    for line in lines :
        n_space = 0
        while n_space < len(line) and line[n_space] == ' ' :
            n_space += 1
        if n_space < len(line) :
            if n_dedent == None :
                n_dedent = n_space
                if n_space + len(dedent) < len(line) :
                    if line[n_space : n_space + len(dedent)] == dedent :
                        n_dedent = n_space + len(dedent) + 1
            else :
                n_check = n_space
                if n_space + len(dedent) < len(line) :
                    if line[n_space : n_space + len(dedent)] == dedent :
                        n_check = n_space + len(dedent) + 1
                if n_check != n_dedent :
                    return None
    if n_dedent == None :
        n_dedent = 0
    return n_dedent
# ----------------------------------------------------------------------------
#
# {xrst_begin start_end_file dev}
# {xrst_spell
#   cmd
#   dedent
# }
# {xrst_comment_ch #}
#
# Convert literal command start, end from text to line numbers
# ############################################################
#
# Prototype
# *********
# {xrst_literal ,
#    # BEGIN_DEF, # END_DEF
#    # BEGIN_RETURN, # END_RETURN
# }
#
# page_file
# *********
# is the name of the file that contains the begin command for this page.
# This is different from the current input file if we are processing
# a template expansion.
#
# page_name
# *********
# is the name of the page where the xrst_literal command appears.
#
# input_file
# **********
# is the name of the file where the xrst_literal command appears.
# This is different for *page_file* when the command appears in a
# template expansion.
#
# display_file
# ************
# is the name of the file that we are displaying. If it is not the same as
# input_file, then it must have appeared in the xrst_literal command.
#
# cmd_line
# ********
# If input_file is equal to display_file, the lines of the file
# between line numbers cmd_line[0] and cmd_line[1] inclusive
# are in the xrst_literal command and are excluded from the search.
#
# start_after
# ***********
# is the starting text. There must be one and only one copy of this text in the
# file (not counting the excluded text). This text has no newlines and cannot
# be empty.  If not, an the error is reported and the program stops.
#
# end_before
# **********
# is the stopping text. There must be one and only one copy of this text in the
# file (not counting the excluded text). This text has no newlines and cannot
# be empty.  Furthermore, the stopping text must come after the end of the
# starting text. If not, an the error is reported and the program stops.
#
# start_line
# **********
# is the line number where start_after appears.
#
# end_line
# ********
# is the line number where end_before appears.
#
# m_start
# *******
# is a match object corresponding to the location of start_after.
# It is only used for reporting errors.
#
# m_end
# *****
# is a match object corresponding to the location of end_before.
# It is only used for reporting errors.
#
# m_data
# ******
# is the data for the entire page, including template expansion.
# It corresponds to *m_start* , *m_end* and is only used for reporting errors.
#
# dedent
# ******
# see :ref:`literal_cmd@dedent` .
# The value dedent == '' is used for dedent not present in the command.
#
# {xrst_end start_end_file}
# BEGIN_DEF
def start_end_file(
    page_file,
    page_name,
    input_file,
    display_file,
    cmd_line,
    start_after,
    end_before,
    m_start,
    m_end,
    m_data,
    dedent,
) :
    assert type(page_file) == str
    assert type(page_name) == str
    assert type(input_file) == str
    assert type(display_file) == str
    assert type(cmd_line[0]) == int
    assert type(cmd_line[1]) == int
    assert cmd_line[0] <= cmd_line[1]
    assert type(start_after) == str
    assert type(end_before) == str
    assert type(m_start) == re.Match
    assert type(m_end) == re.Match
    assert type(m_data) == str
    assert type(dedent) == str
    # END_DEF
    # ------------------------------------------------------------------------
    # exclude_line
    if input_file == display_file :
        exclude_line = cmd_line
    else :
        exclude_line = (0, 0)
    #
    # msg
    msg  = f'in literal command:'
    #
    if start_after == '' :
        msg += ' start_after is empty'
        xrst.system_exit(msg, file_name=page_file, page_name=page_name,
            m_obj = m_start, data = m_data
        )
    if end_before == '' :
        msg += ' end_before is empty'
        xrst.system_exit(msg, file_name=page_file, page_name=page_name,
            m_obj = m_end, data = m_data
        )
    if 0 <= start_after.find('\n') :
        msg += ' a newline appears in start_after'
        xrst.system_exit(msg, file_name=page_file, page_name=page_name,
            m_obj = m_start, data = m_data
        )
    if 0 <= end_before.find('\n') :
        msg += ' a newline appears in end_before'
        xrst.system_exit(msg, file_name=page_file, page_name=page_name,
            m_obj = m_end, data = m_data
        )
    #
    # data
    file_obj  = open(display_file, 'r')
    data      = file_obj.read()
    file_obj.close()
    #
    # start_index, start_line
    start_try = data.find(start_after)
    count     = 0
    while 0 <= start_try :
        line = data[: start_try].count('\n') + 1
        if  line < exclude_line[0] or exclude_line[1] < line :
            start_index = data.find('\n', start_try + len(start_after))
            start_line  = line
            count       = count + 1
        start_try = data.find(start_after, start_try + len(start_after) )
    if count != 1 :
        msg += f'\nstart_after   =  {start_after}'
        msg += f'\ndisplay_file  =  {display_file}'
        msg += f'\nfound {count} matches expected 1'
        if input_file == display_file :
            msg += ' not counting the literal command'
        xrst.system_exit(msg, file_name=page_file, page_name=page_name,
            m_obj = m_start, data = m_data
        )
    #
    # end_index, end_line
    end_try = data.find(end_before)
    count   = 0
    while 0 <= end_try :
        line = data[: end_try].count('\n') + 1
        if  line < exclude_line[0] or exclude_line[1] < line :
            end_index = end_try
            while 0 < end_index and data[end_index] != '\n' :
                end_index -= 1
            end_line  = line
            count     = count + 1
        end_try = data.find(end_before, end_try + len(end_before) )
    if count != 1 :
        msg += f'\nend_before   =  {end_before}'
        msg += f'\ndisplay_file =  {display_file}'
        msg += f'\nfound {count} matches expected 1'
        if input_file == display_file :
            msg += ' not counting the literal command'
        xrst.system_exit(msg, file_name=page_file, page_name=page_name,
            m_obj = m_end, data = m_data
        )
    # ------------------------------------------------------------------------
    # n_dedent
    n_dedent = 0
    if dedent != '' :
        #
        # display_data
        assert 0 <= start_index
        assert start_index <= end_index
        if start_index == end_index:
            display_data = ''
        else :
            assert start_index < end_index
            assert end_index < len(data)
            display_data = data[start_index + 1: end_index ]
            n_dedent     = number_dedent(display_data, dedent)
            if n_dedent == None :
                msg += f' dedent = {dedent}'
                msg += f'\nstart_after   =  {start_after}'
                msg += f'\nend_before    =  {end_before}'
                msg += f'\ndisplay_file  =  {display_file}'
                msg += '\nNumber of characters to dedent not the same '
                msg += 'for all lines'
                xrst.system_exit(msg, file_name=page_file, page_name=page_name,
                    m_obj = m_end, data = m_data
                )
    # ------------------------------------------------------------------------
    # BEGIN_RETURN
    #
    assert type(start_line) == int
    assert type(end_line) == int
    assert type(n_dedent) == int
    return start_line, end_line, n_dedent
    # END_RETURN
