import string
import random

string_length = 25
string_num_chars = 5
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def generate_string():
    string_out = ''
    sub_alphabet = alphabet[:string_num_chars] # Compute once instead of string_length number of times?

    for i in range(string_length):
        string_out += random.choice(sub_alphabet)

    print(string_out)


if __name__ == '__main__':
    generate_string()
    generate_string() # Allows to generate 2 at a time for convenience
