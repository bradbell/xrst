#! /bin/bash -e
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
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
if [ -e dist ]
then
   rm -r dist
fi
echo_eval python -m build
echo_eval twine upload --repository testpypi dist/*
echo 'upload.sh: OK'
exit 0