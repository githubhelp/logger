import serial
while 1:
	ser = serial.Serial(port="/dev/ttyUSB0",baudrate=9600,timeout=3)
	ser.open()
	#ser.flushInput() # flush old input before getting new
	#input = ser.readline()
	ser.close()
