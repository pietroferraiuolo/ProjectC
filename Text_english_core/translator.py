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

OS = platform.system()
if OS == 'Windows':
    base_path = "G:\\Archive\\New Pokemon\\ProjectC\\Text_english_core"
elif OS == 'Linux':
    base_path = os.path.join(os.path.expanduser('~'), 
                                'git',
                                'ProjectC',
                                'Text_english_core'
                                )

def translate_file(file_name, language='it'):
    """
    Main script which allows for the easy translation of a text file.

    It reads the selected file and asks for the translation of each line. When exiting the
    translation (with either 'exit', 'quit' or 'q'), the script saves the translation in a new
    file with the same name as the original file, but with the language code appended at the end.
    The last line translated is saved in the new file, so that the translation can be resumed
    at a later time by loading it (both directly from the file list of from the original file,
    which the user will be asket to load it).

    Parameters
    ----------
    file_name : str
        The name of the file to be translated. this is chosen from the list of files in the
        `text_english_core` folder, from the `Main` script.
    language : str, optional
        The language to translate the file into (default is 'it' for Italian).
        Useful for appending the language code at the end of the file while saving it.
    """
    file = os.path.join(base_path, file_name)
    file_translation = os.path.join(base_path, f"{file_name.split('.')[0]}_{language}.txt")
    last_transl_line = 0
    if os.path.exists(file_translation):
        print(f"File `{file_translation.split('/')[-1]}` already exists. Do you want to load it? (y/n)", end=" ")
        choice = input()
        if choice == 'n':
            print("Overwriting the file.")
            os.remove(file_translation)
            with open(file, 'r') as f:
                lines = f.readlines()
        else:
            file = file_translation
            with open(file, 'r') as f:
                lines = f.readlines()
            print(f"Loaded {int((len(lines)-4)/2)} lines from `{file.split('/')[-1]}`.")
            last_transl_line = int(lines[0].split('# ')[-1].split(' ')[-1])
            print(f"Last modified line: {last_transl_line}.", end=" ")
            lines.pop(0)
    else:
        with open(file, 'r') as f:
            lines = f.readlines()
    print("Type the starting line (leave empty for the first possible line): ", end="")
    start_line = input()
    if start_line == "":
        last_true_transl_line = (last_transl_line+1)*2 if last_transl_line > 0 else 0
        start_line = 4 + last_true_transl_line
    else:
        start_line = 2*int(start_line) + 4
    for i in range(start_line, len(lines), 2):
        line = lines[i]
        n = lines.index(line)
        if n >= start_line:
            n_shown = int((n-4)/2)
            item = line.strip('\n')
            print(f"[{n_shown}] {item} -> ", end="")
            translation = input()
            if translation.lower() in ['exit', 'quit', 'q']:
                lines.insert(0, f"# Translation stopped at line {n_shown-1}\n")
                break
            if translation == "":
                translation = line
                print(translation)
            translation += '\n'
            lines[i+1] = translation
    with open(file_translation, 'w') as f:
        f.write(''.join(lines))
    print(f"Translation saved in {file_translation}")
    return

if __name__ == "__main__":
    files = sorted([f for f in os.listdir(base_path) if f.endswith('.txt')])
    print("Welcome to the Easy Translator for Pokémon Essentials text files.")
    print("To exit the translation, at any time, type 'exit'.\n")
    for i,f in enumerate(files):
        print(f"[{i:02d}] {f}")
    print("\nChoose the file you want to translate: ", end="")
    choice = int(input())
    while choice not in range(len(files)):
        print("Invalid choice. Choose a number from the list: ", end="")
        choice = int(input())
    file_name = files[choice]
    translate_file(file_name)
