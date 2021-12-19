#!/bin/bash

set -u

source /home/pi/Desktop/AGH/IoT/token.sh
HOST="localhost:8000"
TOKEN=$(get_token ${HOST})
SLEEP_TIME=1
typeset -i PEDESTRIANS=$( paste -sd+ /home/pi/Desktop/AGH/IoT/pedestrians | bc)

# register crosswalks
post_crosswalk $HOST "Przejscie_piastowska_Krakow" "Od ulicy Rejmonta" $TOKEN
# post data 
post_stats ${HOST} "Przejscie_piastowska_Krakow" $(date +"%Y-%m-%dT%H:%M:%S") $PEDESTRIANS ${TOKEN}
# delete sent statistics
> /home/joanna/Desktop/AGH/pedestrians
echo 0 > /home/pi/Desktop/AGH/IoT/pedestrians 
