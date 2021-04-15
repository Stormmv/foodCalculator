from tkinter import *
from tkinter import ttk
from tkinter import font
import time
from decimal import Decimal
my_file = open ("Nutrientfile.txt")

file_content = my_file.readlines()

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
        })

class Search:
    def __init__(self, parent):
        #SEARCH FRAME
        self.searchframe = Frame(parent)
        self.searchframe.grid(row=0, columnspan=8)
        self.scrollboi = Scrollbar(self.searchframe, orient=VERTICAL)
        #SEARCH FRAME
        #BLUE PART
        self.searchheader = Frame(self.searchframe, bg="dodgerblue2", width=1000, height=65)
        self.searchheader.grid_propagate(0)
        self.searchheader.grid(row=0, columnspan=9)
        
        #self.breakwarn = Label(self.searchheader, text="Use Mouse To Scroll", bg="dodgerblue2")
        #self.breakwarn.grid(row=0, columnspan=2, padx=(160,10), pady=20)

        self.searchentry = Entry(self.searchheader, width=30)
        self.searchentry.grid(row=0, columnspan=9, padx=(300,10), pady=20)
        
        self.searchbutton = Button(self.searchheader, text="Search", bg="deep sky blue", activebackground="deep sky blue", anchor=NW, command=self.search)
        self.searchbutton.grid(row=0, columnspan=9, sticky=NW, padx=(600,10), pady=20)
        #BLUE PART
        self.listbox = Listbox(self.searchframe, width=100, selectmode=SINGLE, yscrollcommand=self.scrollboi.set)
        self.scrollboi.config(command=self.listbox.yview)
        #self.scrollboi.grid(row=1, column=2)
        self.listbox.grid(row=1, columnspan=9, padx=(0), pady=20)
        #PINK PART

        self.infoheader = Frame(self.searchframe, bg="dodgerblue2", width=1000, height=22)
        self.infoheader.grid_propagate(0)
        self.infoheader.grid(row=2, columnspan=9)
##########
        self.perserving = Label(self.searchframe, text="Per Serving:", bg="dodgerblue2")
        self.perserving.grid(row=2, column=0, sticky=W, padx=10)

        self.enlabel = Label(self.searchframe, text="Energy (kJ)", bg="dodgerblue2")
        self.enlabel.grid(row=2, column=1, sticky=W, padx=10)

        self.prolabel = Label(self.searchframe, text="Protein (g)", bg="dodgerblue2")
        self.prolabel.grid(row=2, column=2, sticky=W, padx=10)

        self.fTotallabel = Label(self.searchframe, text="Fat, Total (g)", bg="dodgerblue2")
        self.fTotallabel.grid(row=2, column=3, sticky=W, padx=10)

        self.fSaturatedlabel = Label(self.searchframe, text="Fat, Saturated (g)", bg="dodgerblue2")
        self.fSaturatedlabel.grid(row=2, column=4, sticky=W, padx=10)

        self.carblabel = Label(self.searchframe, text="Carbohydrates (g)", bg="dodgerblue2")
        self.carblabel.grid(row=2, column=5, sticky=W, padx=10)

        self.suglabel = Label(self.searchframe, text="Sugar (g)", bg="dodgerblue2")
        self.suglabel.grid(row=2, column=6, sticky=W, padx=10)

        self.sodlabel = Label(self.searchframe, text="Sodium (g)", bg="dodgerblue2")
        self.sodlabel.grid(row=2, column=7, sticky=W, padx=10)
###############################################################################################
        self.enlabel1 = Label(self.searchframe, text = "-")
        self.enlabel1.grid(row=3, column=1, sticky=W, padx=(10,2))

        self.prolabel1 = Label(self.searchframe, text = "-")
        self.prolabel1.grid(row=3, column=2, sticky=W, padx=(10,2))

        self.fTotallabel1 = Label(self.searchframe, text = "-")
        self.fTotallabel1.grid(row=3, column=3, sticky=W, padx=(10,2))

        self.fSaturatedlabel1 = Label(self.searchframe, text = "-")
        self.fSaturatedlabel1.grid(row=3, column=4, sticky=W, padx=(10,2))

        self.carblabel1 = Label(self.searchframe, text = "-")
        self.carblabel1.grid(row=3, column=5, sticky=W, padx=(10,2))

        self.suglabel1 = Label(self.searchframe, text = "-")
        self.suglabel1.grid(row=3, column=6, sticky=W, padx=(10,2))

        self.sodlabel1 = Label(self.searchframe, text = "-")
        self.sodlabel1.grid(row=3, column=7, sticky=W, padx=(10,2))
        ################################
        self.infoheader2 = Frame(self.searchframe, bg="dodgerblue2", width=1000, height=22)
        self.infoheader2.grid_propagate(0)
        self.infoheader2.grid(row=4, columnspan=9)
        ################################
        self.customentry = Entry(self.searchframe, width=10)
        self.customentry.grid(row=4, column=0, sticky=W, padx=10)
        self.customentry.insert(END, '1')

        self.enlabel = Label(self.searchframe, text="Energy (kJ)", bg="dodgerblue2")
        self.enlabel.grid(row=4, column=1, sticky=W, padx=10)

        self.prolabel = Label(self.searchframe, text="Protein (g)", bg="dodgerblue2")
        self.prolabel.grid(row=4, column=2, sticky=W, padx=10)

        self.fTotallabel = Label(self.searchframe, text="Fat, Total (g)", bg="dodgerblue2")
        self.fTotallabel.grid(row=4, column=3, sticky=W, padx=10)

        self.fSaturatedlabel = Label(self.searchframe, text="Fat, Saturated (g)", bg="dodgerblue2")
        self.fSaturatedlabel.grid(row=4, column=4, sticky=W, padx=10)

        self.carblabel = Label(self.searchframe, text="Carbohydrates (g)", bg="dodgerblue2")
        self.carblabel.grid(row=4, column=5, sticky=W, padx=10)

        self.suglabel = Label(self.searchframe, text="Sugar (g)", bg="dodgerblue2")
        self.suglabel.grid(row=4, column=6, sticky=W, padx=10)

        self.sodlabel = Label(self.searchframe, text="Sodium (g)", bg="dodgerblue2")
        self.sodlabel.grid(row=4, column=7, sticky=W, padx=10)
        ###################################3
        self.enlabel2 = Label(self.searchframe, text = "-")
        self.enlabel2.grid(row=5, column=1, sticky=W, padx=(10,2))

        self.prolabel2 = Label(self.searchframe, text = "-")
        self.prolabel2.grid(row=5, column=2, sticky=W, padx=(10,2))

        self.fTotallabel2 = Label(self.searchframe, text = "-")
        self.fTotallabel2.grid(row=5, column=3, sticky=W, padx=(10,2))

        self.fSaturatedlabel2 = Label(self.searchframe, text = "-")
        self.fSaturatedlabel2.grid(row=5, column=4, sticky=W, padx=(10,2))

        self.carblabel2 = Label(self.searchframe, text = "-")
        self.carblabel2.grid(row=5, column=5, sticky=W, padx=(10,2))

        self.suglabel2 = Label(self.searchframe, text = "-")
        self.suglabel2.grid(row=5, column=6, sticky=W, padx=(10,2))

        self.sodlabel2 = Label(self.searchframe, text = "-")
        self.sodlabel2.grid(row=5, column=7, sticky=W, padx=(10,2))
        #SEARCH FRAME 
        self.listbox.bind('<<ListboxSelect>>', self.clickevent)
        self.listbox.selection_set(3)

    def clickevent(self, varX):
        counter = 0
        for a in foodData:
            if a['fullName'] == self.listbox.get(self.listbox.curselection()):
        
                self.enlabel1.configure(text=a['energy'])
                self.prolabel1.configure(text=a['protein'])
                self.fTotallabel1.configure(text=a['fatTotal'])
                self.fSaturatedlabel1.configure(text=a['fatSaturated'])
                self.carblabel1.configure(text=a['carbohydrate'])
                self.suglabel1.configure(text=a['sugars'])
                self.sodlabel1.configure(text=a['sodium'])
                
                self.enlabel2.configure(text= ((float(a['energy']) * 1000) * (float(self.customentry.get()))) / 1000)
                self.prolabel2.configure(text= ((float(a['protein']) * 1000) * (float(self.customentry.get()))) / 1000)
                self.fTotallabel2.configure(text= ((float(a['fatTotal']) * 1000) * (float(self.customentry.get()))) / 1000)
                self.fSaturatedlabel2.configure(text= ((float(a['fatSaturated']) * 1000) * (float(self.customentry.get()))) / 1000)
                self.carblabel2.configure(text= ((float(a['carbohydrate']) * 1000) * (float(self.customentry.get()))) / 1000)
                self.suglabel2.configure(text= ((float(a['sugars']) * 1000) * (float(self.customentry.get()))) / 1000)
                self.sodlabel2.configure(text= ((float(a['sodium']) * 1000) * (float(self.customentry.get()))) / 1000)
            counter += 1
    def search(self):
        self.listbox.delete(0, END)
        self.call()

    def call(self):
        counter = 0
        for s in foodData:
            if s['type'].lower() == self.searchentry.get().lower():
                self.listbox.insert(END, s['fullName'])
                counter += 1

root = Tk()
root.title("Search For File") 
root.geometry("1000x355+-10+0") 
interface = Search(root)
root.mainloop()