#!/usr/bin/python

# This example just calls some DAL functions exposed by JEMMA
# Tested with JEMMA v0.9
# Made by: Riccardo <tomasi@ismb.it>

import sys, getopt
from DALClient import *

def main(argv):
	HELPTEXT = "\nUsage: ./py-jemma-dal-rest-client -d <address-of-DAL-endpoint> -c <command> ...\n"
	dal_addr = ''
	cmd = ''
	dev = ''
	fcn= ''
	op = ''
	# Based on example from http://www.tutorialspoint.com/python/python_command_line_arguments.htm
	
	try:
		opts, args = getopt.getopt(argv,"ha:c:d:f:o:",["addr=","cmd=","help","dev=","fcn=","op="])
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
	
	if (dal_addr == ''):
		print "missing address-of-DAL-endpoint"
		print HELPTEXT
		sys.exit()

	if (cmd == ''):
		print "missing cmd"
		print HELPTEXT
		sys.exit()

	if (cmd == 'listd'):
		print "\nListing devices for DAL " + dal_addr + "\n"
		DALClient.request_devices_list(dal_addr);
		print "\n"
	elif (cmd == 'listf'):
		if (dev == ''):
			print "missing dev"
			print HELPTEXT
			sys.exit()		
		print "\nListing functions for device \""+dev+"\" for DAL " + dal_addr + "\n"
		DALClient.request_functions_list(dal_addr,dev);
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
		DALClient.request_operation(dal_addr,dev,fcn,op);
		print "\n"
	else:
		print "Unknown command: " + cmd
		print HELPTEXT
		sys.exit()


if __name__ == "__main__":
   main(sys.argv[1:])
