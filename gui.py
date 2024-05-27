import tkinter as tk
import random
class Gui: 
    
    def __init__(self):
        self.root = tk.Tk(className="num_search")
        self.root.minsize(800, 600)

        self.title_label = tk.Label(self.root, text="Search for a value!")
        self.prompt_label = tk.Label(self.root, text="Type in a value to search for it in this list array")
        self.entry_box = tk.Entry(self.root)
        self.enter_button = tk.Button(self.root, text="Enter", command=self.update_label)
        
        self.create_num_array()
        print(self.create_num_array())
        
        self.title_label.pack()
        self.prompt_label.pack()
        self.entry_box.pack()
        self.enter_button.pack()
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
    
    def run(self):
        self.root.mainloop()
        
