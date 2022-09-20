#! /bin/bash -e
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
   echo $*
   eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/check_version.sh" ]
then
   echo "bin/check_version.sh: must be executed from its parent directory"
   exit 1
fi
#
# check date
if ! version.sh check > /dev/null
then
   version.sh check
   echo 'check_version.sh: Error'
   exit 1
fi
#
# xrst.xrst
# check length of underline
pattern='^Version [0-9]\{4\}[.][0-9]\{1,2\}[.][0-9]\{1,2\}$'
if ! grep "$pattern" xrst.xrst > /dev/null
then
   echo "check_version.sh: can't find following pattern in xrst.xrst"
   echo "$pattern"
   exit 1
fi
cat << EOF > temp.sed
/^Version [0-9]\\{4\\}[.][0-9]\\{1,2\\}[.][0-9]\\{1,2\\}\$/! b end
N
p
: end
EOF
header_text=$(sed -n -f temp.sed xrst.xrst | head -1)
header_underline=$(sed -n -f temp.sed xrst.xrst | tail -1)
text_length=${#header_text}
underline_length=${#header_underline}
if [ "$text_length" != "$underline_length" ]
then
   echo 'Underline not same length as header in xrst.xrst'
   echo "$header_text"
   echo "$header_underline"
   exit 1
fi
echo 'check_version.sh: OK'
exit 0
