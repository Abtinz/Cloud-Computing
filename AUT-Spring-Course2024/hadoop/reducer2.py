from collections import defaultdict
import sys

current_document = None
words_counts = defaultdict(int)

def max_count(document_id, counts):
    max_word = max(counts, key=counts.get)
    max_count = counts[max_word]
    print(f"{document_id}\t{max_word}\t{max_count}")

for document in sys.stdin:
    document_id, word = document.strip().split('\t')
    
    if document_id != current_document:
        if current_document:
            max_count(document_id = current_document,counts = words_counts)
        current_document = document_id
        words_counts.clear()
    
    words_counts[word] += 1

if current_document:
    max_count(document_id = current_document,counts = words_counts)
