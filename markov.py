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
        key = split_data[i], split_data[i+1]    #default type is tuple

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
    words = []


    first_line = random.choice(list(chains.keys()))

    first_link = random.choice(chains[first_line])
    words.extend(list(first_line))
    words.append(first_link)

    print(words)

    newkey = words[-2], words[-1]

    while 
    words.extend(list(first_line))

    # first_line = first_line + (chains.values())

    # for key, value in chains.items():
    #     if words == []:
    #         words.extend(list(key))
    #     newvalue = random.choice(value)
    #     words.append(newvalue)
    #     newkey = words[-2], words[-1]
    #     key = newkey

    # print(words)

        # newkey = (key[1], newvalue)

        # key = newkey

        # ('Would', 'you'): ['could', 'could', 'could', 'could', 'like', 'like']
        # ('you', 'could'): ['you', 'you', 'you', 'you']
        # ('could', 'you'): ['in', 'with', 'in', 'with']
        # ('you', 'in'): ['a', 'a']
        # ('in', 'a'): ['house?', 'box?']
        # ('a', 'house?'): ['Would']

        # Would you like you with a house? Would you a mouse? 
        # Would you Would you Would you them, eggs and ham? 
        # Would you Sam I am?

        # Would you could you in a house? Would you a mouse? 
        # Would you Would you Would you green eggs and ham? 
        # Would you Sam I am?


        # Would you could you could you could you in you in a in a box? 
        # a house? Would house? Would you you with a with a fox? a mouse? 
        # Would mouse? Would you a box? Would box? Would you a fox? Would 
        # fox? Would you you like them, like green eggs green eggs and eggs 
        # and ham? and ham? Would ham? Would you like them, Sam them, Sam I 
        # Sam I am?




    #pair key[1] with random list value
    #find this new pair in old list of tuple keys
    #repeat 

    # ([1]) [randlist] random.choice(chains)


    # while loop:
    # newkey to chains[key]

    # key:you | value:could | key:could | value:you | key:you | value:in 

    # key: you could you in a 

    # for key in chains:
    #     newvalue = random.choice(chains[key])
    #     newkey = (key[1], newvalue)


        

    #key: [1]    
    #value: random.choice(value)



    

    print(" ".join(words))


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
