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
#   bin/update_xrst.py
# '
# list of files and or directories that are moved to new names
# move_paths='
#   xrst/child_commands.py
#   example/child_list.xrst
#   sphinx/test_out/child_cmd.rst
#   sphinx/test_out/child_list_example.rst
# '
# list of sed commands that map old file and directory names to new names.
# The characters @s, @d, @n get converted to a space, dollar sign, new line.
# move_seds='
#   s|child_commands.py|toc_commands.py|
#   s|child_list.xrst|toc_list.xrst|
#   s|child_cmd.rst|toc_cmd.rst|
#   s|child_list_example.rst|toc_list_example.rst|
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
s|child_list|toc_list|g
s|child_cmd|toc_cmd|g
s|child command|toc command|
s|from \.child_commands|from .toc_commands  |g
s|child_commands|toc_commands|g
