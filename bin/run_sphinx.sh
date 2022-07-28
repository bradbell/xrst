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
if [ "$0" != 'bin/run_sphinx.sh' ]
then
    echo 'must execut bin/run_sphinx.sh from its parent directory'
    exit 1
fi
# -----------------------------------------------------------------------------
if [ "$1" != 'html' ] && [ "$1" != 'pdf' ]
then
    echo 'usage: bin/run_sphinx.sh (html|pdf) [line_increment]'
    exit 1
fi
target="$1"
line_increment="$2"
# -----------------------------------------------------------------------------
# preamble
preamble='sphinx/preamble.rst'
# -----------------------------------------------------------------------------
if ! grep BEGIN_LATEX_MACROS $preamble > /dev/null
then
    echo "bin/run_sphinx: can't find BEGIN_LATEX_MACROS in $premable"
fi
if ! grep END_LATEX_MACROS $preamble > /dev/null
then
    echo "bin/run_sphinx: can't find END_LATEX_MACROS in $premable"
fi
# -----------------------------------------------------------------------------
# html
# -----------------------------------------------------------------------------
if [ "$target" == 'html' ]
then
    echo_eval python -m xsrst \
        html doc.xsrst sphinx spelling keyword $line_increment
    sphinx-build -b html sphinx doc/html
    echo 'run_sphinx.sh: OK'
    exit 0
fi
# -----------------------------------------------------------------------------
# pdf
# -----------------------------------------------------------------------------
#
diff=$(git diff $preamble)
if [ "$diff" != '' ]
then
    echo 'bin/run_sphinx.sh pdf:'
    echo "$preamble has changed."
    echo 'You must first test bin/run_sphinx.sh html.'
    echo "Then check in the new $preamble before running bin/run_sphinx.sh pdf."
    exit 1
fi
#
# remove latex macros from preamble
echo "sed -i $preamble -e '/BEGIN_LATEX_MACROS/,/END_LATEX_MACROS/d'"
sed -i $preamble -e '/BEGIN_LATEX_MACROS/,/END_LATEX_MACROS/d'
#
# run xsrst to create rst files
echo_eval python -m xsrst pdf doc.xsrst sphinx spelling keyword $line_increment
#
# run sphinx to create latex
echo_eval sphinx-build -b latex sphinx doc/latex
echo_eval cd doc/latex
#
# change latex \chapter commands to \section commands
echo "sed -i xsrst.tex -e 's|\\chapter{|\\section{|'"
sed -i xsrst.tex -e 's|\\chapter{|\\section{|'
#
# create pdf from latex
echo_eval make xsrst.pdf
#
# restore the preamble
echo_eval git checkout ../../$preamble
# -----------------------------------------------------------------------------
echo 'run_sphinx.sh: OK'
exit 0
