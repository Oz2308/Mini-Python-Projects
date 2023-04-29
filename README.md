# PyCode
*Collection of my Python Code that I wrote.*

## DUSscraperPRD.py 
- The first piece of code is a webscraper that was written in order to scrape articles & their respective links from the DaarusSunnah website.
- The code utilises the BeautifulSoup & Requests library to scrape the data from site from each page where an article is available. 
- The OpenPyXL library is used to output the data scraped to an Excel spreadsheet of 2 coloumns labelled Articles & Links respectively.

## YouTubeAPI Git.py
**_Before you utilise this script you must sign in to the Google Developer Console and get an API key for the YouTube Data API_**
- This code was written so that all videos titles and their links are obtained from any YouTube channel and outputted to a spreadsheet.
- The YouTube Data API v3 was utilised in order to query YouTube channels' all uploads playlist
- Once the data is retrievd, the video titles & links are then outputted to an Excel spreadsheet using the OpenPyXL library to produce two coloumns of data.

## DownloadPDF.py
- When a URL is pasted into this code it will download all PDFS on the URL in 65 second intervals and store them locally on a new folder
- This code mainly uses the BeautifulSoup & Requests libraries