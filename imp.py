import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
import csv
import os
import matplotlib.pyplot as plt
from ttkthemes import ThemedStyle
from tkinter import messagebox

# Function to validate customer ID
def validate_customer_id(input):
    if len(input) == 3 and input[0].isalpha() and input[1:].isdigit():
        return True
    return False

# Function to validate age
def validate_age(input):
    if len(input) == 2:
        try:
            int(input)
            return True
        except ValueError:
            pass
    return False

# Function to validate product ID
def validate_product_id(input):
    # Add your validation criteria for product ID
    return True

# Function to validate marital status
def validate_marital_status(input):
    # Add your validation criteria for marital status
    return True


# Function to validate state
def validate_state(input):
    # Add your validation criteria for state
    return True


# Function to validate zone
def validate_zone(input):
    # Add your validation criteria for zone
    return True


# Function to validate orders
def validate_orders(input):
    # Add your validation criteria for orders
    return True


# Function to validate amount
def validate_amount(input):
    # Add your validation criteria for amount
    return True


# Function to add data
def add_data():
    customer_id = entry_customer_id.get()
    product_id = product_id_var.get()
    age = entry_age.get()
    marital_status = marital_status_var.get()
    state = entry_state.get()
    zone = zone_var.get()
    orders = entry_orders.get()
    amount = entry_amount.get()

    # Validate inputs
    if not validate_customer_id(customer_id):
        # Display error message or take appropriate action
        return

    if not validate_product_id(product_id):
        # Display error message or take appropriate action
        return

    if not validate_age(age):
        # Display error message or take appropriate action
        return

    if not validate_marital_status(marital_status):
        # Display error message or take appropriate action
        return

    if not validate_state(state):
        # Display error message or take appropriate action
        return

    if not validate_zone(zone):
        # Display error message or take appropriate action
        return

    if not validate_orders(orders):
        # Display error message or take appropriate action
        return

    if not validate_amount(amount):
        # Display error message or take appropriate action
        return

    file_exists = os.path.isfile('data.csv')

    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["CustomerID", "ProductID", "Age", "Marital Status", "State", "Zone", "Orders", "Amount"])

        writer.writerow([customer_id, product_id, age, marital_status, state, zone, orders, amount])

    # Clear the entry fields after adding data
    entry_customer_id.delete(0, tk.END)
    product_id_var.set("")
    entry_age.delete(0, tk.END)
    marital_status_var.set("")
    entry_state.delete(0, tk.END)
    zone_var.set("")
    entry_orders.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

# Function to create product ID graph
def create_product_id_graph():
    data = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    product_ids = [row[1] for row in data[1:]]  # Exclude header row
    amounts = [float(row[7]) for row in data[1:]]  # Exclude header row and convert to float

    plt.bar(product_ids, amounts)
    plt.xlabel('ProductID')
    plt.ylabel('Amount')
    plt.title('ProductID vs Amount')
    plt.show()


# Function to create zone graph
def create_zone_graph():
    data = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    zones = [row[5] for row in data[1:]]  # Exclude header row
    amounts = [float(row[7]) for row in data[1:]]  # Exclude header row and convert to float

    plt.bar(zones, amounts)
    plt.xlabel('Zone')
    plt.ylabel('Amount')
    plt.title('Zone vs Amount')
    plt.xticks(rotation=45)
    plt.show()


# Function to create marital status graph
def create_marital_status_graph():
    data = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    marital_status = [row[3] for row in data[1:]]  # Exclude header row
    orders = [int(row[6]) for row in data[1:]]  # Exclude header row and convert to integer

    plt.bar(marital_status, orders)
    plt.xlabel('Marital Status')
    plt.ylabel('Orders')
    plt.title('Marital Status vs Orders')
    plt.show()


# Create the main window
window = tk.Tk()
window.title("Data Entry")
window.geometry("400x400")


# Themed style for the window and buttons
themed_style = ThemedStyle(window)
themed_style.set_theme("arc")  # Choose a theme (e.g., "arc", "radiance", "clam", etc.)

# Create notebook widget
notebook = ttk.Notebook(window)
notebook.pack(pady=10)

# Create data entry tab
data_entry_tab = ttk.Frame(notebook)
notebook.add(data_entry_tab, text="Data Entry")

# Create data visualization tab
data_visualization_tab = ttk.Frame(notebook)
notebook.add(data_visualization_tab, text="Data Visualization")

# Customer ID entry field and label
label_customer_id = ttk.Label(data_entry_tab, text="Customer ID:")
label_customer_id.grid(row=0, column=0, padx=10, pady=10)
entry_customer_id = ttk.Entry(data_entry_tab)
entry_customer_id.grid(row=0, column=1, padx=10, pady=10)
entry_customer_id.focus_set()

# Product ID dropdown and label
label_product_id = ttk.Label(data_entry_tab, text="Product ID:")
label_product_id.grid(row=1, column=0, padx=10, pady=10)
product_id_var = StringVar()
product_id_dropdown = ttk.OptionMenu(data_entry_tab, product_id_var, "", "P01", "P02", "P03", "P04", "P05", "P06", "P07", style="TMenubutton")
product_id_dropdown.grid(row=1, column=1, padx=10, pady=10)

# Age entry field and label
label_age = ttk.Label(data_entry_tab, text="Age:")
label_age.grid(row=2, column=0, padx=10, pady=10)
entry_age = ttk.Entry(data_entry_tab)
entry_age.grid(row=2, column=1, padx=10, pady=10)

# Marital Status dropdown and label
label_marital_status = ttk.Label(data_entry_tab, text="Marital Status:")
label_marital_status.grid(row=3, column=0, padx=10, pady=10)
marital_status_var = StringVar()
marital_status_dropdown = ttk.OptionMenu(data_entry_tab, marital_status_var, "", "0", "1", style="TMenubutton")
marital_status_dropdown.grid(row=3, column=1, padx=10, pady=10)

# State entry field and label
label_state = ttk.Label(data_entry_tab, text="State:")
label_state.grid(row=4, column=0, padx=10, pady=10)
entry_state = ttk.Entry(data_entry_tab)
entry_state.grid(row=4, column=1, padx=10, pady=10)

# Zone dropdown and label
label_zone = ttk.Label(data_entry_tab, text="Zone:")
label_zone.grid(row=5, column=0, padx=10, pady=10)
zone_var = StringVar()
zone_dropdown = ttk.OptionMenu(data_entry_tab, zone_var, "", "Northern", "Southern", "Eastern", "Western", "Central", style="TMenubutton")
zone_dropdown.grid(row=5, column=1, padx=10, pady=10)

# Orders entry field and label
label_orders = ttk.Label(data_entry_tab, text="Orders:")
label_orders.grid(row=6, column=0, padx=10, pady=10)
entry_orders = ttk.Entry(data_entry_tab)
entry_orders.grid(row=6, column=1, padx=10, pady=10)

# Amount entry field and label
label_amount = ttk.Label(data_entry_tab, text="Amount:")
label_amount.grid(row=7, column=0, padx=10, pady=10)
entry_amount = ttk.Entry(data_entry_tab)
entry_amount.grid(row=7, column=1, padx=10, pady=10)

# Add data button
add_button = ttk.Button(data_entry_tab, text="Add Data", command=add_data)
add_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Create product ID graph button
product_id_graph_button = ttk.Button(data_visualization_tab, text="ProductID Graph", command=create_product_id_graph)
product_id_graph_button.pack(pady=10)

# Create zone graph button
zone_graph_button = ttk.Button(data_visualization_tab, text="Zone Graph", command=create_zone_graph)
zone_graph_button.pack(pady=10)

# Create marital status graph button
marital_status_graph_button = ttk.Button(data_visualization_tab, text="Marital Status Graph", command=create_marital_status_graph)
marital_status_graph_button.pack(pady=10)

# Function to clear the input fields
def clear_fields():
    entry_customer_id.delete(0, tk.END)
    product_id_var.set("")
    entry_age.delete(0, tk.END)
    marital_status_var.set("")
    entry_state.delete(0, tk.END)
    zone_var.set("")
    entry_orders.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

# Function to search and delete a row
def search_and_delete():
    customer_id = entry_customer_id.get()
    product_id = product_id_var.get()
    age = entry_age.get()
    marital_status = marital_status_var.get()
    state = entry_state.get()
    zone = zone_var.get()
    orders = entry_orders.get()
    amount = entry_amount.get()

    # Read data from the file
    data = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    # Find the row index to delete
    row_index = None
    for index, row in enumerate(data):
        if row[0] == customer_id and row[1] == product_id and row[2] == age and row[3] == marital_status \
                and row[4] == state and row[5] == zone and row[6] == orders and row[7] == amount:
            row_index = index
            break

    # Delete the row if found
    if row_index is not None:
        del data[row_index]

        # Write updated data back to the file
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        messagebox.showinfo("Success", "Row deleted successfully.")

        # Clear the entry fields after deleting data
        clear_fields()
    else:
        messagebox.showerror("Error", "Row not found.")

# Search and Delete button
search_delete_button = ttk.Button( text="Search and Delete", command=search_and_delete)
search_delete_button.pack(pady=10)

def search_data():
    customer_id = entry_search_customer_id.get()
    if validate_customer_id(customer_id):
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            found_rows = []
            for row in reader:
                if row[0] == customer_id:
                    found_rows.append(row)

            if found_rows:
                display_data(found_rows)
            else:
                messagebox.showinfo("Search Result", f"No data found for Customer ID: {customer_id}")
    else:
        messagebox.showwarning("Invalid Input", "Please enter a valid Customer ID (e.g., A01)")

def search_data():
    customer_id = entry_search_customer_id.get()
    if validate_customer_id(customer_id):
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            found_rows = []
            for row in reader:
                if row[0] == customer_id:
                    found_rows.append(row)

            if found_rows:
                display_data(found_rows)
            else:
                messagebox.showinfo("Search Result", f"No data found for Customer ID: {customer_id}")
    else:
        messagebox.showwarning("Invalid Input", "Please enter a valid Customer ID (e.g., A01)")

def display_data(rows):
    result_window = tk.Toplevel()
    result_window.title("Search Result")
    result_window.geometry("400x400")

    tree_view = ttk.Treeview(result_window)
    tree_view.pack(fill="both", expand=True)

    # Define columns
    tree_view["columns"] = ("CustomerID", "ProductID", "Age", "MaritalStatus", "State", "Zone", "Orders", "Amount")

    # Format columns
    tree_view.column("#0", width=0, stretch=tk.NO)
    tree_view.column("CustomerID", anchor=tk.W, width=80)
    tree_view.column("ProductID", anchor=tk.W, width=80)
    tree_view.column("Age", anchor=tk.W, width=50)
    tree_view.column("MaritalStatus", anchor=tk.W, width=100)
    tree_view.column("State", anchor=tk.W, width=80)
    tree_view.column("Zone", anchor=tk.W, width=80)
    tree_view.column("Orders", anchor=tk.W, width=60)
    tree_view.column("Amount", anchor=tk.W, width=80)

    # Create headings
    tree_view.heading("#0", text="", anchor=tk.W)
    tree_view.heading("CustomerID", text="Customer ID", anchor=tk.W)
    tree_view.heading("ProductID", text="Product ID", anchor=tk.W)
    tree_view.heading("Age", text="Age", anchor=tk.W)
    tree_view.heading("MaritalStatus", text="Marital Status", anchor=tk.W)
    tree_view.heading("State", text="State", anchor=tk.W)
    tree_view.heading("Zone", text="Zone", anchor=tk.W)
    tree_view.heading("Orders", text="Orders", anchor=tk.W)
    tree_view.heading("Amount", text="Amount", anchor=tk.W)

    # Insert data
    for row in rows:
        tree_view.insert("", tk.END, values=row)

    result_window.mainloop()

# Data Entry Tab
data_entry_tab = ttk.Frame(window)
data_entry_tab.pack(pady=10)

# Search Frame
search_frame = ttk.LabelFrame(data_entry_tab, text="Search")
search_frame.pack(pady=10)

# Search Customer ID Label and Entry
label_search_customer_id = ttk.Label(search_frame, text="Customer ID:")
label_search_customer_id.grid(row=0, column=0, padx=5, pady=5)
entry_search_customer_id = ttk.Entry(search_frame)
entry_search_customer_id.grid(row=0, column=1, padx=5, pady=5)

# Search Button
search_button = ttk.Button(search_frame, text="Search", command=search_data)
search_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Start the main loop
window.mainloop()