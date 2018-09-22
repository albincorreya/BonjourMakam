#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "USAGE: ./launchDocker.sh <scripts_folder_path> "
	exit
fi

echo "Building docker image"
docker build -t hamrdocker .

echo "Launching docker.."
docker run -it --rm --name hamr_docker  -v $1:/srv/workspace/ hamrdocker bash

