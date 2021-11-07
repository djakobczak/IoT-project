#!/bin/bash
set -ux

CONTAINER_NAME=${1}
PORT=${2}
IMAGE_NAME=${3}

docker run -d \
    --name ${CONTAINER_NAME} \
    -p ${PORT}:${PORT} \
    ${IMAGE_NAME}
