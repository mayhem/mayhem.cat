#!/bin/bash

docker network create website-network

docker run -d \
    --expose 3031 \
    --name mayhem.cat \
    -v `pwd`/..:/code/mayhem.cat \
    --env "VIRTUAL_HOST=mayhem.cat" \
    --env "LETSENCRYPT_HOST=mayhem.cat" \
    --env "LETSENCRYPT_EMAIL=mayhem@gmail.com" \
    --network=website-network \
    mayhem.cat:beta
