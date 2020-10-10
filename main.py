from selenium import webdriver
from time import sleep


class App:
    def __init__(self, ):
        self.driver = webdriver.Firefox(
            executable_path='/usr/local/bin/geckodriver')
        self.main_url = 'https://www.wsj.com/'
        self.driver.get(self.main_url)
        self.performance()

    def performance(self, ):
        sleep(4)
        self.driver.close()


if __name__ == '__main__':
    app = App()
