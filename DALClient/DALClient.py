import json
import urlparse
import httplib, urllib
import re

class DALClient(object):
	
	def __init__(self,dal_addr):
		self.dal_addr = dal_addr
		
	
	def request_devices_list(self):
		URL = "http://" + self.dal_addr + "/api/devices"
		#print "calling: ", URL
		HEADERS = {"Content-Type":"application/json"}
		domain = urlparse.urlparse(URL).netloc
		connection = httplib.HTTPConnection(domain)
		connection.request("GET", URL, headers=HEADERS)
		rawresponse = connection.getresponse()
		raws = rawresponse.read()
		# this is to de-serialize the json
		deviceslist = json.loads(raws)
		code = deviceslist['code']
		#print "result: " + str(code)
		deviceslist = deviceslist['result']
		#print str(len(deviceslist)) + " devices available:\n"
		#print deviceslist
		#printing device UIDs
		for dev in deviceslist:
			print dev['dal.device.UID']


	def request_functions_list(self,devname):
		DEV_NAME = urllib.quote_plus(devname)
		URL = "http://" + self.dal_addr + "/api/devices/" +DEV_NAME+"/functions"
		#print "calling: ", URL
		HEADERS = {"Content-Type":"application/json"}
		domain = urlparse.urlparse(URL).netloc
		connection = httplib.HTTPConnection(domain)
		connection.request("GET", URL, headers=HEADERS)
		rawresponse = connection.getresponse()
		# this is to de-serialize the json
		functionlist = json.loads(rawresponse.read())
		code = functionlist['code']
		#print "result: " + str(code)
		functionlist = functionlist['result']
		#print str(len(functionlist)) + " functions available:\n"
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

	def request_operation(self,devname,fcn,op):
		DEV_NAME = urllib.quote_plus(devname)
		FCN_NAME = urllib.quote_plus(fcn)
		URL = "http://" + self.dal_addr + "/api/functions/" +DEV_NAME+":"+FCN_NAME
		#print "calling: ", URL
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
			return "OK";
		else:
			return "Error " + str(code) + ": " + response

	def request_property_read(self,devname,fcn,prop):
		DEV_NAME = urllib.quote_plus(devname)
		FCN_NAME = urllib.quote_plus(fcn)
		URL = "http://" + self.dal_addr + "/api/functions/" +DEV_NAME+":"+FCN_NAME
		#print "calling: ", URL
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
			#print json.dumps(res['result'], sort_keys=True,indent=4, separators=(',', ': ')) #thanks https://docs.python.org/2/library/json.html
			return json.dumps(res['result'])
		else:
			return "Error " + str(code) + ": " + response


	def request_property_write(self,devname,fcn,prop,value):
		DEV_NAME = urllib.quote_plus(devname)
		FCN_NAME = urllib.quote_plus(fcn)
		URL = "http://" + self.dal_addr + "/api/functions/" +DEV_NAME+":"+FCN_NAME
		#print "calling: ", URL
		myprop= prop
		myprop = re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), myprop, 1) # thanks http://stackoverflow.com/questions/12410242/python-capitalize-first-letter-only
		OPERATION = "set" + myprop
		HEADERS = {"Content-Type":"application/json"}
		params = "{operation: '"+OPERATION+"',arguments: "+value+"}"
		#print params
		domain = urlparse.urlparse(URL).netloc
		connection = httplib.HTTPConnection(domain)
		connection.request("POST", URL, params, HEADERS)
		rawresponse = connection.getresponse()
		# this is to de-serialize the json
		response=rawresponse.read()
		#print response
		res = json.loads(response)
		code = res['code'];
		if(code==200):
			return "OK"
		else:
			return "Error " + str(code) + ": " + response
