import csv
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

class SmartDevice:
    def __init__(self, name, device_type, price, category, model, release_date, features, color, brand, os):
        self.name = name
        self.device_type = device_type
        self.price = price
        self.category = category
        self.model = model
        self.release_date = release_date
        self.features = features
        self.color = color
        self.brand = brand
        self.os = os

class SmartDeviceData:
    def __init__(self, filename):
        self.filename = filename
        self.devices = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    device = SmartDevice(
                        row['Name'],
                        row['Type'],
                        row['Price'],
                        row['Category'],
                        row['Model'],
                        row['Release'],
                        row['Features'],
                        row['Color'],
                        row['Brand'],
                        row['OS']
                    )
                    self.devices.append(device)
        except FileNotFoundError:
            messagebox.showerror("Error", f"File '{self.filename}' not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred while loading data: {e}")

    def save_data(self):
        try:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Type', 'Price', 'Category', 'Model', 'Release', 'Features', 'Color', 'Brand', 'OS'])
                for device in self.devices:
                    writer.writerow([device.name, device.device_type, device.price, device.category,
                                     device.model, device.release_date, device.features,
                                     device.color, device.brand, device.os])
            messagebox.showinfo("Success", "Data saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred while saving data: {e}")

    def add_device(self, name, device_type, price, category, model, release_date, features, color, brand, os):
        new_device = SmartDevice(name, device_type, price, category, model, release_date, features, color, brand, os)
        self.devices.append(new_device)
        self.save_data()  # Save data after adding a device
        messagebox.showinfo("Success", "Device added successfully!")

    def display_all_devices(self):
        device_list = []
        for device in self.devices:
            device_info = f"Name: {device.name}\nType: {device.device_type}\nPrice: {device.price}\nCategory: {device.category}\nModel: {device.model}\nRelease Date: {device.release_date}\nFeatures: {device.features}\nColor: {device.color}\nBrand: {device.brand}\nOS: {device.os}\n"
            device_list.append(device_info)
            
        devices_text = "\n\n".join(device_list)
        messagebox.showinfo("Devices", devices_text)

    def search_device(self, search_term):
        search_term = search_term.lower()
        found_devices = [device for device in self.devices if search_term in device.name.lower() or search_term in device.category.lower()]
        if found_devices:
            device_list = []
            for device in found_devices:
                device_info = f"Name: {device.name}\nType: {device.device_type}\nCategory: {device.category}"
                device_list.append(device_info)
            devices_text = "\n\n".join(device_list)
            messagebox.showinfo("Found Devices", devices_text)
        else:
            messagebox.showinfo("No Devices Found", "No devices found matching the search criteria.")

    def remove_device(self, index):
        try:
            if 0 <= index < len(self.devices):
                removed_device = self.devices.pop(index)
                self.save_data()  # Save data after removing a device
                messagebox.showinfo("Success", f"Device '{removed_device.name}' removed successfully!")
            else:
                messagebox.showerror("Error", "Invalid device number.")
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred while removing device: {e}")

    def update_device(self, index, name, device_type, price, category, model, release_date, features, color, brand, os):
        try:
            if 0 <= index < len(self.devices):
                updated_device = SmartDevice(name, device_type, price, category, model, release_date, features, color, brand, os)
                self.devices[index] = updated_device
                self.save_data()  # Save data after updating a device
                messagebox.showinfo("Success", f"Device '{updated_device.name}' updated successfully!")
            else:
                messagebox.showerror("Error", "Invalid device number.")
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred while updating device: {e}")


smart_device_data = SmartDeviceData(r'DIT102/final proj/data.csv')

#GUI Part

root = tk.Tk()
root.title('Smart Device Management')
root.geometry('600x600+600+400')

# Function to handle adding a new device
def add_device():
    add_window = tk.Toplevel(root)
    add_window.title("Add New Device")

    # Entry fields
    tk.Label(add_window, text="Name:").grid(row=0, column=0)
    tk.Label(add_window, text="Type:").grid(row=1, column=0)
    tk.Label(add_window, text="Price:").grid(row=2, column=0)
    tk.Label(add_window, text="Category:").grid(row=3, column=0)
    tk.Label(add_window, text="Model:").grid(row=4, column=0)
    tk.Label(add_window, text="Release Date:").grid(row=5, column=0)
    tk.Label(add_window, text="Features:").grid(row=6, column=0)
    tk.Label(add_window, text="Color:").grid(row=7, column=0)
    tk.Label(add_window, text="Brand:").grid(row=8, column=0)
    tk.Label(add_window, text="OS:").grid(row=9, column=0)

    name_entry = ttk.Entry(add_window)
    type_entry = ttk.Entry(add_window)
    price_entry = ttk.Entry(add_window)
    category_entry = ttk.Entry(add_window)
    model_entry = ttk.Entry(add_window)
    release_date_entry = ttk.Entry(add_window)
    features_entry = ttk.Entry(add_window)
    color_entry = ttk.Entry(add_window)
    brand_entry = ttk.Entry(add_window)
    os_entry = ttk.Entry(add_window)

    name_entry.grid(row=0, column=1)
    type_entry.grid(row=1, column=1)
    price_entry.grid(row=2, column=1)
    category_entry.grid(row=3, column=1)
    model_entry.grid(row=4, column=1)
    release_date_entry.grid(row=5, column=1)
    features_entry.grid(row=6, column=1)
    color_entry.grid(row=7, column=1)
    brand_entry.grid(row=8, column=1)
    os_entry.grid(row=9, column=1)

    # Function to add the device
    def add_device_to_list():
        name = name_entry.get()
        device_type = type_entry.get()
        price = price_entry.get()
        category = category_entry.get()
        model = model_entry.get()
        release_date = release_date_entry.get()
        features = features_entry.get()
        color = color_entry.get()
        brand = brand_entry.get()
        os = os_entry.get()

        smart_device_data.add_device(name, device_type, price, category, model, release_date, features, color, brand, os)
        add_window.destroy()

    # add device confirm button
    ttk.Button(add_window, text="Add Device", command=add_device_to_list).grid(row=10, columnspan=2)

#display all devices
def display_devices():
    smart_device_data.display_all_devices()

# search for devices
def search_devices():
    search_term = simpledialog.askstring("Search Devices", "Enter Name or Category:")
    if search_term:
        smart_device_data.search_device(search_term)

#remove a device
def remove_device():
    index = simpledialog.askinteger("Remove Device", "Enter the device number to remove:") - 1
    if index is not None:
        smart_device_data.remove_device(index)

#update a device
def update_device():
    index = simpledialog.askinteger("Update Device", "Enter the device number to update:") - 1
    if index is not None:
        device = smart_device_data.devices[index]
        update_window = tk.Toplevel(root)
        update_window.title(f"Update Device: {device.name}")

        # Entry fields with current values
        ttk.Label(update_window, text="Name:").grid(row=0, column=0)
        ttk.Label(update_window, text="Type:").grid(row=1, column=0)
        ttk.Label(update_window, text="Price:").grid(row=2, column=0)
        ttk.Label(update_window, text="Category:").grid(row=3, column=0)
        ttk.Label(update_window, text="Model:").grid(row=4, column=0)
        ttk.Label(update_window, text="Release Date:").grid(row=5, column=0)
        ttk.Label(update_window, text="Features:").grid(row=6, column=0)
        ttk.Label(update_window, text="Color:").grid(row=7, column=0)
        ttk.Label(update_window, text="Brand:").grid(row=8, column=0)
        ttk.Label(update_window, text="OS:").grid(row=9, column=0)

        name_entry = ttk.Entry(update_window, textvariable=tk.StringVar(value=device.name))
        type_entry = ttk.Entry(update_window, textvariable=tk.StringVar(value=device.device_type))
        price_entry = ttk.Entry(update_window, textvariable=tk.StringVar(value=device.price))
        category_entry = ttk.Entry(update_window, textvariable=tk.StringVar(value=device.category))
        model_entry = ttk.Entry(update_window, textvariable=tk.StringVar(value=device.model))
        release_date_entry = ttk.Entry(update_window, textvariable=tk.StringVar(value=device.release_date))
        features_entry = ttk.Entry(update_window, textvariable=tk.StringVar(value=device.features))
        color_entry = ttk.Entry(update_window, textvariable=tk.StringVar(value=device.color))
        brand_entry = ttk.Entry(update_window, textvariable=tk.StringVar(value=device.brand))
        os_entry = ttk.Entry(update_window, textvariable=tk.StringVar(value=device.os))

        name_entry.grid(row=0, column=1)
        type_entry.grid(row=1, column=1)
        price_entry.grid(row=2, column=1)
        category_entry.grid(row=3, column=1)
        model_entry.grid(row=4, column=1)
        release_date_entry.grid(row=5, column=1)
        features_entry.grid(row=6, column=1)
        color_entry.grid(row=7, column=1)
        brand_entry.grid(row=8, column=1)
        os_entry.grid(row=9, column=1)

        # Function to update the device
        def update_device_in_list():
            name = name_entry.get()
            device_type = type_entry.get()
            price = price_entry.get()
            category = category_entry.get()
            model = model_entry.get()
            release_date = release_date_entry.get()
            features = features_entry.get()
            color = color_entry.get()
            brand = brand_entry.get()
            os = os_entry.get()

            smart_device_data.update_device(index, name, device_type, price, category, model, release_date, features, color, brand, os)
            update_window.destroy()

        # Confirm Button
        ttk.Button(update_window, text="Update Device", command=update_device_in_list).grid(row=10, columnspan=2)

#Main menu buttons
ttk.Button(root, text="Add Device", command=add_device).pack(pady=5)
ttk.Button(root, text="Display Devices", command=display_devices).pack(pady=5)
ttk.Button(root, text="Search Devices", command=search_devices).pack(pady=5)
ttk.Button(root, text="Remove Device", command=remove_device)
ttk.Button(root, text="Update Device", command=update_device).pack(pady=5)
ttk.Button(root, text="Delete Device", command=remove_device).pack(pady=5)
ttk.Button(root, text="Exit", command=lambda:root.quit() ).pack(pady=5)

# Run the tkinter main loop
root.mainloop()
