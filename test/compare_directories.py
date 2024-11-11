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
    only_in_dir1 = []
    only_in_dir2 = []

    # Find common files and compare them
    common_files = files1.keys() & files2.keys()
    for file in common_files:
        if not filecmp.cmp(files1[file], files2[file], shallow=False):
            differences.append((files1[file], files2[file]))

    # Find files only in dir1
    only_in_dir1 = [files1[file] for file in files1.keys() - files2.keys()]
    # Find files only in dir2
    only_in_dir2 = [files2[file] for file in files2.keys() - files1.keys()]

    return differences, only_in_dir1, only_in_dir2


def do_compare(dir1, dir2, file_extension):
    print('')
    print('-' * 70)
    print(f'Comparing dir1      = {dir1}')
    print(f'          dir2      = {dir2}')
    print(f'          file_extension = {file_extension}')
    print('')

    diff_files, only_in_dir1, only_in_dir2 = compare_files_in_directories(
        dir1, dir2, file_extension)

    if diff_files:
        print("Differences found between the following files:")
        for file1, file2 in diff_files:
            print(f"{file1} and {file2} are different.")
    else:
        print("No differences found among common files.")

    if only_in_dir1:
        print("\nFiles only in the FIRST directory:")
        for file in only_in_dir1:
            print(file)

    if only_in_dir2:
        print("\nFiles only in the SECOND directory:")
        for file in only_in_dir2:
            print(file)

    if not only_in_dir1 and not only_in_dir2:
        print("\nNo files are unique to either directory.")


def main():
    # ..

    dir1 = '..'
    dir2 = '../../gitlab/montty'
    file_extension = '.toml'
    do_compare(dir1, dir2, file_extension)
    file_extension = '.md'
    do_compare(dir1, dir2, file_extension)

    # ../src

    dir1 = '../src'
    dir2 = '../../../gitlab/montty/src'
    file_extension = '.py'
    do_compare(dir1, dir2, file_extension)
    file_extension = '.sh'
    do_compare(dir1, dir2, file_extension)

    # test

    dir1 = '../test'
    dir2 = '../../../gitlab/montty/test'
    file_extension = '.py'
    do_compare(dir1, dir2, file_extension)
    file_extension = '.sh'
    do_compare(dir1, dir2, file_extension)


if __name__ == "__main__":
    main()
