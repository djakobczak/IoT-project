#!/bin/bash

set -u

source ./common.sh

HOST="localhost:8000"
CROSSWALKS=("crosswalk1" "crosswalk2" "crosswalk3")
TOKEN=$(get_token ${HOST})
SLEEP_TIME=5

# register crosswalks
post_crosswalk $HOST ${CROSSWALKS[0]} "lorem ipsum" $TOKEN
post_crosswalk $HOST ${CROSSWALKS[1]} "lorem ipsum" $TOKEN
post_crosswalk $HOST ${CROSSWALKS[2]} "lorem ipsum" $TOKEN

while true; do
    PEDESTRIANS_NUM=$((1 + $RANDOM % 100))
    CROSSWALK_IDX=$(($RANDOM % 3))

    post_stats ${HOST} ${CROSSWALKS[${CROSSWALK_IDX}]} $(date +"%Y-%m-%dT%H:%M:%S") ${PEDESTRIANS_NUM} ${TOKEN}
    sleep ${SLEEP_TIME}
done
