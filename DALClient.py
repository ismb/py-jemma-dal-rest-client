import json
import urlparse
import httplib, urllib
import re

class DALClient(object):
	
	@staticmethod
	def request_devices_list(dal_addr):
		URL = "http://" + dal_addr + "/api/devices"
		print URL
		HEADERS = {"Content-Type":"application/json"}
		domain = urlparse.urlparse(URL).netloc
		connection = httplib.HTTPConnection(domain)
		connection.request("GET", URL, headers=HEADERS)
		rawresponse = connection.getresponse()
		# this is to de-serialize the json
		deviceslist = json.loads(rawresponse.read())
		print str(len(deviceslist)) + " devices available:\n"
		#printing device UIDs
		for dev in deviceslist:
			print dev['dal.device.UID']


	@staticmethod
	def request_functions_list(dal_addr,devname):
		DEV_NAME = urllib.quote_plus(devname)
		URL = "http://" + dal_addr + "/api/devices/" +DEV_NAME+"/functions"
		#print URL
		HEADERS = {"Content-Type":"application/json"}
		domain = urlparse.urlparse(URL).netloc
		connection = httplib.HTTPConnection(domain)
		connection.request("GET", URL, headers=HEADERS)
		rawresponse = connection.getresponse()
		# this is to de-serialize the json
		functionlist = json.loads(rawresponse.read())
		print str(len(functionlist)) + " functions available:\n"
		#printing device UIDs
		for fcn in functionlist:
			myfcn = fcn['dal.function.UID']
			myfcn = myfcn.replace(devname + ":","");
			print myfcn
			ops = fcn['dal.function.operation.names']
			props = fcn['dal.function.property.names']
			if(len(ops)!=0):
				print "\toperations: " + ','.join(ops) #thanks http://www.decalage.info/en/python/print_list 
			if(len(props)!=0):
				print "\tproperties: " + ','.join(props) 		
			print "\n"


	@staticmethod
	def request_operation(dal_addr,devname,fcn,op):
		DEV_NAME = urllib.quote_plus(devname)
		FCN_NAME = urllib.quote_plus(fcn)
		URL = "http://" + dal_addr + "/api/functions/" +DEV_NAME+":"+FCN_NAME
		#print URL
		OPERATION = op
		HEADERS = {"Content-Type":"application/json"}
		params = "{operation: '"+OPERATION+"'}"
		
		domain = urlparse.urlparse(URL).netloc
		connection = httplib.HTTPConnection(domain)
		connection.request("POST", URL, params, HEADERS)
		rawresponse = connection.getresponse()
		# this is to de-serialize the json
		response=rawresponse.read()
		res = json.loads(response)
		code = res['code'];
		if(code==200):
			print "\tOK";
		else:
			print "Error " + str(code) + ": " + response

	@staticmethod
	def request_property_read(dal_addr,devname,fcn,prop):
		DEV_NAME = urllib.quote_plus(devname)
		FCN_NAME = urllib.quote_plus(fcn)
		URL = "http://" + dal_addr + "/api/functions/" +DEV_NAME+":"+FCN_NAME
		#print URL
		myprop= prop
		myprop = re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), myprop, 1) # thanks http://stackoverflow.com/questions/12410242/python-capitalize-first-letter-only
		OPERATION = "get" + myprop
		HEADERS = {"Content-Type":"application/json"}
		params = "{operation: '"+OPERATION+"'}"
		
		domain = urlparse.urlparse(URL).netloc
		connection = httplib.HTTPConnection(domain)
		connection.request("POST", URL, params, HEADERS)
		rawresponse = connection.getresponse()
		# this is to de-serialize the json
		response=rawresponse.read()
		res = json.loads(response)
		code = res['code'];
		if(code==200):
			print json.dumps(res['result'], sort_keys=True,indent=4, separators=(',', ': ')) #thanks https://docs.python.org/2/library/json.html
		else:
			print "Error " + str(code) + ": " + response


