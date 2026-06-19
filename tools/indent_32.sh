#! /usr/bin/env bash
set -e -u
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2023-26 Bradley M. Bell
# ----------------------------------------------------------------------------
# script_path
script_dir="$( dirname -- "${BASH_SOURCE[0]}" )"
script_dir="$( cd -- "$script_dir" &> /dev/null && pwd )"
script_path="$script_dir/$(basename $0)"
#
if [ ! -e 'tools/indent_32.sh' ]
then
  echo "tools/indent_32.sh: must be executed from its parent directory"
  exit 1
fi
if [ "$#" != 0 ]
then
  echo 'indent_32 does not expect any arguments'
  exit 1
fi
#! /usr/bin/env bash
set -e -u
git reset --hard
for file in $(git ls-files )
do
    if [[ "$file" =~ test_rst/.* ]]
    then
        echo "skip $file"
    else
        echo "process $file"
        ext=$(echo $file | sed -e 's|.*[.]|.|')
        #
        if [ "$ext" != '.yml' ] \
        && [ "$ext" != '.yaml' ] \
        && [ "$ext" != '.png' ] \
        && [ "$ext" != '.xml' ] \
        && [ "$ext" != "$file" ]
        then
            if ! indent_32.py $file
            then
                echo "error: $file"
                exit 1
            fi
        fi
    fi
done
for file in $(git ls-files test_rst)
do
    ext=$(echo $file | sed -e 's|.*[.]\([^.]*\).rst|.\1|')
    #
    if [ "$ext" != '.yaml' ]
    then
        if ! rst_32.py $file
        then
            echo "error: $file"
            exit 1
        fi
    fi
done
#
echo 'Use tools/check_xrst.sh to see if indent_32.py and rst_32.py work.'
echo "$script_path: OK"
exit 0
