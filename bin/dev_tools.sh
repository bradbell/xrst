#! /usr/bin/env bash
set -e -u
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-24 Bradley M. Bell
# -----------------------------------------------------------------------------
if [ $# != 1 ]
then
   echo 'usage: bin/devel_tools.sh directory'
   echo 'copies the current development tools from xrst.git to directory/bin'
   exit 1
fi
directory="$1"
if [ ! -d "$directory/.git" ]
then
   echo "dev_tools.sh: $directory is not a git repository"
   exit 1
fi
if [ ! -d "$directory/bin" ]
then
   echo "dev_tools.sh: $directory/bin is not a diretory"
   exit 1
fi
# -----------------------------------------------------------------------------
dev_tools='
   check_copy.sh
   check_invisible.sh
   check_tab.sh
   check_version.sh
   git_commit.sh
   grep_and_sed.sh
'
echo
echo "copying the following files into $directory/bin:"
echo $dev_tools
for file in $dev_tools
do
   destination="$directory/bin/$file"
   if [ -e "$destination" ]
   then
      res=''
      while [ "$res" != yes ] and [ "$res" != no ]
      do
         read -p "$destination exists, overwrite it [yes/no] ?" res
      done
      if [ "$res" == 'yes' ]
      then
         cp bin/$file $destination
      fi
   else
      cp bin/$file $destination
   fi
done
# -----------------------------------------------------------------------------
echo
cat << EOF
You need to Edit the settings in
   $directory/bin/dev_settings.py
Also look for SECTION THAT DEPENDS ON GIT REPOSITORY" in
   $directory/bin/check_version.sh

dev_tools.sh: OK
EOF
exit 0
