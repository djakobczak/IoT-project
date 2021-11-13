set -uxe

#TODO add .env (import from second machine)

BASE_URL="http://localhost:8000/api/v1"

post_crosswalk(){
    local name=${1}
    local desc=${2}
    local token=${3}

    curl -X "POST" \
        "${BASE_URL}/crosswalks/" \
        -H "accept: application/json" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $token" \
        -d "{
            \"name\": \"${name}\",
            \"description\": \"${desc}\"
        }"
}

post_stats(){
    local crosswalk_name=${1}
    local timestamp=${2}
    local pedestrians=${3}
    local token=${4}

    curl -X "POST" \
        "${BASE_URL}/statistics/" \
        -H "accept: application/json" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $token" \
        -d "{
            \"crosswalk_name\": \"${crosswalk_name}\",
            \"timestamp\": \"${timestamp}\",
            \"pedestrians\": \"${pedestrians}\"
        }"
}

post_admin(){
    curl -X "POST" \
        "${BASE_URL}/users/" \
        -H "accept: application/json" \
        -H "Content-Type: application/json" \
        -d "{
            \"username\": \"admin\",
            \"password\": \"secret\"
        }"
}

get_token(){
    TOKEN=$(curl -s -X 'POST' \
        'http://localhost:8000/api/v1/login/access-token' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/x-www-form-urlencoded' \
        -d 'grant_type=&username=admin&password=secret&scope=&client_id=&client_secret=' | jq -r ".access_token")
    echo $TOKEN
}

post_admin
TOKEN=$(get_token)

post_crosswalk "crosswalk1" "lorem ipsum" $TOKEN
post_crosswalk "crosswalk2" "lorem ipsum" $TOKEN
post_crosswalk "crosswalk3" "lorem ipsum" $TOKEN

post_stats "crosswalk1" "2021-11-10T21:34:38.227Z" "20" $TOKEN
post_stats "crosswalk1" "2021-11-11T21:34:38.227Z" "200" $TOKEN
post_stats "crosswalk2" "2021-11-11T20:34:38.227Z" "30" $TOKEN
post_stats "crosswalk2" "2021-11-11T21:34:38.227Z" "35" $TOKEN
post_stats "crosswalk3" "2021-10-11T21:34:38.227Z" "10" $TOKEN
post_stats "crosswalk3" "2021-11-11T21:34:38.227Z" "100" $TOKEN
