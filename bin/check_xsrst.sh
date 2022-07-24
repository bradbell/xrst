#! /bin/bash -e
# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
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
if [ "$0" != "bin/check_xsrst.sh" ]
then
    echo "bin/check_xsrst.sh: must be executed from its parent directory"
    exit 1
fi
# -----------------------------------------------------------------------------
if [ -e doc ]
then
    echo_eval rm -r doc
fi
# -----------------------------------------------------------------------------
echo "bin/xsrst.py html doc.xsrst sphinx spelling keyword"
if ! bin/xsrst.py \
    html doc.xsrst sphinx spelling  keyword 2> check_xsrst.$$
then
    type_error='error'
else
    type_error='warning'
fi
if [ -s check_xsrst.$$ ]
then
    cat check_xsrst.$$
    rm check_xsrst.$$
    echo "$0: exiting due to $type_error above"
    exit 1
fi
rm check_xsrst.$$
# -----------------------------------------------------------------------------
file_list=$(ls sphinx/xsrst/*.rst | sed -e "s|^sphinx/xsrst/||" )
for file in $file_list
do
    if [ ! -e sphinx/test_out/$file ]
    then
        echo "The output file sphinx/test_out/$file does not exist."
        echo 'Check that the corresponding sections are correct and then:'
        echo "    cp sphinx/xsrst/$file sphinx/test_out/$file"
        exit 1
    elif ! diff sphinx/test_out/$file sphinx/xsrst/$file
    then
        echo "sphinx/xsrst/$file changed; above is output of"
        echo "    diff sphinx/test_out/$file sphinx/xsrst/$file"
        echo 'If the new file is currect, replace old with new using:'
        echo "    cp sphinx/xsrst/$file sphinx/test_out/$file"
        exit 1
    else
        echo "$file: OK"
    fi
done
# -----------------------------------------------------------------------------
file_list=$(ls sphinx/test_out/*.rst | sed -e 's|^sphinx/test_out/||' )
for file in $file_list
do
    if [ ! -e sphinx/xsrst/$file ]
    then
        echo "The output file sphinx/xsrst/$file does not nexist."
        echo "Use the following command to remove sphinx/test_out/$file ?"
        echo "    git rm sphinx/test_out/$file"
        exit 1
    fi
done
# -----------------------------------------------------------------------------
echo_eval sphinx-build -b html sphinx doc
# -----------------------------------------------------------------------------
echo "$0: OK"
exit 0
