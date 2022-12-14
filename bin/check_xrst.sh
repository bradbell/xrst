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
# run from html directory so that project_directory is not working directory
if [ ! -e build ]
then
   mkdir build
fi
cd    build
#
# ./xrst.toml
sed -e "s|^project_directory *=.*|project_directory = '..'|"  \
   ../xrst.toml > xrst.toml
#
for group_list in 'default' 'default user dev'
do
   if [ -e rst ]
   then
      echo_eval rm -r rst
   fi
   args='--local_toc'
   if [ "$group_list" == 'default' ]
   then
      args="$args --config_file ../xrst.toml"
   else
      args="$args --config_file xrst.toml"
   fi
   args="$args --group_list $group_list"
   args="$args --html_theme sphinx_rtd_theme"
   echo "python -m xrst $args"
   if ! python -m xrst $args 2> check_xrst.$$
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
file_list=$(ls build/rst/*.rst | sed -e 's|^build/rst/||' )
for file in $file_list
do
   if [ ! -e test_rst/$file ]
   then
      echo "The output file test_rst/$file does not exist."
      echo 'Should we use the following command to fix this'
      echo "    cp build/rst/$file test_rst/$file"
      continue_yes_no
      cp build/rst/$file test_rst/$file
   elif ! diff build/rst/$file test_rst/$file
   then
      echo "build/rst/$file changed; above is output of"
      echo "    diff build/rst/$file test_rst/$file"
      echo 'Should we use the following command to fix this'
      echo "    cp build/rst/$file test_rst/$file"
      continue_yes_no
      cp build/rst/$file test_rst/$file
   else
      echo "$file: OK"
   fi
done
# -----------------------------------------------------------------------------
file_list=$(ls test_rst/*.rst | sed -e 's|^test_rst/||' )
for file in $file_list
do
   if [ ! -e build/rst/$file ]
   then
      echo "The output file build/rst/$file does not exist."
      echo 'Should we use the following command to fix this'
      echo "    git rm -f test_rst/$file"
      continue_yes_no
      git rm -f test_rst/$file
   fi
done
# -----------------------------------------------------------------------------
echo "$0: OK"
exit 0
