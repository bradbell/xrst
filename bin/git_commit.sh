#! /usr/bin/env bash
# ---------------------------------------------------------------------------
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2023 Bradley M. Bell
# ---------------------------------------------------------------------------
set -e -u
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
   echo $*
   eval $*
}
# -----------------------------------------------------------------------------
if [ $# != 0 ]
then
   echo 'usage: bin/git_commit.sh: does not expect arugments'
   exit 1
fi
if [ "$0" != 'bin/git_commit.sh' ]
then
   echo 'bin/git_commit.sh: must execute this script from its parent directory'
   exit 1
fi
if [ ! -e './.git' ]
then
   echo 'bin/git_commit.sh: cannot find ./.git'
   exit 1
fi
# -----------------------------------------------------------------------------
# EDITOR
set +u
if [ "$EDITOR" == '' ]
then
   echo 'bin/git_commit.sh: EDITOR is not defined.'
   exit 1
fi
set -u
# -----------------------------------------------------------------------------
# new files
list=$(git status --porcelain | sed -n -e '/^?? /p' | sed -e 's|^?? ||')
for file in $list
do
   res=''
   while [ "$res" != 'delete' ] && [ "$res" != 'add' ] && [ "$res" != 'abort' ]
   do
      read -p "$file is uknown to git, [delete/add/abort] ?" res
   done
   if [ "$res" == 'delete' ]
   then
      echo_eval rm $file
   elif [ "$res" == 'abort' ]
   then
      echo 'bin/git_commit.sh: aborting'
      exit 1
   fi
done
# -----------------------------------------------------------------------------
# git_commit.log
branch=$(git branch --show-current)
cat << EOF > git_commit.log
$branch: Replace the contents of this file with a summary for this commit.
If you delete all the lines in this file, this commit will abort.
Below is a list of the files that will be changed by this commit.
You may want to remove these names, or put comments next to individual files:
EOF
git status --porcelain >> git_commit.log
$EDITOR git_commit.log
#
line[0]=\
"$branch: Replace the contents of this file with a summary for this commit."
line[1]=\
'If you delete all the lines in this file, this commit will abort.'
line[2]=\
'Below is a list of the files that will be changed by this commit.'
line[3]=\
'You may want to remove these names, or put comments next to individual files:'
for index in {0..3}
do
   if grep "${line[$index]}" git_commit.log > /dev/null
   then
      echo 'Aborting because you left following line in commit log:'
      echo "   ${line[$index]}"
      exit 1
   fi
done
# -----------------------------------------------------------------------------
# git add
echo_eval git add --all
#
#
# git commit
git commit --file=git_commit.log
#
echo 'bin/git_commit.sh: OK'
exit 0
