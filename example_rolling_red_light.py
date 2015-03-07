#!/bin/python

from DALClient import *
import signal
import sys
from time import sleep

DAL_ADDR="home-dal"
L = ['ZigBee:ColorLight 1:ah.app.6623462357111102-11',"ZigBee:ColorLight 2:ah.app.6623462357111156-11","ZigBee:ColorLight 3:ah.app.6623462355301534-11","ZigBee:ColorLight 4:ah.app.6623462357112017-11","ZigBee:Striscia 5:ah.app.6623462354059585-11","ZigBee:Striscia 6:ah.app.6623462354059559-11"]
SLEEPTIME=0.5;

def run_program():
	global DAL_ADDR
	global L
	global SLEEPTIME

	#turn of everything
	DALClient.request_operation(DAL_ADDR,L[0],"OnOff","setFalse");
	DALClient.request_operation(DAL_ADDR,L[1],"OnOff","setFalse");
	DALClient.request_operation(DAL_ADDR,L[2],"OnOff","setFalse");
	DALClient.request_operation(DAL_ADDR,L[3],"OnOff","setFalse");
	DALClient.request_operation(DAL_ADDR,L[4],"OnOff","setFalse");
	DALClient.request_operation(DAL_ADDR,L[5],"OnOff","setFalse");


	#set all to dark value
	#DALClient.request_property_write(DAL_ADDR,L[0],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"0"}]');

	#set all to red hue/saturation
	#DALClient.request_property_write(DAL_ADDR,L[0],"ColorControl","HS",'[{"type":"java.lang.Short","value":"253"},{"type":"java.lang.Short","value":"253"}]');
	
	# loop values
	i=0;
	while (True):
		current = i % len(L)
		print "Light " + str(current) + " UP";
		DALClient.request_property_write(DAL_ADDR,L[current],"ColorControl","HS",'[{"type":"java.lang.Short","value":"253"},{"type":"java.lang.Short","value":"253"}]');
		DALClient.request_operation(DAL_ADDR,L[current],"OnOff","setTrue");
		sleep(SLEEPTIME);
		print "Light " + str(current) + " DOWN";
		DALClient.request_operation(DAL_ADDR,L[current],"OnOff","setFalse");
		i+=1;


def Exit_gracefully(signal, frame):
	global DAL_ADDR,L
	print "Exiting gracefully... "
	DALClient.request_operation(DAL_ADDR,L[0],"OnOff","setFalse");
	DALClient.request_operation(DAL_ADDR,L[1],"OnOff","setFalse");
	DALClient.request_operation(DAL_ADDR,L[2],"OnOff","setFalse");
	DALClient.request_operation(DAL_ADDR,L[3],"OnOff","setFalse");
	DALClient.request_operation(DAL_ADDR,L[4],"OnOff","setFalse");
	DALClient.request_operation(DAL_ADDR,L[5],"OnOff","setFalse");
	print "Ok."
	sys.exit(0)


if __name__ == '__main__':
	signal.signal(signal.SIGINT, Exit_gracefully)
	run_program()

