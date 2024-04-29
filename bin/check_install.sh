#! /usr/bin/env bash
set -e -u
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-24 Bradley M. Bell
# -----------------------------------------------------------------------------
if [ "$0" != "bin/check_install.sh" ]
then
   echo "bin/check_install.sh: must be executed from its parent directory"
   exit 1
fi
# -----------------------------------------------------------------------------
#
# prefix
prefix="$(pwd)/build/prefix"
#
# run_xrst
run_xrst="^ *python_executable, '-m', 'xrst',\$"
#
# run_xrst
run_xrst="      python_executable, '-m', 'xrst',"
#
# test_driver
test_driver='pytest/test_rst.py'
if ! grep "$run_xrst" $test_driver > /dev/null
then
   echo "bin/check_install.sh: cannot fine following in $test_driver"
   echo $run_xrst
   exit 1
fi
#
# install
pip install --prefix=$prefix .
#
# PYTHONPATH
count=$(find $prefix -name 'site-packages' | wc -l)
if [ "$count" != 1 ]
then
   echo "check_install.sh: $count site-packages below $prefix"
   find $prefix -name 'site-packages'
   exit 1
fi
site_packages="$(find $prefix -name 'site-packages')"
if [ -z "${PYTHONPATH+x}" ]
then
   PYTHONPATH="$site_packages"
elif [ "$PYTHONPATH" == '' ]
then
   PYTHONPATH="$site_packages"
else
   PYTHONPATH="$site_packages:$PYTHONPATH"
fi
#
# test_driver
# Using prefix runs the installed and not the source version of xrst
sed -i \
   -e  "s|$run_xrst|'$prefix/bin/xrst', '--suppress_spell_warnings', |" \
   $test_driver
#
# pytest
pytest -s pytest
#
# test_driver
sed -i \
   -e  "s|'$prefix/bin/xrst', '--suppress_spell_warnings', |$run_xrst|" \
   $test_driver
#
# -----------------------------------------------------------------------------
echo 'check_install.sh: OK'
exit 0
