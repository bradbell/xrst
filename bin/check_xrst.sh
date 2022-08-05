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
if [ "$0" != "bin/check_xrst.sh" ]
then
    echo "bin/check_xrst.sh: must be executed from its parent directory"
    exit 1
fi
# -----------------------------------------------------------------------------
if [ -e doc ]
then
    echo_eval rm -r doc
fi
PYTHONPATH="$PYTHONPATH:$(pwd)"
# -----------------------------------------------------------------------------
# start_group_list
#
echo "python -m xrst doc.xrst -g start"
if ! python -m xrst doc.xrst -g start 2> check_xrst.$$
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
start_group_list=$(ls sphinx/rst/*.rst | sed -e "s|^sphinx/rst/||" )
echo "start_group_list=$start_group_list"
rm -r sphinx/rst
# -----------------------------------------------------------------------------
# change directory to test case where root_directory is not working directory
mkdir doc
cd    doc
echo "python -m xrst ../doc.xrst"
if ! python -m xrst ../doc.xrst 2> ../check_xrst.$$
then
    type_error='error'
else
    type_error='warning'
fi
cd ..
# -----------------------------------------------------------------------------
if [ -s check_xrst.$$ ]
then
    cat check_xrst.$$
    rm check_xrst.$$
    echo "$0: exiting due to $type_error above"
    exit 1
fi
rm check_xrst.$$
# -----------------------------------------------------------------------------
file_list=$(ls sphinx/rst/*.rst | sed -e "s|^sphinx/rst/||" )
for file in $file_list
do
    for start_file in start_group_list
    do
        if [ "$file" == "$start_file" ]
        then
            echo "The output file sphinx/rst/$file"
            echo 'is in both the empty group and start group builds'
            exit 1
        fi
    done
    if [ ! -e sphinx/test_out/$file ]
    then
        echo "The output file sphinx/test_out/$file does not exist."
        echo 'Should we use the following command to fix this'
        echo "    cp sphinx/rst/$file sphinx/test_out/$file"
        read -p '[yes/no] ?' response
        if [ "$response" != 'yes' ]
            then exit 1
        fi
        cp sphinx/rst/$file sphinx/test_out/$file
    elif ! diff sphinx/rst/$file sphinx/test_out/$file
    then
        echo "sphinx/rst/$file changed; above is output of"
        echo "    diff sphinx/rst/$file sphinx/test_out/$file"
        echo 'Should we use the following command to fix this'
        echo "    cp sphinx/rst/$file sphinx/test_out/$file"
        read -p '[yes/no] ?' response
        if [ "$response" != 'yes' ]
            then exit 1
        fi
        cp sphinx/rst/$file sphinx/test_out/$file
    else
        echo "$file: OK"
    fi
done
# -----------------------------------------------------------------------------
file_list=$(ls sphinx/test_out/*.rst | sed -e 's|^sphinx/test_out/||' )
for file in $file_list
do
    if [ ! -e sphinx/rst/$file ]
    then
        echo "The output file sphinx/rst/$file does not exist."
        echo 'Should we use the following command to fix this'
        echo "    git rm -f sphinx/test_out/$file"
        read -p '[yes/no] ?' response
        if [ "$response" != 'yes' ]
            then exit 1
        fi
        git rm -f sphinx/test_out/$file
    fi
done
# -----------------------------------------------------------------------------
echo_eval sphinx-build -b html sphinx doc
# -----------------------------------------------------------------------------
echo "$0: OK"
exit 0
