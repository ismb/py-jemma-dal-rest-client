#!/bin/python

from DALClient import *
import signal
import sys
from time import sleep
from random import randint
import collections

DAL_ADDR="home-dal"
L = ['ZigBee:ColorLight 1:ah.app.6623462357111102-11',"ZigBee:ColorLight 2:ah.app.6623462357111156-11","ZigBee:ColorLight 3:ah.app.6623462355301534-11","ZigBee:ColorLight 4:ah.app.6623462357112017-11","ZigBee:Striscia 5:ah.app.6623462354059585-11","ZigBee:Striscia 6:ah.app.6623462354059559-11"]
SLEEPTIME=1;

COLORS = collections.deque([(253,253),(40,253),(80,253),(120,253),(160,253),(200,253)]);
VALUES = collections.deque([253,10,10,10,10,10]);
#COLORS.rotate(1)
#print COLORS[0]
#print COLORS[1][0]
#print COLORS[1][1]
#
def run_program():
	global DAL_ADDR
	global L
	global SLEEPTIME
	
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
		print str(i)
		COLORS.rotate(1)
		VALUES.rotate(1)
		DALClient.request_property_write(DAL_ADDR,L[0],"ColorControl","HS",'[{"type":"java.lang.Short","value":"'+str(COLORS[0][0])+'"},{"type":"java.lang.Short","value":"'+str(COLORS[0][1])+'"}]');
		DALClient.request_property_write(DAL_ADDR,L[0],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"'+str(VALUES[0])+'"}]');
		DALClient.request_property_write(DAL_ADDR,L[1],"ColorControl","HS",'[{"type":"java.lang.Short","value":"'+str(COLORS[1][0])+'"},{"type":"java.lang.Short","value":"'+str(COLORS[1][1])+'"}]');
		DALClient.request_property_write(DAL_ADDR,L[1],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"'+str(VALUES[1])+'"}]');
		DALClient.request_property_write(DAL_ADDR,L[2],"ColorControl","HS",'[{"type":"java.lang.Short","value":"'+str(COLORS[2][0])+'"},{"type":"java.lang.Short","value":"'+str(COLORS[2][1])+'"}]');
		DALClient.request_property_write(DAL_ADDR,L[2],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"'+str(VALUES[2])+'"}]');
		DALClient.request_property_write(DAL_ADDR,L[3],"ColorControl","HS",'[{"type":"java.lang.Short","value":"'+str(COLORS[3][0])+'"},{"type":"java.lang.Short","value":"'+str(COLORS[3][1])+'"}]');
		DALClient.request_property_write(DAL_ADDR,L[3],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"'+str(VALUES[3])+'"}]');
		DALClient.request_property_write(DAL_ADDR,L[4],"ColorControl","HS",'[{"type":"java.lang.Short","value":"'+str(COLORS[4][0])+'"},{"type":"java.lang.Short","value":"'+str(COLORS[4][1])+'"}]');
		DALClient.request_property_write(DAL_ADDR,L[4],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"'+str(VALUES[4])+'"}]');
		DALClient.request_property_write(DAL_ADDR,L[5],"ColorControl","HS",'[{"type":"java.lang.Short","value":"'+str(COLORS[5][0])+'"},{"type":"java.lang.Short","value":"'+str(COLORS[5][1])+'"}]');
		DALClient.request_property_write(DAL_ADDR,L[5],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"'+str(VALUES[5])+'"}]');
		if(i%6==0):
			#to create some asyncronicity
			VALUES.rotate(1)	
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
	print "Ok."
	sys.exit(0)


if __name__ == '__main__':
	signal.signal(signal.SIGINT, Exit_gracefully)
	run_program()

