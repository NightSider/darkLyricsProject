import darklyrics
import glob
import os


# TODO
# read txt's in bands
# safe all bandnames locally
# get lyrics for each band (darklyrics.get_all_lyrics('bandname')
# save lyrics in a txt file
# analyze the txt file with counter for each word

if not os.path.isfile('all_bands.txt'):
    data = glob.glob('./bands/metal_dataset/*.txt')
    common_data_file = open('all_bands.txt', 'w')

    for path in data:
        file_handler = open(path, "r")
        for line in file_handler:
            common_data_file.write(line)
        file_handler.close()
    common_data_file.close()

band_file = file_handler = open('all_bands.txt', "r")
lyrics_file = open('all_lyrics.txt', 'w')
for line in band_file:
    try:
        lyrics_file.write(darklyrics.get_all_lyrics(line))
        print('\nFOUND!\n')
    except darklyrics.LyricsNotFound:
        print('No lyrics found')
band_file.close()
lyrics_file.close()



