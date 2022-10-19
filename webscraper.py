import requests
import threading
from bs4 import BeautifulSoup
import os
 
# makes a directory for Math Problems
path = "Math Problems"
print(path)
 
# Create the directory
# 'Math Problems'
if not os.path.exists(path):
   os.makedirs(path)
print("Directory '% s' created" % path)

# URL provided that our program scrapes through    
URL = "https://cms.math.ca/competitions/cmo/"
 
 # Parse text obtained 
response = requests.get(URL)

# gets the raw HTML of the page  
page = requests.get(URL).text 
soup = BeautifulSoup(page, features="html.parser") 

# Base URL to which most of the PDFs in the application stem from  
BASEURL = "https://cms.math.ca/"
download_urls = []
 
# iterate through each <a> tag on the page 
# grabbing tags with 'href' links that end with pdf 
# some pdfs have 'cms.math.ca' in url while other don't 
# account for this with by generalizing all download_urls in our array through 
# an if statement 
for a in soup.find_all("a", href=True): 
   href = a["href"] 
   if href.endswith("pdf"):
       if "cms.math.ca" not in href:
           downloadLink = BASEURL + href
       else:
           downloadLink = href
       download_urls.append(downloadLink)
# for each file in download_url, take the string of text behind the last /
# name the file that string of text 
# download file to Math Problems directory 
# print which files have been scraped and successfully downloaded
for file in download_urls: 
   fileName = file.split("/")[-1] 
   fileRequest = requests.get(file) 
   with open("Math Problems//" + fileName, "wb") as f: 
       f.write(fileRequest.content) 
       f.close()
       print("File ", fileName, " downloaded")
  

