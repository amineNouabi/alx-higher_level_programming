#!/bin/bash
# Send POST req with plain data as query params
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
