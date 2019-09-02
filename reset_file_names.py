"""
Easy way to recover original files for testing the clean_lyric_driver.py module
Due to the numerous .txt lyric files that have different patterns and orders,
this little script was written to quickly restore the lyric text back to its original state.
"""

from shutil import copyfile
import os
from txt_lyrics import test_files

files_to_clean, original_files = test_files()

files_to_clean.sort()

print(files_to_clean)

path = os.getcwd()  # C:\Users\adamc\PycharmProjects\lyric_cleaner
# print(os.path.join(path, original_files[1]))
print()

for i in range(0, int(len(original_files))):
    og = os.path.join(path, original_files[i])
    ng = os.path.join(path, files_to_clean[i])

    print(f'Found Original File: {og}')
    print(f'Writing as: {ng}', '\n')

    copyfile(og, ng)
