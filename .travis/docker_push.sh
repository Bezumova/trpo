#!/bin/sh

docker login -u "bezumova" -p "$DOCKER_PASSWORD"
docker push bezumova/trpo
