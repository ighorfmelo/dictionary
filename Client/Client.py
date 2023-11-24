import socket
import TrieTransform

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 7777))
print('Connected!\n')

def get_output_file(letter):
    file_ranges = {'first': 'abcdefghi', 'second': 'jklmnopq', 'third': 'rstuvwxyz'}
    for key, value in file_ranges.items():
        if letter.lower() in value:
            return f"{key}_output.csv"
    return "unknown_output.csv"

word = str(input('Palavra>'))

letter = word[0].lower()
fileName = get_output_file(letter)


client.send(fileName.encode())

with open(fileName, 'wb') as file:
    while 1:
        data = client.recv(1000000000)
        if not data:
            break
        file.write(data)

print('Received!\n')

trie = TrieTransform.build_trie_from_file(fileName)

definition = trie.search(word)
if definition:
    print(f'A definição da palavra "{word}" é: {definition}')
else:
    print(f'A palavra "{word}" não está na trie.')

