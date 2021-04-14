from tkinter import *
from tkinter import ttk

my_file = open ("Nutrientfile.txt")

file_content = my_file.readlines()

foodData = []
nameLabels = []
energyLabels = []

for line in file_content:
    Vid = line.split('\t')[0]
    Vtype = line.split('\t')[1].split(',')[0].replace('"','')
    Vfull = line.split('\t')[1].replace('"','')
    Venergy = line.split('\t')[2]
    Vprotein = line.split('\t')[3]
    VfatTotal = line.split('\t')[4]
    VfatSaturated = line.split('\t')[5]
    Vcarbohydrate = line.split('\t')[6]
    Vsugars = line.split('\t')[7]
    Vsodium = line.split('\t')[8]

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
        self.searchframe.pack(fill=BOTH, expand=1)
        #SEARCH FRAME
        #CANVAS
        self.mycanvas = Canvas(self.searchframe)
        self.mycanvas.pack(side=LEFT, fill=BOTH, expand=1)
        #CANVAS
        #SCROLL BOI
        self.scrollboi = ttk.Scrollbar(self.searchframe, orient=VERTICAL, command=self.mycanvas.yview)
        self.scrollboi.pack(side=RIGHT, fill=Y)
        #SCROLL BOI
        #FANCY STUFF
        self.mycanvas.configure(yscrollcommand=self.scrollboi.set)
        self.mycanvas.bind('<Configure>', lambda e: self.mycanvas.configure(scrollregion=self.mycanvas.bbox("all")))
        self.searchframe2 = Frame(self.mycanvas)
        self.searchframe2.pack(expand=1)
        self.mycanvas.create_window((0, 0), window=self.searchframe2, anchor="nw")
        #FANCY STUFF
        #BLUE PART
        self.searchheader = Frame(self.searchframe2, bg="dodgerblue2", width=1000, height=65)
        self.searchheader.grid_propagate(0)
        self.searchheader.grid(row=0, columnspan=8)
        
        self.breakwarn = Label(self.searchheader, text="DO NOT EXPAND THE GUI", bg="dodgerblue2")
        self.breakwarn.grid(row=0, column=0, padx=(100,10), pady=20)

        self.searchentry = Entry(self.searchheader, width=30)
        self.searchentry.grid(row=0, column=1, padx=(400,10), pady=20)

        self.searchbutton = Button(self.searchheader, text="Search", bg="deep sky blue", activebackground="deep sky blue", anchor=NW, command=self.call)
        self.searchbutton.grid(row=0, column=2, sticky=NW, padx=0, pady=20)
        #BLUE PART
        #PINK PART

        self.infoheader = Frame(self.searchframe2, bg="orchid", width=1000, height=22)
        self.infoheader.grid_propagate(0)
        self.infoheader.grid(row=1, columnspan=8)

        self.namelabel = Label(self.searchframe2, text="Name", bg="orchid")
        self.namelabel.grid(row=1, column=0, sticky=W, padx=10)

        self.energylabel = Label(self.searchframe2, text="Energy (kJ)", bg="orchid")
        self.energylabel.grid(row=1, column=1, sticky=W, padx=10)
        #PINK PART
        #SEARCH FRAME 
    def call(self):
        root.geometry("1000x601+-10+0")
        i = 0
        for i in range(len(nameLabels)):
            nameLabels[i].grid_remove()
            energyLabels[i].grid_remove()

        nameLabels.clear()
        energyLabels.clear()

        counter = 0
             
        for s in foodData:
            if s['type'].lower() == self.searchentry.get().lower():

                nameLabels.append(Label(self.searchframe2, text = (s['fullName'])))
                nameLabels[counter].grid(row = 3 + counter, column = 0, sticky=W, padx=10, pady=2)
                energyLabels.append(Label(self.searchframe2, text = (s['energy'])))
                energyLabels[counter].grid(row = 3 + counter, column = 1, sticky=W, padx=10, pady=2)
                counter += 1
root = Tk()
root.title("Search For File") 
root.geometry("1000x600+-10+0") 
interface = Search(root)
root.mainloop()
