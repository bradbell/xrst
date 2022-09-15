# ----------------------------------------------------------------------------
# None of the lists below can have white space or a dollar sign in an entry.
#
# list of directories that are added to the repository by batch_edit.sh
# new_directories='
# '
# list of files that are deleted by batch_edit.sh
# delete_files='
# '
# List of files that are not edited by the sed commands in this file
# (with the possible exception of the extra_seds commands).
# The files in bin/devel.sh ignore_files are automatically in this list
# (see devel.sh for pattern matching convention).
# ignore_files='
# '
# list of files and or directories that are moved to new names
# move_paths='
# '
# list of sed commands that map old file and directory names to new names.
# The characters @s, @d, @n get converted to a space, dollar sign, new line.
# move_seds='
# '
# list of files that get edited by the extra_seds command
# extra_files='
# '
# list of sed commands that are applied to the extra files,
# after the other sed commands in this file.
# The characters @s, @d, @n get converted to a space, dollar sign, new line.
# extra_seds='
# '
# ----------------------------------------------------------------------------
# Put other sed commands below here and without # at start of line
s/get_started@this_example_file/get_started@This Example File/
s/literal_example@this_example_file/literal_example@This Example File/
s/toc_list_example@children.py_file/toc_list_example@children.py File/
s/toc_list_example@toc_list_command/toc_list_example@toc_list Command/
s/toc_list_example@this_example_file/toc_list_example@This Example File/
s/spell_example@text/spell_example@Text/
s/spell_example@spelling_file/spell_example@Spelling File/
s/spell_example@math/spell_example@Math/
s/spell_example@double_words/spell_example@Double Words/
s/spell_example@this_example_file/spell_example@This Example File/
s/suspend_example@factorial/suspend_example@Factorial/
s/suspend_example@product/suspend_example@Product/
s/suspend_example@this_example_file/suspend_example@This Example File/
s/code_example@factorial/code_example@Factorial/
s/code_example@this_example_file/code_example@This Example File/
s/comment_example@factorial/comment_example@Factorial/
s/comment_example@this_example_file/comment_example@This Example File/
s/comment_ch_example@discussion/comment_ch_example@Discussion/
s/comment_ch_example@indent/comment_ch_example@Indent/
s/comment_ch_example@this_example_file/comment_ch_example@This Example File/
s/heading_example@level_one/heading_example@Level One/
s/heading_example@level_one@level_two/heading_example@Level One@Level Two/
s/heading_example@another_level_one/heading_example@Another Level One/
s/heading_example@another_level_one@level_two/heading_example@Another Level One@Level Two/
s/heading_example@another_level_one@x/heading_example@Another Level One@x/
s/heading_example@links/heading_example@Links/
s/heading_example@linking_headings_using__ref_/heading_example@Linking Headings Using _ref_/
s/heading_example@this_example_file/heading_example@This Example File/
s/indent_example@discussion/indent_example@Discussion/
s/indent_example@this_example_file/indent_example@This Example File/
s/configure_example@this_example_file/configure_example@This Example File/
s/child_example_one@link_to_second_child/child_example_one@Link to Second Child/
s/child_example_one@this_example_file/child_example_one@This Example File/
s/child_example_two@link_to_first_child/child_example_two@Link to First Child/
s/user_guide@version_2022.9.14/user_guide@Version 2022.9.14/
s/user_guide@git_repository/user_guide@Git Repository/
s/user_guide@pip_install/user_guide@Pip Install/
s/user_guide@run_program/user_guide@Run Program/
s/user_guide@purpose/user_guide@Purpose/
s/user_guide@contents/user_guide@Contents/
s/run_xrst@syntax/run_xrst@Syntax/
s/run_xrst@sphinx_dir@preamble.rst@example/run_xrst@sphinx_dir@preamble.rst@Example/
s/run_xrst@sphinx_dir@spelling@example/run_xrst@sphinx_dir@spelling@Example/
s/run_xrst@sphinx_dir@keyword@example/run_xrst@sphinx_dir@keyword@Example/
s/run_xrst@sphinx_dir@page_rst_files/run_xrst@sphinx_dir@Page RST Files/
s/run_xrst@sphinx_dir@other_generated_files/run_xrst@sphinx_dir@Other Generated Files/
s/begin_cmd@syntax/begin_cmd@Syntax/
s/begin_cmd@page/begin_cmd@Page/
s/begin_cmd@output_file/begin_cmd@Output File/
s/begin_cmd@parent_page/begin_cmd@Parent Page/
s/toc_cmd@syntax/toc_cmd@Syntax/
s/toc_cmd@syntax@hidden/toc_cmd@Syntax@hidden/
s/toc_cmd@syntax@list/toc_cmd@Syntax@list/
s/toc_cmd@syntax@table/toc_cmd@Syntax@table/
s/toc_cmd@table_of_contents/toc_cmd@Table of Contents/
s/toc_cmd@file_names/toc_cmd@File Names/
s/toc_cmd@children/toc_cmd@Children/
s/toc_cmd@child_links/toc_cmd@Child Links/
s/toc_cmd@example/toc_cmd@Example/
s/spell_cmd@syntax/spell_cmd@Syntax/
s/spell_cmd@purpose/spell_cmd@Purpose/
s/spell_cmd@capital_letters/spell_cmd@Capital Letters/
s/spell_cmd@double_words/spell_cmd@Double Words/
s/spell_cmd@example/spell_cmd@Example/
s/suspend_cmd@syntax/suspend_cmd@Syntax/
s/suspend_cmd@purpose/suspend_cmd@Purpose/
s/suspend_cmd@example/suspend_cmd@Example/
s/code_cmd@syntax/code_cmd@Syntax/
s/code_cmd@purpose/code_cmd@Purpose/
s/code_cmd@requirements/code_cmd@Requirements/
s/code_cmd@rest_of_line/code_cmd@Rest of Line/
s/code_cmd@spell_checking/code_cmd@Spell Checking/
s/code_cmd@example/code_cmd@Example/
s/literal_cmd@syntax/literal_cmd@Syntax/
s/literal_cmd@purpose/literal_cmd@Purpose/
s/literal_cmd@white_space/literal_cmd@White Space/
s/literal_cmd@no_start_or_stop/literal_cmd@No start or stop/
s/literal_cmd@spell_checking/literal_cmd@Spell Checking/
s/literal_cmd@example/literal_cmd@Example/
s/comment_cmd@syntax/comment_cmd@Syntax/
s/comment_cmd@purpose/comment_cmd@Purpose/
s/comment_cmd@example/comment_cmd@Example/
s/comment_ch_cmd@syntax/comment_ch_cmd@Syntax/
s/comment_ch_cmd@purpose/comment_ch_cmd@Purpose/
s/comment_ch_cmd@command_location/comment_ch_cmd@Command Location/
s/comment_ch_cmd@input_stream/comment_ch_cmd@Input Stream/
s/comment_ch_cmd@example/comment_ch_cmd@Example/
s/indent@example/indent@Example/
s/heading_links@index/heading_links@Index/
s/heading_links@labels/heading_links@Labels/
s/heading_links@labels@level_zero/heading_links@Labels@Level Zero/
s/heading_links@labels@other_levels/heading_links@Labels@Other Levels/
s/heading_links@labels@conversion/heading_links@Labels@Conversion/
s/heading_links@labels@discussion/heading_links@Labels@Discussion/
s/heading_links@example/heading_links@Example/
s/wish_list@tabs/wish_list@Tabs/
