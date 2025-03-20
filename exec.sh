#!/bin/zsh

if [[ -a .env ]]
then
  source .env
fi

if [[ -a .dev_env ]]
then
  source .dev_env
fi

podman container stop jars_api
podman container rm -f jars_api
podman run \
--detach \
--tty \
--name=jars_api \
--publish=5277:80 \
localhost/jars_api_image:latest
