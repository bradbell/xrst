#! /bin/bash -e
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-23 Bradley M. Bell
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
   echo $*
   eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/upload.sh" ]
then
   echo "bin/upload.sh: must be executed from its parent directory"
   exit 1
fi
if [ "$PASSWORD" == '' ]
then
   echo 'bin/upload.sh: Must set PASSWORD environment variable before running'
   exit 1
fi
if [ -e dist ]
then
   rm -r dist
fi
echo_eval python -m build
echo_eval twine upload dist/* -u$USER -p$PASSWORD
echo 'upload.sh: OK'
exit 0
