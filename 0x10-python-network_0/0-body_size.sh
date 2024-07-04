#!/usr/bin/env bash
# This script sends a request to a URL and displays the size of the body of the response

if [ $# -ne 1 ]; then
	echo "Usage: $0 URL"
	exit 1
fi

curl -is "$1" | grep "Content-Length" | tr -s " " | cut -d":" -f2
