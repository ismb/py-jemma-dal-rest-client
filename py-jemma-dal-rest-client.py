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
	
	# Based on example from http://www.tutorialspoint.com/python/python_command_line_arguments.htm
	
	try:
		opts, args = getopt.getopt(argv,"ha:c:d:",["addr=","cmd=","help","dev="])
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
		print "\nListing functions for device \""+dev+"\" for DAL " + dal_addr + "\n"
		DALClient.request_functions_list(dal_addr,dev);
		print "\n"
	else:
		print "Unknown command: " + cmd
		print HELPTEXT
		sys.exit()


if __name__ == "__main__":
   main(sys.argv[1:])
