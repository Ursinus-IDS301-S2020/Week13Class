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
    def __init__(self):
        self.counts = {} # A dictionary
        # that holds all of the counts
        # for each state
    
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
        for i in range(len(text)):
            state = text[i]
            next_state = text[(i+1)%len(text)]
            if not state in self.counts:
                self.counts[state] = {}
            if next_state in self.counts[state]:
                self.counts[state][next_state] += 1
            else:
                self.counts[state][next_state] = 1
    
    def load_file_sentences(self, filename):
        """
        Incorporate each line in a file separately
        """
        fin = open(filename, "r")
        for line in fin.readlines():
            line = line.rstrip()
            self.add_text(line)
        fin.close()
    
    def make_random_text(self, state, N):
        """
        Sample from the counts
        """
        for i in range(N):
            print(state, end='')
            state = pick_random_element(self.counts[state])

m = Markov()
m.load_file_sentences('sithquotes.txt')
#m.add_text("Hello everyone! I'm excited about your presentations")
m.make_random_text('e', 500)