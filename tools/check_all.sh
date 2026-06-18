#! /usr/bin/env bash
set -e -u
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-26 Bradley M. Bell
# -----------------------------------------------------------------------------
# echo_eval
echo_eval() {
    echo $*
    eval $*
}
# -----------------------------------------------------------------------------
if [ ! -e 'tools/check_all.sh' ]
then
    echo "tools/check_all.sh: must be executed from its parent directory"
    exit 1
fi
#
# flags, skip_check_copy
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
        echo "tools/check_all.sh: "$1" is not one of the following"
        echo '--skip_external_links'
        echo '--skip_check_copy'
        echo '--suppress_spell_warnings'
        exit 1
        ;;

    esac
    #
    shift
done
#
# sed
source tools/grep_and_sed.sh
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
check_list=$(ls tools/check_* | $sed \
    -e '/^tools[/]check_copy.sh/d' \
    -e '/^tools[/]check_xrst.sh/d' \
    -e '/^tools[/]check_all.sh/d' \
)
if [ "$skip_check_copy" == 'no' ]
then
    tools/check_copy.sh
fi
for check in $check_list
do
    echo_eval $check
done
#
# tools/check_xrst.sh
echo_eval tools/check_xrst.sh $flags
#
# tox
if [ "$flags" == '' ]
then
    tox
fi
#
echo "check_all.sh $flags: OK"
exit 0
