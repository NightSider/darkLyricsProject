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
                    albums = darklyrics.get_albums(line)
                    print(albums)
                    time.sleep(1)
                    for album in albums:
                        songs = darklyrics.get_songs(line, album)
                        print(songs)
                        time.sleep(1)
                        for song in songs:
                            lyrics_file.write(darklyrics.get_lyrics(song, line))
                            time.sleep(1)
                    print('\nFOUND!\n')
                    # time.sleep(1)
                except darklyrics.LyricsNotFound:
                    print('No lyrics found for ' + line)
                    # time.sleep(1)
                time.sleep(1)
            band_file.close()
            lyrics_file.close()


#write_all_bands_to_file()
#write_all_lyrics_to_file()
try:
    print(darklyrics.get_lyrics('The Ancient Covenant', 'The Faceless'))
    print(darklyrics.get_lyrics('The Ancient Covenant'))
    print(darklyrics.get_songs('The Faceless'))
    print(darklyrics.get_albums('The Faceless'))
    print(darklyrics.get_all_lyrics('The Faceless'))
except darklyrics.LyricsNotFound:
    print('No lyrics found')
