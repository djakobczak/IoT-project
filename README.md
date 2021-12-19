# IoT-project

This repository contains files related to university project, that was focused on
creation of small IoT system. Plan was to design a system that improve pedestrains
safety. To achieve that few components were developed:

* ML people detection script for RaspberryPi
* master-slave protocol
* communication with the server
* server (both frontend and backend) that gathers statistics from crosswalks and visualize them

## Prerequisites

Requirements:

* python3.8+
* poetry
* docker (optional)

Before you run this project create `.env` configuration file for both backend and frontend.

Sample backend configuration (should be placed in `./backend/`):

``` bash

REGISTRY_HOST="localhost:5000"

BACKEND_PORT=8000
BACKEND_HOST="0.0.0.0"
BACKEND_CONTAINER_NAME=iot-backend
BACKEND_IMAGE_NAME=iot-backend

FRONTEND_PORT=9000
FRONTEND_HOST="0.0.0.0"
FRONTEND_CONTAINER_NAME=iot-frontend
FRONTEND_IMAGE_NAME=iot-frontend

OPERATOR_USERNAME=admin
OPERATOR_PASSWORD=secret
RASPBERRY_PI_USERNAME=provider
RASPBERRY_PI_PASSWORD=supersecret

SECRET_KEY=<PUT YOUR SECRET HERE>
ALGORITHM="HS256"
```

Sample frontend configuration (should be placed in `./frontend/`):

``` bash

REGISTRY_HOST="localhost:5000"

BACKEND_PORT=8000
BACKEND_HOST="0.0.0.0"
BACKEND_CONTAINER_NAME=iot-backend
BACKEND_IMAGE_NAME=iot-backend

FRONTEND_PORT=9000
FRONTEND_HOST="0.0.0.0"
FRONTEND_CONTAINER_NAME=iot-frontend
FRONTEND_IMAGE_NAME=iot-frontend

OPERATOR_USERNAME=admin
OPERATOR_PASSWORD=secret

SECRET_KEY=<PUT YOUR SECRET HERE>
ALGORITHM="HS256"

# use 'http://localhost:${BACKEND_PORT}/api/v1' if you do not run app in docker
BACKEND_URL='http://${BACKEND_CONTAINER_NAME}:${BACKEND_PORT}/api/v1'
```

## Run application

Application can run directly on host or within docker containers.

### Running directly on host

Run backend

``` bash

cd backend
poetry shell
poetry install (requried only if it is the first app launch on the system)
export PYTHONPATH=.
python app/main.py
```

Run frontend

``` bash

cd frontend
poetry shell
poetry install (requried only if it is the first app launch on the system)
python index.py

```

Now you can go to `localhost:${BACKEND_PORT}/docs` (BACKEND_PORT is set in `.env` file) to check the API documentation. Frontend is served on `localhost:${FRONTEND_PORT}/dash`.

### Running within containers

Alternatively, you can build docker images with the `setup.sh` and run both services with the same script.

---
NOTE: `setup.sh` requires some env variables to be set. So either export them manualy or define them in `.env` file.

---

``` bash

$ bash setup.sh  # build images
+ '[' -f .env ']'
+ source .env
++ REGISTRY_HOST=localhost:5000
++ BACKEND_PORT=8000
...
$ bash setup.sh run  # run both containers
```

You can use `docker ps` to verify if containers are up.

In order to initialize app database with sample data run `init_sample_db.sh`.
