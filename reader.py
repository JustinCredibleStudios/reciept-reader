# Reciept Reader Prototype
# Justin S. Miller Octotber 2, 2024

# Importing Libararies
from tkinter import *
from tkinter import filedialog
import os

# Defining Functions
def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Process the uploaded file
        print("File uploaded:", file_path)
        
        # Defining the Destinations
        destination_folder = "C:/Users/Jusrin S. Millero/OneDrive/Desktop/CodeProjects/Receipt_Reader"
        
        # Saving the file to the destination folder
        with open(os.path.join(destination_folder, os.path.basename(file_path)), "wb") as destination_file:
            with open(file_path, "rb") as source_file:
                destination_file.write(source_file.read())
                
        
        # Update the Gui
        print("File saved to:", os.path.join(destination_folder, os.path.basename(file_path)))


# Creating the window
window = Tk()

# Contructing the window
window.title("Receipt Reader")
window.geometry("900x900")

button = Button(window, text="Upload Receipt", command=upload_file)
button.pack()

# Drawing the window
window.mainloop()