# CresicorWebscraper

## Project Description 
Cresicor operates in an old fashioned industry that does not have any modern data sharing processes, APIs, etc. As a result, our users download a lot of data from various sources manually, a very tedious and error-prone process. We are building tools that can automate this data pulling process. This problem concentrates on building a web scraper in Python that can automate the process of pulling data in a couple of toy examples. 

Write a webscraper application in Python that downloads all PDF files from this [webpage](https://cms.math.ca/competitions/cmo/) into a folder called “Math Problems.” 

### How to Run 
To run the code, be sure to pull all files from this repository into the workplace that you want to run the code in. For me, I use Visual Studio Code. After choosing which directory I want to pull this project in using the terminal command **cd**, I then typed **git pull https://github.com/nchen55555/CresicorWebscraper.git** where the URL utilized here can be accessed under the green Code button in the repository. From there, you should have access to the **webscraper.py** code. To run the code, type in the terminal **python3 -m webscraper**. The program will then run the code, creating a new directory "Math Problems" within the directory that you've pulled the code into. You will then be able to access all the downloaded files from this [webpage](https://cms.math.ca/competitions/cmo/).
