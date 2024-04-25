import requests
from bs4 import BeautifulSoup

def extract_article_sections(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")
        # Initialize a dictionary to store sections
        sections = {}

        # Extract the title of the article
        title = soup.find("h1", class_="c-article-title").text.strip()
        sections["Title"] = title

        # Find all sections of the article
        article_sections = soup.find_all("div", class_="c-article-section")

        # Extract content from each section
        for section in article_sections:
            section_title = section.find("h2", class_="c-article-section__title").text.strip().upper()

            # Check if the section title should be excluded
            excluded_titles = [
                "ABBREVIATIONS",
                "REFERENCES",
                "ACKNOWLEDGEMENTS",
                "FUNDING",
                "AUTHOR INFORMATION",
                "ETHICS DECLARATIONS",
                "ADDITIONAL INFORMATION",
                "RIGHTS AND PERMISSIONS",
                "ABOUT THIS ARTICLE"
            ]
            if section_title.upper() not in excluded_titles:
                section_content = section.find("div", class_="c-article-section__content").text.strip()
                sections[section_title] = section_content

        return sections

    else:
        print("Failed to retrieve the webpage")
        return None
# # Define the URL
# url = "https://fbj.springeropen.com/articles/10.1186/s43093-024-00326-4"

# # Extract article sections
# article_sections = extract_article_sections(url)
# for title, content in article_sections.items():
#     print(title)
#     print(content)
#     print()