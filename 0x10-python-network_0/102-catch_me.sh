#!/bin/bash
# request to 0.0.0.0:5000/catch_me results in  a message You got me!
curl -sL -X PUT 0.0.0.0:5000/catch_me
