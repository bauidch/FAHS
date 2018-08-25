#!/bin/bash

DATE=$(date +"%d.%m.%Y_%H%M")

fswebcam -r 1280x720 --title "FAHS" --subtitle "Cam 1" /home/pi/webcam/$DATE.jpg
