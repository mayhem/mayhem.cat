#!/bin/bash

docker run -d \
    --expose 3031 \
    --name mayhem.cat \
    -v /home/website/mayhem.cat:/code/mayhem.cat \
    --env "VIRTUAL_HOST=mayhem.cat" \
    --env "LETSENCRYPT_HOST=mayhem.cat" \
    --env "LETSENCRYPT_EMAIL=mayhem@gmail.com" \
    --network=website-network \
    stash:beta
