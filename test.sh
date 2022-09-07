#!/bin/sh

set -x

curl -X POST http://0.0.0.0:3000/urls/ \
    -H 'Content-Type: application/json' \
    -d '{"long_url":"https://hello.url/long/long/long"}'


curl -X GET http://0.0.0.0:3000/urls/aaa
curl -X GET http://0.0.0.0:3000/urls/aaa
curl -X GET http://0.0.0.0:3000/urls/aaa
curl -X GET http://0.0.0.0:3000/urls/aaa
curl -X GET http://0.0.0.0:3000/urls/aaa
curl -X GET http://0.0.0.0:3000/urls/aaa
curl -X GET http://0.0.0.0:3000/urls/aaa
curl -X GET http://0.0.0.0:3000/urls/aaa
curl -X GET http://0.0.0.0:3000/urls/aaa

curl -X PUT http://0.0.0.0:3000/urls/aaa \
    -H 'Content-Type: application/json' \
    -d '{"long_url":"https://hello.url/other/long"}'


curl -X GET http://0.0.0.0:3000/urls/aaa

curl -X GET http://0.0.0.0:3000/urls/aaa/stats

curl -X DELETE http://0.0.0.0:3000/urls/aaa
curl -X GET http://0.0.0.0:3000/urls/aaa/stats
curl -X GET http://0.0.0.0:3000/urls/aaa