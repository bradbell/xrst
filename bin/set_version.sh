#! /bin/bash -e
# -----------------------------------------------------------------------------
#                      xrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
    echo $*
    eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/set_version.sh" ]
then
    echo "bin/set_version.sh: must be executed from its parent directory"
    exit 1
fi
# -----------------------------------------------------------------------------
version=$(date +%G.%m.%d | sed -e 's|\.0|.|')
cat << EOF > temp.sed
s|^version *= *'[0-9]*[.][0-9]*[.][0-9]*' *\$|version = '$version'|
s|^Version *[0-9]*[.][0-9]*[.][0-9]* *\$|Version $version|
EOF
file_list='
    doc.xrst
    pyproject.toml
'
for file in $file_list
do
    echo "diff $file"
    sed -f temp.sed $file > temp.out
    if ! diff $file temp.out
    then
        mv temp.out $file
    else
        rm temp.out
    fi
done
# -----------------------------------------------------------------------------
echo "$0: OK"
exit 0
