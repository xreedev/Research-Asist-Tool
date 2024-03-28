
import main
import math

test="""Test new.Test Old"""
def calcidf(line):
    idf=0
    line_words=line.split()
    all_sentences=test.split(".")
    print(all_sentences)
    for wrd in line_words:
        for sentence in all_sentences:
            if wrd in sentence:
                idf+=1
    print(len(all_sentences),idf)
    return len(all_sentences)/idf

print(calcidf("Test"))
