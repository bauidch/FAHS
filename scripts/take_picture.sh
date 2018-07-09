#!/bin/bash

DATE=$(date +"%d.%m.%Y_%H%M")

fswebcam -r 1280x720 --no-banner /home/pi/webcam/$DATE.jpg