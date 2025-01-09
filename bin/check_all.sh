#! /usr/bin/env bash
set -e -u
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-25 Bradley M. Bell
# -----------------------------------------------------------------------------
# echo_eval
echo_eval() {
   echo $*
   eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/check_all.sh" ]
then
   echo "bin/check_all.sh: must be executed from its parent directory"
   exit 1
fi
#
# check_exteranl_links
check_external_links='yes'
if [ "$#" != 0 ]
then
   if [ "$1" == '--skip_external_links' ]
   then
      check_external_links='no'
   else
      echo 'usage: bin/check_all.sh [--skip_external_links]'
      exit 1
   fi
fi
#
# sed
source bin/grep_and_sed.sh
#
# check_list
check_list=$(ls bin/check_* | $sed \
   -e '/^bin[/]check_xrst.sh/d' \
   -e '/^bin[/]check_all.sh/d' \
)
for check in $check_list
do
   echo_eval $check
done
#
# bin/check_xrst.sh
echo_eval bin/check_xrst.sh $check_external_links
#
# tox
tox
#
if [ "$check_external_links" == 'yes' ]
then
   echo 'check_all.sh: OK'
else
   echo 'check_all.sh --skip_external_links: OK'
fi
exit 0
