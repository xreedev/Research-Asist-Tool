import requests
from bs4 import BeautifulSoup


def fetch_paper_content(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')
            print(soup)

            # Extract the title
            title = soup.find('h1', class_='document-title').text.strip()

            # Extract the abstract
            abstract = soup.find('div', class_='abstract-text').text.strip()

            # Extract the authors
            authors = [author.text.strip() for author in soup.select('.authors-list .author')]

            # Extract the publication date
            pub_date = soup.find('span', class_='publish-date').text.strip()

            # Extract the DOI
            doi = soup.find('span', class_='epub-section__doi').text.strip()

            # Return the extracted information
            return {
                'title': title,
                'abstract': abstract,
                'authors': authors,
                'publication_date': pub_date,
                'doi': doi
            }
        else:
            print("Failed to fetch the page:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred while fetching the page:", str(e))
        return None


if __name__ == "__main__":
    # URL of the paper
    paper_url = "https://ieeexplore.ieee.org/document/9845197"

    # Fetch the paper content
    paper_content = fetch_paper_content(paper_url)
    print(paper_content)

    if paper_content:
        # Print the extracted information
        print("Title:", paper_content['title'])
        print("Authors:", ", ".join(paper_content['authors']))
        print("Publication Date:", paper_content['publication_date'])
        print("DOI:", paper_content['doi'])
        print("Abstract:", paper_content['abstract'])
    else:
        print("Failed to fetch paper content.")
