#!/bin/bash
# This script sends a request to a URL passed as an argument, and displays only the status code of the response
curl "$1" -s -o /dev/null -w "%{http_code}"
