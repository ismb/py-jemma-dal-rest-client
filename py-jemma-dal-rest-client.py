#!/usr/bin/python

# This example just calls some DAL functions exposed by JEMMA
# Tested with JEMMA v0.9
# Made by: Riccardo <tomasi@ismb.it>

import sys, getopt
from DALClient import DALClient

def main(argv):
	HELPTEXT = "\nUsage: ./py-jemma-dal-rest-client -d <address-of-DAL-endpoint> -c <command> ...\n"

	# Based on example from http://www.tutorialspoint.com/python/python_command_line_arguments.htm

	dal_addr = ''
	cmd = ''
	dev = ''
	fcn= ''
	op = ''
	prop=""
	value=""
	
	mydal="";
	
	try:
		opts, args = getopt.getopt(argv,"ha:c:d:f:o:p:v:",["addr=","cmd=","help","dev=","fcn=","op=","prop=","value="])
	except getopt.GetoptError:
		print HELPTEXT
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print HELPTEXT
			sys.exit()
		elif opt in ("-a", "--addr"):
			dal_addr = arg
		elif opt in ("-c", "--cmd"):
			cmd = arg
		elif opt in ("-d", "--dev"):
			dev = arg			
		elif opt in ("-f", "--fcn"):
			fcn = arg			
		elif opt in ("-o", "--op"):
			op = arg			
		elif opt in ("-p", "--prop"):
			prop = arg	
		elif opt in ("-v", "--value"):
			value = arg	
						
	if (dal_addr == ''):
		print "missing address-of-DAL-endpoint"
		print HELPTEXT
		sys.exit()
	else:
		print "DAL endpoint: " + dal_addr
		mydal = DALClient.DALClient(dal_addr);
	
	if (cmd == ''):
		print "missing cmd"
		print HELPTEXT
		sys.exit()

	if (cmd == 'listd'):
		print "\nListing devices for DAL " + dal_addr + "\n"
		mydal.request_devices_list();
		print "\n"
	elif (cmd == 'listf'):
		if (dev == ''):
			print "missing dev"
			print HELPTEXT
			sys.exit()		
		print "\nListing functions for device \""+dev+"\" for DAL " + dal_addr + "\n"
		mydal.request_functions_list(dev);
		print "\n"
	elif (cmd == 'operate'):
		if (dev == ''):
			print "missing dev"
			print HELPTEXT
			sys.exit()		
		if (fcn == ''):
			print "missing fcn"
			print HELPTEXT
			sys.exit()		
		if (op == ''):
			print "missing op"
			print HELPTEXT
			sys.exit()		
		print "\nOperating function \""+fcn+"\" with op \""+op+"\" on device \""+dev+"\" for DAL " + dal_addr + "\n"
		res = mydal.request_operation(dev,fcn,op);
		print res + "\n"
	elif (cmd == 'read'):
		if (dev == ''):
			print "missing dev"
			print HELPTEXT
			sys.exit()		
		if (fcn == ''):
			print "missing fcn"
			print HELPTEXT
			sys.exit()		
		if (prop == ''):
			print "missing prop"
			print HELPTEXT
			sys.exit()		
		print "\nReading property \""+prop+"\" on function \""+fcn+"\" on device \""+dev+"\" for DAL " + dal_addr + "\n"
		res = mydal.request_property_read(dev,fcn,prop);
		print res + "\n"
	elif (cmd == 'write'):
		if (dev == ''):
			print "missing dev"
			print HELPTEXT
			sys.exit()		
		if (fcn == ''):
			print "missing fcn"
			print HELPTEXT
			sys.exit()		
		if (prop == ''):
			print "missing prop"
			print HELPTEXT
			sys.exit()		
		if (value == ''):
			print "missing value"
			print HELPTEXT
			sys.exit()
		print "\nWriting property \""+prop+"\" on function \""+fcn+"\" on device \""+dev+"\" for DAL " + dal_addr + " to value: "+value+"\n"
		res = mydal.request_property_write(dev,fcn,prop,value);
		print res + "\n"
	else:
		print "Unknown command: " + cmd
		print HELPTEXT
		sys.exit()


if __name__ == "__main__":
   main(sys.argv[1:])
