#!/usr/bin/env bash

pid_workers="$(pidof python)"
if [ ! -z "$pid_workers" ]; then
    kill -9 ${pid_workers}
fi

python /var/www/FAHS/scripts/grapper.py > /dev/null &
