# TODO: 1. access file directory besides mine (works for other users) 2.  open each file and parse for bad lyrics. 4. overwrite file

import os
import csv
import txt_lyrics


def file_ending_parser(file_list):
    file_endings = ['.txt', '.lrc']
    text_lyrics = []
    lrc_lyrics = []
    unknown_lyrics = []

    for file in file_list:
        if file_endings[0] in file:
            text_lyrics.append(file)
        elif file_endings[1] in file:
            lrc_lyrics.append(file)
        else:
            unknown_lyrics.append(file)

    return text_lyrics, lrc_lyrics


if __name__ == '__main__':
    os.chdir(r'C:\Users\adamc\foobar_lyrics')
    list_of_files = os.listdir()

    list_of_text_lyrics, list_of_lrc_lyrics = file_ending_parser(list_of_files)

    print('Number of lyric files to parse through:', len(list_of_files))
    print(list_of_text_lyrics)
