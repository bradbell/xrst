#! /usr/bin/env bash
set -e -u
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-25 Bradley M. Bell
# -----------------------------------------------------------------------------
if [ $# != 1 ] && [ $# != 2 ]
then
cat << EOF
usage: bin/devel_tools.sh dest_repo [spdx_license_id]
Copies the current development tools from xrst.git/bin to dest_repo/bin

spdx_license_id is the SPDX-License-Identifier for files in this package.
If spdx_license_id is not present, and dest_repo/bin/dev_settings.sh exists,
the value of spdx_license_id for this package is printed. 
EOF
   exit 1
fi
dest_repo="$1"
if [ $# == 1 ]
then
   file="$dest_repo/bin/dev_settings.sh"
   if [ ! -e $file ]
   then
      echo "dev_tools.sh: can not find $file"
      exit 1
   fi

   source $dest_repo/bin/dev_settings.sh
   echo "spdx_license_id = '$spdx_license_id'"
   exit 0
fi
spdx_license_id="$2"
if [ ! -d "$dest_repo/.git" ]
then
   echo "dev_tools.sh: $dest_repo is not a git repository"
   exit 1
fi
if [ ! -d "$dest_repo/bin" ]
then
   echo "dev_tools.sh: $dest_repo/bin is not a diretory"
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
   new_release.sh
   sort.sh
'
for file in $dev_tools
do
   if [ $file == dev_settings.sh ] || [ $file == grep_and_sed.sh ]
   then
      if [ -x bin/$file ]
      then
         echo "bin/$file is executable"
         exit 1
      fi
   else
      line_two=$($sed -n -e '2,2p' bin/$file)
      if [ "$line_two" != 'set -e -u' ]
      then
         echo "Line 2 of bin/$file is not equal to:"
         echo 'set -e -u'
         exit 1
      fi
   fi
done
#
# xrst_repo
xrst_repo=$(pwd)
#
# dest_repo
cd $dest_repo
#
# sed.$$
cat << EOF > sed.$$
s|\\(SPDX-License-Identifier:\\) GPL-3.0-or-later|\\1 $spdx_license_id|
s|^spdx_license_id=.*|spdx_license_id='$spdx_license_id'|
EOF
#
# check for overwriting changes
for file in $dev_tools
do
   dest_path="$dest_repo/bin/$file"
   xrst_path="$xrst_repo/bin/$file"
   $sed -f sed.$$ $xrst_path > temp.$$
   if [ -e $dest_path ]
   then
      if ! diff $dest_path temp.$$ > /dev/null
      then
         temp=$(git ls-files bin/$file)
         if [ "$temp" == '' ]
         then
            echo "$dest_path"
            echo 'not in repository and has changes that would be overwritten'
            rm temp.$$
            rm sed.$$
            exit 1
         else
            if ! git diff --exit-code bin/$file > /dev/null
            then
               echo "$dest_path"
               echo 'is in repository and has changes that are not checked in'
               rm temp.$$
               rm sed.$$
               exit 1
            fi
         fi
      fi
   fi
done
rm temp.$$
#
# package_name, version_file_list
package_name=''
version_file_list=''
if [ -e $dest_repo/bin/dev_settings.sh ]
then
   source $dest_repo/bin/dev_settings.sh
fi
#
# $des_repo/bin/*.sh
echo "Copying the following development tools into $dest_repo/bin"
echo "and setting SPDX-License-Identifier to $spdx_license_id"
for file in $dev_tools
do
   echo "bin/$file"
   dest_path="$dest_repo/bin/$file"
   xrst_path="$xrst_repo/bin/$file"
   $sed -f sed.$$ $xrst_path > $dest_path
   if [ -x "$xrst_path" ]
   then
      chmod +x $dest_path
   fi
done
#
#
# $dest_repo/bin/dev_settings.sh
cat << EOF > sed.$$
/^version_file_list=' *$/! b one
: loop_1
N
/\\n' *$/! b loop_1
s|.*|@version_file_list@|
#
: one
/^no_copyright_list=' *$/! b two
: loop_2
N
/\\n' *$/! b loop_2
s|.*|@no_copyright_list@|
#
: two
/^invisible_and_tab_ok=' *$/! b three
: loop_3
N
/\\n' *$/! b loop_3
s|.*|@invisible_and_tab_ok@|
#
: three
/^check_commit=' *$/! b four
: loop_4
N
/\\n' *$/! b loop_4
s|.*|@check_commit@|
#
: four
EOF
sed -i $dest_repo/bin/dev_settings.sh -f sed.$$
rm sed.$$
#
# $dest_repo/bin/dev_settings.sh
$sed -i $dest_repo/bin/dev_settings.sh \
   -e "s|^package_name=.*|package_name='$package_name'|"
for variable in \
   version_file_list \
   no_copyright_list \
   invisible_and_tab_ok \
   check_commit
do
   if [ -z ${variable+x} ]
   then
      replace=''
   else
      replace=$(echo ${!variable} | $sed -e 's|[ \n]|\\n   |g' -e 's|^|   |')
   fi
   if [[ "$replace" =~ ^\s*$ ]]
   then
      $sed -i $dest_repo/bin/dev_settings.sh \
         -e "s|@$variable@|$variable='\n'|"
   else
      $sed -i $dest_repo/bin/dev_settings.sh \
         -e "s|@$variable@|$variable='\n$replace\n'|"
   fi
done
# -----------------------------------------------------------------------------
echo
cat << EOF
Check the folloiwing file for empty variables that need to be defined:
   $dest_repo/bin/dev_settings.sh

See the comments at the top of each development tool from a description
of how to use it.

dev_tools.sh: OK
EOF
exit 0
