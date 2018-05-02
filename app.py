from tkinter import *

from tkinter import *

class InventoryManagement(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Inventory Management")
        self.grid()

        Label(self, text="Search (Item Number): ").grid(row=0, column=1, padx=6, pady=6, sticky=E)

        self._box1 = StringVar()
        self._input = Entry(self, width=20, textvariable=self._box1)
        self._input.grid(row=0, column=2, padx=8, pady=10, sticky=W)

        self.btn1 = Button(self, text="Search", command=self.runningInventory)
        self.btn1.grid(row=0, column=3, padx=8,pady=10,sticky=W)

        self.btn2 = Button(self, text="Reset", command=self.clearSearch)
        self.btn2.grid(row=0, column=4, padx=8, pady=10, sticky=W)

        self.scroll = Scrollbar(self)
        self.scroll.grid(row=3,column=6)
        self.text = Text(self,width=60,height=10,wrap=WORD,yscrollcommand=self.scroll.set)
        self.text.grid(row=3,column=1,columnspan=5, padx=15)
        self.scroll.config(command=self.text.yview)

        Label(self, text="Item Number ").grid(row=6, column=0, padx=6, pady=6, sticky=E)

        self._box2 = StringVar()
        self._input = Entry(self, width=20, textvariable=self._box2)
        self._input.grid(row=6, column=1, padx=8, pady=10, sticky=W)

        Label(self, text="Item Name ").grid(row=6, column=3, padx=6, pady=6, sticky=E)

        self._box3 = StringVar()
        self._input = Entry(self, width=20, textvariable=self._box3)
        self._input.grid(row=6, column=4, padx=8, pady=10)

        Label(self, text="On Hand ").grid(row=10, column=0, padx=6, pady=6, sticky=E)

        self._box4 = StringVar()
        self._input = Entry(self, width=20, textvariable=self._box4)
        self._input.grid(row=10, column=1, padx=8, pady=10, sticky=W)

        Label(self, text="Price ").grid(row=10, column=3, padx=6, pady=6, sticky=E)

        self._box5 = StringVar()
        self._input = Entry(self, width=20, textvariable=self._box5)
        self._input.grid(row=10, column=4, padx=8, pady=10)

        self.btn3 = Button(self, text="Add Item", command=self.addItem)
        self.btn3.grid(row=13, column=1, padx=5, pady=10, sticky=W)

        self.btn4 = Button(self, text="Edit Item", command=self.editItem)
        self.btn4.grid(row=13, column=2, padx=5, pady=10, sticky=W)

        self.btn4 = Button(self, text="Delete Item", command=self.deleteItem)
        self.btn4.grid(row=13, column=3, padx=5, pady=10)

    def addItem(self):

        items = []

        searchVal = StringVar()
        iNum = IntVar()
        iName = StringVar()
        oHand = IntVar()
        iPrice = IntVar()

        iNum = self._box2.get()
        iName = self._box3.get()
        oHand = self._box4.get()
        iPrice = self._box5.get()

        record = {'Item Number':iNum, 'Item Name':iName, 'On Hand':oHand, 'Item Price':iPrice}
        items.append(record)

        self.text.insert(END, iNum + '\t\t' + iName + '\t\t' + oHand + '\t\t' + iPrice + '\t\t')

        return

    def runningInventory(self):
        self.text.delete(1.0, END)
        self.text.insert(END,'Item Number' + '\t\t' + 'Item Name' + '\t\t' + 'On Hand' + '\t\t' + 'Price' + '\t\t')
        self.text.insert(END, '------------------------------------------------------------')

        return

    def clearSearch(self):
        self._box1.set('')

    def editItem(self):
        return

    def deleteItem(self):
        return

def main():
    InventoryManagement().mainloop()

main()

