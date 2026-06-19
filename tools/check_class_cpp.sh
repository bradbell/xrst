#! /usr/bin/env bash
set -e -u
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-26 Bradley M. Bell
# -----------------------------------------------------------------------------
# script_path
script_dir="$( dirname -- "${BASH_SOURCE[0]}" )"
script_dir="$( cd -- "$script_dir" &> /dev/null && pwd )"
script_path="$script_dir/$(basename $0)"
#
# bash function that echos and executes a command
echo_eval() {
    echo $*
    eval $*
}
# -----------------------------------------------------------------------------
if [ ! -e 'tools/check_class_cpp.sh' ]
then
    echo "tools/check_class_cpp.sh: must be executed from its parent directory"
    exit 1
fi
if [ ! -e build ]
then
    mkdir build
fi
echo_eval g++ example/class.cpp -o build/class
if ! build/class
then
    echo 'check_cpass_cpp.sh: Error'
    exit 1
fi
echo "$script_path: OK"
exit 0
