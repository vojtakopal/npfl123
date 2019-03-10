import numpy as np

def entropy(vocabulary):
    vals = np.array(list(vocabulary.values()))
    return -np.sum(vals * np.log(vals))
