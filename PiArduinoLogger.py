import serial
import os

def Parse(Data):
	
	directory = os.path.dirname(__file__)

	print(Data[11]);
	
	if((int(Data[11]) == 1) and (str(Data[13]) != "F")):
		f = open(directory + "/LP.txt","a") #Opens file in (a) append mode
		f.write(str(Data[11:]))					
		f.close();
		print("LP file altered\n")
	
	elif((int(Data[11]) == 2) and (str(Data[13]) == ",")):
		f = open(directory + "/Mag.txt","a") #Opens file in (a) append mode
		f.write(str(Data[11:]))					
		f.close();		

		print("Mag file altered\n")

	elif((int(Data[11]) == 3) and (str(Data[13]) == ",")):
		f = open(directory + "/Temp.txt","a") #Opens file in (a) append mode
		f.write(str(Data[11:]))				
		f.close();			

		print("Temp file altered\n");
	   
	elif((int(Data[11]) == 4) and (str(Data[13]) == ",")):
		f = open(directory + "/GPS.txt","a") #Opens file in (a) append mode
		f.write(str(Data[11:]))					
		f.close();			
	
		print("GPS file altered\n")
	
	elif((int(Data[11]) == 5) and (str(Data[13]) == ",")):
		f = open(directory + "/HK.txt","a") #Opens file in (a) append mode
		f.write(str(Data[11:]))					
		f.close();			
		
		print("Houskeeping file altered\n")
	
	elif((int(Data[11]) == 6) and (str(Data[13]) == ",")):
		f = open(directory + "/LPCal.txt","a") #Opens file in (a) append mode
		f.write(str(Data[11:]))		
		f.close();
		print("LPCal file altered\n")
	else:
		print("##Simplex Package##\n");
	
def main():
	
	print("Raspberry Pi Transmission Logger started...\n")

	ser = serial.Serial('/dev/ttyACM1',38400,timeout=10)
	Data = []

	while(1):	
				
		Data = ser.readline().encode()
		
		if((len(Data) == 0) or (str(Data[0]) == ",") or (Data[0] == None) or (len(Data) < 10)):
			Data = 0;
		else:
			print Data
			if (str(Data[9]) == "C"): Parse(Data);
			else: Data = 0;
			
			
					

if __name__ == '__main__':
    main()
