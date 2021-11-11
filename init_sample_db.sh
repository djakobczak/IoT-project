set -uxe

#TODO add .env (import from second machine)

BASE_URL="http://localhost:8000/api/v1"

post_crosswalk(){
    local name=${1}
    local desc=${2}

    curl -X "POST" \
        "${BASE_URL}/crosswalks/" \
        -H "accept: application/json" \
        -H "Content-Type: application/json" \
        -d "{
            \"name\": \"${name}\",
            \"description\": \"${desc}\"
        }"
}

post_stats(){
    local crosswalk_id=${1}
    local timestamp=${2}
    local pedestrians=${3}

    curl -X "POST" \
        "${BASE_URL}/statistics/" \
        -H "accept: application/json" \
        -H "Content-Type: application/json" \
        -d "{
            \"crosswalk_name\": \"${crosswalk_id}\",
            \"timestamp\": \"${timestamp}\",
            \"pedestrians\": \"${pedestrians}\"
        }"
}

post_crosswalk "crosswalk1" "lorem ipsum"
post_crosswalk "crosswalk2" "lorem ipsum"
post_crosswalk "crosswalk3" "lorem ipsum"

post_stats "crosswalk1" "2021-11-10T21:34:38.227Z" "20"
post_stats "crosswalk1" "2021-11-11T21:34:38.227Z" "200"
post_stats "crosswalk2" "2021-11-11T20:34:38.227Z" "30"
post_stats "crosswalk2" "2021-11-11T21:34:38.227Z" "35"
post_stats "crosswalk3" "2021-10-11T21:34:38.227Z" "10"
post_stats "crosswalk3" "2021-11-11T21:34:38.227Z" "100"
