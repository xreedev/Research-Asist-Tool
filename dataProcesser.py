import re
new_data=[]
all_words=[]
all_lines=[]


def processData(ieee_paper_data):
    global new_data
    global all_lines
    global all_words
    new_data=re.split(r"\b\d+\.\s*(?:Introduction|Related Work|Methodology|Results|Discussion|Conclusion)",ieee_paper_data)[1:]
    all_words=ieee_paper_data.split()
    all_lines=ieee_paper_data.split(".")

def getClassifiedData(ieee_paper_data):
    processData(ieee_paper_data)
    return new_data

def getAllWords(ieee_paper_data):
    processData(ieee_paper_data)
    return all_words

def getAllLines(ieee_paper_data):
    processData(ieee_paper_data)
    return all_lines



sections = "\n0.Introduction\n1.Related Work\n2.Methodology\n3.Discussion\n4.Conclusion"
#done