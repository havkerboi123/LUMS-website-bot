
from langchain_community.document_loaders import WebBaseLoader
import os

# Function to read links from a text file
def read_links(file_path):
    with open(file_path, 'r') as file:
        links = file.readlines()
    # Strip newline characters from each link
    links = [link.strip() for link in links]
    return links

file_path = 'lums/pk_links.txt'
links = read_links(file_path)

def get_text_from_site(url):
    # Setting a custom user agent
    os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    loader = WebBaseLoader(url)
    
    documents = loader.load()
    return documents

website_content = []
for link in links:
    website_content.append(get_text_from_site(link))
    print("scrapped : " , link)  
    

with open('lums/website_content.txt', 'w') as output_file:
    for content in website_content:
        for d in content:
            output_file.write(d.page_content)  # Access the text content of the Document object
            output_file.write("\n")  # Add a newline for better readability
