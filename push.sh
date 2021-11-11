set -ux

IMAGE_NAME=${1}

docker image push localhost:5000/${IMAGE_NAME}:latest
