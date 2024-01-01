#! /usr/bin/env bash
set -e -u
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-23 Bradley M. Bell
# -----------------------------------------------------------------------------
year='2024' # Year for this stable version 
release='0' # first release for each year starts with 0
# -----------------------------------------------------------------------------
if [ $# != 0 ]
then
   echo 'bin/new_release.sh does not expect any arguments'
   exit 1
fi
if [ "$0" != 'bin/new_release.sh' ]
then
   echo 'bin/new_release.sh: must be executed from its parent directory'
   exit 1
fi
if [ ! -e './.git' ]
then
   echo 'bin/new_release.sh: cannot find ./.git'
   exit 1
fi
# -----------------------------------------------------------------------------
#
# branch
branch=$(git branch --show-current)
if [ "$branch" != 'master' ]
then
   echo 'bin/new_release.sh: must start execution using master branch'
   exit 1
fi
#
# tag
tag=$year.0.$release
#
# pyproject.toml
sed -i pyproject.toml \
-e "s|version\\( *\\)= *'[0-9]\\{4\\}[.][0-9]*[.][0-9]*'|version\\1= '$tag'|"
#
# check_version
# check_version.sh will use pyproject.toml version becasue it has 0 the form
# year.0.release.
bin/check_version.sh
#
# git_status
git_status=$(git status --porcelain)
if [ "$git_status" != '' ]
then
   echo 'bin/new_release: git staus --porcelean is not empty for master branch'
   echo 'use bin/git_commit.sh to commit its changes'
   exit 1
fi
