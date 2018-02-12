#!/usr/bin/env bash
function networkIsExists () {
    network=$(docker network ls | grep my_lan)
    if [ -z "$network" ]; then
        echo 0;
        exit 1;
    fi
    echo 1;
    exit 1;
}

function manageNetwork() {
    networkExistence=$(networkIsExists)
    if [ "$networkExistence" -eq "0" ]; then
        docker network create -d bridge my_lan \
            --opt com.docker.network.bridge.enable_ipv6=true \
            --ipam-driver=default \
            --subnet=172.16.238.0/24 \
            --gateway=172.16.238.1
    fi
}