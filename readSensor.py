import serial, re

def readSensor():
	try:	
		ser = serial.Serial(port="/dev/ttyUSB0",baudrate=9600,timeout=3)
		ser.open()
		ser.flushInput() # flush old input before getting new
		input = ser.readline()
		ser.close()
	except:
		print "opening and reading serial port failed"
		ser.close()
#	finally:
#		ser.close()
	try:
		sensor = re.split(" Sensor: | ", input)[1]
	except:
		print "Incorretly formated:", input
		return False
		
	if sensor == "Temp":
		try:
			id=re.split("Sensor: | ID: | Temp: |C\r\n", input)[2]
			value=re.split("Sensor: | ID: | Temp: |C\r\n", input)[3]
		except:
			return False
	elif sensor == "Error":
		print input
	else:
		print "Incorretly formated:", input

	return value, id, sensor 

def main():
	value, id, sensor = readSensor()
	if sensor == "Temp":
		print "ID:", id, "Temp: ", value, "C"
	else:
		print "Sensor:", sensor, "ID:", id, "Value:", value

if __name__ == "__main__":
	main()
	main()
