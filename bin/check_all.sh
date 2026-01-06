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
# external_links, suppress_spell_warnings
flags=''
skip_check_copy='no'
while [ "$#" != 0 ]
do
   case "$1" in

      --skip_external_links)
      flags+=" $1"
      ;;

      --skip_check_copy)
      skip_check_copy='yes'
      ;;

      --suppress_spell_warnings)
      flags+=" $1"
      ;;

      *)
      echo "bin/check_all.sh: command line argument "$1" is not"
      echo '--skip_external_links or --suppress_spell_warnings'
      exit 1
      ;;
   esac
   #
   shift
done
#
# sed
source bin/grep_and_sed.sh
#
# typos
if which typos >& /dev/null
then
   if ! typos
   then
      echo 'check_all: see typos errors above'
      exit 1
   fi
fi
#
# check_list
check_list=$(ls bin/check_* | $sed \
   -e '/^bin[/]check_copy.sh/d' \
   -e '/^bin[/]check_xrst.sh/d' \
   -e '/^bin[/]check_all.sh/d' \
)
if [ "$skip_check_copy" == 'no' ]
then
   bin/check_copy.sh
fi
for check in $check_list
do
   echo_eval $check
done
#
# bin/check_xrst.sh
echo_eval bin/check_xrst.sh $flags
#
# tox
if [ "$flags" == '' ]
then
   tox
fi
#
echo "check_all.sh $flags: OK"
exit 0
