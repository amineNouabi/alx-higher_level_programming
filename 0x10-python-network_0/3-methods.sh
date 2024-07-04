#!/bin/bash
# Fetch Allowed Methods from server
curl -si -X OPTIONS "$1" | grep "Allow:" | awk -F': ' '{print $2}'
