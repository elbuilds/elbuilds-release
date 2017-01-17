# elbuilds-release

## ABOUT

This package contains yum configuration for the elbuilds repository for Enterprise Linux, as well as the public GPG keys used to sign packages.

## BUILD

```bash
git clone https://github.com/elbuilds/elbuilds-release.git
./elbuilds-release/tar.sh
cd elbuilds-release
git checkout spec
mkdir -pv /tmp/rpmbuild/{SPECS,SOURCES}
cp -vf elbuilds-release.spec /tmp/rpmbuild/SPECS
cp -vf ../elbuilds-release.tar.gz /tmp/rpmbuild/SOURCES
rpmbuild -D '_topdir /tmp/rpmbuild' -ba /tmp/rpmbuild/SPECS/elbuilds-release.spec
```

## COPYING

Copyright (c) 2017 秦凡东 (Qin Fandong)

Read [LICENSE](LICENSE) for more.

