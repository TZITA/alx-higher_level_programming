#!/bin/bash
# sends a GET request with a new header variable
curl -sH "X-School-User-Id: 98" "$1"
