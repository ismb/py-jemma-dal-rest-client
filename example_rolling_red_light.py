#!/bin/python

from DALClient import DALClient
import signal
import sys
from time import sleep

DAL_ADDR="home-dal"
L = ['ZigBee:Applique 1:ah.app.6623462357111102-11',"ZigBee:Applique 2:ah.app.6623462357111156-11","ZigBee:Applique 3:ah.app.6623462355301534-11","ZigBee:Applique 4:ah.app.6623462357112017-11","ZigBee:Ledstrip 1:ah.app.6623462354059585-11","ZigBee:Ledstrip 2:ah.app.6623462354059559-11"]
SLEEPTIME=0.5;

def run_program():
	global DAL_ADDR
	global L
	global SLEEPTIME
	global mydal
	
	mydal = DALClient.DALClient(DAL_ADDR);

	#turn off everything
	mydal.request_operation(L[0],"OnOff","setFalse");
	mydal.request_operation(L[1],"OnOff","setFalse");
	mydal.request_operation(L[2],"OnOff","setFalse");
	mydal.request_operation(L[3],"OnOff","setFalse");
	mydal.request_operation(L[4],"OnOff","setFalse");
	mydal.request_operation(L[5],"OnOff","setFalse");


	#set all to dark value
	#mydal.request_property_write(L[0],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"0"}]');

	#set all to red hue/saturation
	#mydal.request_property_write(L[0],"ColorControl","HS",'[{"type":"java.lang.Short","value":"253"},{"type":"java.lang.Short","value":"253"}]');
	
	# loop values
	i=0;
	while (True):
		current = i % len(L)
		print "Light " + str(current) + " UP";
		mydal.request_property_write(L[current],"ColorControl","HS",'[{"type":"java.lang.Short","value":"253"},{"type":"java.lang.Short","value":"253"}]');
		mydal.request_operation(L[current],"OnOff","setTrue");
		sleep(SLEEPTIME);
		print "Light " + str(current) + " DOWN";
		mydal.request_operation(L[current],"OnOff","setFalse");
		i+=1;


def Exit_gracefully(signal, frame):
	global DAL_ADDR,L
	print "Exiting gracefully... "
	mydal.request_operation(L[0],"OnOff","setFalse");
	mydal.request_operation(L[1],"OnOff","setFalse");
	mydal.request_operation(L[2],"OnOff","setFalse");
	mydal.request_operation(L[3],"OnOff","setFalse");
	mydal.request_operation(L[4],"OnOff","setFalse");
	mydal.request_operation(L[5],"OnOff","setFalse");
	print "Ok."
	sys.exit(0)


if __name__ == '__main__':
	signal.signal(signal.SIGINT, Exit_gracefully)
	run_program()

