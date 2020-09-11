#!/bin/bash
set -o errexit

sed -i \
  -e "s/PORT/${APP_PORT}/g" \
  /etc/nginx/sites-available/test-api

/usr/sbin/nginx -g "error_log /dev/stdout info;"

exec "$@"