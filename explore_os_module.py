
#task 1 Directory Inspector
import os 

#function that lists all files and and subdirectories 
def list_directory_contents():
    user_dir = input("Input directory: ")
    try:
    # List all items in the directory
        print(user_dir)
        open_dir = os.listdir(user_dir)
    # Print the list of items
        print("Contents of the directory:")
        for line in open_dir:
            print(line)
    #error messages
    except FileNotFoundError:
        print("Directory doesn't exist.")
    except PermissionError:
        print("Permission not granted.")


list_directory_contents()
