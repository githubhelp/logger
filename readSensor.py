import serial, re

def getTemp():
	ser = serial.Serial(port="/dev/ttyUSB1", baudrate=9600, timeout=10)
	ser.open()
	value = ser.readline()
	sensor = re.split(" Sensor: | ", value)[1]
	if sensor == "Temp":
		id = re.split("Sensor: | ID: | Temp: |C\r\n", value)[2]
		temp = re.split("Sensor: | ID: | Temp: |C\r\n", value)[3]
	elif sensor == "Error":
		print value
	else:
		print "Incorretly formated:". value

	ser.close()

	return temp, id

def main():
	temp, id = getTemp()
	print "ID:", id, "Temp: ", temp, "C"

if __name__ == "__main__":
	main()
