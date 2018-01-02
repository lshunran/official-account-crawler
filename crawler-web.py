# -*- coding: utf-8 -*-

import web
import sys
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

urls = (
    '/officialaccount', 'officialAccount'

)

class officialAccount:
    def GET(self):
        data = []

        i = web.input()
        
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)

        driver = webdriver.PhantomJS(executable_path=[YOUR-PhantomJS-PATH])

        # For example, In my Mac: driver = webdriver.PhantomJS(executable_path='/Users/ashun/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
        
        driver.get('https://www.newrank.cn/public/info/detail.html?account=' + i.id)

        wait = WebDriverWait(driver, 20)

        wait.until(EC.presence_of_element_located((By.ID, 'info_detail_article_top')))

        for title in driver.find_elements_by_css_selector('a.ellipsis'):
            print(title.get_attribute('title'))
            data.append(title.get_attribute('title'))

        driver.close()

        result = {
            'data': data
        }
        return json.dumps(result, ensure_ascii=False)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
