#!/usr/bin/env bash

set -ex

RDIR=$(dirname $(readlink -f "$0"))
WDIR=$(dirname "$RDIR")
TARBALL="${RDIR}.tar.gz"
TAR='tar'

{
  command "$TAR" -v -zc -f "$TARBALL" -C "$WDIR" $(basename "$RDIR")
  # No need to deal with return value because '-e' has set.
}

