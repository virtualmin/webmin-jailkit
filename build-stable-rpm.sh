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
VERSION="${version}.${BUILD}"

if [ -f epoch ]; then
  epoch="--epoch $(cat epoch)"
else
  epoch=""
fi

# FIXME after PR is merged to Webmin
mkdir -p ${HOME}/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
mkdir -p "${HOME}/rpmbuild/RPMS/noarch"
perl makemodulerpm.pl --rpm-depends --licence 'GPLv3' --allow-overwrite $epoch "$MOD" "$VERSION"

# Copy to build/deploy server
scp -i "${HOME}/.ssh/id_ed25519" "${HOME}/rpmbuild/RPMS/noarch/${NAME}-${VERSION}-1.noarch.rpm" "$BUILD_SSH_USER@build.virtualmin.com:/home/build/result/vm/7/gpl-devel/rpm/noarch"
# Add it to the publish queue
ssh -i "${HOME}/.ssh/id_ed25519" "$BUILD_SSH_USER@build.virtualmin.com" "flock /home/build/rpm-publish-queue -c 'echo vm/7/gpl-devel/rpm/noarch/${NAME}-${VERSION}-1.noarch.rpm >> /home/build/rpm-publish-queue'"

