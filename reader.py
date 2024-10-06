# Reciept Reader Prototype
# Justin S. Miller Octotber 2, 2024

# Importing Libararies
import os
from tkinter import *
from tkinter import filedialog
import subprocess

# import creates3bucket

# Defining Global Variables
destination_folder = "C:\\Users\\Jusrin S. Millero\\OneDrive\\Desktop\\CodeProjects\\Receipt_Reader\\files"



# Defining Functions
def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        # Check if file is a PDF
        if file_path.endswith(".pdf"):
            print("File uploaded successfully")
            # Saving the file to the destination folder
            with open(os.path.join(destination_folder, os.path.basename(file_path)), "wb") as destination_file:
                with open(file_path, "rb") as source_file:
                    destination_file.write(source_file.read())
        else:
            print("Invalid file type. Please upload a PDF file.")
        
        # Update the Gui
        print("File saved to:", os.path.join(destination_folder, os.path.basename(file_path)))
            
                
        
        # Calling the function to check if the folder is full or empty
        check_folder()

# Function that will see if files folder is full or empty
def check_folder():
    if os.path.exists(destination_folder):
        if not os.listdir(destination_folder):
            print("Folder is empty")
        else:
            subprocess.run(["python", "creates3bucket.py"])

# Creating the window
window = Tk()

# Contructing the window
window.title("Receipt Reader")
window.geometry("500x500")

button = Button(window, text="Upload Receipt", command=upload_file)
button.pack()

# Drawing the window
window.mainloop()