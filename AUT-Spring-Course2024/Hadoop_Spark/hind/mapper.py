#!/usr/bin/env python
"""mapper.py - This mapper script reads text input from standard input, in the format "document_id,text".
It processes each line to extract words and emits each word along with the document ID it appeared in. 
Each word is emitted only once per document to ensure uniqueness.
"""

import sys

for line in sys.stdin:
    document_id, text = line.split(',')
    #here we will find each word of each document
    words = text.split()
    
    for word in words:
        print(f'{document_id}\t{word}')