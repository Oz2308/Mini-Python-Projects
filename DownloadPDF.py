import requests
from bs4 import BeautifulSoup
import os
import time

# Paste the link of the site that has the links to the PDFs in URL
URL = ""
headers = headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Accept': 'application/pdf'
}

# Gets the content of the site i.e. the html code
site = requests.get(URL, headers=headers)
siteSRC = site.content

# Creates Soup Object & parses it using lxml
soup = BeautifulSoup(siteSRC, 'lxml')

# Find class that each article uses. Finds all a tags in the site
links = soup.find_all("a")

# Gets all html links in the site and only saves the PDF links to the list below
all_pdfs = []
for link in links:
    href = link.get("href")
    if href.endswith(".pdf"):
        all_pdfs.append(href)

# Creates folder in the C drive if folder doesn't exist
pdf_dir = os.path.join("C:/", "pdf_folder")
if not os.path.exists(pdf_dir):
    os.makedirs(pdf_dir)

# For each PDF link in the list above, the PDF will be downloaded to the folder
for pdf in all_pdfs:
    response = requests.get(pdf, headers=headers)
    # print(response.status_code)
    file_path = os.path.join(pdf_dir, pdf.split("/")[-1])
    with open(file_path, "wb") as f:
        f.write(response.content)
        time.sleep(60)
        
