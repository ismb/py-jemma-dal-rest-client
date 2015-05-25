#!/bin/python

from DALClient import DALClient
import signal
import sys
from time import sleep
from random import randint
import collections

DAL_ADDR="home-dal"
L = ['ZigBee:Applique 1:ah.app.6623462357111102-11',"ZigBee:Applique 2:ah.app.6623462357111156-11","ZigBee:Applique 3:ah.app.6623462355301534-11","ZigBee:Applique 4:ah.app.6623462357112017-11","ZigBee:Ledstrip 1:ah.app.6623462354059585-11","ZigBee:Ledstrip 2:ah.app.6623462354059559-11"]


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
	global mydal
	
	mydal = DALClient.DALClient(DAL_ADDR);
	
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
		print str(i)
		COLORS.rotate(1)
		VALUES.rotate(1)
		mydal.request_property_write(L[0],"ColorControl","HS",'[{"type":"java.lang.Short","value":"'+str(COLORS[0][0])+'"},{"type":"java.lang.Short","value":"'+str(COLORS[0][1])+'"}]');
		mydal.request_property_write(L[0],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"'+str(VALUES[0])+'"}]');
		mydal.request_property_write(L[1],"ColorControl","HS",'[{"type":"java.lang.Short","value":"'+str(COLORS[1][0])+'"},{"type":"java.lang.Short","value":"'+str(COLORS[1][1])+'"}]');
		mydal.request_property_write(L[1],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"'+str(VALUES[1])+'"}]');
		mydal.request_property_write(L[2],"ColorControl","HS",'[{"type":"java.lang.Short","value":"'+str(COLORS[2][0])+'"},{"type":"java.lang.Short","value":"'+str(COLORS[2][1])+'"}]');
		mydal.request_property_write(L[2],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"'+str(VALUES[2])+'"}]');
		mydal.request_property_write(L[3],"ColorControl","HS",'[{"type":"java.lang.Short","value":"'+str(COLORS[3][0])+'"},{"type":"java.lang.Short","value":"'+str(COLORS[3][1])+'"}]');
		mydal.request_property_write(L[3],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"'+str(VALUES[3])+'"}]');
		mydal.request_property_write(L[4],"ColorControl","HS",'[{"type":"java.lang.Short","value":"'+str(COLORS[4][0])+'"},{"type":"java.lang.Short","value":"'+str(COLORS[4][1])+'"}]');
		mydal.request_property_write(L[4],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"'+str(VALUES[4])+'"}]');
		mydal.request_property_write(L[5],"ColorControl","HS",'[{"type":"java.lang.Short","value":"'+str(COLORS[5][0])+'"},{"type":"java.lang.Short","value":"'+str(COLORS[5][1])+'"}]');
		mydal.request_property_write(L[5],"MultiLevelControl","data",'[{"type":"java.math.BigDecimal","value":"'+str(VALUES[5])+'"}]');
		if(i%6==0):
			#to create some asyncronicity
			VALUES.rotate(1)	
		sleep(SLEEPTIME);
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

