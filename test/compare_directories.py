#!/usr/bin/env python

import os
import filecmp

def collect_files(directory, file_extension):
    """Recursively collect files with the specified extension from the directory."""
    matched_files = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(file_extension):
                matched_files[file] = os.path.join(root, file)
    return matched_files

def compare_files_in_directories(dir1, dir2, file_extension):
    """Compare files of the specified extension in two directories."""
    files1 = collect_files(dir1, file_extension)
    files2 = collect_files(dir2, file_extension)
    
    differences = []

    # Find common files and compare them
    for file in files1.keys() & files2.keys():  # intersection
        if not filecmp.cmp(files1[file], files2[file], shallow=False):
            differences.append((files1[file], files2[file]))

    return differences

if __name__ == "__main__":
    #dir1_path = input("Enter the first directory path: ")
    #dir2_path = input("Enter the second directory path: ")
    #ext = input("Enter the file extension (e.g., .txt): ")
    dir1_path = '../src'
    dir2_path = '../../../gitlab/montty/src'
    ext = '.py'
    
    diff_files = compare_files_in_directories(dir1_path, dir2_path, ext)
    
    if diff_files:
        print("Differences found between the following files:")
        for file1, file2 in diff_files:
            print(f"{file1} and {file2} are different.")
    else:
        print("No differences found among common files.")


#if __name__ == "__main__":
#    dir1_path = '../'
#    dir2_path = '../../../gitlab/montty'
#    ext = '.py'
#    do_compare(dir1_path, dir2_path, ext)
    
