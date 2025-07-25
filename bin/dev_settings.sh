# ---------------------------------------------------------------------------
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2003-25 Bradley M. Bell
# ---------------------------------------------------------------------------
# source bin/dev_settings.sh
# Sets the value of the the development tool variables for this package.
#
# Unless this is xrst.git/bin/dev_settings.sh,
# only edit the value for each of the variables, any other changes will
# be lost the next time xrst.git/bin/dev_tools.sh updates this file.
# ---------------------------------------------------------------------------
#
# Directories
# If an file name below is a directory it specifies all the
# files in the directory.
#
# spdx_license_id
# Each file, except those specified by no_copyright_list, should have a line
# that ends with the following text:
spdx_license_id='SPDX-License-Identifier: GPL-3.0-or-later'
#
# package_name
package_name='xrst'
#
# index_page_name
# is the xrst index page_name for this projects documentation.
index_page_name='user-guide'
#
# version_file_list
# The possible patterns for a latest version number are:
#     yyyymmdd or yyyy.month.day
# whee yyyymmdd is an eight decimal digit representation of the date.
# yyyy is the year (as four decimal digits yyy), month is a number
# between 1 and 12, and the day is a number between 1 and 31
# The possible patterns for a release version number are:
#     yyyy0000.release or yyyy.0.release
# where release is a number between 0 and 99.
#
# The patterns above without release are used for the master and main branches
# and corresponds to the current year, month and day.
# The patterns above with release are used for stable/* branches.
#
# The first version file of the list below must have one copy of its
# version surrounded by single or double quotes. This determines the version
# when the branch is not master or main. All occurrences of the version, in the
# files listed below, with the following forms are updated by check_version.sh:
#     $package_name-$version  or '$version' or "$version"
#
# We use tag for the version corresponding to the current stable release.
# This is (is not) the same as the current version on a stable branch
# (on the master or main branch). All occurrences of the tag, in the files
# listed below, with the following forms are updated by new_release.sh:
#     archive/$tag.tar.gz
# In addition, all occurrences of stable-yyyy and release-yyyy are updated.
version_file_list='
   pyproject.toml
   test_rst/user-guide.rst
   user/user.xrst
   xrst/run_xrst.py
'
# All the occurrences of the version in the files above are checked to see
# that they agree.
#
#
# no_copyright_list
# These files and directories do not have the spdx license id in them.
# If an entry below is a directory it specifies all the files in the directory.
# BEGIN_SORT_THIS_LINE_PLUS_2
no_copyright_list='
   .gitignore
   .readthedocs.yaml
   bin/input_files.sh
   gpl-3.0.txt
   readme.md
   test_rst
'
# END_SORT_THIS_LINE_MINUS_2
#
# invisible_and_tab_ok
# These files are not checked for invisible white space or tabs.
# If an entry below is a directory it specifies all the files in the directory.
invisible_and_tab_ok='
'
#
# check_git_commit
# These files may have automatic changes that should not be committed every time.
# Including them in this list gives the user the option to abort their changes.
check_git_commit='
'
