#!/bin/bash
rdb_file="./dump.rdb"
redis_cli="/usr/local/bin/redis-cli"

timestamp=`date +%s`
cp $rdb_file "$timestamp.rdb"

echo save| $redis_cli
exit 1