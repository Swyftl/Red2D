import tkinter as tk
from tkinter import messagebox
import json

# Example inputs table (list of dictionaries)
inputs = []

# Function to add a new input
def add_input():
    input_name = input_name_entry.get()
    keys = keys_entry.get().split(',')
    
    # Check for valid input
    if not input_name or not keys:
        messagebox.showerror("Error", "Please provide both an input name and keys.")
        return
    
    # Add to the inputs list
    inputs.append({'name': input_name, 'keys': keys})
    update_input_list()

# Function to delete the selected input
def delete_input():
    try:
        selected_index = input_listbox.curselection()[0]
        del inputs[selected_index]
        update_input_list()
    except IndexError:
        messagebox.showerror("Error", "Please select an input to delete.")

# Function to update the displayed list of inputs
def update_input_list():
    input_listbox.delete(0, tk.END)
    for input_data in inputs:
        input_listbox.insert(tk.END, f"{input_data['name']}: {', '.join(input_data['keys'])}")

# Function to save inputs to a file
def save_to_file():
    with open('input.R2D', 'w') as file:
        json.dump(inputs, file, indent=4)
    messagebox.showinfo("Saved", "Input file saved successfully!")

# Function to load inputs from the file
def load_from_file():
    global inputs
    try:
        with open('input.R2D', 'r') as file:
            inputs = json.load(file)
        update_input_list()
    except FileNotFoundError:
        messagebox.showwarning("File Not Found", "No previous input file found.")
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Error loading input file.")

# Set up the main tkinter window
root = tk.Tk()
root.title("Input Editor for Game Engine")

# Input Name Section
input_name_label = tk.Label(root, text="Input Name:")
input_name_label.grid(row=0, column=0)

input_name_entry = tk.Entry(root)
input_name_entry.grid(row=0, column=1)

# Keys Section
keys_label = tk.Label(root, text="Assigned Keys (comma-separated):")
keys_label.grid(row=1, column=0)

keys_entry = tk.Entry(root)
keys_entry.grid(row=1, column=1)

# Add Input Button
add_input_button = tk.Button(root, text="Add Input", command=add_input)
add_input_button.grid(row=2, column=0, columnspan=2)

# Listbox to display current inputs
input_listbox = tk.Listbox(root, width=50, height=10)
input_listbox.grid(row=3, column=0, columnspan=2)

# Delete Input Button
delete_input_button = tk.Button(root, text="Delete Selected Input", command=delete_input)
delete_input_button.grid(row=4, column=0, columnspan=2)

# Save Button
save_button = tk.Button(root, text="Save to File", command=save_to_file)
save_button.grid(row=5, column=0, columnspan=2)

# Load Button
load_button = tk.Button(root, text="Load from File", command=load_from_file)
load_button.grid(row=6, column=0, columnspan=2)

# Start the tkinter main loop
root.mainloop()
