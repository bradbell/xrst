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
#   xrst/file_command.py
#   example/file.cpp
#   sphinx/test_out/file_cmd.rst
#   sphinx/test_out/file_example.rst
# '
# list of sed commands that map old file and directory names to new names.
# The characters @s, @d, @n get converted to a space, dollar sign, new line.
# move_seds='
#   s|file_command.py|literal_command.py|
#   s|file.cpp|literal.cpp|
#   s|file_cmd.rst|literal_cmd.rst|
#   s|file_example.rst|literal_example.rst|
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
s|file\.cpp|literal.cpp|g
#
s|'file_\([0-3]\)'|'literal_\1'|g
#
s|from .file_command   |from .literal_command|
s|file_command|literal_command|g
s|file_example|literal_example|g
s|file_cmd|literal_cmd|g
#
s|file command|literal command|g
s|File Command|Literal Command|g
#
