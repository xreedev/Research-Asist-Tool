import data

#the input to this module is a dictionary and output is all the extractive summaries of values in dictionary
stop_words=data.stop_words
def removeStopWords(line, stop_words):
    clean_line = ""
    words = line.split()
    for word in words:
        if word not in stop_words:
            clean_line += word + " "  # Add a space between words
    return clean_line.strip()  # Remove trailing space and return

class Line:
    def __init__(self, line):
        self.line = line  # The actual line text
        self.tfidf = 0

    # Set the TF-IDF value
    def settfidf(self, ti):
        self.tfidf = ti

    # Get the TF-IDF value
    def gettfidf(self):
        return self.tfidf

    # Get the line text
    def getline(self):
        return self.line

# Function to calculate Term Frequency
def calctfidf(line, word, all_lines):
    tf = line.split().count(word)
    idf = sum(1 for sentence in all_lines if word in sentence)
    net_idf = len(all_lines) / (idf + 1)  # Adding 1 to idf to avoid division by zero
    total = (tf * net_idf) / 100
    return round(total, 3)

def tfidfVectorise(clean_data, stop_words,benchmark):
    lines_list = []

    for value in clean_data.values():
        all_lines=value.split(".")
        sec_lines = value.split(".")  # Split data into sentences
        for lines in sec_lines:
            total_tfidf = 0
            newline = removeStopWords(lines, stop_words)
            for word in newline.split():
                total_tfidf += calctfidf(lines, word, all_lines)
            line_obj = Line(lines)
            line_obj.settfidf(total_tfidf)
            lines_list.append(line_obj)

    filtered_data = {}

    for section, value in clean_data.items():
        filtered_lines = []
        for line_obj in lines_list:
            if line_obj.getline() in value:
                total_tfidf = line_obj.gettfidf()
                if total_tfidf >= benchmark:
                    filtered_lines.append(line_obj.getline())
        filtered_data[section] = ".".join(filtered_lines)

    return filtered_data
