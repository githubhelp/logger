import serial, sys, glob

#returns first ttyUSB* port avalible
def findPort():
	return glob.glob("/dev/ttyUSB*")[0]

def writeLED(led, status):
	ser = serial.Serial(port=findPort(),baudrate=9600,timeout=3)
	if status == True:	
		ser.write(led.upper()[0])
	elif status == False:
		ser.write(led.lower()[0])
		
	ser.close()

def writeLED_PWM(led, level):
	ser = serial.Serial(port=findPort(),baudrate=9600,timeout=3)
	ser.write(led.lower()[0])
	ser.write(chr(level))
	ser.close()
		
def main():
	try:
		if (sys.argv[2] == "on"):
			writeLED(sys.argv[1], True)
		elif (sys.argv[2] == "off"):
			writeLED(sys.argv[1], False)
		elif (sys.argv[2].isdigit()):
			writeLED_PWM(sys.argv[1], int(sys.argv[2]))
	except:
		print "Error:", sys.exc_info()
		print "Input:", sys.argv
		pass

if __name__ == "__main__":
	main()
