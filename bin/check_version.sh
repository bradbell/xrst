#! /usr/bin/env bash
set -e -u
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-24 Bradley M. Bell
# -----------------------------------------------------------------------------
# Begin: section that depends on the git repository that this file is in.
#
# version
version=$(
   sed -n -e '/^ *version *=/p' pyproject.toml | \
      sed -e 's|.*= *||' -e "s|'||g"
)
#
# year
year=$( echo $version | sed -e 's|\..*||' )
#
# version_file_list
# The version number in the files below is updated using the temp.sed script
version_file_list='
   pyproject.toml
   setup.py
   test_rst/user-guide.rst
   user/user.xrst
   xrst/run_xrst.py
'
#
# temp.sed
# This sed script is used to edit the files in version_file_list above.
# $version will be the proper version number when this function is called.
# $year will be the year corresponding to the version.
cat << EOF > temp.sed
#
# xrst/user.xrst
s|xrst-[0-9]\\{4\\}[.][0-9]*[.][0-9]*|xrst-$version|g
s|stable-[0-9]\\{4\\}|stable-$year|g
#
# pyproject.toml setup.py and xrst/run_xrst.py
s|version\\( *\\)= *'[0-9]\\{4\\}[.][0-9]*[.][0-9]*'|version\\1= '$version'|
EOF
#
# End: section that depends on the git repository that this file is in.
# -----------------------------------------------------------------------------
if [ $# != 0 ]
then
   echo 'bin/check_version.sh: does not expect any arguments'
   exit 1
fi
if [ "$0" != 'bin/check_version.sh' ]
then
   echo 'bin/check_version.sh: must be executed from its parent directory'
   exit 1
fi
if [ ! -e './.git' ]
then
   echo 'bin/check_version.sh: cannot find ./.git'
   exit 1
fi
# -----------------------------------------------------------------------------
#
# check_version
check_version() {
   sed "$1" -f temp.sed > temp.out
   if ! diff "$1" temp.out
   then
      version_ok='no'
      #
      if [ -x "$1" ]
      then
         mv temp.out "$1"
         chmod +x "$1"
      else
         mv temp.out "$1"
      fi
   fi
}
# branch
branch=$(git branch | sed -n -e '/^[*]/p' | sed -e 's|^[*] *||')
#
# version
if [ "$branch" == 'master' ]
then
   version=$(date +%Y.%m.%d | sed -e 's|\.0*|.|g')
fi
if echo $branch | grep '^stable/' > /dev/null
then
   if ! echo $version | grep '[0-9]\{4\}[.]0[.]' > /dev/null
   then
      echo 'check_version.sh: stable version does not begin with yyyy.0.'
      exit 1
   fi
fi
#
# version_ok
version_ok='yes'
#
# check_version
for file in $version_file_list
do
   check_version $file
done
#
# ----------------------------------------------------------------------------
if [ "$version_ok" == 'no' ]
then
   echo 'bin/check_version.sh: version numbers were fixed (see above).'
   echo "Re-execute bin/check_version.sh $version ?"
   exit 1
fi
echo 'check_version.sh OK'
exit 0
