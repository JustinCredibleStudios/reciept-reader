# Analyzing Text from pdf
# Justin Miller
# 10/6/2024


# Importing Libraries
import os
import boto3

# Define file name
file_name = "files\\supply_store_receipt.pdf"



# Declaring the Document for analysis
document = file_name

# Creating a textract client
textract = boto3.client('textract')

# calling response
response = textract.analyze_document(
    Document={
        'Bytes': open(document, 'rb').read(),
    },
    FeatureTypes=['TABLES', 'FORMS'],
)

#print(response)

# Print detected text
with open("output.txt", "w") as f:

    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            print (item["Text"], file=f) 