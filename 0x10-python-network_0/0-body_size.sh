#!/bin/bash
# Takes in a URL, sends a request to that URL,
# and displays the size of the body of the response.

curl -Iso ~/111 $1
grep -o '(?<=Content-Length: )\d+' ~/111
rm ~/111
