import Tkinter, tkFileDialog
import csv 

def convert(flat_list): #This is a mess

    ReturnList = []
#This iterates the raw data, converts it and places into a new array (immuatabe)
    for i in range(len(flat_list)):
        ReturnList.append(int(flat_list[i],16))
    save_Data_File(ReturnList)

def save_Data_File(ReturnList):
    
    fname = tkFileDialog.asksaveasfile(mode = 'w', defaultextension=".csv")
    if fname is None:
        return
    i = 0
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
#The Tkinter is a standard library for basic GUI
    root = Tkinter.Tk()
    root.withdraw() #This bit stops the tkinter root window from showing, more of formality, you don't want to see
                    #this, it is ugly
    path = tkFileDialog.askopenfile()#This prompts the user to point at the file they want to choose to convert
        
    data =csv.reader(path)
    
    l = list(data)# For whatever reason this makes a list of list, it is annoying
    
    flat_list = [] #This is to be the data that needs to be converted, after it has been flattened

#This takes a list of list and places it into a list that isn't a list of list
    for sublist in l:
        for item in sublist:
            flat_list.append(item)
    
    flat_list = filter(None,flat_list) #This filters the list of blank spaces
    
    convert(flat_list)
if __name__ == "__main__":
    main()
