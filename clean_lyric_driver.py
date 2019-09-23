# TODO: add .lyrc parser, as .txt parser is finished

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


def log_writer():
    print('\nNumber of .txt lyric files to parse through:', len(list_of_text_lyrics))
    print("************* EXECUTING LYRIC PARSER ON TEXT FILES *************")

    path = r'C:\Users\adamc\PycharmProjects\lyric_cleaner'
    log_name = os.path.join(path, 'log.txt')

    with open(log_name, 'w', newline='', encoding='utf-8') as opened_file:
        for text_file in list_of_text_lyrics:
            opened_file.write(text_file + '\n')

            txt_lyrics.main(text_file)
    print("\n################ COMPLETE ################")


if __name__ == '__main__':
    os.chdir(r'C:\Users\adamc\foobar_lyrics')  # only works for me
    list_of_files = os.listdir()

    list_of_text_lyrics, list_of_lrc_lyrics = file_ending_parser(list_of_files)
    log_writer()
