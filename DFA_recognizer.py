import re

class DFA:
    def __init__(self, states, alphabet, transitions, initial_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.accept_states = accept_states

    def is_accepting(self, input_string):
        current_state = self.initial_state

        for char in input_string:
            if char not in self.alphabet:
                return False

            current_state = self.transitions[current_state].get(char)
            if current_state is None:
                return False

        return current_state in self.accept_states

# This function takes the file path and a DFA instance as parameters
def highlight_text(file_path, dfa):
    with open(file_path, 'r') as file:
        text = file.read()

    words = re.findall(r'\b\w+\b', text)
    highlighted_text = text

    for word in words:
        if dfa.is_accepting(word.lower()):
            highlighted_text = re.sub(r'\b{}\b'.format(word), '\033[92m{}\033[0m'.format(word), highlighted_text)

    print(highlighted_text)

# Input text file
file_path = 'SampleText1.txt'

states = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
          15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29}
alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
transitions = {
        0: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'h': 5, 'i': 6, 'm': 7, 't': 8, 'w':9},
    # a, am, an, are
        1: {'m': 11, 'n': 12, 'r': 13},
        11: {},
        12: {},
        13: {'e': 14},
        14: {},
    # be
        2: {'e': 15},
        15: {},
    # can
        3: {'a': 16},
        16: {'n': 17},
        17: {},
    # do, did
        4: {'o': 18, 'i': 19},
        18: {},
        19: {'d': 20},
        20: {},
    # had, has
        5: {'a': 21},
        21: {'d': 22, 's': 23},
        22: {},
        23: {},
    # is
        6: {'s': 24},
        24: {},
    # may
        7: {'a': 25},
        25: {'y': 26},
        26: {},
    #the
        8: {'h': 27},
        27: {'e': 28},
        28: {},
    #was
        9: {'a': 29},
        29: {'s': 10},
        10: {}
}
initial_state = 0
accept_states = {1, 10, 11, 12, 14, 15, 17, 18, 20, 22, 23, 24, 26, 28}

dfa = DFA(states, alphabet, transitions, initial_state, accept_states)

highlight_text(file_path, dfa)
