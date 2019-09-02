import csv
import os


def test_files():
    current_dir = os.getcwd()
    lyric_dir = 'lyrics'
    new_work_dir = os.path.join(current_dir, lyric_dir)
    os.chdir(new_work_dir)

    all_txt_files = os.listdir()

    parsing_test_list = []
    original_files = []

    for lyric_file in all_txt_files:
        if '(ORIGINAL)' not in lyric_file:
            parsing_test_list.append(lyric_file)
        else:
            original_files.append(lyric_file)

    return parsing_test_list, original_files


def main(file_to_work_on):
    # CLASSES AND FUNCTIONS FOR MAIN

    class LyricsFromText:

        def __init__(self, lyric):
            # FUNCTIONS FOR CLASS
            def already_cleaned():
                bool_list = []
                if length_of_lyrics >= 4:
                    try:
                        if isinstance(lyric[0][0], str):
                            if f'Artist : {artist}' in lyric[0][0]:
                                bool_list.append(True)
                            else:
                                bool_list.append(False)
                        if isinstance(lyric[1][0], str):
                            if f'Title : {song_title}' in lyric[1][0]:
                                bool_list.append(True)
                            else:
                                bool_list.append(False)
                        if len(lyric[2]) == 0:
                            bool_list.append(True)
                        else:
                            bool_list.append(False)
                    except IndexError:
                        bool_list.append(False)

                if all(bool_list):
                    self.clean = True
                    return self.clean
                else:
                    self.clean = False

            def tail_finder():

                flag = True
                counter = 10

                # tries to retrieve the last 10 rows of the lyric file
                if length_of_lyrics > 1:
                    while flag:
                        try:
                            tail = lyric[-counter:]
                            # index = length_of_lyrics -
                            index = length_of_lyrics - len(tail)
                            return tail, index
                        except IndexError:
                            flag = True
                            counter -= 1

            def difficult_middle_finder():
                self.head = None
                (self.tail,
                 self.index) = tail_finder()  # retries tail and index (last few lines and the location of end)

                # if len(self.tail) == len(lyric):  # dont overlap middle and tail as middle contains all lyrics
                #     self.tail = None

                # Tries to find the actual lyrics in the file when the lyric text file is not known a priori

                if self.index != 0:  # if there actually is a middle section! Find It

                    key_words.append(artist.lower())  # appends artist to key word search
                    key_words.append(song_title.lower())  # appends song title to key word search

                    key_positions = [[] for _ in range(0, len(key_words))]
                    new_line_position = []

                    for j, word in enumerate(key_words):  # searches through key words
                        for i in range(0, 4):  # searches first 3 lines
                            if len(lyric[i]) != 0:
                                if key_words[j] in lyric[i][0].lower():
                                    key_positions[j].append(i)
                                    break  # continue to next word

                    for i in range(0, 4):  # searches first 3 lines
                        if len(lyric[i]) == 0:
                            new_line_position.append(i)  # appends empty line

                    nested_index = [item for item in key_positions]
                    nested_index.append(new_line_position)
                    #  [key_positions[0], key_positions[1], new_line_position]
                    max_index = []
                    # flag_index = False

                    for item in nested_index:
                        if len(item) != 0:
                            # flag_index = True  # at least one index is present
                            if len(max_index) == 0:
                                max_index.append(max(item))
                            elif max(item) > max_index[0]:
                                max_index[0] = max(item)

                    if len(max_index) == 0:
                        max_index.append(-1)  # no header using the search criteria above was found

                    self.middle = lyric[max_index[0] + 1: self.index]  # middle chunk of lyrics
                    return self.middle

                else:  # there is no middle, just a tail
                    self.middle = None
                    return self.middle

            # START OF CLASS
            length_of_lyrics = len(lyric)
            key_words = ['artist', 'title']

            already_cleaned()

            if self.clean:  # if lyric is already cleaned, do nothing and return class
                return

            if length_of_lyrics >= 4:  # difficult case where lyric file may have artist, title, and breaks in any order
                for i in range(0, 4):
                    if len(lyric[i]) != 0:
                        if 'instrumental' in lyric[i][0].lower():
                            self.head = None
                            self.middle = [['Instrumental']]
                            self.tail = None
                            return

            if len(lyric[0]) != 0:  # if there is a header, assume standard format
                if key_words[0] and key_words[1] in lyric[0][0].lower():  # Most common lyric file order
                    self.head = (lyric[0])  # retries header (1st line of lyrics file)
                    (self.tail,
                     self.index) = tail_finder()  # retries tail and index (last few lines and the location of end)
                    self.middle = lyric[1:self.index]  # middle chunk of lyrics
                    return
                else:
                    difficult_middle_finder()

            else:  # not instrumental or common format
                difficult_middle_finder()

    def fix_header():

        if lyric_obj.head is not None:
            title_position = lyric_obj.head[0].find('Title : ')

            if song_title in lyric_obj.head[0]:
                correct_song_title = song_title
                # correct_song_title = lyric_obj.head[0].split(song_title)[1]
                hanging_lyric = lyric_obj.head[0].split(song_title)[1]
            else:
                song_title_length = len(song_title)
                stripped_song_title = lyric_obj.head[0].split('Title : ')[1]
                correct_song_title = stripped_song_title[:song_title_length]
                hanging_lyric = lyric_obj.head[0].split(correct_song_title)[1]
            # except

            if 'Unfortunately, we are not licensed' in hanging_lyric:
                hanging_lyric = None

            new_header = \
                [
                    [lyric_obj.head[0][:title_position]],  # e.g. 'Artist : Black Sabbath'
                    ['Title : ' + correct_song_title],  # e.g. 'Title : Iron Man'
                    [],  # empty line between header and lyrics
                ]

            if hanging_lyric is not None:
                new_header.append([hanging_lyric])  # e.g. 'Has he lost his Mind?'

                # cant split song title from lyrics if song title parsed from text file had special symbols in it
            return new_header
        else:  # create titles for lyrics if none are already in the txt file
            new_header = [[f'Artist : {artist}'],
                          [f'Title : {song_title}'],
                          []]
            return new_header

    def fix_tail():
        if lyric_obj.tail is not None:

            texts_to_remove = \
                [
                    artist.lower(),
                    'Credits',  # remove string
                    'Lyrics licensed by',  # Remove all lines below this
                    'External links',  # sometimes line above is not included, thus remove all below this
                    'Nominate as Song of the Day',  # also should be removed
                    'iTunes: ',  # also should be removed
                ]
            new_tail = []
            flag = False

            for line in lyric_obj.tail:  # iterate over all the nested list
                for text in texts_to_remove:  # iterate over list
                    if len(line) != 0:  # line cannot be empty
                        if text.lower() in line[0].lower():
                            if artist.lower() == text:
                                break  # dont include artist name if its there

                            if text == texts_to_remove[0] or \
                                    text == texts_to_remove[2]:  # 'Credits' or 'External..' found
                                new_string = line[0].split(text)[0]  # remove the 'Credits' from lyrics
                                new_tail.append([new_string])
                                new_tail.append([])  # space between official end of lyrics
                                break  # return to outer loop

                            else:  # found bad text at bottom and terminate
                                return new_tail  # failed condition and rest of

                        elif text == texts_to_remove[-1]:  # only append if checked entire list

                            # lyrics are legit, only append after iterating over entire list
                            left_stripped_line = [line[0].lstrip()]  # strip left leading white spaces
                            new_tail.append(left_stripped_line)

                    else:  # append empty line
                        new_tail.append([])
                        break
        else:
            new_tail = None

        return new_tail

    # START OF CODE FOR MAIN

    song_title = file_to_work_on.split(' - ')[1].split('.txt')[0]
    artist = file_to_work_on.split(' - ')[0]

    cleaned_file_str = artist + ' - ' + song_title + ' - cleaned.txt'

    with open(file_to_work_on, 'r', newline='', encoding='utf-8') as original_file:
        lyric_list = list(csv.reader(original_file, delimiter='\n'))
        lyric_obj = LyricsFromText(lyric_list)

        if not lyric_obj.clean:  # if not clean modify text file
            replacement_headers = fix_header()
            replacement_tail = fix_tail()

            try:
                replacement_lyrics = replacement_headers + lyric_obj.middle + replacement_tail
            except TypeError:  # when certain methods return None
                # print('CAUTION ON: ', file_to_work_on)
                possible_none_types = [replacement_headers, lyric_obj.middle, replacement_tail]
                replacement_lyrics = []

                for var_type in possible_none_types:
                    if var_type is not None:
                        replacement_lyrics += var_type
                #
                # print('ERROR ON: ', file_to_work_on)
                # print(type(replacement_headers), type(lyric_obj.middle), type(replacement_tail))
                # print(replacement_headers, lyric_obj.middle, replacement_tail)
                # exit()

            with open(file_to_work_on, 'w', newline='', encoding='utf-8') as new_file:

                lyric_writer = csv.writer(new_file, delimiter='\n')

                for row in replacement_lyrics:
                    lyric_writer.writerow(row)

        else:  # FILE IS ALREADY CLEAN
            pass


if __name__ == '__main__':  # test functionality with 1 file

    file_list, _ = test_files()

    for file in file_list:
        main(file)

    # main(file_list[8])
