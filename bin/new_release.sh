#! /usr/bin/env bash
set -e -u
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-25 Bradley M. Bell
# -----------------------------------------------------------------------------
year='2025' # Year for this stable version
release='2' # first release for each year starts with 0
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
if [ "$branch" != 'master' ] || [ "$branch" == 'main' ]
then
   echo 'bin/new_release.sh: execute using master or main branch'
   exit 1
fi
#
# sed
source bin/grep_and_sed.sh
#
# first_version_file
source bin/dev_settings.sh
first_version_file=$(echo $version_file_list | $sed -e 's|^ *||' -e 's| .*||')
#
# version_type
cat << EOF > temp.sed
/["'][0-9]{8}["']/b one
/["'][0-9]{8}[.][0-9]{1,2}["']/b one
/["'][0-9]{4}[.][0-9]{1,2}[.][0-9]{1,2}["']/b one
b end
#
: one
s|.*["']([0-9]{8})["'].*|\\1|
s|.*["']([0-9]{8})[.][0-9]{1,2}["'].*|\\1|
s|.*["']([0-9]{4}[.][0-9]{1,2}[.][0-9]{1,2})["'].*|\\1|
p
#
: end
EOF
version=$($sed -n -r -f temp.sed $first_version_file)
if [[ "$version" =~ ^[0-9]{8}$ ]]
then
   version_type=1
elif [[ "$version" =~ ^[0-9]{8}[.][0-9]{1,2}$ ]]
then
   version_type=2
   echo "new_release.sh: version in $first_version_file"
   echo "is for a release but this is the $branch branch"
   exit 1
elif [[ "$version" =~ ^[0-9]{4}[.][0-9]{1,2}[.][0-9]{1,2}$ ]]
then
   version_type=3
   if [[ "$version" =~  ^[0-9]{4}[.][0].*$ ]]
   then
      echo "new_release.sh: version in $first_version_file"
      echo "is for a release but this is the $branch branch"
      exit 1
   fi
else
   echo "check_version.sh: can't find version number in $first_version_file"
   exit 1
fi
#
# tag
if [ "$version_type" == 1 ]
then
   tag="$year0000.$release"
else
   tag=$year.0.$release
fi
#
# tag_commited
tag_commited='no'
if git tag --list | grep "$tag" > /dev/null
then
   tag_commited='yes'
fi
#
# stable_branch
stable_branch=stable/$year
#
# stable_local_hash
pattern=$(echo " *refs/heads/$stable_branch" | $sed -e 's|/|[/]|g')
stable_local_hash=$(
   git show-ref $stable_branch | \
      $sed -n -e "/$pattern/p" | \
         $sed -e "s|$pattern||"
)
#
# stable_remote_hash
pattern=$(echo " *refs/remotes/origin/$stable_branch" | $sed -e 's|/|[/]|g')
stable_remote_hash=$(
   git show-ref $stable_branch | \
      $sed -n -e "/$pattern/p" | \
         $sed -e "s|$pattern||"
)
#
# master_local_hash
pattern=$(echo " *refs/heads/master" | $sed -e 's|/|[/]|g')
master_local_hash=$(
   git show-ref master | \
      $sed -n -e "/$pattern/p" | \
         $sed -e "s|$pattern||"
)
#
# master_remote_hash
pattern=$(echo " *refs/remotes/origin/master" | $sed -e 's|/|[/]|g')
master_remote_hash=$(
   git show-ref master | \
      $sed -n -e "/$pattern/p" | \
         $sed -e "s|$pattern||"
)
#
# ----------------------------------------------------------------------------
# Changes to master branch
# ----------------------------------------------------------------------------
#
# user.xrst
$sed -i user/user.xrst \
   -e "s|stable-[0-9]\{4\}|stable-$year|g" \
   -e "s|release-[0-9]\{4\}|release-$year|g" \
   -e "s|archive/[0-9]\{4\}[.]0[.][0-9]*.tar.gz|archive/$tag.tar.gz|"
#
# check_version
# changes to version ?
if ! bin/check_version.sh
then
   echo 'Continuing even thought bin/check_version made changes.'
fi
#
# check_all.sh
if [ "$tag_commited" == 'yes' ]
then
   bin/check_all.sh
else
   bin/check_all.sh --skip_external_links
fi
#
# git_status
git_status=$(git status --porcelain)
if [ "$git_status" != '' ]
then
   echo "bin/new_release: git staus is not empty for $branch branch"
   echo 'use bin/git_commit.sh to commit its changes ?'
   exit 1
fi
# ----------------------------------------------------------------------------
# Changes to stable branch
# ----------------------------------------------------------------------------
if ! git show-ref $stable_branch > /dev/null
then
   echo "bin/new_release: neither local or remvoe $stable_branch exists."
   echo 'Use the following to create it ?'
   echo "   git branch $stable_branch"
   exit 1
fi
if ! git checkout $stable_branch
then
   echo "bin/new_release: should be able to checkout $stable_branch"
   exit 1
fi
#
# user.xrst
$sed -i user/user.xrst \
   -e "s|stable-[0-9]\{4\}|stable-$year|g" \
   -e "s|release-[0-9]\{4\}|release-$year|g" \
   -e "s|archive/[0-9]\{4\}[.]0[.][0-9]*.tar.gz|archive/$tag.tar.gz|"
#
# upload.sh
$sed -i bin/upload.sh \
   -e 's|--repository testpypi|--repository pypi|'
#
# first_version_file
cat << EOF > temp.sed
s|(["'])[0-9]{8}(["'])|\\1$tag\\2|
s|(["'])[0-9]{4}[.][0-9]{1,2}[.][0-9]{1,2}(["'])|\\1$tag\\2|
EOF
$sed -r -f temp.sed -i $first_version_file
if ! grep "['\"]$tag['\"]" $first_version_file > /dev/null
then
   echo "bin/rew_release: branch = $stable_branch"
   echo "Version number should be $tag in $first_version_file"
   exit 1
fi
#
# check_all.sh
if [ "$tag_commited" == 'yes' ]
then
   bin/check_all.sh
else
   bin/check_all.sh --skip_external_links
fi
#
# git_status
git_status=$(git status --porcelain)
if [ "$git_status" != '' ]
then
   echo "bin/new_release: git staus --porcelean not empty for $stable_branch"
   echo 'use bin/git_commit.sh to commit its changes ?'
   exit 1
fi
# -----------------------------------------------------------------------------
#
# stable_remote
if [ "$stable_remote_hash" == '' ]
then
   empty_hash='yes'
   echo "bin/new_release: remote $stable_branch does not exist."
   echo 'Use the following to create it ?'
   echo "   git push origin $stable_branch"
   exit 1
fi
if [ "$stable_local_hash" != "$stable_remote_hash" ]
then
   empty_hash='yes'
   echo "bin/new_release: local and remote $stable_branch differ."
   echo "local  $stable_local_hash"
   echo "remote $stable_remote_hash"
   echo 'Use git push to fix this ?'
   exit 1
fi
#
# push tag
if [ "$tag_commited" == 'no' ]
then
   read -p 'commit release or abort [c/a] ?' response
   if [ "$response" == 'a' ]
   then
      exit 1
   fi
   echo "git tag -a -m 'created by new_release.sh' $tag $stable_remote_hash"
   git tag -a -m 'created by new_release.sh' $tag $stable_remote_hash
   #
   echo "git push origin $tag"
   git push origin $tag
   #
   echo 'bin/new_release.sh: must be re-run to check external links'
   exit 1
fi
# ----------------------------------------------------------------------------
echo 'bin/new_release.sh: OK'
exit 0
