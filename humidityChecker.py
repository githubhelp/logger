#!/usr/bin/python

import time, os, twitter
import readSensor
import ConfigParser

#settings        id        name      threshold
sensorLookUp = {"PIN0" : ("flower1", 500)}

def check():
	sensorReadings = {}
	readings = 0
	while 1:
		try:
			value, id, sensor = readSensor.readSensor()
		except:
			print "not able to get sensor reading",
			continue

		try:
			if sensor != "Humidity":
				continue
			#if sensor have allready have been read then we have 
			#read them all
			if sensorReadings.has_key(sensorLookUp[id][0]):
				break

			sensorReadings[sensorLookUp[id][0]] = int(value)
		except:
			print "ID:", id, "not found in sensorLookUp, please add"
		
	return sensorReadings;

class TweetRc(object):
	def __init__(self):
		self._config = None

	def getUsername(self):
		return self._getOption('username')

	def getPassword(self):
		return self._getOption('password')

	def _getOption(self, option):
		try:
			return self._getConfig().get('Tweet', option)
		except:
			return None

	def _getConfig(self):
		if not self._config:
			self._config = ConfigParser.ConfigParser()
			self._config.read(os.path.expanduser('~/.tweetrc'))
		return self._config


def alarm(name, value):
	print name, "got dry value:", value
	rc = TweetRc()
	api = twitter.Api(username=rc.getUsername(), password=rc.getPassword())
	api.PostUpdate("Im starting to get thirsty now, please give me " +
	               "something to drink :)")

def dealarm(name, value):
	print name, "got dry value:", value
	rc = TweetRc()
	api = twitter.Api(username=rc.getUsername(), password=rc.getPassword())
	api.PostUpdate("nom nom nom, i got some water now :)")

def main():
	thresholdLimit = 5 # how many time in a row before triggering alarm
	thresholdGuard = {}
	for id, setting in sensorLookUp.items() :
		#                            threshold    #triggerd
		thresholdGuard[setting[0]] = [setting[1], 0]
 
	while 1:
		readings = check()
		for name, value in readings.items():
			if thresholdGuard[name][1] == -1:
				dealarm(name, value)
				thresholdGuard[name][1] = 0 #deactive alarm
			elif thresholdGuard[name][0] > value:
				thresholdGuard[name][1] += 1
				print name, value, "trigged"
			else:
				thresholdGuard[name][1] = 0	
			if thresholdGuard[name][1] >= thresholdLimit:
				alarm(name, value)
				thresholdGuard[name][1] = -1 #active alarm
			print ".",
		time.sleep(30) # sleep 30 seconds	
			

if __name__ == "__main__":
	main()
