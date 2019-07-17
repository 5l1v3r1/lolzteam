from selenium import webdriver
import re, datetime, time, os

def login(driver):
        driver.get('https://lolzteam.net/login/')
        while True:
                time.sleep(3)
                if driver.current_url == 'https://lolzteam.net/':
                        token = driver.find_element_by_name('_xfToken').get_attribute('value')
                        break
        return token

def get_contests(driver):
        one = driver.get('https://lolzteam.net/forums/contests/')
        html1 = driver.page_source
        first = re.findall(r'threads\/\d{6,10}\/', html1)

        two = driver.get('https://lolzteam.net/forums/contests/page-2')
        html2 = driver.page_source
        second = re.findall(r'threads\/\d{6,10}\/', html2)

        three = driver.get('https://lolzteam.net/forums/contests/page-3')
        html3 = driver.page_source
        third = re.findall(r'threads\/\d{6,10}\/', html3)

        all = first + second + third
        rep = list(dict.fromkeys(all))
        return rep

def with_like(driver, token, rep):
        x = 0
        with open('{}.txt'.format(datetime.datetime.now().strftime("%d%m%Y-%H%M%S")), 'w') as f:
                try:
                        for i in rep:
                            driver.get('https://lolzteam.net/'+i)
                            like_url = driver.find_elements_by_xpath("//a[@class='Tooltip PopupTooltip LikeLink item control like']")[0].get_attribute('href')
                            driver.get(like_url)
                            driver.find_element_by_xpath("//input[@type='submit']").click()
                            rep[x] = 'https://lolzteam.net/'+i+'participate?_xfToken='+token
                            driver.get(rep[x])
                            f.write(rep[x])
                            x += 1
                except: pass
                driver.quit()
                os.system("taskkill /im chromedriver.exe")

def simple(driver, token, rep):
        x = 0
        with open('{}.txt'.format(datetime.datetime.now().strftime("%d%m%Y-%H%M%S")), 'w') as f:
            for i in rep:
                    rep[x] = 'https://lolzteam.net/'+i+'participate?_xfToken='+token
                    driver.get(rep[x])
                    f.write(rep[x])
                    x += 1
        driver.quit()
        os.system("taskkill /im chromedriver.exe")

def main():
        kak = input('С лайками/без(1,0): ')
        driver = webdriver.Chrome()
        token = login(driver)
        rep = get_contests(driver)
        if kak == '1':
              with_like(driver, token, rep)
        elif kak == '0':
                simple(driver, token, rep)
        else: print('Error')

if __name__ == '__main__':
        main()
