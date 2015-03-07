#!/bin/python

from DALClient import *
import signal
import sys
from time import sleep
from random import randint

DAL_ADDR="home-dal"
L = ['ZigBee:ColorLight 1:ah.app.6623462357111102-11',"ZigBee:ColorLight 2:ah.app.6623462357111156-11","ZigBee:ColorLight 3:ah.app.6623462355301534-11","ZigBee:ColorLight 4:ah.app.6623462357112017-11","ZigBee:Striscia 5:ah.app.6623462354059585-11","ZigBee:Striscia 6:ah.app.6623462354059559-11"]
SLEEPTIME=0.5;

B = "ZigBee:Disco Ball Colorata:ah.app.5149012995480293-1"

def run_program():
	global DAL_ADDR
	global L
	global SLEEPTIME
	
	#Turning on DiscoBall
	DALClient.request_operation(DAL_ADDR,B,"OnOff","setTrue");

	#turn of everything
	DALClient.request_operation(DAL_ADDR,L[0],"OnOff","setTrue");
	DALClient.request_operation(DAL_ADDR,L[1],"OnOff","setTrue");
	DALClient.request_operation(DAL_ADDR,L[2],"OnOff","setTrue");
	DALClient.request_operation(DAL_ADDR,L[3],"OnOff","setTrue");
	DALClient.request_operation(DAL_ADDR,L[4],"OnOff","setTrue");
	DALClient.request_operation(DAL_ADDR,L[5],"OnOff","setTrue");

	#set all to bright value
	DALClient.request_property_write(DAL_ADDR,L[0],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"253"}]');
	DALClient.request_property_write(DAL_ADDR,L[1],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"253"}]');
	DALClient.request_property_write(DAL_ADDR,L[2],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"253"}]');
	DALClient.request_property_write(DAL_ADDR,L[3],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"253"}]');
	DALClient.request_property_write(DAL_ADDR,L[4],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"253"}]');
	DALClient.request_property_write(DAL_ADDR,L[5],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"253"}]');

	# loop values
	i=0;
	while (True):
		current = randint(0,5)
		h = randint(1,253)
		s = randint(1,253)
		print "Light " + str(current) + "->("+str(h)+","+str(s)+")";
		DALClient.request_property_write(DAL_ADDR,L[current],"ColorControl","HS",'[{"type":"java.lang.Short","value":"'+str(h)+'"},{"type":"java.lang.Short","value":"'+str(s)+'"}]');
		sleep(SLEEPTIME);
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
	#Turning on DiscoBall
	DALClient.request_operation(DAL_ADDR,B,"OnOff","setFalse");
	print "Ok."
	sys.exit(0)


if __name__ == '__main__':
	signal.signal(signal.SIGINT, Exit_gracefully)
	run_program()

