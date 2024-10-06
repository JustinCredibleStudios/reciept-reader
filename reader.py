# Reciept Reader Prototype
# Justin S. Miller Octotber 2, 2024

# Importing Libararies
import os
import boto3
from tkinter import *
from tkinter import filedialog

            
def textanalysis():
    file_name = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    
    document = file_name
    
    textract = boto3.client('textract')
    
    response = textract.analyze_document(
        Document={
            'Bytes': open(document, 'rb').read(),
        },
        FeatureTypes=['TABLES', 'FORMS'],
    )
    
    with open("output.txt", "w") as f:

        for item in response["Blocks"]:
            if item["BlockType"] == "LINE":
                print (item["Text"], file=f)
   

# Creating the window
window = Tk()

# Contructing the window
window.title("Receipt Reader")
window.geometry("50x50")

button = Button(window, text="anaylze", command=textanalysis)
button.pack()

# Drawing the window
window.mainloop()