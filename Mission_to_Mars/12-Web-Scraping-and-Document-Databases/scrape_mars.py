# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
#import pymongo
#from flask import Flask, render_template, redirect
#from flask_pymongo import PyMongo


# In[3]:
#from splinter import Browser
#from bs4 import BeautifulSoup


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
   

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[4]:


    # Visit Nasa news url through splinter module
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)


    # In[5]:


    # HTML Object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')


    # In[6]:


    # Retrieve the latest news title and paragraph
    news_title = soup.find_all('div', class_='content_title')[0].text
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text

    # Display scrapped data 
    print(news_title)
    print("--------------------------------------------------------------------")
    print(news_p)


    # ## JPL Mars Space Images - Featured Image

    # In[7]:


    # Mars Image to be scraped
    jpl_nasa_url = 'https://www.jpl.nasa.gov'
    images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'


    # In[8]:


    browser.visit(images_url)
    html = browser.html


    # In[9]:


    images_soup = bs(html, 'html.parser')


    # In[10]:


    # Retrieve featured image link
    relative_image_path = images_soup.find_all('img')[3]["src"]
    featured_image_url = jpl_nasa_url + relative_image_path
    print(featured_image_url)


    # ## Mars Facts

    # In[11]:


    url = "https://space-facts.com/mars/"
    browser.visit(url)


    # In[12]:


    # Use Pandas to "read_html" to parse the URL
    tables = pd.read_html(url)


    # In[13]:


    #Find Mars Facts DataFrame in the lists of DataFrames
    #df = tables[0]


    # In[14]:


    #Assign the columns
    #df.columns = ['Mar_Earth_Comparision', 'Mars', 'Earth']
    #html_table = df.to_html(table_id="html_tbl_css",justify='left',index=False)
    #data = df.to_dict(orient='records')  # Here's our added param..
    #df


    # In[15]:


    #Find Mars Facts DataFrame in the lists of DataFrames
    df_1 = tables[0]


    # In[16]:


    #Assign the columns
    df_1.columns = ['Attributes', 'Values']
    html_table = df_1.to_html(table_id="html_tbl_css",justify='left',index=False)
    #data = df_1.to_dict(orient='records')  # Here's our added param..
    #df_1


    # In[17]:


    # Use Pandas to convert the data to a HTML table string
    #table_one = df.to_html()


    # In[18]:


    # Use Pandas to convert the data to a HTML table string
    #table_two = df_1.to_html()


    # In[19]:


    # printing table_one 
    #print(table_one)


    # In[20]:


    # printing table_one 
    #print(table_two)


    # ## Mars Hemisphere

    # In[21]:


    #Visit the Mars Hemispheres url through splinter module
    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)


    # In[22]:


    #Parse with 'html.parser';creation with beautifulsoup object
    html_hemispheres = browser.html
    soup = bs(html_hemispheres, 'html.parser')


    # In[24]:


    #Create an empty list of links for the hemispheres
    hemisphere_image_urls=[]
    products=soup.find ('div', class_='result-list')
    hemispheres=products.find_all('div',{'class':'item'})

    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + end_link    
        browser.visit(image_link)
        html_hemispheres = browser.html
        soup = bs(html_hemispheres, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        hemisphere_image_urls.append({"title": title, "img_url": image_url})


    # In[25]:


    #Display hemisphere image urls
    hemisphere_image_urls


    # In[26]:


    mars_dict = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "fact_table": html_table,
        #"comparison_table": table_one,
        "hemisphere_images": hemisphere_image_urls
    }


    # In[27]:


    return mars_dict


# In


