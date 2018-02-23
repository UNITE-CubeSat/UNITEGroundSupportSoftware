import serial
import os


def main():

	print("Diagnostic Logger started...\n")
	logNum = 1
	
	ser = serial.Serial('/dev/ttyACM0',9600,timeout=10)
	
	directory = os.path.dirname(__file__)

	while(1):
	
		line = str(ser.readline())

		if((len(line) == 0) or (str(line[0]) == ",") or (line[0] == None) or (len(line) < 10)):
			line = 0;
		else:
			print line
			

		#lengthOfLog = ser.inWaiting()
		
		#if (lengthOfLog > 0):
			#line = str(ser.readline())
			#print(line)

			if (("47,55," in line) or ("Pic" in line)):
				duplexFile = open(directory + '/DuplexComm.txt','a')
				duplexFile.write(line)
				duplexFile.close()
			else :
				logFile = open(directory + '/Diagnostic_Logs/DiagData_' + str(logNum) + '.log', 'a')
				logFile.write(line)
				logFile.close()			

				if "EOF" in line: 
					print("Logged " + str(logNum) + " Files")
					logNum += 1
			
					print("Waiting for Log #" + str(logNum))			
			
			

if __name__ == '__main__':
    main()
