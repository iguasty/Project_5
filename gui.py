import tkinter as tk
import random
class Gui: 
    
    def __init__(self):
        self.root = tk.Tk(className="num_search")
        self.root.minsize(800, 600)

        # self.title_label = tk.Label(self.root, text="Search for a value!")
        # self.prompt_label = tk.Label(self.root, text="Type in a value to search for it in this list array")
        # self.entry_box = tk.Entry(self.root)
        # self.enter_button = tk.Button(self.root, text="Enter", command=self.update_label)
        
        # self.create_num_array()
        # print(self.create_num_array())
        
        # self.title_label.pack()
        # self.prompt_label.pack()
        # self.box.pack()
        # self.enter_button.pack()
        self.create_boxes()
        # print(self.search())
        self.root.mainloop()
        
    def update_label(self):
        """update label text"""
        newtext = self.entry_box.get()
        self.prompt_label.config(text=newtext)
        return newtext
    
    def create_num_array(self):
        num_array = []
        for i in range(100):
            val = random.randint(1, 1000)
            num_array.append(val)
        return num_array
    
    def create_boxes(self):
        self.entry_box = tk.Entry(self.root)
        # self.box = tk.Label(self.root, text="Test") 
        self.boxes = [] #list of entry boxes
        self.rows = 10
        self.columns = 10
        #creates 10 text boxes and appends them to list
        
        for i in range(self.rows):
            self.row_boxes = []
            # self.box = tk.Label(self.root, text="Tester")
            # self.box.pack(side="top")
            # self.boxes.append(self.entry_box)       
            array = self.create_num_array() 
            
            for j in range(self.columns):
                self.box = tk.Label(self.root, text=array[j])
                self.box.grid(row=i, column=j, padx=5, pady=5)
                self.row_boxes.append(self.entry_box) 
                # self.search()
            self.boxes.append(self.row_boxes)
                
        # print(array)
        self.prompt_label = tk.Label(self.root, text="Type in a value to search for it in this list array")    
        self.enter_button = tk.Button(self.root, text="Enter", command=self.search)
        self.entry_box.grid(row=self.rows, column=0, columnspan=self.columns-1, sticky="nsew")
        self.prompt_label.grid(row=self.rows+1, column=0, columnspan=self.columns-1, sticky="nsew")
        self.enter_button.grid(row=self.rows+2, column=0, columnspan=self.columns-1, sticky="nsew")
        
        # self.title_label = tk.Label(self.root, text="Search for a value!")
                
        # self.title_label.pack(side="bottom")
        
    # def search(self):
    #     nummatch = None
    #     try:
    #         for i in range(100):            
    #             # for j in range(self.columns):
    #             searchnum = self.boxes[i].cget("text")          
    #             number = float(searchnum)
    #             print(number)
    #             print(self.boxes[i])
    #             return number
    #     except ValueError:
    #         return ValueError
        
    def run(self):
        self.root.mainloop()
        
