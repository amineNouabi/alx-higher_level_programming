#!/bin/bash
# Send GET request with a Header variable set
curl -s -X GET -H "X-School-User-Id: 98" "$1"
