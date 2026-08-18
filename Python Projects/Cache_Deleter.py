import os
import shutil
#current_dir = os.getcwd()
current_dir = "C:\\Users\\Admin\\AppData\\Local\\Temp"
print("Current directory:", current_dir)

try:
    for filename in os.listdir(current_dir):
        file_path = os.path.join(current_dir, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted file: {filename}")
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(f"Deleted directory: {filename}")
        except PermissionError:
            print(f"Skipped (in use): {filename}")
        except OSError as e:
            print(f"Skipped (in use): {filename} - {e}")
    print("Deletion process completed.")
except PermissionError as e:
    print(f"An error occurred: {e}")