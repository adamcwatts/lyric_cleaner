# Python script for parsing and cleaning lyric files downloaded from Foobar Music player using the Lyric Show 3 addon

Lyrics automatically downloaded often have advertisements at the bottom of the .txt lyrics such as:

"External links
Nominate as Song of the Day
iTunes: buy Demon Amazon: search for…"

Clean_lyric_driver.py is currently set up using local path for where my lyrics are automatically downloaded, e.g., 'C:\Users\adamc\foobar_lyrics'
Currently only works for text files .txt and not .lyrc files that are synced with time

txt.lyrics.py can be run locally using the test case lyrics included in the folder or imported as a module for the main driver to run at a specific location

reset_file_names.py is a script for resetting the test case lyrics back to their original form. Makes testing much easier.