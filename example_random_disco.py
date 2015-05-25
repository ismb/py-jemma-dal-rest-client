#!/bin/python

from DALClient import DALClient
import signal
import sys
from time import sleep
from random import randint

DAL_ADDR="home-dal"
L = ['ZigBee:Applique 1:ah.app.6623462357111102-11',"ZigBee:Applique 2:ah.app.6623462357111156-11","ZigBee:Applique 3:ah.app.6623462355301534-11","ZigBee:Applique 4:ah.app.6623462357112017-11","ZigBee:Ledstrip 1:ah.app.6623462354059585-11","ZigBee:Ledstrip 2:ah.app.6623462354059559-11"]
SLEEPTIME=0.5;

B = "ZigBee:DiscoBall:ah.app.5149012995480293-1"

def run_program():
	global DAL_ADDR
	global L
	global SLEEPTIME
	global mydal
	
	mydal = DALClient.DALClient(DAL_ADDR);
	
	#Turning on DiscoBall
	mydal.request_operation(B,"OnOff","setTrue");

	#turn of everything
	mydal.request_operation(L[0],"OnOff","setTrue");
	mydal.request_operation(L[1],"OnOff","setTrue");
	mydal.request_operation(L[2],"OnOff","setTrue");
	mydal.request_operation(L[3],"OnOff","setTrue");
	mydal.request_operation(L[4],"OnOff","setTrue");
	mydal.request_operation(L[5],"OnOff","setTrue");

	#set all to bright value
	mydal.request_property_write(L[0],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"253"}]');
	mydal.request_property_write(L[1],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"253"}]');
	mydal.request_property_write(L[2],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"253"}]');
	mydal.request_property_write(L[3],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"253"}]');
	mydal.request_property_write(L[4],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"253"}]');
	mydal.request_property_write(L[5],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"253"}]');

	# loop values
	i=0;
	while (True):
		current = randint(0,5)
		h = randint(1,253)
		s = randint(1,253)
		print "Light " + str(current) + "->("+str(h)+","+str(s)+")";
		mydal.request_property_write(L[current],"ColorControl","HS",'[{"type":"java.lang.Short","value":"'+str(h)+'"},{"type":"java.lang.Short","value":"'+str(s)+'"}]');
		sleep(SLEEPTIME);
		i+=1;


def Exit_gracefully(signal, frame):
	global DAL_ADDR,L,mydal
	print "Exiting gracefully... "
	mydal.request_operation(L[0],"OnOff","setFalse");
	mydal.request_operation(L[1],"OnOff","setFalse");
	mydal.request_operation(L[2],"OnOff","setFalse");
	mydal.request_operation(L[3],"OnOff","setFalse");
	mydal.request_operation(L[4],"OnOff","setFalse");
	mydal.request_operation(L[5],"OnOff","setFalse");
	#Turning on DiscoBall
	mydal.request_operation(B,"OnOff","setFalse");
	print "Ok."
	sys.exit(0)


if __name__ == '__main__':
	signal.signal(signal.SIGINT, Exit_gracefully)
	run_program()

