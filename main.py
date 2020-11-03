from telnetlib import EC
from time import sleep

import requests
from lxml import html
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.support import expected_conditions as EC

from data import tabs, subs


class App:
    def __init__(self, ):
        self.error = None
        self.i = 0
        self.t = 0
        self.x = 0
        self.y = 0
        self.item = 0
        self.main_url = 'https://www.wsj.com/'
        # navigation modes: AUDIO TRANSLATION / AUTOMATIC BROWSING
        # self.scrape()
        # self.scrapingLinks(self.main_url)
        # self.cover()
        self.magazine()

    def scrape(self):
        ua = UserAgent()
        header = {'user-agent': ua.random}
        response = requests.get(self.main_url, headers=header)
        soup = BeautifulSoup(response.content, 'lxml')
        print("JOURNAL CONTENTS:")
        for link in soup.find_all('p'):
            print(link.getText())

    def scrapingLinks(self, url):
        """crawl all the links on the page to use them in subsequent searches"""
        print("\nGetting links from the url:" + url)

        try:
            response = requests.get(url)
            parsed_body = html.fromstring(response.text)

            # regular expression to get links
            links = parsed_body.xpath('//a/@href')
            print('links% s found' % len(links))
            for link in links:
                print(link)

        except Exception as e:
            print(e)
            print("Connection error with " + url)
            pass

    def drivers(self):
        """download the drivers if they are not installed"""
        try:
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            self.error = False
        except Exception as e:
            self.error = True
            print('Firefox browser not found in os\n', e)

        if self.error:
            try:
                self.driver = webdriver.Chrome(ChromeDriverManager().install())
                self.error = False
            except Exception as e:
                self.error = True
                print('Chrome browser not found in os\n', e)

        if self.error:
            try:
                self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
                self.error = False
            except Exception as e:
                self.error = True
                print('Edge browser not found in os\n', e)

        if self.error:
            try:
                self.driver = webdriver.Opera(executable_path=OperaDriverManager().install())
                self.error = False
            except Exception as e:
                self.error = True
                print('Opera browser not found in os\n', e)

        self.driver.get(self.main_url)

        print("USER AGENT:\n", self.driver.execute_script("return navigator.userAgent"))

    def cover(self):  # todo: check cover news
        """browse all the covers of the main menu"""
        self.drivers()
        print("1 \tHome")

        for tab in tabs:
            for j in tab.keys():
                print("%s \t%s" % (tab[j], j))
                timeout = 15
                try:
                    element_present = EC.presence_of_element_located((By.XPATH, '//nav/ul/li[' + tab[j] + ']/a'))
                    WebDriverWait(self.driver, timeout).until(element_present).click()
                except TimeoutException:
                    print("Timed out waiting for page to load")
                sleep(8)

        self.driver.close()

    def switcher(self, section):
        """switches all sections of the dropdown menu"""
        if section == 1:
            self.i, self.t = 0, 0
            self.x = slice(0, 7, 1)  # ATTENTION leaving blank space among values may not work
            self.y = tabs[0]['World']
        if section == 2:
            self.i, self.t = 7, 1
            self.x = slice(7, 11, 1)
            self.y = tabs[1]['U.S.']
        if section == 3:
            self.i, self.t = 11, 2
            self.x = slice(11, 13, 1)
            self.y = tabs[2]['Politics']
        if section == 4:
            self.i, self.t = 13, 4
            self.x = slice(13, 16, 1)
            self.y = tabs[4]['Business']
        if section == 5:
            self.i, self.t = 16, 5
            self.x = slice(16, 18, 1)
            self.y = tabs[5]['Tech']
        if section == 6:
            self.i, self.t = 18, 6
            self.x = slice(18, 24, 1)
            self.y = tabs[6]['Markets']
        if section == 7:
            self.i, self.t = 24, 8
            self.x = slice(24, 36, 1)
            self.y = tabs[8]['Life & Arts']
        if section == 8:
            self.i, self.t = 36, 9
            self.x = slice(36, 38, 1)
            self.y = tabs[9]['Real State']
        if section == 9:
            self.i, self.t = 38, 10
            self.x = slice(38, -1, 1)
            self.y = tabs[10]['WSJ.Magazine']

        return self.i, self.t, self.x, self.y

    def magazine(self):
        """browses all sections of the dropdown menu"""
        self.drivers()
        i, t, x, y = self.switcher(1)
        print("TAB Key: " + ' '.join(tabs[t].keys()) + " - TAB Value: " + ' '.join(tabs[t].values()))
        print("SUBS SLICE DICT LIST:\n\t", subs[x])

        for sub in subs[x]:
            self.driver.implicitly_wait(1)
            for k in sub.keys():
                element_to_hover_over = self.driver.find_element_by_xpath(
                    '//nav/ul/li[' + y + ']/a')  # tab
                hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
                hover.perform()
                element = WebDriverWait(self.driver, 100).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//nav/ul/li[" + y + "]/div/div/ul[1]/li[" + sub[k] + "]/a"))
                )
                try:
                    ActionChains(self.driver).click(element).perform()
                    if self.item == 0:
                        print("REAL-TIME PERFORMANCE:")
                    print(' '.join(subs[i].keys()))
                    self.item += 1
                    i += 1
                except WebDriverException:
                    print("Element is not clickable")
                sleep(4)

        self.driver.close()


if __name__ == '__main__':
    app = App()
