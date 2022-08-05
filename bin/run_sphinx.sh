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
if [ "$0" != 'bin/run_sphinx.sh' ]
then
    echo 'must execut bin/run_sphinx.sh from its parent directory'
    exit 1
fi
# -----------------------------------------------------------------------------
if [ "$1" != 'html' ] && [ "$1" != 'pdf' ]
then
    echo 'usage: bin/run_sphinx.sh (html|pdf) [error_line]'
    exit 1
fi
target="$1"
if [ "$2" == '' ]
then
    error_line=''
else
    error_line="-e $2"
fi
# -----------------------------------------------------------------------------
# preamble
preamble='sphinx/preamble.rst'
# -----------------------------------------------------------------------------
# html
# -----------------------------------------------------------------------------
if [ "$target" == 'html' ]
then
    echo_eval python -m xrst doc.xrst -g start, -t html -s sphinx $error_line
    sphinx-build -b html sphinx doc
    echo 'run_sphinx.sh: OK'
    exit 0
fi
# -----------------------------------------------------------------------------
# pdf
# -----------------------------------------------------------------------------
#
# run xrst to create rst files
echo_eval python -m xrst doc.xrst -t pdf -s sphinx $error_line
#
# run sphinx to create latex
echo_eval sphinx-build -b latex sphinx doc/latex
echo_eval cd doc/latex
#
# create pdf from latex
echo_eval make xrst.pdf
#
# -----------------------------------------------------------------------------
echo 'run_sphinx.sh: OK'
exit 0
