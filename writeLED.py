import serial, sys
def writeLED(led, status):
	ser = serial.Serial(port="/dev/ttyUSB0",baudrate=9600,timeout=3)
	if status == True:	
		ser.write(led.upper()[0]);
	elif status == False:
		ser.write(led.lower()[0]);
		
	ser.close();
def main():
	try:
		if (sys.argv[2] == "on"):
			writeLED(sys.argv[1], True)
		if (sys.argv[2] == "off"):
			writeLED(sys.argv[1], False)
	except:
		print sys.argv
		pass

if __name__ == "__main__":
	main()
