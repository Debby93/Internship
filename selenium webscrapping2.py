#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install seleniumimport selenium')


# In[2]:


import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time
import pandas as pd


# In[48]:


''' Question1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data. 
This task will be done in following steps: 
1.	First get the webpage https://www.shine.com/ 
2.	Enter “Data Analyst” in “Job title, Skills” field and enter “Bangalore” in “enter the  location” field. 
3.	Then click the search button. 
4.	Then scrape the data for the first 10 jobs results youWrite a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data. 
This task will be done in following steps: 
1.	First get the webpage https://www.shine.com/ 
2.	Enter “Data Analyst” in “Job title, Skills” field and enter “Bangalore” in “enter the  location” field. 
3.	Then click the search button. 
4.	Then scrape the data for the first 10 jobs results you get. 
5.	Finally create a dataframe of the scraped data
 get. 
5.	Finally create a dataframe of the scraped data
'''


# In[3]:


driver=webdriver.Chrome()


# In[4]:


driver.get('https://www.shine.com/ ')


# In[6]:


designation=driver.find_element(By.CLASS_NAME,"form-control  ")
designation.send_keys('Data Analyst')


# In[7]:


location=driver.find_element(By.XPATH,'/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input')
location.send_keys('Bangalore')


# In[8]:


search=driver.find_element(By.CLASS_NAME,"searchForm_btnWrap_advance__VYBHN")
search.click()


# In[9]:


job_title=[]
job_location=[]
job_experience=[]
company_name=[]


# In[10]:


title_tags=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]')
for i in title_tags[0:10]:
    job_title.append(i.text)
    
location_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags[0:10]:
    job_location.append(i.text)
    
experience_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in experience_tags[0:10]:
    job_experience.append(i.text)
    
company_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]/span')
for i in company_tags[0:10]:
    company_name.append(i.text)


# In[11]:


print(len(job_title),len(job_location),len(job_experience),len(company_name))


# In[12]:


df=pd.DataFrame({"Title":job_title,"Location":job_location,"Experience":job_experience,"Company":company_name})
df


# In[13]:


#QUestion2 Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name


# In[14]:


driver=webdriver.Chrome()


# In[15]:


driver.get('https://www.shine.com/ ')


# In[17]:


designation=driver.find_element(By.CLASS_NAME,"form-control  ")
designation.send_keys("Data Scientist")


# In[18]:


location=driver.find_element(By.XPATH,'/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input')
location.send_keys("Bangalore")


# In[19]:


search=driver.find_element(By.CLASS_NAME,"searchForm_btnWrap_advance__VYBHN")
search.click()


# In[20]:


job_title=[]
job_location=[]
company_name=[]


# In[40]:


title_tags=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]')
for i in title_tags[0:10]:
    job_title.append(i.text)
    
location_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags[0:10]:
    job_location.append(i.text)
company_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]/span')
for i in company_tags[0:10]:
    company_name.append(i.text)    


# In[41]:


print(len(job_title),len(job_location),len(company_name))


# In[43]:


df=pd.DataFrame({"Title":job_title,"Location":job_location,"Company":company_name})
df[0:10]


# In[ ]:





# In[44]:


#Question3


# In[45]:


driver=webdriver.Chrome()


# In[46]:


driver.get('https://www.shine.com/ ')


# In[47]:


designation=driver.find_element(By.CLASS_NAME,"form-control  ")
designation.send_keys("Data Scientist")


# In[48]:


search=driver.find_element(By.CLASS_NAME,"searchForm_btnWrap_advance__VYBHN")
search.click()


# In[53]:


location=driver.find_element(By.CLASS_NAME,"filter_filter_lists_items__wlFfo")
location.send_keys("Delhi")


# In[54]:


#Question 4 scrap data of first 100 sunglasses


# In[55]:


driver=webdriver.Chrome()


# In[56]:


driver.get('https://www.flipkart.com/')


# In[59]:


designation=driver.find_element(By.CLASS_NAME,"_3704LK")
designation.send_keys("Sunglasses")


# In[60]:


search=driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
search.click()


# In[62]:


product_brand=[]
product_price=[]
product_discount=[]


# In[63]:


start=0
end=3
for page in range(start,end):
    brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand_tags[0:100]:
        product_brand.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(3)
    
for page in range(start,end):
    price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in price_tags[0:100]:
        product_price.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(3)
    
for page in range(start,end):
    discount=driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')
    for i in discount[0:100]:
        product_discount.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(3)
    


# In[64]:


print(len(product_brand),len(product_price),len(product_discount))


# In[65]:


df=pd.DataFrame({"Brand":product_brand,"Price":product_price,"Discount":product_discount})
df[0:100]


# In[66]:


#Question 5 Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link


# In[3]:


import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time
import pandas as pd


# In[4]:


driver=webdriver.Chrome()


# In[5]:


driver.get('https://www.flipkart.com/appl e-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LST MOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART')


# In[6]:


rating=[]
review_summary=[]
full_review=[]


# In[16]:


rating_tags=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
for i in rating_tags[0:100]:
    rating.append(i.text)
    
summary_tags=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
for i in summary_tags[0:100]:
    review_summary.append(i.text)
    
review_tags=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
for i in review_tags[0:100]:
    full_review.append(i.text)


# In[18]:


print(len(rating),len(review_summary),len(full_review))


# In[19]:


#Question6 Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the search field. 


# In[20]:


driver=webdriver.Chrome()


# In[21]:


driver.get('http://www.flipkart.com/')


# In[24]:


designation=driver.find_element(By.CLASS_NAME,"_3704LK")
designation.send_keys("sneakers")


# In[25]:


search=driver.find_element(By.CLASS_NAME,"L0Z3Pu")
search.click()


# In[26]:


brand=[]
product_description=[]
price=[]


# In[35]:


start=1
end=3
for page in range(start,end):
    brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand_tags[0:100]:
        brand.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(3)
    
for page in range(start,end):
    description_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in description_tags[0:100]:
        product_description.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(3)
    
for page in range(start,end):
    price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in price_tags[0:100]:
        price.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(3)


# In[36]:


print(len(brand),len(product_description),len(price))


# In[37]:


print(brand)[0:100]


# In[38]:


print(product_description)[0:100]


# In[39]:


print(price)[0:100]


# In[40]:


#Question 8 : Write a python program to scrape data for Top 1000 Quotes of All Time.  


# In[41]:


driver=webdriver.Chrome()


# In[42]:


driver.get('http://www.azquotes.com/')


# In[43]:


top_quote=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[3]/ul/li[5]/a')
top_quote.click()


# In[44]:


quote=[]
author=[]
type_of_quote=[]


# In[45]:


start=0
end=10
for page in range(start,end):
    quote_tags=driver.find_elements(By.XPATH,'//a[@class="title"]')
    for i in quote_tags:
        quote.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div[1]/div/div[3]/li[12]')
    next_button.click()
    time.sleep(3)
for page in range(start, end):
    author_tags=driver.find_elements(By.XPATH,'//div[@class="author"]')
    for i in author_tags:
        author.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div[1]/div/div[3]/li[12]')
    next_button.click()
    time.sleep(3)
    
for page in range(start,end):
    quote_types=driver.find_elements(By.XPATH,'//div[@class="tags"]')
    for i in quote_types:
        type_of_quote.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div[1]/div/div[3]/li[12]')
    next_button.click()
    time.sleep(3)


# In[47]:


df=pd.DataFrame({"Quotes":quote,"Authors":author,"Type of Quote":type_of_quote})
df[0:1000]


# In[49]:


#Question 10


# In[50]:


driver=webdriver.Chrome()


# In[51]:


driver.get('https://www.motor1.com/')


# In[58]:


designation=driver.find_element(By.CLASS_NAME,"features-search_input")
designation.send_keys("50 most expensive cars in the world")


# In[59]:


search=driver.find_element(By.XPATH,'/html/body/div[10]/div[6]/form/input[2]')
search.click()


# In[60]:


click=driver.find_element(By.XPATH,'/html/body/div[10]/div[9]/div/div[1]/div/div/div[1]/div/div[1]/h3/a')
click.click()


# In[61]:


car_name=[]
car_price=[]


# In[ ]:


name_tags=driver.find_elements(By.XPATH,//h3[@class="subheader"])
for i in name_tags:
    car_name.append(i.text)
price_tags=driver.find_elements(By.XPATH,)


# In[62]:


#Question 9 Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead, Term of office,


# In[63]:


driver=webdriver.Chrome()


# In[64]:


driver.get('https://www.jagranjosh.com/')


# In[65]:


jk_designation=driver.find_element(By.XPATH,'/html/body/div/header/nav/div/div/div[3]/ul/li[7]/a')
jk_designation.click()


# In[66]:


#couldnt find the page for list of former Prime Ministers of India


# In[67]:


#Question 7 Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then set CPU Type filter to “Intel Core i7” as shown in the below image


# In[69]:


driver=webdriver.Chrome()


# In[70]:


driver.get('https://www.amazon.in/')


# In[ ]:





# In[ ]:




