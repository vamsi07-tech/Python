'''
Use the os module to:
Print the current working directory
List all files and folders in the current directory
Create a new folder my_folder

Use the shutil module to:
Copy a file from one folder to another
Move a file to a new folder
Delete a file (careful: irreversible!)'''

import os
import shutil

# Get the current working directory
current_dir = os.getcwd()
print("Current directory:", current_dir)
os.makedirs("my_folder", exist_ok=True)

# List all files and folders in the current directory
print("\nFiles and folders in current directory:")
print(os.listdir(current_dir))

# Create a dummy file for testing
test_file = "F:\\Python\\my_folder\\my_file.txt"
with open(test_file, 'w') as f:
    f.write("This is a test file")

# Copy a file
shutil.copy(test_file, "F:\\Python\\my_folder\\my_file_copy.txt")
print(f"\nFile copied successfully")

# Create directory for moving
os.makedirs("F:\\Python\\my_folder\\new_directory", exist_ok=True)
# Move a file or directory
shutil.move("F:\\Python\\my_folder\\my_file_copy.txt", "F:\\Python\\my_folder\\new_directory\\my_file_copy.txt")
print("File moved successfully")