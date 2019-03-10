#!/bin/bash
usage() {
    cat <<EOM
    Usage:
    $(basename $0) [path_to_dstc2]

EOM
    exit 0
}

[ -z $1 ] && { usage; }

DATASET=$1
find $DATASET -name "log.json" | xargs cat | sed -r -n "s/^.*transcript\": \"(.*)\",/\1/p"