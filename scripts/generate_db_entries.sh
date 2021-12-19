#!/bin/bash

set -u

source ./common.sh

HOST="localhost:8000"
CROSSWALKS=("crosswalk1" "crosswalk2" "crosswalk3" "crosswalk4" "crosswalk5" "crosswalk6" "crosswalk7" "crosswalk8" "crosswalk9" "crosswalk10" "crosswalk11" "crosswalk12")
TOKEN=$(get_token ${HOST})
SLEEP_TIME=1

# register crosswalks
post_crosswalk $HOST ${CROSSWALKS[0]} "lorem ipsum" $TOKEN
post_crosswalk $HOST ${CROSSWALKS[1]} "lorem ipsum" $TOKEN
post_crosswalk $HOST ${CROSSWALKS[2]} "lorem ipsum" $TOKEN
post_crosswalk $HOST ${CROSSWALKS[3]} "lorem ipsum" $TOKEN
post_crosswalk $HOST ${CROSSWALKS[4]} "lorem ipsum" $TOKEN
post_crosswalk $HOST ${CROSSWALKS[5]} "lorem ipsum" $TOKEN
post_crosswalk $HOST ${CROSSWALKS[6]} "lorem ipsum" $TOKEN
post_crosswalk $HOST ${CROSSWALKS[7]} "lorem ipsum" $TOKEN
post_crosswalk $HOST ${CROSSWALKS[8]} "lorem ipsum" $TOKEN
post_crosswalk $HOST ${CROSSWALKS[9]} "lorem ipsum" $TOKEN
post_crosswalk $HOST ${CROSSWALKS[10]} "lorem ipsum" $TOKEN
post_crosswalk $HOST ${CROSSWALKS[11]} "lorem ipsum" $TOKEN

while true; do
    PEDESTRIANS_NUM=$((1 + $RANDOM % 100))
    CROSSWALK_IDX=$(($RANDOM % 11))

    post_stats ${HOST} ${CROSSWALKS[${CROSSWALK_IDX}]} $(date +"%Y-%m-%dT%H:%M:%S") ${PEDESTRIANS_NUM} ${TOKEN}
    sleep ${SLEEP_TIME}
done
