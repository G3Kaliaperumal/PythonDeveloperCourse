# pip install translate --user
# Available documentation: https://en.wikipedia.org/wiki/ISO_639-1
from translate import Translator
import pdb

language = 'ta'  # Tamil


def translate_line(line):
    translator = Translator(to_lang=language)
    translation = translator.translate(line)
    return translation


try:
    with open('files\\test1.txt', mode='r') as input_file, open('files\\translated_test.txt', mode='w', encoding='utf_32') as output_file:
        line = input_file.readline()
        while(line):
            output_file.write(translate_line(line))
            line = input_file.readline()
except (FileNotFoundError, FileExistsError):
    print('Invalid file paths')
