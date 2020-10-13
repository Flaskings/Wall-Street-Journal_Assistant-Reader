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
        self.performance()
        self.menu = [
            {'Home': ''},
            {'World':
                 [{'Regions': ['Africa', 'Asia', 'Canada', 'China', 'Europe', 'Latin America', 'Middle East']},
                  {'Sections': 'Economy'},
                  {'More': 'World Video'}]
             },
            {'U.S.':
                 [{'Sections': ['Economy', 'Law', 'New', 'York', 'Politics']},
                  {'Columns & Blogs': ['Real Time Economics', 'Washington Wire']},
                  {'More': ['WSJ Noted.', 'Journal Report', 'U.S.Video', "What's News Podcast"]}]
             },
            {'Politics':
                 [{'Sections': ['Election 2020', 'Campaign Wire']},
                  {'More': ['WSJ/NBC News Poll', 'Politics Video']}]
             },
            {'Economy':
                 [{'Blogs': 'Real Time Economics'},
                  {'WSJ Pro': ['Bankruptcy', 'Central Banking', 'Private Equity', 'Strategic Intelligence',
                               'Venture Capital']},
                  {'More': ['Economic Forecasting Survey', 'Economy Video']}]
             },
            {'Business':
                 [{'Sections': ['Management', 'Tech/WSJ.D', 'The Future of Everything']},
                  {'Industries':
                       ['Aerospace & Defense'
                        'Autos & Transportation'
                        'Commercial Real Estate'
                        'Consumer Products'
                        'Energy'
                        'Entrepreneurship'
                        'Financial Services'
                        'Food & Services'
                        'Health Care'
                        'Hospitality'
                        'Law',
                        'Manufacturing',
                        'Media & Marketing',
                        'Natural Resources',
                        'Retail']},
                  {'C-Suite':
                       ['CFO Journal',
                        'CIO Journal',
                        'CMO Today',
                        'Logistics Report',
                        'Risk & Compliance',
                        'The Experience Report']},
                  {'Columns': 'Heard on the Street'},
                  {'WSJ Pro':
                       ['Artificial Intelligence',
                        'Bankruptcy',
                        'Central Banking',
                        'Cybersecurity',
                        'Private Equity',
                        'Strategic Intelligence',
                        'Venture Capital']},
                  {'More':
                       ['Business Video',
                        'Journal Report',
                        'Business Podcast']}]
             }
        ]

    def cover_look(self):  # todo: check cover news
        pass

    def performance(self, ):
        sleep(2)
        self.driver.close()


if __name__ == '__main__':
    app = App()
