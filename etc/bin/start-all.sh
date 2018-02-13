#!/usr/bin/env bash
root=$( cd "$(dirname "$0")" ; pwd -P )

mysql="$root/../../mysql/docker-compose.yml"
elk="$root/../../elk/docker-compose.yml"
rabbit="$root/../../rabbit-mq/docker-compose.yml"

docker-compose -f $elk -f $rabbit -f $mysql up