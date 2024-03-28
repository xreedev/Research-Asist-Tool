def tfidfVector(ieee_paper_data,classified_data,all_lines):
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
    def calctfidf(line, word):
        tf = 0
        line_words = line.split()
        for wrd in line_words:
            if wrd == word:
                tf += 1
        idf = 0

        for sentence in all_lines:
            if word in sentence:
                idf += 1
        net_idf = len(all_lines) // (idf + 1)  # Adding 1 to idf to avoid division by zero
        total = (tf * net_idf) / 100
        return round(total, 3)

    lines_list = []

    # Loop through each data
    for value in classified_data.values():
        sec_lines = value.split(".")  # Split data into sentences
        # Loop through each line in the data
        for lines in sec_lines:
            words = lines.split()  # Split line into words
            total_tfidf = 0
            # Calculate total TF-IDF for the line
            for word in words:
                total_tfidf += calctfidf(lines, word)
            # Create a new line object for each line
            line_obj = Line(lines)
            line_obj.settfidf(total_tfidf)
            # Add the line object to the list
            lines_list.append(line_obj)

    # Create filtered_data dictionary to store filtered lines
    filtered_data = {}

    # Loop through each section in classified_data
    for section, value in classified_data.items():
        filtered_lines = []
        # Loop through each line in lines_list
        for line_obj in lines_list:
            if line_obj.getline() in value:
                total_tfidf = line_obj.gettfidf()  # Total TF-IDF for the line
                if total_tfidf >= 1.5:
                    filtered_lines.append(line_obj.getline())
        # Update filtered_data with the filtered lines for the section
        filtered_data[section] = ".".join(filtered_lines)
    return filtered_data
