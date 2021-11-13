#!/bin/bash
set -ux

CONTAINER_NAME=${1}
PORT=${2}
IMAGE_NAME=${3}
NETWORK_NAME=${4}

docker run -d \
    --name ${CONTAINER_NAME} \
    -p ${PORT}:${PORT} \
    ${IMAGE_NAME}

docker network connect ${NETWORK_NAME} ${CONTAINER_NAME}
