#!/bin/bash

set -ux

if [ -f .env ]; then
    source .env
fi

ACTION=${1:-"build"}
IMAGE_TAG_BACKEND="${REGISTRY_HOST}/${BACKEND_IMAGE_NAME}"
IMAGE_TAG_FRONTEND="${REGISTRY_HOST}/${FRONTEND_IMAGE_NAME}"


if [ "$ACTION" = "build" ] || [ "$ACTION" = "all" ]; then
    /bin/bash build.sh backend ${BACKEND_IMAGE_NAME}
    /bin/bash build.sh frontend ${FRONTEND_IMAGE_NAME}
fi

if [ "$ACTION" = "run" ] || [ "$ACTION" = "all" ]; then
    /bin/bash run.sh ${BACKEND_CONTAINER_NAME} ${BACKEND_PORT} ${BACKEND_IMAGE_NAME}
    /bin/bash run.sh ${FRONTEND_CONTAINER_NAME} ${FRONTEND_PORT} ${FRONTEND_IMAGE_NAME}
fi

if [ "$ACTION" = "stop" ]; then
    docker stop ${BACKEND_CONTAINER_NAME} 2> /dev/null
    docker stop ${FRONTEND_CONTAINER_NAME} 2> /dev/null
    docker rm $(docker ps -qa) 2> /dev/null # TODO add grep
fi

if [ "$ACTION" = "push" ]; then
    /bin/bash push.sh ${BACKEND_IMAGE_NAME}
    /bin/bash push.sh ${FRONTEND_IMAGE_NAME}
fi
