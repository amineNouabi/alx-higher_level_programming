#!/bin/bash
# Send a GET request to the URL provided as the first argument
response=$(curl -s -w "%{http_code}" -o temp_body.txt "$1")

# Check if the status code is 200
if [ "$response" -eq 200 ]; then
	# Display the body of the response
	cat temp_body.txt
fi

# Clean up temporary file
rm temp_body.txt
