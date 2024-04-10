import re


def removeStopWords(data, stop_words):
    clean_data = ""
    all_words = data.split()
    for word in all_words:
        if word.lower() not in stop_words:
            clean_data += word
            clean_data += " "
    return clean_data


def getAllWords(ieee_paper_data):
    all_words = ieee_paper_data.split()
    return all_words


def getAllLines(paper_text):
    new_string = ""
    for values in paper_text.values():
        new_string += values
        all_lines = new_string.split(".")
    return all_lines


sections = "\n0.Introduction\n1.Related Work\n2.Methodology\n3.Discussion\n4.Conclusion"


def classify(ieee_paper_data):
    classified_data = re.split(r"\b\d+\.\s*(?:Introduction|Related Work|Methodology|Results|Discussion|Conclusion)",
                               ieee_paper_data)[1:]
    classified_dataset = {"Introduction": classified_data[0], "Related Work": classified_data[1],
                          "Methodology": classified_data[2], "Results": classified_data[3],
                          "Discussion": classified_data[4], "Conclusion": classified_data[5]}

    return classified_dataset


def cleanData(ieee_paper_data, stop_words):
    clean_data = re.split(r"\b\d+\.\s*(?:Introduction|Related Work|Methodology|Results|Discussion|Conclusion)",
                          removeStopWords(ieee_paper_data, stop_words))[1:]
    clean_dataset = {"Introduction": clean_data[0], "Related Work": clean_data[1], "Methodology": clean_data[2],
                     "Discussion": clean_data[3], "Conclusion": clean_data[4]}
    return clean_dataset
