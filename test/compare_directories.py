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

def do_compare(dir1, dir2, file_extension):
    diff_files = compare_files_in_directories(dir1, dir2, file_extension)
   
    print('-' * 70)
    print(f'Comparing dir1 {dir1}\n          dir2 {dir2}\n          extension {file_extension}')

    if diff_files:
        print("Differences found between the following files:")
        for file1, file2 in diff_files:
            print(f"{file1} and {file2} are different.")
    else:
        print("No differences found among common files.")


if __name__ == "__main__":
    dir1 = '../src'
    dir2 = '../../../gitlab/montty/src'
    file_extension = '.py'
    do_compare(dir1, dir2, file_extension)
    
    dir1 = '../test'
    dir2 = '../../../gitlab/montty/test'
    file_extension = '.py'
    do_compare(dir1, dir2, file_extension)
    
