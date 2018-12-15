#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time
from urllib.parse import urlsplit
import requests
import shutil
import time 


# In[2]:


#create path for Splinter 

executable_path = {"executable_path": "/applications/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# In[3]:


#First Web Scrape Mars News
URL = "https://mars.nasa.gov/news/"
browser.visit(URL)


# In[4]:


html = browser.html
soup = bs(html, 'html.parser')
#print(soup.prettify())


# In[5]:


article = soup.find("div", class_="list_text")

Date = article.find("div", class_="list_date").text.strip()

Paragraph = article.find("div", class_="article_teaser_body").text.strip()
Title = article.find("div", class_="content_title").text.strip()

print(Date)
print(Title)
print(Paragraph)


# In[6]:


#2nd Scraping JPL
#HTML.Browser
URL2 = "https://jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(URL2)
browser.click_link_by_id('full_image')
time.sleep(4)
#browser.click_link_by_partial_text('more info')
#time.sleep(2)
#img_url = browser.find_by_css('.main_image')[0]
html = browser.html
image_soup = bs(html, "lxml")
img_url = image_soup.find('img', class_ = 'fancybox-image')['src']
ImageURL = "https://www.jpl.nasa.gov"+ img_url
ImageURL

#AHHHHHHHHH


# In[7]:


URL3 = "https://twitter.com/marswxreport?lang=en"
browser.visit(URL3)

WeatherDate = browser.find_by_css('._timestamp')[0]
tweet_date = bs(WeatherDate.outer_html,'lxml').select('span')[0].text.strip()
tweet_date

# doesn't take into account other tweets, just grabs whatever the first one is
WeatherReport = browser.find_by_css('.tweet-text')[0]
tweet_weather = bs(WeatherReport.outer_html,'lxml').select('p')[0].text.strip()
tweet_weather


# In[8]:


URL3 = "http://space-facts.com/mars/"
#browser.visit(url3)

MarsData = pd.read_html(URL3)
MarsTable = MarsData[0]
MarsTable.columns = ['Fun Mars Fact', 'Fun Mars Value']
MarsTable


# In[9]:


#hemisphere Parsing out

URL4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url4)


# In[10]:


html = browser.html
soup = bs(html, 'html.parser')
mars_hemisphere=[]


# In[101]:


#RUn 4 loop
for i in range (4):
    time.sleep(5)
    images = browser.find_by_tag('h3')
    images[i].click()
    html = browser.html
    
    #beautiufl Soup
    soup = bs(html, 'html.parser')
    partial = soup.find("img", class_="wide-image")["src"]
    
    
    img_title = soup.find("h2",class_="title").text
    img_url = 'https://astrogeology.usgs.gov'+ partial
    
    
    dictionary={"title":img_title,"img_url":img_url}
    mars_hemisphere.append(dictionary)
    browser.back()


# In[102]:


print (mars_hemisphere)

