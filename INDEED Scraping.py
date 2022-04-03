#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pandas as pd
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from IPython.core.display import display,HTML
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#wait = WebDriverWait (driver,10)
import time 
import string 
import os

driver = webdriver.Chrome("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")
driver.maximize_window()
print('Ok')


# In[7]:




def extract_page(page):
    url = 'https://in.indeed.com/jobs?q=education&l=Delhi%2C%20Delhi&vjk=85bbb52d09fedc87'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

def extract_content(soup):
    job_elements = soup.find_all("a", class_="tapItem")
    for job_element in job_elements:
        title = job_element.find("h2", class_="jobTitle")
        if (len(title.findChildren()) > 1):
            title = title.find_next("span").find_next("span").text
        else: 
            title = title.text
        company = job_element.find("span", class_="companyName")
        location = job_element.find("div", class_="companyLocation")
        description = job_element.find("div", class_="job-snippet")
        salary = job_element.find("div", class_="salary-snippet")
        if salary:
            salary = salary.text.strip()
        else:
            salary = '' 
        post_date = job_element.find('span', 'date').text
        today = datetime.today().strftime('%Y-%m-%d')
        record = (title, company.text, location.text, post_date, today, salary, description.text.strip().replace('\n', ' '))
        records.append(record)
    return 

records = []
for i in range(0, 60, 10):
    print(f'Scraping job details from page {round(i/10+1)}')
    page = extract_page(0)
    extract_content(page)
    
print("Process finished! Create a dataframe to store the results")

df = pd.DataFrame(records)
df.columns = ['JobTitle', 'Company', 'Location', 'DatePosted', 'DateExtracted', 'Salary', 'Description']
print(df.head())
df.to_csv("results.csv")


# In[6]:


df


# In[8]:


df.max()


# In[11]:


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df


# In[ ]:




