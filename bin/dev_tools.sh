#! /usr/bin/env bash
set -e -u
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-24 Bradley M. Bell
# -----------------------------------------------------------------------------
if [ $# != 2 ]
then
   echo 'usage: bin/devel_tools.sh directory spdx_license_id'
   echo 'Copies the current development tools from xrst.git to directory/bin'
   echo 'spdx_license_id is the SPDX-License-Identifier for files in direcory'
   exit 1
fi
directory="$1"
spdx_license_id="$2"
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
#
# sed
source bin/grep_and_sed.sh
# -----------------------------------------------------------------------------
# dev_tools
dev_tools='
   check_copy.sh
   check_invisible.sh
   check_sort.sh
   check_tab.sh
   check_version.sh
   dev_settings.sh
   git_commit.sh
   grep_and_sed.sh
   sort.sh
'
#
# xrst_directory
xrst_directory=$(pwd)
#
# check for overwriting changes
cd $directory/bin
for file in $dev_tools
do
   destination="$directory/bin/$file"
   temp=$(git ls-files $file)
   if [ "$temp" != '' ]
   then
      if ! git diff --exit-code $file
      then
         echo "$destination"
         echo 'has changes that are not checked in'
         exit 1
      fi
   fi
done
cd $xrst_directory
#
#
cat << EOF > sed.$$
s|\\(SPDX-License-Identifier:\\) GPL-3.0-or-later|\\1 $spdx_license_id|
s|^spdx_license_id=.*|spdx_license_id=$spdx_license_id|
EOF
echo "Copying the following files into $directory/bin"
echo "and setting SPDX-License-Identifier to $spdx_license_id"
for file in $dev_tools
do
   echo "bin/$file"
   destination="$directory/bin/$file"
   $sed -f sed.$$ bin/$file > $destination
done
rm sed.$$ 
# -----------------------------------------------------------------------------
echo
cat << EOF
You need to edit the settings in
   $directory/bin/dev_settings.py
Also look for SECTION THAT DEPENDS ON GIT REPOSITORY" in
   $directory/bin/check_version.sh

dev_tools.sh: OK
EOF
exit 0
