from selenium import webdriver
import urllib.request
import time
import re
from bs4 import BeautifulSoup
import pyautogui
from selenium.webdriver.common.keys import Keys

#여기서 부터 시작 입니다.
start = 0
while True :
    URL = "https://www.marathonbet.com/ko/betting/?page="+str(start)+"&pageAction=getPage"
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'html.parser')
    # text = driver.find_element_by_class_name('category-label')
    text = soup.find_all('h2')
    for i in text :
        print(i.get_text())
        t = i.get_text()
        t1 = t.find('결과')
        if t1 == 0 :
            break
        start+=1
        driver.close()


# print(soup.get_text())
# for i in text :
#     print(i)





# text = ""
# for i in range(1,25) :
#     pyautogui.click()
#     URL = "https://www.marathonbet.com/ko/betting/Football"
#     driver = webdriver.Chrome(executable_path='chromedriver')
#     driver.get(url=URL)
#     html_doc = driver.page_source
#     soup = BeautifulSoup(html_doc, 'html.parser')
#     text = soup.get_text()
#     print(text)
#     time.sleep(2)

# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)
#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     print(new_height)
#     if new_height == last_height:
#         break
#     last_height = new_height






# league_name = soup.find_all(class_='category-container')
# l_name = soup.select('h2')
# print(l_name)
# for i in l_name :
#     print(i.get_text())
# driver.close()