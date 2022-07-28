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
#   release_notes/2022.xrst
# '
# list of files and or directories that are moved to new names
# move_paths='
#   bin/xrst.py
# '
# list of sed commands that map old file and directory names to new names.
# The characters @s, @d, @n get converted to a space, dollar sign, new line.
# move_seds='
#   s|bin/xrst.py|xrst/run_xrst.py|
# '
# list of files that get edited by the extra_seds command
# extra_files='
#   doc.xrst
#   setup.py
#   sphinx/test_out/xrst.py.rst
# '
# list of sed commands that are applied to the extra files,
# after the other sed commands in this file.
# The characters @s, @d, @n get converted to a space, dollar sign, new line.
# extra_seds='
#   s|python.-m.xrst|xrst/xrst_py.py|
# '
# ----------------------------------------------------------------------------
# Put other sed commands below here and without # at start of line
s|bin/xrst.py|python -m xrst|
s|xrst\.py|run_xrst|g
