import numpy as np

def pick_random_element(count):
    """
    Parameters
    ----------
    count: {string: int}
        A dictionary of all transition
        counts from some state
        we're in to all other states
    Returns
    -------
    The next character, randomly sampled
    from the empirical probabilities
    determined from the counts
    """
    keys = list(count.keys())
    counts = np.array(list(count.values()))
    counts = np.cumsum(counts)
    r = np.random.rand()*counts[-1]
    idx = np.searchsorted(counts, r)
    return keys[idx]

class Markov(object):
    def __init__(self, k):
        """
        Parameters
        ----------
        k: int >= 1
            Specifies the length of the grams
        """
        self.counts = {} # A dictionary
        # that holds all of the counts
        # for each state
        self.k = k
    
    def add_text(self, text):
        """
        Update the counts based on a new
        piece of text.  Loop through every character
        and count what the next character is
        Parameters
        ----------
        text: string
            The text
        """
        text2 = text + text
        for i in range(len(text)):
            state = text2[i:i+self.k]
            next_char = text2[i+self.k]
            if not state in self.counts:
                self.counts[state] = {}
            if next_char in self.counts[state]:
                self.counts[state][next_char] += 1
            else:
                self.counts[state][next_char] = 1
    
    def load_file_sentences(self, filename):
        """
        Incorporate each line in a file separately
        """
        fin = open(filename, "r")
        for line in fin.readlines():
            line = line.rstrip()
            line = line.lower()
            self.add_text(line)
        fin.close()
    
    def make_random_text(self, N, state = None):
        """
        Sample from the counts
        """
        if not state:
            keys = list(self.counts.keys())
            idx = np.random.randint(len(keys))
            state = keys[idx]
        print(state, end='')
        for i in range(N):
            next_char = pick_random_element(self.counts[state])
            print(next_char, end='')
            state = state[1::] + next_char

start = "ancien"
m = Markov(len(start))
m.load_file_sentences("sithquotes.txt")
m.load_file_sentences("ursinustweets.txt")
#m.add_text("Hello everyone! I'm excited about your presentations")
m.make_random_text(250, start)