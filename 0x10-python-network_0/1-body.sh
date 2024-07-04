#!/bin/bash
# Make a get request to arg passed URL and prints response body to std out if status is 200
curl -X GET -s -w "%{http_code}" "$1" | grep -q '200$' && curl -s "$1"
