import os
from tkinter import filedialog, Tk

# Define the storage directory and file
STORAGE_FILE = os.path.join(os.path.expanduser("~"), ".crosshair-saver")


# Function to load the last used directory
def load_last_directory():
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r") as f:
            return f.read().strip() or "/"
    return "/"


# Function to save the last used directory
def save_last_directory(directory):
    with open(STORAGE_FILE, "w") as f:
        f.write(directory)


last_used_directory = load_last_directory()


def create_cfg_file():
    os.system("cls")
    print(
        """
   ___               _         _       ___                   
  / __|_ _ ___ _____| |_  __ _(_)_ _  / __| __ ___ _____ _ _ 
 | (__| '_/ _ (_-<_-< ' \/ _` | | '_| \__ \/ _` \ V / -_) '_|
  \___|_| \___/__/__/_||_\__,_|_|_|   |___/\__,_|\_/\___|_|  
                                                                                                                                                                                                            
"""
    )
    global last_used_directory

    crosshaircode = input("Enter Crosshair Code: ").strip()
    name = input("Enter Name: ").strip()

    if not crosshaircode or not name:
        print("Error: Please fill out both fields!")
        return

    # Hide the main tkinter window
    root = Tk()
    root.withdraw()
    filepath = filedialog.asksaveasfilename(
        initialdir=last_used_directory,
        title="Save As",
        initialfile=f"ch_{name}.cfg",
        filetypes=[("CFG Files", "*.cfg")],
    )
    root.destroy()

    if not filepath:
        return

    # Update last_used_directory after user selects a path
    last_used_directory = os.path.dirname(filepath)
    save_last_directory(last_used_directory)

    with open(filepath, "w") as file:
        file.write(f"apply_crosshair_code {crosshaircode}\n")
        file.write("clear\n")
        file.write(f'echo "{name} loaded"\n')


if __name__ == "__main__":
    while True:
        create_cfg_file()
