"""Count words in file."""

import sys

def tokenize(filename):
    data = open(filename)
    all_lines = []
    alpha_words = []
    non_dupe_words = []

    for line in data:
        line_lst = line.strip().split(' ')
        for item in line_lst:
             all_lines.append(item)
             
    for word in all_lines:
        if word.isalpha() == True:
             alpha_words.append(word)
        if word.isalpha() == False:
            try:
                c = word.replace(word[-1], "")
                alpha_words.append(c)
            except:
                continue
            
    for word in alpha_words:
        c = word.lower()

        if c not in non_dupe_words:
            non_dupe_words.append(c)

              
        
    print(non_dupe_words)
                       
        
    return non_dupe_words


def count_words(words):
    word_count = {}

    for word in words:
            word_count[word] = word_count.get(word, 0) + 1
            
    return word_count 


def print_word_counts(word_counts):
    for word, count in word_counts.items():
        print(word, count)


words = tokenize(sys.argv[1])
word_counts = count_words(words)
print_word_counts(word_counts)