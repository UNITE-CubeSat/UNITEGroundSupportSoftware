import Tkinter, tkFileDialog
import csv 
from Tkinter import *

#def langmuir():
#def magnetometer():
#def temp():
def GetInstrument():
    Instrument = raw_input("Type the letter of your subsystem  T(Temp), M(Mag), L(Langmuir), G(GPS) \n")
    return Instrument
def getFile():
    flat_list = []
    root = Tkinter.Tk()
    root.withdraw()
    path =tkFileDialog.askopenfile()
    data = csv.reader(path)
    l = list(data)
    for i in xrange(0,len(l),1):
        del l[i][len(l[i])-2]
        del l[i][1]
        del l[i][0]
#    print(l)
    for sublist in l:
        for item in sublist:
            flat_list.append(item)
    flat_list[:] = [item for item in flat_list if item != '']
    print(flat_list)
#Temp Sensor Filter
    return flat_list
def convert(flat_list): #This function converts the data from hex to decimal

    ReturnList = []
    for i in range(len(flat_list)):
        ReturnList.append(int(flat_list[i],16)) #,int(flat_list[],16) after flat_list
    return ReturnList

def save_Data_File(ReturnList):
    
    fname = tkFileDialog.asksaveasfile(mode = 'w', defaultextension=".csv")
    if fname is None:
        return
    i = 0
#This formats the temperature data in an 8 column format
    for x in range(len(ReturnList)):
        if(i<8):
            fname.write(str(ReturnList[x]))
            fname.write(",")
            i += 1
        else:
            fname.write("\n")
            fname.write(str(ReturnList[x]))
            fname.write(",")
            i=1
    fname.close
    print("File has been saved")

def main():
    flat_list = getFile()
    ConvertedList = [] #This is the list of data from HEX to Decimal
    
    ConvertedList =  convert(flat_list)
    save_Data_File(ConvertedList)

if __name__ == "__main__":
    main()
