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
if [ "$1" != 'html' ] && [ "$1" != 'tex' ]
then
   echo 'usage: bin/run_xrst.sh (html|tex) [--rst_line_numbers]'
   exit 1
fi
if [ "$2" != '' ] && [ "$2" != '--rst_line_numbers' ]
then
   echo 'usage: bin/run_xrst.sh (html|tex) [--rst_line_numbers]'
   exit 1
fi
target="$1"
rst_line_numbers="$2"
# -----------------------------------------------------------------------------
echo_eval python -m xrst  \
   --page_source \
   --group_list  default user \
   --html_theme  sphinx_book_theme \
   --target      $target \
   $rst_line_numbers
# -----------------------------------------------------------------------------
echo 'run_xrst.sh: OK'
exit 0
