#!/usr/bin/env python

import os
import shutil

# Modify the Paths:
#     Change /path/to/source and /path/to/destination to your actual
#     source and destination directories
#
# Set the File Extensions:
#     Update the file_extensions list with the file types you want to copy
#
# Run the Script:
#     Save the script to a .py file and run it with Python
#
# Important Notes
#     The script uses shutil.copy2 to preserve file metadata.
#     Make sure you have the necessary permissions to read from the source
#     and write to the destination directories
#
# https://docs.python.org/3/library/shutil.html
# https://www.geeksforgeeks.org/python-shutil-copy2-method/


def copy_files(src_dir, dest_dir, extensions):
    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)

    # Walk through the source directory
    for dirpath, dirnames, filenames in os.walk(src_dir):
        for filename in filenames:
            # Check if the file has one of the specified extensions
            if any(filename.endswith(ext) for ext in extensions):
                # Construct full file paths
                src_file = os.path.join(dirpath, filename)
                dest_file = os.path.join(
                    dest_dir, os.path.relpath(src_file, src_dir))

                # Create the destination directory if it doesn't exist
                os.makedirs(os.path.dirname(dest_file), exist_ok=True)

                # Copy the file
                shutil.copy2(src_file, dest_file)
                print(f"Copied: {src_file} to {dest_file}")


if __name__ == "__main__":
    # Add any extensions you want to copy
    file_extensions = ['.md', '.png', '.sh', '.csv', '.py']
    # src
    source_directory = "./src"
    destination_directory = "../../github/montty/src"
    copy_files(source_directory, destination_directory, file_extensions)

    # test
    source_directory = "./test"
    destination_directory = "../../github/montty/test"
    copy_files(source_directory, destination_directory, file_extensions)
