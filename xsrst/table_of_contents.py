# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
import xsrst
#
# Create the table of contents and replace the '{xsrst_section_number}'
# for this section and all its child sections.
#
# tmp_dir
# is the temporary directory whre the rst files are written.
#
# target:
# is either 'html' or 'pdf'. If target is 'pdf',  in the file
# tmp_dir/section_name.rst the text {xsrst_section_number}
# is replaced by the section number which includes the counter for each level.
# If target is 'html', {xsrst_section_number} is removed with not replacement.
#
# level:
# is the level for this section in the table of contents. This is positive
# and level one corresponds the the top level (root of the tree).
# If it is one, this is the first section; i.e, section_index = 0.
#
# count:
# is a list with length level-1 that contains the count of the number of
# sections that come before this section at level-1 and each level above
# this level. Each element of this list is an int.
#
# section_index:
# is the index of this section in section_info
#
# section_info:
# is a list with length equal to the number of sections.
# The value section[section_index] is a dictionary for this seciton
# with the following key, value pairs (all the keys are strings:
# key            value
# section_name   a str continaing the name of this section.
# section_title  a str containing the title for this section.
# parent_section an int index in section_info for the parent of this section.
#
# content:
# The return content is the table of contents entries for this section
# and all the sections below this section.
#
# content =
def table_of_contents(
    tmp_dir, target, section_info, level, count, section_index
) :
    assert type(target) == str
    assert type(tmp_dir) == str
    assert type(level) == int
    assert type(count) == list
    assert type(section_index) == int
    assert type( section_info[section_index] ) == dict
    #
    assert target in [ 'html', 'pdf']
    assert level >= 1
    assert len(count) == level-1
    #
    # section_name, section_title, parent_section
    section_name   = section_info[section_index]['section_name']
    section_title  = section_info[section_index]['section_title']
    #
    # content, section_number
    if level == 1 :
        assert section_index == 0
        content  = '\n.. _xsrst_table_of_contents:\n\n'
        content += 'Table of Contents\n'
        content += '*****************\n'
        content += ':ref:`' + section_name + '`\n\n'
        section_number = ''
    else :
        assert section_index != 0
        assert type( count[level-2] ) == int
        content  = '| '
        for i in range(level - 2 ) :
            content += ' |space| '
        section_number = ''
        for i in range(level - 1) :
            section_number += str(count[i])
            if i + 1 < level - 1 :
                section_number += '.'
        content  += f':ref:`{section_number}<{section_name}>` '
        content  += section_title + '\n'
    #
    # replace {xsrst_section_number} in tmp_dir/section_name.rst
    file_name = tmp_dir + '/' + section_name + '.rst'
    file_ptr  = open(file_name, 'r')
    file_data = file_ptr.read()
    file_ptr.close()
    if target == 'pdf' :
        file_data = xsrst.replace_section_number(file_data, section_number)
    else :
        file_data = xsrst.replace_section_number(file_data, '')
    file_ptr  = open(file_name, 'w')
    file_ptr.write(file_data)
    file_ptr.close()
    #
    # in_parent_file_list, in_child_cmd_list
    in_parent_file_list = list()
    in_child_cmd_list   = list()
    for child_index in range( len( section_info ) ) :
        if section_info[child_index]['parent_section'] == section_index :
            if section_info[child_index]['in_parent_file'] :
                in_parent_file_list.append(child_index)
            else :
                in_child_cmd_list.append(child_index)
    #
    # child_count, child_content
    child_count   = count + [0]
    child_content = ''
    for child_index in in_child_cmd_list + in_parent_file_list :
        #
        # child_index corresponds to a child of this section
        child_count[-1] += 1
        child_content += table_of_contents(
            tmp_dir, target, section_info, level + 1, child_count, child_index
        )
    #
    # child_content
    # if the number of children greater than one, put a blank line before
    # and after the child table of contents
    number_children = child_count[-1]
    if 1 < number_children :
        if not child_content.startswith('|\n') :
            child_content = '|\n' + child_content
        if not child_content.endswith('|\n') :
            child_content = child_content + '|\n'
    #
    # content
    content += child_content
    return content
