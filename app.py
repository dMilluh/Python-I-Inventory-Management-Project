from tkinter import *

class InventoryManagement(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Inventory Management")
        self.grid()

        Label(self, text="Item Name: ").grid(row=0, column=1, padx=6, pady=6, sticky=E)

        self._box1 = StringVar()
        self._input = Entry(self, width=20, textvariable=self._box1)
        self._input.grid(row=0, column=2, padx=8, pady=10, sticky=W)

        self.btn1 = Button(self, text="Search", command=self.searchInventory)
        self.btn1.grid(row=0, column=3, padx=8,pady=10,sticky=W)

        self.btn2 = Button(self, text="Reset", command=self.clearSearch)
        self.btn2.grid(row=0, column=4, padx=8, pady=10, sticky=W)

        self.scroll = Scrollbar(self)
        self.scroll.grid(row=3,column=6)
        self.text = Text(self,width=60,height=10,wrap=WORD,yscrollcommand=self.scroll.set)
        self.text.grid(row=3,column=1,columnspan=5)
        self.scroll.config(command=self.text.yview)

        self.btn3 = Button(self, text="Add Item", command=self.addItem)
        self.btn3.grid(row=4, column = 1, padx=8, pady=10, sticky=E)

        self.btn4 = Button(self, text="Edit Item", command=self.addItem)
        self.btn4.grid(row=4, column = 2, padx=8, pady=10, sticky=W)

    def searchInventory(self):
        self.text.delete(1.0, END)
        self.text.insert(END, 'Item Name' + '\t\t' + 'On Hand' + '\t\t' + 'Price' + '\t\t')
        self.text.insert(END, '-----------------------------------------------')

        return

    def clearSearch(self):
        self._box1.set('')

    def addItem(self):
        return

    def editItem(self):
        return

def main():
    InventoryManagement().mainloop()

main()


