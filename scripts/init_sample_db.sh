#!/bin/bash

set -uxe

#TODO add .env (import from second machine)
source ./common.sh

HOST="localhost:8000"

post_admin ${HOST}
TOKEN=$(get_token ${HOST})

post_crosswalk ${HOST} "crosswalk1" "lorem ipsum" $TOKEN
post_crosswalk ${HOST} "crosswalk2" "lorem ipsum" $TOKEN
post_crosswalk ${HOST} "crosswalk3" "lorem ipsum" $TOKEN

post_stats ${HOST} "crosswalk1" "2021-11-10T21:34:38.227Z" "20" $TOKEN
post_stats ${HOST} "crosswalk1" "2021-11-11T21:34:38.227Z" "200" $TOKEN
post_stats ${HOST} "crosswalk2" "2021-11-11T20:34:38.227Z" "30" $TOKEN
post_stats ${HOST} "crosswalk2" "2021-11-11T21:34:38.227Z" "35" $TOKEN
post_stats ${HOST} "crosswalk3" "2021-10-11T21:34:38.227Z" "10" $TOKEN
post_stats ${HOST} "crosswalk3" "2021-11-11T21:34:38.227Z" "100" $TOKEN
