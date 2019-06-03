from selenium import webdriver
import re, datetime, time, os
driver = webdriver.Chrome()


driver.get('https://lolzteam.net/login/')
while True:
        time.sleep(3)
        if driver.current_url == 'https://lolzteam.net/':
                token = driver.find_element_by_name('_xfToken').get_attribute('value')
                break


one = driver.get('https://lolzteam.net/forums/contests/')
html1 = driver.page_source
first = re.findall(r'threads\/\d{6}\/', html1)

two = driver.get('https://lolzteam.net/forums/contests/page-2')
html2 = driver.page_source
second = re.findall(r'threads\/\d{6}\/', html2)

three = driver.get('https://lolzteam.net/forums/contests/page-3')
html3 = driver.page_source
third = re.findall(r'threads\/\d{6}\/', html3)

all = first + second + third
rep = list(dict.fromkeys(all))
x = 0
with open('{}.txt'.format(datetime.datetime.now().strftime("%d%m%Y-%H%M%S")), 'w') as f:
    for i in rep:
            rep[x] = 'https://lolzteam.net/'+i+'participate?_xfToken='+token
            driver.get(rep[x])
            f.write(rep[x]+'\n')
            x += 1
driver.quit()
os.system("taskkill /im chromedriver.exe")
