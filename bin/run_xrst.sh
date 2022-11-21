#! /bin/bash -e
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
   echo $*
   eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != 'bin/run_xrst.sh' ]
then
   echo 'must execut bin/run_xrst.sh from its parent directory'
   exit 1
fi
# -----------------------------------------------------------------------------
if [ "$1" != 'html' ] && [ "$1" != 'pdf' ]
then
   echo 'usage: bin/run_xrst.sh (html|pdf) [rst_line]'
   exit 1
fi
target="$1"
if [ "$2" == '' ]
then
   rst_line=''
else
   rst_line="--rst $2"
fi
# -----------------------------------------------------------------------------
# preamble
preamble='sphinx/preamble.rst'
# -----------------------------------------------------------------------------
# html
# -----------------------------------------------------------------------------
if [ "$target" == 'html' ]
then
   echo_eval python -m xrst xrst.toml \
      --group default,user \
      $rst_line \
      --html sphinx_book_theme
   echo 'run_xrst.sh: OK'
   exit 0
fi
# -----------------------------------------------------------------------------
# pdf
# -----------------------------------------------------------------------------
echo_eval python -m xrst xrst.toml --group default,user \
      --target pdf $rst_line
#
# -----------------------------------------------------------------------------
echo 'run_xrst.sh: OK'
exit 0
