from bs4 import BeautifulSoup
import requests
import logging
import os

logger = logging.getLogger(__name__)

def crawl(alph):
    for letter in alph:
        logger.info(f"processing letter {letter}...")
        url = "http://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_" + letter + ".html"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        dictionary = soup.find_all('p')
        for entries in dictionary:
            word = entries.find('b').getText()
            pos = entries.find('i').getText()
            cut = len(word) + len(pos) + 4
            definition = entries.getText()[cut:]
            yield word, pos, definition

def write_to_csv(output_file, data):
    output_file.write(";".join(data) + "\n")

if __name__ == '__main__':
    alph = "abcdefghijklmnopqrstuvwxyz"
    if os.environ.get('DEV'):
        alph = "x"

    # Create three output files based on letter ranges
    file_ranges = {'first': 'abcdefghi', 'second': 'jklmnopq', 'third': 'rstuvwxyz'}
    output_files = {key: open(f"{key}_output.csv", 'w', encoding='utf-8') for key in file_ranges}
    
    # Write headers to each output file
    for file in output_files.values():
        write_to_csv(file, ["word", "pos", "definition"])

    try:
        for word, pos, definition in crawl(alph):
            first_letter = word[0].lower() if word else 'other'
            for key, value in file_ranges.items():
                if first_letter in value:
                    write_to_csv(output_files[key], [word, pos, definition])
                    break
    finally:
        # Close all output files
        for file in output_files.values():
            file.close()