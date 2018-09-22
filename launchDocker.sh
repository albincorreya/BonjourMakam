#!/bin/bash

echo "Building docker image"
docker build -t hamrdocker .

echo "Launching docker.."
docker run -it --rm --name hamr_docker hamrdocker bash
