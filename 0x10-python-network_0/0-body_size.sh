#!/bin/bash
# This script sends a request to a URL and displays the size of the body of the response
curl -is "$1" | grep "Content-Length" | tr -s " " | cut -d":" -f2
