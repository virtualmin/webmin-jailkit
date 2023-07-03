#!/bin/bash
# Build and publish a package, called by github actions

# echo, exit on error/undefined vars
set -xeu

MOD='jailkit'
NAME="wbm-$MOD"

# Always increasing. Also a human-readable datetime.
BUILD=$(date +'%Y%m%d%H%M')

# Load module.info to get version
version=$(grep version $MOD/module.info | cut -d'=' -f2)
VERSION="${version}.devel.${BUILD}"

if [ -f epoch ]; then
  epoch="--epoch $(cat epoch)"
else
  epoch=""
fi

mkdir tmp
# FIXME after PR is merged to Webmin
mkdir -p ${HOME}/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
mkdir -p "${HOME}/rpmbuild/RPMS/noarch"
ls "${HOME}/rpmbuild/RPMS/noarch"
ls "${HOME}/rpmbuild/SOURCES"
ls "${HOME}/rpmbuild/SPECS"
perl makemodulerpm.pl --rpm-depends --licence 'GPLv3' --allow-overwrite --target-dir tmp $epoch "$MOD" "$VERSION"
mv "tmp/${NAME}_${VERSION}_all.deb" .

# Publish to pulp, I guess?
