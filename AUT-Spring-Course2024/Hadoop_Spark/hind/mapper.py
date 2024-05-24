#!/usr/bin/env python
"""mapper.py - This mapper script reads text input from standard input, in the format "document_id,text".
It processes each line to extract words and emits each word along with the document ID it appeared in. 
Each word is emitted only once per document to ensure uniqueness.
"""

import sys

for document in sys.stdin:
    document_id, line = document.strip().split(',')
    
    #here we will find each word of each document
    text = line.split()
  
    for word in text:
        print(f"{word}\t{document_id}")