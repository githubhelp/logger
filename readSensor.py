import serial, re

def readSensor():
	ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=3)
	ser.open()
	value = ser.readline()
	try:
		sensor = re.split(" Sensor: | ", value)[1]
	except:
		print "Incorretly formated:", value
		return readSensor()
		
	if sensor == "Temp":
		id = re.split("Sensor: | ID: | Temp: |C\r\n", value)[2]
		temp = re.split("Sensor: | ID: | Temp: |C\r\n", value)[3]
	elif sensor == "Error":
		print value
	else:
		print "Incorretly formated:", value

	ser.close()

	return temp, id

def main():
	temp, id = readSensor()
	print "ID:", id, "Temp: ", temp, "C"

if __name__ == "__main__":
	main()
