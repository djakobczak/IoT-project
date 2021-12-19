#!/bin/bash

get_token(){
    local HOST=${1}

    TOKEN=$(curl -s -X "POST" \
        "http://${HOST}/api/v1/login/access-token" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d "grant_type=&username=admin&password=secret&scope=&client_id=&client_secret=" | jq -r ".access_token")
    echo $TOKEN
}

post_crosswalk(){
    local host=${1}
    local name=${2}
    local desc=${3}
    local token=${4}

    curl -X "POST" \
        "${host}/api/v1/crosswalks/" \
        -H "accept: application/json" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $token" \
        -d "{
            \"name\": \"${name}\",
            \"description\": \"${desc}\"
        }"
}

post_stats(){
    local host=${1}
    local crosswalk_name=${2}
    local timestamp=${3}
    local pedestrians=${4}
    local token=${5}

    curl -X "POST" \
        "${host}/api/v1/statistics/" \
        -H "accept: application/json" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $token" \
        -d "{
            \"crosswalk_name\": \"${crosswalk_name}\",
            \"timestamp\": \"${timestamp}\",
            \"pedestrians\": \"${pedestrians}\"
        }"
}
