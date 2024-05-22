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
   git_commit.sh
   check_version.sh
   check_copy.sh
'
echo
echo "copy following files into $directory/bin:"
echo $dev_tools
for file in $dev_tools
do
   cp bin/$file $directory/bin/$file
done
# -----------------------------------------------------------------------------
echo
echo 'Look for: "SECTION THAT DEPENDS ON GIT REPOSITORY" in'
echo 'check_version.sh and check_copy.sh'
echo 'dev_tools.sh: OK'
exit 0
