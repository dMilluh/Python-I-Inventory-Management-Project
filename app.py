''' Simple Inventory Management - Written by Daniel Miller for class CIT 144 - Python I
        Written with Python using Tkinter
'''

from tkinter import *
from tkinter.ttk import *

root = Tk()


class InventoryManagement(Frame):

    # Creates constructor for main frame of application

    def __init__(self):
        Frame.__init__(self)
        self.master.title('Inventory Management')
        self.grid()
        self.items = []
        root.geometry("650x425")

        # Lines 23 - 36 are top of application, search feature labels/entry/buttons

        Label(self, text='Search (Item Number): ').grid(row=0,
                                                        column=1, padx=6, pady=20, sticky=E)

        self._box1 = IntVar()
        self._input = Entry(self, width=20, textvariable=self._box1)
        self._input.grid(row=0, column=2, padx=8, pady=20, sticky=W)

        self.btn1 = Button(self, text='Search',
                           command=self.searchInventory)
        self.btn1.grid(row=0, column=3, padx=8, pady=20, sticky=W)

        self.btn2 = Button(self, text='Reset', command=self.clearSearch)
        self.btn2.grid(row=0, column=4, padx=8, pady=20, sticky=W)

        # Lines 40 - 45 is the main text area for inventory display

        self.scroll = Scrollbar(self)
        self.scroll.grid(row=3, column=6)
        self.text = Text(self, width=60, height=10, wrap=WORD,
                         yscrollcommand=self.scroll.set)
        self.text.grid(row=3, column=0, columnspan=5, padx=20, pady=20)
        self.scroll.config(command=self.text.yview)

        # Lines 49 - 75 are labels/entry boxes for new/edit item entry

        Label(self, text='Item Number ').grid(row=6, column=0, padx=6,
                                              pady=6, sticky=W)

        self._box2 = StringVar()
        self._input1 = Entry(self, width=20, textvariable=self._box2)
        self._input1.grid(row=6, column=1, padx=8, pady=10, sticky=E)

        Label(self, text='Item Name ').grid(row=6, column=2, padx=6,
                                            pady=6, sticky=E)

        self._box3 = StringVar()
        self._input = Entry(self, width=20, textvariable=self._box3)
        self._input.grid(row=6, column=3, padx=8, pady=10, sticky=E)

        Label(self, text='On Hand ').grid(row=10, column=0, padx=6,
                                          pady=6, sticky=E)

        self._box4 = StringVar()
        self._input = Entry(self, width=20, textvariable=self._box4)
        self._input.grid(row=10, column=1, padx=8, pady=10, sticky=W)

        Label(self, text='Price ').grid(row=10, column=2, padx=6,
                                        pady=6, sticky=E)

        self._box5 = StringVar()
        self._input = Entry(self, width=20, textvariable=self._box5)
        self._input.grid(row=10, column=3, padx=8, pady=10)

        # Lines 79 - 88 are buttons for corresponding functions to add/edit/delete items from text area

        self.btn3 = Button(self, text='Add Item', command=self.addItem)
        self.btn3.grid(row=11, column=1, padx=5, pady=20, sticky=W)

        self.btn4 = Button(self, text='Edit Item',
                           command=self.editItem)
        self.btn4.grid(row=11, column=2, padx=5, pady=20, sticky=W)

        self.btn4 = Button(self, text='Delete Item',
                           command=self.deleteItem)
        self.btn4.grid(row=11, column=3, padx=5, pady=20, sticky=W)

        # Lines 91 - 98 inserts headers into text area and sets focus to Item Number entry box
        self.text.insert(END, 'Item Number' + '\t\t' + 'Item Name'
                         + '\t\t' + 'On Hand' + '\t\t' + 'Price'
                         + '\t\t')
        self.text.insert(END,
                         '------------------------------------------------------------'
                         )

        self._input1.focus_set()


    ''' addItem() function inserts headers into text area, grabs values from entry boxes 
        and appends them to a list of dictionaries if entry boxes are not empty.  It then prints
        each item(dictionary) to the text area and clears the entry boxes. '''


    def addItem(self):
        self.text.delete(1.0, END)
        self.text.insert(END, 'Item Number' + '\t\t' + 'Item Name'
                         + '\t\t' + 'On Hand' + '\t\t' + 'Price'
                         + '\t\t')
        self.text.insert(END,
                         '------------------------------------------------------------'
                         )

        items = self.items

        iNum = self._box2.get()
        iName = self._box3.get()
        oHand = self._box4.get()
        iPrice = self._box5.get()
    
        if (iNum != '' and iName != '' and oHand != '' and iPrice != ''):
            record = {
                0: iNum,
                1: iName,
                2: oHand,
                3: iPrice,
            }
            items.append(record)

            for item in items:
                self.text.insert(END, item[0] + '\t\t' + item[1] + '\t\t'
                                 + item[2] + '\t\t' + item[3] + '\t\t')
        else:
            self.text.delete(1.0, END)
            self.text.insert(END, 'Error: One or more fields have been left blank.')

        self._box2.set('')
        self._box3.set('')
        self._box4.set('')
        self._box5.set('')
        self._input1.focus_set()


    ''' searchInventory() function inserts headers into text area, gets value of search box entry and compares to
        list of dictionaries.  If the search box value matches the item number key,
         it inserts the dictionaries values into the text area. '''


    def searchInventory(self):
        self.text.delete(1.0, END)
        self.text.insert(END, 'Item Number' + '\t\t' + 'Item Name'
                         + '\t\t' + 'On Hand' + '\t\t' + 'Price'
                         + '\t\t')
        self.text.insert(END,
                         '------------------------------------------------------------'
                         )

        searchVal = str(self._box1.get())

        for item in self.items:
            if item[0] == searchVal:
                self.text.insert(END, item[0] + '\t\t' + item[1]
                                 + '\t\t' + item[2] + '\t\t' + item[3]
                                 + '\t\t')


    # Simple function attached to reset button to clear the search box

    def clearSearch(self):
        self._box1.set('')


    ''' editItem() function clears the entry boxes to prevent errors.  It then grabs the search box value and compares
        to the list of dictionaries.  If the dictionary's item number matches the value it inserts the value of the 
        dictionary into the entry boxes for editing. '''


    def editItem(self):
        self._box2.set('')
        self._box3.set('')
        self._box4.set('')
        self._box5.set('')

        items = self.items

        searchVal = str(self._box1.get())

        for item in items:
            if item[0] == searchVal:
                self.items.remove(item)
                self._box2.set(item[0])
                self._box3.set(item[1])
                self._box4.set(item[2])
                self._box5.set(item[3])

        self._box1.set('')
        self._input1.focus_set()


    # Simple function to delete dictionary with item number that matches the search box value

    def deleteItem(self):
        self.text.delete(1.0, END)
        self.text.insert(END, 'Item Number' + '\t\t' + 'Item Name'
                         + '\t\t' + 'On Hand' + '\t\t' + 'Price'
                         + '\t\t')
        self.text.insert(END,
                         '------------------------------------------------------------'
                         )

        items = self.items

        searchVal = str(self._box1.get())

        for item in items:
            if item[0] == searchVal:
                self.items.remove(item)

        for item in items:
            self.text.insert(END, item[0] + '\t\t' + item[1] + '\t\t'
                             + item[2] + '\t\t' + item[3] + '\t\t')

        self._box1.set('')


def main():
    InventoryManagement().mainloop()


main()