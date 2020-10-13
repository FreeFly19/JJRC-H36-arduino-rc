import serial, time

arduino=serial.Serial('/dev/cu.usbmodem1411', 115200, timeout=.01)
time.sleep(2)
arduino.write("2000,1500,1500,1500\n")
time.sleep(1)
arduino.write("1000,1500,1500,1500\n")
time.sleep(2)
arduino.write("1500,1500,1500,1500\n")
time.sleep(1)
arduino.write("1000,1500,1500,1500\n")

