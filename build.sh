#!/bin/bash

set -xu

BUILD_PROJECT=${1}
IMAGE_TAG=${2:-""}
IMAGE_NAME="iot-${BUILD_PROJECT}"

docker build -t ${IMAGE_TAG} -f ./${BUILD_PROJECT}/docker/Dockerfile ./${BUILD_PROJECT}
