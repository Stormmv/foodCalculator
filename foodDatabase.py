###################       FOOD DATABASE        ###################
###################     BY MICHAEL VISSER      ###################
#IMPORTS ALL THE NECESARY MODULES
from tkinter import *
from tkinter import ttk
from tkinter import font
import time
from decimal import Decimal
#IMPORTS ALL THE NECESARY MODULES
#OPENS THE FILE AND READS IT
my_file = open ("Nutrientfile.txt")
file_content = my_file.readlines()
#OPENS THE FILE AND READS IT
#MAKES A LIST OF ALL THE ID'S, TYPES, FULL NAMES, ECT
foodData = []

for n in range(1, len(file_content)):
    Vid = file_content[n].split('\t')[0]
    Vtype = file_content[n].split('\t')[1].split(',')[0].replace('"','')
    Vfull = file_content[n].split('\t')[1].replace('"','')
    Venergy = file_content[n].split('\t')[2]
    Vprotein = file_content[n].split('\t')[3]
    VfatTotal = file_content[n].split('\t')[4]
    VfatSaturated = file_content[n].split('\t')[5]
    Vcarbohydrate = file_content[n].split('\t')[6]
    Vsugars = file_content[n].split('\t')[7]
    Vsodium = file_content[n].split('\t')[8].replace('\n', '')

    foodData.append({
        'id': Vid,
        'type': Vtype,
        'fullName': Vfull,
        'energy': Venergy,
        'protein': Vprotein,
        'fatTotal': VfatTotal,
        'fatSaturated': VfatSaturated,
        'carbohydrate': Vcarbohydrate,
        'sugars': Vsugars,
        'sodium': Vsodium,
        }) #this was found on github.com/dcralph
#MAKES A LIST OF ALL THE ID'S, TYPES, FULL NAMES, ECT
#CLASS FOR THE GUI
class Search:
    def __init__(self, parent):
        #CREATES MAIN FRAME
        self.searchframe = Frame(parent)
        self.searchframe.grid(row=0, columnspan=8)
        self.scrollboi = Scrollbar(self.searchframe, orient=VERTICAL)
        #CREATES MAIN FRAME
        #CREATES THE BACKROUND
        self.back = PhotoImage(file="bg.gif")
        self.backlabel = Label(self.searchframe, image=self.back)
        self.backlabel.place(x=0)
        #CREATES THE BACKROUND
        #CREATES TOP BLUE PART
        self.searchheader = Frame(self.searchframe, bg="navy", width=1000, height=65)
        self.searchheader.grid_propagate(0)
        self.searchheader.grid(row=0, columnspan=9)
        #CREATES TOP BLUE PART
        #SHOWS THE BACKROUND AT THE TOP
        self.searchbacklabel = Label(self.searchheader, image=self.back)
        self.searchbacklabel.place(x=0)
        #SHOWS THE BACKROUND AT THE TOP
        #CREATES ENTRY BOX IN TOP BLUE PART
        self.searchentry = Entry(self.searchheader, width=30)
        self.searchentry.grid(row=0, columnspan=9, padx=(300,10), pady=20)
        #ENTRY BOX IN TOP BLUE PART
        #CREATES BLUE SEARCH BUTTON
        self.searchbutton = Button(self.searchheader, text="Search", fg="gray99", bg="mediumblue", activebackground="mediumblue", anchor=NW, command=self.search)
        self.searchbutton.grid(row=0, columnspan=9, sticky=NW, padx=(600,10), pady=20)
        #CREATES BLUE SEARCH BUTTON
        #CREATES A SCROLLABLE LIST BOX
        self.listbox = Listbox(self.searchframe, width=100, selectmode=SINGLE, yscrollcommand=self.scrollboi.set)
        self.scrollboi.config(command=self.listbox.yview)
        self.listbox.grid(row=1, columnspan=9, padx=(0), pady=20)
        #CREATES A SCROLLABLE LIST BOX
        #CREATES MIDDLE BLUE PART       
        self.infoheader = Frame(self.searchframe, bg="navy", width=1000, height=22)
        self.infoheader.grid_propagate(0)
        self.infoheader.grid(row=2, columnspan=9)
        #CREATES MIDDLE BLUE PART       
        #CREATES LABELS IN THE MIDDLE BLUE PART
        self.perserving = Label(self.searchframe, text="Per Serving:", fg="gray99", bg="navy")
        self.perserving.grid(row=2, column=0, sticky=W, padx=10)

        self.enlabel = Label(self.searchframe, text="Energy (kJ)", fg="gray99", bg="navy")
        self.enlabel.grid(row=2, column=1, sticky=W, padx=10)

        self.prolabel = Label(self.searchframe, text="Protein (g)", fg="gray99", bg="navy")
        self.prolabel.grid(row=2, column=2, sticky=W, padx=10)

        self.fTotallabel = Label(self.searchframe, text="Fat, Total (g)", fg="gray99", bg="navy")
        self.fTotallabel.grid(row=2, column=3, sticky=W, padx=10)

        self.fSaturatedlabel = Label(self.searchframe, text="Fat, Saturated (g)", fg="gray99", bg="navy")
        self.fSaturatedlabel.grid(row=2, column=4, sticky=W, padx=10)

        self.carblabel = Label(self.searchframe, text="Carbohydrates (g)", fg="gray99", bg="navy")
        self.carblabel.grid(row=2, column=5, sticky=W, padx=10)

        self.suglabel = Label(self.searchframe, text="Sugar (g)", fg="gray99", bg="navy")
        self.suglabel.grid(row=2, column=6, sticky=W, padx=10)

        self.sodlabel = Label(self.searchframe, text="Sodium (g)", fg="gray99", bg="navy")
        self.sodlabel.grid(row=2, column=7, sticky=W, padx=10)
        #CREATES LABELS IN THE MIDDLE BLUE PART
        #CREATES LABELS THAT GET CHANGED WHEN PRESSING BUTTON
        self.infoheaderedit = Frame(self.searchframe, bg="navy", width=1000, height=22)
        self.infoheaderedit.grid_propagate(0)
        self.infoheaderedit.grid(row=3, columnspan=9)
        
        self.enlabel1 = Label(self.searchframe, text = " ", fg="gray99", bg="navy")
        self.enlabel1.grid(row=3, column=1, sticky=W, padx=(10,2))

        self.prolabel1 = Label(self.searchframe, text = " ", fg="gray99", bg="navy")
        self.prolabel1.grid(row=3, column=2, sticky=W, padx=(10,2))

        self.fTotallabel1 = Label(self.searchframe, text = " ", fg="gray99", bg="navy")
        self.fTotallabel1.grid(row=3, column=3, sticky=W, padx=(10,2))

        self.fSaturatedlabel1 = Label(self.searchframe, text = " ", fg="gray99", bg="navy")
        self.fSaturatedlabel1.grid(row=3, column=4, sticky=W, padx=(10,2))

        self.carblabel1 = Label(self.searchframe, text = " ", fg="gray99", bg="navy")
        self.carblabel1.grid(row=3, column=5, sticky=W, padx=(10,2))

        self.suglabel1 = Label(self.searchframe, text = " ", fg="gray99", bg="navy")
        self.suglabel1.grid(row=3, column=6, sticky=W, padx=(10,2))

        self.sodlabel1 = Label(self.searchframe, text = " ", fg="gray99", bg="navy")
        self.sodlabel1.grid(row=3, column=7, sticky=W, padx=(10,2))
        #CREATES LABELS THAT GET CHANGED WHEN PRESSING BUTTON
        #CREATES BOTTOM BLUE PART
        self.infoheader2 = Frame(self.searchframe, bg="navy", width=1000, height=22)
        self.infoheader2.grid_propagate(0)
        self.infoheader2.grid(row=4, columnspan=9)
        #CREATES BOTTOM BLUE PART
        #CREATES THE ENTRY BOX AT THE BOTTOM OF THE GUI
        self.customentry = Entry(self.searchframe, width=10)
        self.customentry.grid(row=4, column=0, sticky=W, padx=10)
        self.customentry.insert(END, '1')
        #CREATES THE ENTRY BOX AT THE BOTTOM OF THE GUI
        #CREATES LABELS IN BOTTOM BLUE PART
        self.enlabel = Label(self.searchframe, text="Energy (kJ)", fg="gray99", bg="navy")
        self.enlabel.grid(row=4, column=1, sticky=W, padx=10)

        self.prolabel = Label(self.searchframe, text="Protein (g)", fg="gray99", bg="navy")
        self.prolabel.grid(row=4, column=2, sticky=W, padx=10)

        self.fTotallabel = Label(self.searchframe, text="Fat, Total (g)", fg="gray99", bg="navy")
        self.fTotallabel.grid(row=4, column=3, sticky=W, padx=10)

        self.fSaturatedlabel = Label(self.searchframe, text="Fat, Saturated (g)", fg="gray99", bg="navy")
        self.fSaturatedlabel.grid(row=4, column=4, sticky=W, padx=10)

        self.carblabel = Label(self.searchframe, text="Carbohydrates (g)", fg="gray99", bg="navy")
        self.carblabel.grid(row=4, column=5, sticky=W, padx=10)

        self.suglabel = Label(self.searchframe, text="Sugar (g)", fg="gray99", bg="navy")
        self.suglabel.grid(row=4, column=6, sticky=W, padx=10)

        self.sodlabel = Label(self.searchframe, text="Sodium (g)", fg="gray99", bg="navy")
        self.sodlabel.grid(row=4, column=7, sticky=W, padx=10)
        #CREATES LABELS IN BOTTOM BLUE PART
        #CREATES LABELS THAT GET CHANGED WHEN BUTTON PRESSED (DEPENDS WHAT IS IN ENTRY BOX)
        self.infoheaderedit2 = Frame(self.searchframe, bg="navy", width=1000, height=22)
        self.infoheaderedit2.grid_propagate(0)
        self.infoheaderedit2.grid(row=5, columnspan=9)

        self.enlabel2 = Label(self.searchframe, text = " ", fg="gray99", bg="navy")
        self.enlabel2.grid(row=5, column=1, sticky=W, padx=(10,2))

        self.prolabel2 = Label(self.searchframe, text = " ", fg="gray99", bg="navy")
        self.prolabel2.grid(row=5, column=2, sticky=W, padx=(10,2))

        self.fTotallabel2 = Label(self.searchframe, text = " ", fg="gray99", bg="navy")
        self.fTotallabel2.grid(row=5, column=3, sticky=W, padx=(10,2))

        self.fSaturatedlabel2 = Label(self.searchframe, text = " ", fg="gray99", bg="navy")
        self.fSaturatedlabel2.grid(row=5, column=4, sticky=W, padx=(10,2))

        self.carblabel2 = Label(self.searchframe, text = " ", fg="gray99", bg="navy")
        self.carblabel2.grid(row=5, column=5, sticky=W, padx=(10,2))

        self.suglabel2 = Label(self.searchframe, text = " ", fg="gray99", bg="navy")
        self.suglabel2.grid(row=5, column=6, sticky=W, padx=(10,2))

        self.sodlabel2 = Label(self.searchframe, text = " ", fg="gray99", bg="navy")
        self.sodlabel2.grid(row=5, column=7, sticky=W, padx=(10,2))
        #CREATES LABELS THAT GET CHANGED WHEN BUTTON PRESSED (DEPENDS WHAT IS IN ENTRY BOX)
        #GOES TO CLICKEVENT WHEN YOU SELECT SOMETHING IN THE LIST BOX
        self.listbox.bind('<<ListboxSelect>>', self.clickevent)
        self.listbox.selection_set(3)
        #GOES TO CLICKEVENT WHEN YOU SELECT SOMETHING IN THE LIST BOX

    #DEFINES THE CLICK EVENT FUNCTION    
    def clickevent(self, varX):
        for a in foodData: #FOR THE NUMBER OF THINGS IN FOOD DATA
            if a['fullName'] == self.listbox.get(self.listbox.curselection()): #IF (NUMBER IN FOODDATA+FULLNAME) IS THE SAME AS THE THING CLICKED ON IN THE LIST BOX THEN:
        
                #EDIT FIRST SET OF EDITABLE LABELS
                self.enlabel1.configure(text=a['energy'])
                self.prolabel1.configure(text=a['protein'])
                self.fTotallabel1.configure(text=a['fatTotal'])
                self.fSaturatedlabel1.configure(text=a['fatSaturated'])
                self.carblabel1.configure(text=a['carbohydrate'])
                self.suglabel1.configure(text=a['sugars'])
                self.sodlabel1.configure(text=a['sodium'])
                #EDIT FIRST SET OF EDITABLE LABELS
                #EDIT SECOND SET OF EDITABLE LABELS (AND TIMES THE NUBERS BY THE NUMBER IN THE ENTRY BOX)               
                self.enlabel2.configure(text= ((float(a['energy']) * 1000) * (float(self.customentry.get()))) / 1000)   #FANCY MATH SO IT DOESNT SPIT OUT WEIRD NUMBERS
                self.prolabel2.configure(text= ((float(a['protein']) * 1000) * (float(self.customentry.get()))) / 1000)
                self.fTotallabel2.configure(text= ((float(a['fatTotal']) * 1000) * (float(self.customentry.get()))) / 1000)
                self.fSaturatedlabel2.configure(text= ((float(a['fatSaturated']) * 1000) * (float(self.customentry.get()))) / 1000)
                self.carblabel2.configure(text= ((float(a['carbohydrate']) * 1000) * (float(self.customentry.get()))) / 1000)
                self.suglabel2.configure(text= ((float(a['sugars']) * 1000) * (float(self.customentry.get()))) / 1000)
                self.sodlabel2.configure(text= ((float(a['sodium']) * 1000) * (float(self.customentry.get()))) / 1000)
                #EDIT SECOND SET OF EDITABLE LABELS (AND TIMES THE NUBERS BY THE NUMBER IN THE ENTRY BOX)

    #DEFINES THE SEARCH FUNCTION
    def search(self):
        self.listbox.delete(0, END) #CLEARS THE LIST BOX

        self.enlabel1.configure(text=' ') #RESETS THE LABELS THAT DISPLAY THE VALUES
        self.prolabel1.configure(text=' ')
        self.fTotallabel1.configure(text=' ')
        self.fSaturatedlabel1.configure(text=' ')
        self.carblabel1.configure(text=' ')
        self.suglabel1.configure(text=' ')
        self.sodlabel1.configure(text=' ')

        self.enlabel2.configure(text=' ') #RESETS THE LABELS THAT DISPLAY THE VALUES
        self.prolabel2.configure(text=' ')
        self.fTotallabel2.configure(text=' ')
        self.fSaturatedlabel2.configure(text=' ')
        self.carblabel2.configure(text=' ')
        self.suglabel2.configure(text=' ')
        self.sodlabel2.configure(text=' ')
        
        self.call()                 #GO TO THE CALL FUNCTION

    #DEFINES THE CALL FUNCTION
    def call(self):
        for s in foodData: #FOR THE NUMBER OF THINGS IN FOOD DATA
            if s['type'].lower() == self.searchentry.get().lower(): #IF THE (NUMBER IN FOODDATA + THE FOOD TYPE) IS THE SAME AS WHAT IS IN THE TOP ENTRY BOX THEN:
                self.listbox.insert(END, s['fullName'])             #INSERT ITEMS IN THE LIST BOX

#FANCY GUI STUFF
root = Tk()
root.title("Search For File") 
root.geometry("1000x355+300+150")
interface = Search(root)
root.mainloop()
#FANCY GUI STUFF