"""
translator.py

Author
------
Pietro Ferraiuolo
@ pietro.ferraiuolo@inaf.it

Description
-----------
This script allows for a fast and easy translation of a text file from
Pokémon Essentials, in particular the files whithin the `text_english_core`
folder.
"""

import os
import platform 
from googletrans import Translator

t = Translator()
OS = platform.system()
if OS == 'Windows':
    base_path = os.path.join(os.path.expanduser('~'),
                                'Documents',
                                'GitHub',
                                'ProjectC',
                                'Text_english_core'
                                )
elif OS == 'Linux':
    base_path = os.path.join(os.path.expanduser('~'), 
                                'git',
                                'ProjectC',
                                'Text_english_core'
                                )
# TODO
# Strip every line of the \n upon reading, so that the translation is not affected by it
# Join the correct translation to the line in the file

def translate_file(file_name):
    file = os.path.join(base_path, file_name)
    file_translation = os.path.join(base_path, f"{file_name.split('.')[0]}_it.txt")
    with open(file, 'r') as f:
        lines = f.readlines()
    print("Type the line number from which you want to start the translation (empty for first line)", end="")
    start_line = input()
    if start_line == "":
        start_line = 4
    else:
        start_line = int(start_line)
    for i in range(start_line, len(lines), 2):
        line = lines[i]
        n = lines.index(line)
        if n >= start_line:
            item = line.strip('\n')
            print(f"[{n-4}] {item} -> ", end="")
            tranlsation = input()
            if tranlsation == 'exit':
                break
            if tranlsation == "":
                tranlsation = t.translate(line, src='en', dest='it').text
                print(tranlsation)
    with open(file_translation, 'w') as f:
        f.write('\n'.join(lines))
    print(f"Translation saved in {file_translation}")
    return

if __name__ == "__main__":
    files = [f for f in os.listdir(base_path) if f.endswith('.txt')]
    print("Welcome to the Easy Translator for Pokémon Essentials text files.")
    print("To exit the translation, at any time, type 'exit'.\n")
    for i,f in enumerate(files):
        print(f"[{i:2d}] {f}")
    print("\nChoose the file you want to translate: ")
    choice = int(input())
    while choice not in range(len(files)):
        print("Invalid choice. Choose a number from the list.")
        choice = int(input())
    file_name = files[choice]
    translate_file(file_name)