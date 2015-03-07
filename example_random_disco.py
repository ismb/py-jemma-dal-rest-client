#!/bin/bash

# Just print functions of interested devices

DAL_ADDR=home-dal

./py-jemma-dal-rest-client.py -a $DAL_ADDR -c listd 
./py-jemma-dal-rest-client.py -a $DAL_ADDR -c listf -d "ZigBee:ColorLight 1:ah.app.6623462357111102-11"
./py-jemma-dal-rest-client.py -a $DAL_ADDR -c listf -d "ZigBee:ColorLight 2:ah.app.6623462357111156-11"
./py-jemma-dal-rest-client.py -a $DAL_ADDR -c listf -d "ZigBee:ColorLight 3:ah.app.6623462355301534-11"
./py-jemma-dal-rest-client.py -a $DAL_ADDR -c listf -d "ZigBee:ColorLight 4:ah.app.6623462357112017-11"
./py-jemma-dal-rest-client.py -a $DAL_ADDR -c listf -d "ZigBee:Striscia 5:ah.app.6623462354059585-11"
./py-jemma-dal-rest-client.py -a $DAL_ADDR -c listf -d "ZigBee:Striscia 6:ah.app.6623462354059559-11"
./py-jemma-dal-rest-client.py -a $DAL_ADDR -c listf -d "ZigBee:Disco Ball Colorata:ah.app.5149012995480293-1"



