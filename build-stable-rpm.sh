#!/bin/bash
# Build and publish a package, called by github actions

# echo, exit on error/undefined vars
set -xeu

MOD='jailkit'
NAME="wbm-$MOD"

# Load module.info to get version
version=$(grep version $MOD/module.info | cut -d'=' -f2)
VERSION="${version}"

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
chmod g+w "${HOME}/rpmbuild/RPMS/noarch/${NAME}-${VERSION}-1.noarch.rpm"
scp -i "${HOME}/.ssh/id_ed25519" -p "${HOME}/rpmbuild/RPMS/noarch/${NAME}-${VERSION}-1.noarch.rpm" "$BUILD_SSH_USER@build.virtualmin.com:/home/build/result/vm/7/gpl/rpm/noarch"
scp -i "${HOME}/.ssh/id_ed25519" -p "${HOME}/rpmbuild/RPMS/noarch/${NAME}-${VERSION}-1.noarch.rpm" "$BUILD_SSH_USER@build.virtualmin.com:/home/build/result/vm/6/gpl/universal"
# Add it to the publish queue
ssh -i "${HOME}/.ssh/id_ed25519" "$BUILD_SSH_USER@build.virtualmin.com" "flock /home/build/rpm-publish-queue -c 'echo vm/7/gpl/rpm/noarch/${NAME}-${VERSION}-1.noarch.rpm >> /home/build/rpm-publish-queue'"
ssh -i "${HOME}/.ssh/id_ed25519" "$BUILD_SSH_USER@build.virtualmin.com" "flock /home/build/rpm-publish-queue -c 'echo vm/6/gpl/universal/${NAME}-${VERSION}-1.noarch.rpm >> /home/build/rpm-publish-queue'"
