#!/bin/python
import os

# Declare Globals
rom_directory = 'C:/Users/Dan-Desktop/Local Stuff/Roms/'
rom_ext = ".gbc"
sep = " ("

# Go through directory
for file in os.listdir(rom_directory):

    # Get the new filename
    segment = file.split(sep, 1)[0]
    new_filename = segment+rom_ext

    # Now rename the file
    os.rename(rom_directory+file, rom_directory+new_filename)
