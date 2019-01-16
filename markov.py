"""Generate Markov text from text files."""
import random


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    the_data = open(file_path, 'r')

    return the_data.read()


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
    """

    split_data = open_and_read_file(input_path).split()

    chains = {}

    # iterate over the split_data list of words
    # each iteration, we take word1 and word2, which will be a tuple that is
    # a dictionary key
    # the value will be word3
    # 1st iteration:
    #   ('Would', 'you') : ['could']
    #   ('you', 'could') : ['you']


    for i in range(0, len(split_data) - 1):
        key = split_data[i], split_data[i+1]

        #if key exists, add to existing value
        # value = chains.get(key, []).append(split_data[i+2])
        # chains[key] = value
        if i == (len(split_data) - 2):
            break
        if key in chains:   #checks for duplicates
            value = chains.get(key)
            value.append(split_data[i+2])
        else:
            value = []
            value.append(split_data[i+2])
            chains[key] = value
    
    # for key, value in chains.items():
    #     print(f'{key}: {value}')

# Would you could you in a house?
# Would you could you with a mouse?
# Would you could you in a box?
# Would you could you with a fox?
# Would you like green eggs and ham?
# Would you like them, Sam I am?

    return chains


def make_text(chains):
    """Return text from chains."""
    words = [ ]
    #('Would', 'you'): ['could', 'could', 'could', 'could', 'like', 'like']
    # ('you', 'could'): ['you', 'you', 'you', 'you']

    # ([1]) [randlist] random.choice(chains)

    for key, value in chains.items():
        newvalue = random.choice(value)
        newkey = (key[1], newvalue)
        words.append(newvalue)
        key = newkey
        # print(newkey)


    

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
