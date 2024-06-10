import tkinter as tk
import random

def __init__(self):
    self.root = tk.Tk(className="num_search")
    self.root.minsize(800, 600)
    self.create_boxes()
    self.root.mainloop()

def search(index=0, previous_index=None):
    """Search method to search for number in array"""
    # clear any previous highlights
    for i in range(100):
        label_list[i].config(bg="SystemButtonFace")
    # if index is out of range stop search
    if index >= len(label_list):
        print("Number not found in grid!")
        label_list[previous_index].config(bg="SystemButtonFace")
        return

    # unhighlight previous label
    if previous_index is not None:
        label_list[previous_index].config(bg="SystemButtonFace")

    search_number = num_input.get()  # get the number entered in the entry box    
    current_label = label_list[index]  # get the current label
    current_label.config(bg="yellow")  # highlight the current label

    # check if label matches search number
    if number_found(current_label.cget("text"), search_number):
        current_label.config(bg="green")  # highlight the matching label and stop searching
        print(current_label.cget("text") + " is found!")
    else:
        # event for next iteration
        root.after(delay, search, index + 1, index)  # delay

def number_found(label_text, search_number):
    """Check if the label text matches the search number."""
    return label_text == search_number

def create_num_array():
    """Generate grid of 100 randomly generated numbers"""
    global label_list
    label_list = []
    for i in range(10):
        for j in range(10):
            random_number = str(random.randint(0, 1000))
            label = tk.Label(root, text=random_number, padx=10, pady=5, borderwidth=.5, relief="groove")
            label.grid(row=i, column=j, padx=5, pady=5)
            label_list.append(label)

# create main window
root = tk.Tk()
root.title("Search Label")
delay = 100  # delay in millis for searching

# create an entry box
num_input = tk.Entry(root)
num_input.grid(row=11, column=5, pady=10, sticky="nsew")

# create search button
search_button = tk.Button(root, text="Search", command=search)
search_button.grid(row=12, column=5, columnspan=1, pady=10)

create_num_array()

# start Tkinter loop
root.mainloop()
