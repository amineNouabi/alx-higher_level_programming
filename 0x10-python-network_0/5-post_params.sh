#!/bin/bash
# Send POST req with plain data as query params
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
