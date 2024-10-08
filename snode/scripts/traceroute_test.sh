#!/bin/bash
echo "Bash version ${BASH_VERSION}..."
for i in {0..30..1}
do
  echo "$i Durand"
  meshtastic --port 'com4' --traceroute '!336462e4'
  echo "$i Dish"
  meshtastic --port 'com4' --traceroute '!433f0700'
  echo "$i Jasper Ridge"
  meshtastic --port 'com4' --traceroute '!336918e8'
done
