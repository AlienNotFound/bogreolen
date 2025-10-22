#!/bin/sh

set -e
host="$MYSQL_HOST"
user="root"
port="3306"
password="$MYSQL_ROOT_PASSWORD"
mysql_admin=/usr/bin/mariadb-admin

echo "Waiting for MySQL at $host..."
until $mysql_admin ping -h "$MYSQL_HOST" -uroot -p"$MYSQL_ROOT_PASSWORD" --silent --ssl=0; do
  sleep 2
  echo "MySQL not ready, retrying..."
done

echo "MySQL is ready!"
