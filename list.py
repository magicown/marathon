from selenium import webdriver
import urllib.request
import time
import re
from bs4 import BeautifulSoup
import pyautogui
from selenium.webdriver.common.keys import Keys
import json

# 리그명을 가져온다.
def get_league_name(soup) :
    text = soup.find_all('h2')
    for i in text :
        t = i.get_text() # h2로 가져온 리그 타이틀을 변수에 저장한다.
        league_name_list.append(t.replace(".","")) # 리그명중에 "."을 없앤다.
        if t.find('결과') == 0 : #html 소스중에 결과라는 텍스트가 있으면 while문의 빠져 나간다.
            return False            

# 리그 아이디를 구한다.
def get_league_id(soup) :        
    league_id = [item["data-category-treeid"] for item in soup.find_all() if "data-category-treeid" in item.attrs]
    league_id_temp = []
    for i in league_id:      
        league_id_temp.append(i.replace('\\"',""))

    return league_id_temp


#여기서 부터 시작 입니다.
start = 0
league_name_list = []
league_id = []
result_chk = True
while result_chk == True :
    # 브라우저 없이 크롬을 실행한다.
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR") # 한국어!
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")


    URL = "https://www.marathonbet.com/ko/betting/?page="+str(start)+"&pageAction=getPage"
    driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=options)
    driver.get(url=URL)

    driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5]}})")    
    driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
    driver.execute_script("const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")

    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'html.parser')
    make_json = soup.get_text()
    json_data = json.loads(make_json)    
    if json_data[1]['val'] == False :
        result_chk = False
    else :    
        # print(json_data[0]['content'])
        json_t = html_doc.split('"content":"')
        json_t1 = json_t[1].split('"},{"prop"')
        print(json_t1[0].replace('\&quot;',''))
        print(json.loads(json_t))
        res = get_league_name(soup)       
        if res == False :
            result_chk = False # while문의 빠져 나간다.
        else :
            league_id = get_league_id(soup)
    start+=1    
    result_chk = False    

# print(league_id)
# print(league_name_list)
driver.quit()