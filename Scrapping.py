
# coding: utf-8

# In[4]:


#Buiding a Amazon web scrapper using selenium and Beautiful Soap


#importing libraries
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup


# In[36]:


# to initialize incognito mode setting up option
option = webdriver.ChromeOptions()
option.add_argument('— incognito')


# In[37]:


# to locate the chrome driver from the drive
browser = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=option)


# In[38]:


# link to open
browser.get('https://www.amazon.in/s?k=one+pluse7pro&crid=1FY954HRPXM2A&sprefix=one+pl%2Caps%2C327&ref=nb_sb_ss_i_1_6')


# In[42]:


source = browser.page_source


# In[46]:


soup = BeautifulSoup(source,'html.parser')


# In[57]:


#further list of links using classs name
links = []
for anchor_tag in soup.find_all('div',attrs={'class':'s-result-list s-search-results sg-row'}):
    for link in anchor_tag.find_all('data-asin'):
        print(link)
    


# In[65]:


hyperLinks =[]
for links in soup.find_all('div',attrs ={'class':'sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28'}):
    for link in links.find_all('a'):
        hyperLinks.append(link['href'])


# In[66]:


base_url = 'https://www.amazon.in'


# In[68]:


complete_url = []
for link in hyperLinks:
    complete_url.append(base_url+link)


# In[95]:


Title =[]
ReviwsCount =[]
ActualPrice =[]
DiscountedPrice =[]
newdevice = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=option)
for link in complete_url:
    try :
        newdevice.get(link)
        WebDriverWait(newdevice,15)
    #     browser.wa
        singlepage = newdevice.page_source
        singlesoup=BeautifulSoup(singlepage,'html.parser')
        Title.append(singlesoup.find('span',attrs={'id':'productTitle'}).text.strip())
        ReviwsCount.append(singlesoup.find('span',attrs={'id':'acrCustomerReviewText'}).text.strip())
        ActualPrice.append(singlesoup.find('span',attrs={'class':'priceBlockStrikePriceString a-text-strike'}).text.strip(' ₹\xa0'))
        DiscountedPrice.append(singlesoup.find('span',attrs={'id':'priceblock_dealprice'}).text.strip(' ₹\xa0'))
    except:
        continue
        priceblock_ourprice


# In[96]:


# to see the data in the form of dataframes
import pandas as pd


# In[97]:


data =[Title,ReviwsCount,ActualPrice,DiscountedPrice]


# In[98]:


df= pd.DataFrame(data)


# In[100]:


df.head().T

