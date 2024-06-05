import sys

#we will load inputs in STDIN from input.txt v2
for document in sys.stdin:
    doc_id, line = document.split(',')
    words = line.split()
    
    for word in words:
        print(f'{doc_id}\t{word}')