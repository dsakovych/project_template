#!/usr/bin/env bash
root=$( cd "$(dirname "$0")" ; pwd -P )

mysql="$root/../../mysql/docker-compose.yml"
elk="$root/../../elk/docker-compose.yml"


docker-compose -f $elk -f $mysql up