import os
import filecmp

# The script collects files with the specified extension from both 
# directories
#
# It identifies common files (those with the same name) in both 
# directories
#
# For each common file, it uses filecmp.cmp to compare the contents
#
# It prints out any files that differ
#
# Make sure the directories you provide contain files with the 
# specified extension for the comparison to be meaningful
#

def compare_files_in_directories(dir1, dir2, file_extension):
    # Gather all files with the specified extension in both directories
    files1 = {f for f in os.listdir(dir1) if f.endswith(file_extension)}
    files2 = {f for f in os.listdir(dir2) if f.endswith(file_extension)}
    
    # Find common files between the two directories
    common_files = files1.intersection(files2)
    differences = []

    # Compare each common file
    for file in common_files:
        file1 = os.path.join(dir1, file)
        file2 = os.path.join(dir2, file)
        if not filecmp.cmp(file1, file2, shallow=False):
            differences.append((file1, file2))

    return differences

if __name__ == "__main__":
    #dir1_path = input("Enter the first directory path: ")
    #dir2_path = input("Enter the second directory path: ")
    #ext = input("Enter the file extension (e.g., .txt): ")
    dir1_path = './src'
    dir2_path = '../../github/montty/src'
    ext = '.py'
    
    diff_files = compare_files_in_directories(dir1_path, dir2_path, ext)
    
    if diff_files:
        print("Differences found between the following files:")
        for file1, file2 in diff_files:
            print(f"{file1} and {file2} are different.")
    else:
        print("No differences found among common files.")

