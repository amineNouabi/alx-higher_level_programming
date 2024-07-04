#!/bin/bash
# Send GET request with a Header variable set
curl -si -X GET -H "X-School-User-Id: 98" "$1"
