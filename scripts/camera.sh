#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

raspistill -w 640 -h 480 -o /home/pi/camera/$DATE.jpg -n
