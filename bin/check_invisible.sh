#! /usr/bin/env bash
set -e -u
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-22 Bradley M. Bell
# -----------------------------------------------------------------------------
if [ "$0" != "bin/check_invisible.sh" ]
then
   echo "bin/check_invisible.sh: must be executed from its parent directory"
   exit 1
fi
# ----------------------------------------------------------------------------
#
# file_list
file_list=$(
   git ls-files | sed \
      -e '/^makefile.in$/d' \
      -e '/^aspell.pwd$/d'
)
#
# check_invisible.$$
cat << EOF > check_invisible.$$
s|[ \\t][ \\t]*\$||
s| *\t|\t|g
1{/^[ \\t]*\$/d}
\${/^[ \\t]*\$/d}
EOF
#
# file
for file in $file_list
do
   sed -f check_invisible.$$ $file > temp.$$
   if ! diff $file temp.$$ > temp.2.$$
   then
      echo "original (<) invisible white space removed (>)"
      cat temp.2.$$
      res=''
      while [ "$res" != 'yes' ] && [ "$res" != 'no' ]
      do
	      read -p "Remove invisible white space in $file [yes/no] ?" res
      done
	   if [ "$res" == 'yes' ]
      then
         if [ -x $file ]
         then
            chmod +x temp.$$
         fi
         mv temp.$$ $file
      else
         rm temp.$$
      fi
   else
      rm temp.$$
   fi
done
rm check_invisible.$$
echo 'check_invisible.sh: OK'
exit 0
