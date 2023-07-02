#!/bin/bash
# Build and publish a package, called by github actions

MOD='jailkit'
NAME="webmin-$MOD"

# Always increasing. Also a human-readable datetime.
BUILD=$(date +'%Y%m%d%H%M')

# Load module.info to get version
version=$(grep version $MOD/module.info | cut -d'=' -f2)
VERSION="${version}.devel.${BUILD}"

mkdir tmp
perl makemoduledeb.pl --deb-depends --licence 'GPLv3' --email 'joe@virtualmin.com' --allow-overwrite --target-dir tmp "$MOD" "$VERSION"
mv "tmp/${NAME}_${VERSION}_all.deb" .

# Publish to aptly
curl --user $APTLY_USER:$APTLY_PASSWD -X POST -F file=@${NAME}_${VERSION}_all.deb https://aptly.virtualmin.com/api/files/${NAME}_${VERSION}
#curl --user $APTLY_USER:$APTLY_PASSWD -X POST https://aptly.virtualmin.com/api/repos/virtualmin-7-gpl-devel/file/${NAME}_${VERSION}
#curl --user $APTLY_USER:$APTLY_PASSWD https://aptly.virtualmin.com/api/publish/filesystem:7-gpl/virtualmin-devel
