#!/bin/bash

set -e

git config pull.rebase false
git config --global --add core.sharedRepository group
git config --global --add safe.directory /movie_recommendations
git fetch
git pull


python3 docker_start.py 5432
python3 csv_parser/Parser.py 5432
