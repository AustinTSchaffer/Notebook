#!/bin/bash

echo "============================================="
echo "Testing 'env.Dockerfile'"
echo "Build image once, then try multiple printenvs" 
echo "under different conditions."
echo "============================================="

docker build -t docker-certification/testenv -f ./env.Dockerfile .

echo "Incoming terminal spam..."

echo "=========================="
echo "TEST 1 - No ENV Overwrites"
echo "=========================="

docker container run --rm docker-certification/testenv printenv

echo "=========================="
echo "TEST 2 - One ENV Overwrite"
echo "=========================="

docker container run --rm \
    -e MYVAR="Some new value for MYVAR" \
    docker-certification/testenv printenv

echo "================================"
echo "TEST 3 - Multiple ENV Overwrites"
echo "================================"

docker container run --rm \
    -e MYVAR="Some new value for MYVAR" \
    -e TEST_MULTILINE_VAR_2="Some new value for TEST_MULTILINE_VAR_2" \
    docker-certification/testenv printenv

echo "====================================="
echo "TEST 4 - One Variable Specified Twice"
echo "====================================="

docker container run --rm \
    -e MYVAR="Some new value for MYVAR" \
    -e TEST_MULTILINE_VAR_2="Some new value for TEST_MULTILINE_VAR_2" \
    -e MYVAR="A different value for MYVAR" \
    docker-certification/testenv printenv

echo "================================="
echo "TEST 5 - Overwrite Variable (DNE)"
echo "================================="

docker container run \
    --rm \
    -e THIS_VAR_DNE="What does this do?" \
    docker-certification/testenv printenv

echo "==================================="
echo "Done with tests, deleting the image"
echo "==================================="

docker image rm docker-certification/testenv
