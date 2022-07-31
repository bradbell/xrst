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
# -----------------------------------------------------------------------------
# change directory to test case where root_directory is not working directory
PYTHONPATH="$PYTHONPATH:$(pwd)"
mkdir doc
cd    doc
echo "python -m xrst html ../doc.xrst sphinx"
if ! python -m xrst html ../doc.xrst sphinx 2> ../check_xrst.$$
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
    if [ ! -e sphinx/test_out/$file ]
    then
        echo "The output file sphinx/test_out/$file does not exist."
        echo 'Check that the corresponding sections are correct and then:'
        echo "    cp sphinx/rst/$file sphinx/test_out/$file"
        exit 1
    elif ! diff sphinx/rst/$file sphinx/test_out/$file
    then
        echo "sphinx/rst/$file changed; above is output of"
        echo "    diff sphinx/rst/$file sphinx/test_out/$file"
        echo 'If the new file is currect, replace old with new using:'
        echo "    cp sphinx/rst/$file sphinx/test_out/$file"
        exit 1
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
        echo "Use the following command to remove sphinx/test_out/$file ?"
        echo "    git rm -f sphinx/test_out/$file"
        exit 1
    fi
done
# -----------------------------------------------------------------------------
echo_eval sphinx-build -b html sphinx doc
# -----------------------------------------------------------------------------
echo "$0: OK"
exit 0
