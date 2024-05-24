#!/usr/bin/env python
"""reducer.py - Processes key-value pairs received from the mapper, where each key is a word 
and each value is a document ID where the word appeared. This script aggregates the document IDs 
for each word and outputs the word alongside the set of unique document IDs where the word was found.
The reducer reads lines of input from standard input, where each line has a format of 'word,document_id'.
The input lines are expected to be sorted by the word. The reducer uses this sorted order to efficiently
aggregate document IDs by using a set data structure, transitioning between different words as it processes
the input lines one-by-one.
"""

#we will use defaultdict for saving key values in reduce phase
from collections import defaultdict
import sys

inverted_index = defaultdict(set)

for line in sys.stdin:
    value, document_id = line.strip().split('\t')
    inverted_index[value].add(document_id)

#now lets map words and their keys
for word, document_id_sets in inverted_index.items():
    print(f"{word}\t{', '.join(document_id_sets)}")
