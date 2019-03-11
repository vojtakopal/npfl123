#!/bin/bash
usage() {
    cat <<EOM
    Usage:
    $(basename $0) [path_to_babi]

EOM
    exit 0
}

[ -z $1 ] && { usage; }

DATASET=$1
find $DATASET -name "dialog-babi-task*" | xargs cat | cut -d" " -f2-