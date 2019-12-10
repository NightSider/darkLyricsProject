from typing import TextIO

import darklyrics
import glob
import os
import time


# TODO
# - read txt's in bands
# - safe all bandnames locally
# working on: get lyrics for each band (darklyrics.get_all_lyrics('bandname')
# save lyrics in a txt file
# analyze the txt file with counter for each word

script_dir = os.path.split(os.path.abspath(__file__))[0]


def get_lyrics(band):
    print(darklyrics.get_all_lyrics(band))
    return darklyrics.get_all_lyrics(band)


def write_all_bands_to_file():
    if not os.path.isfile('all_bands.txt'):
        data = glob.glob('./bands/*.txt')
        with open('all_bands.txt', 'w', encoding='utf-8') as common_data_file:
            for path in data:
                path = os.path.join(script_dir, path)
                print(path)
                with open(path, "r", encoding='utf-8') as file_handler:
                    for line in file_handler:
                        common_data_file.write(line)
                    file_handler.close()
            common_data_file.close()


def write_all_lyrics_to_file():
    with open('all_bands.txt', "r", encoding='utf-8') as band_file:
        with open('all_lyrics.txt', 'w', encoding='utf-8') as lyrics_file:
            for line in band_file:
                try:
                    lyrics_file.write(get_lyrics(line))
                    print('\nFOUND!\n')
                    #time.sleep(1)
                except darklyrics.LyricsNotFound:
                    print('No lyrics found')
                    #time.sleep(1)
            band_file.close()
            lyrics_file.close()


print(darklyrics.get_all_lyrics('aborted'))
write_all_bands_to_file()
write_all_lyrics_to_file()

