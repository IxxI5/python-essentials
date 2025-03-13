# Import the `os` module for working with directories
import os

# Create a directory for demonstration purposes
dir_path = os.path.join(os.getcwd(), "demo_dir")
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

print(f"-> Directory {dir_path} created successfully.")

wait = input("-> Check Explorer in VS Code: Press Enter to continue...")

# Create a file for demonstration purposes
file_path = os.path.join(dir_path, "demo_file.txt")

try:
    # Open a file in write mode ('w')
    with open(file_path, 'w') as file:
        # Write to the file
        file.write("Hello, World!")
    print(f"-> File {file_path} created successfully.")
except Exception as e:
    print(f"Error creating file {file_path}: {str(e)}")

wait = input("-> Check Explorer in VS Code: Press Enter to continue...")

# **Opening and Closing Files**
# ---------------------------

try:
    # Open the file in read mode ('r')
    with open(file_path, 'r') as file:
        # Read the file contents
        print(file.read())  # Output: Hello, World!
except Exception as e:
    print(f"Error reading file {file_path}: {str(e)}")

wait = input("-> Check Explorer in VS Code: Press Enter to continue...")

# **File Modes**
# -------------

try:
    # Open the file in append mode ('a')
    with open(file_path, 'a') as file:
        # Append to the file
        file.write("\nThis is appended text.")
    print(f"-> File {file_path} appended successfully.")
except Exception as e:
    print(f"Error appending to file {file_path}: {str(e)}")

wait = input("-> Check Explorer in VS Code: Press Enter to continue...")

# Open the file in read mode ('r') again
try:
    with open(file_path, 'r') as file:
        # Read the updated file contents
        print(file.read())  # Output: Hello, World!\nThis is appended text.
except Exception as e:
    print(f"Error reading file {file_path}: {str(e)}")

wait = input("-> Check Explorer in VS Code: Press Enter to continue...")

# **Binary File Modes**
# --------------------

# Open a binary file in write mode ('wb')
binary_file_path = os.path.join(dir_path, "demo_binary_file.bin")
try:
    with open(binary_file_path, 'wb') as file:
        # Write binary data to the file
        file.write(b"Hello, Binary World!")
    print(f"-> Binary file {binary_file_path} created successfully.")
except Exception as e:
    print(f"Error creating binary file {binary_file_path}: {str(e)}")

wait = input("-> Check Explorer in VS Code: Press Enter to continue...")

# Open the binary file in read mode ('rb')
try:
    with open(binary_file_path, 'rb') as file:
        # Read the binary file contents
        print(file.read())  # Output: b'Hello, Binary World!'
except Exception as e:
    print(f"Error reading binary file {binary_file_path}: {str(e)}")

wait = input("-> Check Explorer in VS Code: Press Enter to continue...")

# **Working with Directories**
# ---------------------------

# List the files in the directory
print(os.listdir(dir_path))  # Output: ['demo_file.txt', 'demo_binary_file.bin']

# Create a subdirectory
subdir_path = os.path.join(dir_path, "subdir")
if not os.path.exists(subdir_path):
    os.makedirs(subdir_path)
    print(f"-> Subdirectory {subdir_path} created successfully.")

# List the files in the subdirectory
print(f"-> Files in {subdir_path}: {os.listdir(subdir_path)}")  # Output: []

wait = input("-> Check Explorer in VS Code: Press Enter to continue...")

# Remove the subdirectory
os.rmdir(subdir_path)

print(f"-> Subdirectory {subdir_path} removed successfully.")
wait = input("-> Check Explorer in VS Code: Press Enter to continue...")

# Remove the file
os.remove(file_path)

print(f"-> File {file_path} removed successfully.")
wait = input("-> Check Explorer in VS Code: Press Enter to continue...")

# Remove the file
os.remove(binary_file_path)

print(f"-> Binary file {binary_file_path} removed successfully.")   
wait = input("-> Check Explorer in VS Code: Press Enter to continue...")