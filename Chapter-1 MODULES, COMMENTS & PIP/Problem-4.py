import os

# Specify the directory (current directory in this example)
directory = '/'

# List and print all files and folders in the directory
for item in os.listdir(directory):
    print(item)