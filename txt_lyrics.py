import csv


def main(file_to_work_on):
    class LyricsFromText:

        def __init__(self, lyric):
            def tail_finder():
                length_of_lyrics = len(lyric)
                # print(length_of_lyrics)
                flag = True
                counter = 10

                if length_of_lyrics > 1:
                    while flag:
                        try:
                            tail = lyric[-counter:]
                            index = length_of_lyrics - counter
                            return tail, index
                        except IndexError:
                            flag = True
                            counter -= 1

            self.head = (lyric[0])  # retries header (1st line of lyrics file)
            (self.tail, self.index) = tail_finder()  # retries tail and index (last few lines and the location of end)
            self.middle = lyric[1:self.index]  # middle chunk of lyrics

            # print(self.tailing)

    def fix_header():
        title_position = lyric_obj.head[0].find('Title : ')

        if title_position != -1:
            new_header = [
                [lyric_obj.head[0][:title_position]],  # e.g. 'Artist : Black Sabbath'
                ['Title : ' + song_title],  # e.g. 'Title : Iron Man'
                [],  # empty line between header and lyrics
                [lyric_obj.head[0].split(song_title)[1]],  # e.g. 'Has he lost his Mind?'
            ]
            return new_header
        else:  # create titles for lyrics if none are already in the txt file
            new_header = [[f'Artist : {artist}'],
                          [f'Title : {song_title}'],
                          []]
            return new_header

    def fix_tail():
        texts_to_remove = [
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
                if text in line[0]:
                    if text == texts_to_remove[0]:  # 'Credits' is found
                        new_string = line[0].split(texts_to_remove[0])[0]  # remove the 'Credits' from lyrics
                        new_tail.append([new_string])
                        new_tail.append([])  # space between official end of lyrics
                        break  # return to outer loop

                    else:  # found bad text
                        return new_tail  # failed condition and rest of

                elif text == texts_to_remove[-1]:  # faster to check condition or use enumerate and check number?
                    # lyrics are legit and only append after iterating over entire list
                    new_tail.append(line)

    song_title = file_to_work_on.split(' - ')[1].split('.txt')[0]
    artist = file_to_work_on.split(' - ')[0]

    cleaned_file_str = artist + ' - ' + song_title + ' - cleaned.txt'

    with open(file_to_work_on, 'r', newline='') as original_file:
        lyric_list = list(csv.reader(original_file))
        lyric_obj = LyricsFromText(lyric_list)

        replacement_headers = fix_header()
        replacement_tail = fix_tail()

        replacement_lyrics = replacement_headers + lyric_obj.middle + replacement_tail

    with open(file_to_work_on, 'w', newline='') as new_file:

        lyric_writer = csv.writer(new_file)

        for row in replacement_lyrics:
            lyric_writer.writerow(row)


if __name__ == '__main__':  # test functionality with 1 file
    file_name = 'Black Sabbath - Spiral Architect.txt'
    main(file_name)
