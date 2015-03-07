import json
import urlparse
import httplib, urllib

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
		print URL
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
			print fcn['dal.function.UID']
			ops = fcn['dal.function.operation.names']
			props = fcn['dal.function.property.names']
			if(len(ops)!=0):
				print "\toperations: " + ','.join(ops) #thanks http://www.decalage.info/en/python/print_list 
			if(len(props)!=0):
				print "\tproperties: " + ','.join(props) 		
			print "\n"



