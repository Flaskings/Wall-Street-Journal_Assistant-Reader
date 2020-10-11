from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager


class App:
    def __init__(self, ):
        self.error = None
        try:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        except Exception as e:
            self.error = True
            print('Chrome browser not found in os\n', e)
        try:
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        except Exception as e:
            self.error = True
            print('Firefox browser not found in os\n', e)
        try:
            self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        except Exception as e:
            self.error = True
            print('Edge browser not found in os\n', e)
        try:
            self.driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        except Exception as e:
            self.error = True
            print('Opera browser not found in os\n', e)
        self.main_url = 'https://www.wsj.com/'
        self.driver.get(self.main_url)
        self.performance()

    def performance(self, ):
        sleep(2)
        self.driver.close()


if __name__ == '__main__':
    app = App()
