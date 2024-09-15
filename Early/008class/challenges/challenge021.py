# Challenge 021
# Make a script that opens and plays a .mp3 audio file.

import pygame as py

py.mixer.init()

py.mixer.music.load('zelda.mp3')

py.mixer.music.play()

print('Enjoy your music... remember the good times you had playing The Legend of Zelda: Wind Waker...')

while py.mixer.music.get_busy():
    py.time.Clock().tick(10)

