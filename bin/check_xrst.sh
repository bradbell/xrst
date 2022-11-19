#! /bin/bash -e
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
# bash function that echos and executes a command
function echo_eval {
   echo $*
   eval $*
}
# -----------------------------------------------------------------------------
# bash funciton that prompts [yes/no] and returns (exits 1) on yes (no)
function continue_yes_no {
   read -p '[yes/no] ? ' response
   while [ "$response" != 'yes' ] && [ "$response" != 'no' ]
   do
      echo "response = '$response' is not yes or no"
      read -p '[yes/no] ? ' response
   done
   if [ "$response" == 'no' ]
      then exit 1
   fi
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/check_xrst.sh" ]
then
   echo "bin/check_xrst.sh: must be executed from its parent directory"
   exit 1
fi
PYTHONPATH="$PYTHONPATH:$(pwd)"
# -----------------------------------------------------------------------------
# html
# run from html directory so that root_directory is not working directory
if [ -e html ]
then
   rm -r html
fi
mkdir html
cd    html
#
for group_list in ',' ',user,dev'
do
   if [ -e ../rst ]
   then
      echo_eval rm -r ../rst
   fi
   args="--group $group_list --html sphinx_rtd_theme"
   echo "python -m xrst ../xrst.xrst $args"
   if ! python -m xrst ../xrst.xrst $args 2> check_xrst.$$
   then
      type_error='error'
   else
      type_error='warning'
   fi
   if [ -s check_xrst.$$ ]
   then
      cat check_xrst.$$
      rm check_xrst.$$
      echo "$0: exiting due to $type_error above"
      exit 1
   fi
done
rm check_xrst.$$
cd ..
# -----------------------------------------------------------------------------
file_list=$(ls rst/*.rst | sed -e "s|^rst/||" )
for file in $file_list
do
   if [ ! -e test_rst/$file ]
   then
      echo "The output file test_rst/$file does not exist."
      echo 'Should we use the following command to fix this'
      echo "    cp rst/$file test_rst/$file"
      continue_yes_no
      cp rst/$file test_rst/$file
   elif ! diff rst/$file test_rst/$file
   then
      echo "rst/$file changed; above is output of"
      echo "    diff rst/$file test_rst/$file"
      echo 'Should we use the following command to fix this'
      echo "    cp rst/$file test_rst/$file"
      continue_yes_no
      cp rst/$file test_rst/$file
   else
      echo "$file: OK"
   fi
done
# -----------------------------------------------------------------------------
file_list=$(ls test_rst/*.rst | sed -e 's|^test_rst/||' )
for file in $file_list
do
   if [ ! -e rst/$file ]
   then
      echo "The output file rst/$file does not exist."
      echo 'Should we use the following command to fix this'
      echo "    git rm -f test_rst/$file"
      continue_yes_no
      git rm -f test_rst/$file
   fi
done
# -----------------------------------------------------------------------------
echo "$0: OK"
exit 0
