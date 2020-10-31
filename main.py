from telnetlib import EC
from time import sleep
from selenium import webdriver
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

        self.main_url = 'https://www.wsj.com/'
        self.driver.get(self.main_url)

        # navigation modes
        # self.cover()
        self.magazine()

    def cover(self):  # todo: check cover news
        """browse all the covers of the main menu"""
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

    def magazine(self):
        """browse all sections of the dropdown menu"""
        i_1, t_1 = 0, 0
        x_1 = slice(0,7,1)  # ATTENTION leaving blank space among values may not work
        y_1 = tabs[0]['World']
        i_2, t_2 = 7, 1
        x_2 = slice(7,11,1)
        y_2 = tabs[1]['U.S.']
        i_3, t_3 = 11, 2
        x_3 = slice(11,13,1)
        y_3 = tabs[2]['Politics']
        print("TAB Key: " + ' '.join(tabs[t_3].keys()) + " - TAB Value: " + ' '.join(tabs[t_3].values()))
        print("SUBS SLICE DICT LIST:\n\t", subs[x_3])
        for sub in subs[x_3]:
            for k in sub.keys():
                element_to_hover_over = self.driver.find_element_by_xpath(
                    '//nav/ul/li[' + y_3 + ']/a')  # tab
                hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
                hover.perform()
                sleep(1)
                element = WebDriverWait(self.driver, 100).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//nav/ul/li[" + y_3 + "]/div/div/ul[1]/li[" + sub[k] + "]/a"))
                )
                try:
                    ActionChains(self.driver).click(element).perform()
                    print(' '.join(subs[i_3].keys()))
                    i_3 += 1
                except WebDriverException:
                    print("Element is not clickable")
                sleep(4)

        self.driver.close()


if __name__ == '__main__':
    app = App()
