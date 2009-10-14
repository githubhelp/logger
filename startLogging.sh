#kill previus running instance(s)
killall python sensorLogger.py 
cd /home/simon/logger
nohup python sensorLogger.py &
