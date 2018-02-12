#!/usr/bin/env bash

function buildPath() {
    isNeedGoBack=false
    while getopts ":b" opt; do
      case $opt in
        b)
          isNeedGoBack=true;
          ;;
        \?)
          isNeedGoBack=false;
          ;;
      esac
    done
    dir="$( cd "$(dirname "$0")" ; pwd -P )"
    backPart='/../../..'
    if [ isNeedGoBack = true ]; then
        backPart='/../../../..'
    fi
    if [ -z ${1} ]; then
        echo "$dir$backPart/docker-compose.deprecated.yml";
        exit 1;
    else
        echo "$dir$backPart/${1}/docker-compose.yml";
        exit 1;
    fi
}