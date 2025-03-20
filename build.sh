#!/bin/zsh
echo "Sourcing environment variables..."
if [[ -a .env ]]
then
  source .env
fi
if [[ -a .dev_env ]]
then
  source .dev_env
fi

echo "Checking environment..."
if ! [[ -n $JARS_LOG_LEVEL && -n $ROOT_LOG_LEVEL ]] ;
then
  echo "Error: One or more required environment variables aren't specified:
  JARS_LOG_LEVEL: $JARS_LOG_LEVEL
  ROOT_LOG_LEVEL: $ROOT_LOG_LEVEL"
  return 1
fi

build_no_cache () {
  if ! podman build \
  --no-cache \
  --env ROOT_LOG_LEVEL="$ROOT_LOG_LEVEL" \
  --env JARS_LOG_LEVEL="$JARS_LOG_LEVEL" \
  --env FLASK_ENV="$FLASK_ENV" \
  --build-arg uuid=1001 \
  --build-arg guid=1002 \
  --tag jars_api_image \
  --file Dockerfile
  then
    echo "Error: unable to build the image (no cache)"
    return 1
  fi
}

build_with_cache () {
  if ! podman build \
  --env ROOT_LOG_LEVEL="$ROOT_LOG_LEVEL" \
  --env JARS_LOG_LEVEL="$JARS_LOG_LEVEL" \
  --env FLASK_ENV="$FLASK_ENV" \
  --build-arg uuid=1001 \
  --build-arg guid=1002 \
  --tag jars_api_image \
  --file Dockerfile
  then
    echo "Error: unable to build the image with cache"
    return 1
  fi
}

vared -p 'Build with no cache? ' -c no_cache
echo "Building the JARS image..."
re='^[yY][eE]?[sS]?$'
if [[ $no_cache =~ $re ]]
then
  build_no_cache
else
  build_with_cache
fi


echo "Checking for jars_api container..."
if podman container ps -a | grep -s "jars_api" ;
then
  echo "Stopping and removing existing jars_api container..."
  podman container stop jars_api
  podman container rm jars_api
fi

echo "Creating jars_api container..."
if ! podman create \
--replace \
--name=jars_api \
localhost/jars_api_image:latest
then
  echo "Error: Failed creating jars_api container"
  return 1
fi
return 0
