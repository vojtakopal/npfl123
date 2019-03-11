#!/usr/bin/env python
import argparse
from entropy import entropy

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--dataset", required=True, type=str, help="Parsed dataset.")
args = parser.parse_args()

vocabulary = {}
total = 0
with open(args.dataset, "r") as data:
    for line in data:
        line = line.rstrip("\n")
        words = line.lower().split(" ")
        for word in words:
            if vocabulary.get(word) == None:
                vocabulary[word] = 0
            
            vocabulary[word] += 1
            total += 1

for word in vocabulary:
    vocabulary[word] /= total

print(entropy(vocabulary))
        