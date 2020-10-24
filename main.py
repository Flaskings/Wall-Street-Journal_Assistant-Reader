from telnetlib import EC
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.support import expected_conditions as EC


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
        self.menu = [
            {'World':
                 [{'Regions':
                       ['Africa',
                        'Asia',
                        'Canada',
                        'China',
                        'Europe',
                        'Latin America',
                        'Middle East']},
                  {'Sections': 'Economy'},
                  {'More': 'World Video'}]
             },
            {'U.S.':
                 [{'Sections':
                       ['Economy',
                        'Law',
                        'New',
                        'York',
                        'Politics']},
                  {'Columns & Blogs':
                       ['Real Time Economics',
                        'Washington Wire']},
                  {'More':
                       ['WSJ Noted.',
                        'Journal Report',
                        'U.S.Video',
                        "What's News Podcast"]}]
             },
            {'Politics':
                 [{'Sections':
                       ['Election 2020',
                        'Campaign Wire']},
                  {'More':
                       ['WSJ/NBC News Poll',
                        'Politics Video']}]
             },
            {'Economy':
                 [{'Blogs': 'Real Time Economics'},
                  {'WSJ Pro':
                       ['Bankruptcy',
                        'Central Banking',
                        'Private Equity',
                        'Strategic Intelligence',
                        'Venture Capital']},
                  {'More':
                       ['Economic Forecasting Survey',
                        'Economy Video']}]
             },
            {'Business':
                 [{'Sections':
                       ['Management',
                        'Tech/WSJ.D',
                        'The Future of Everything']},
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
             },
            {'Tech':
                 [{'Sections':
                       ['CIO Journal',
                        'The Future of Everything']},
                  {'Columns & Blogs':
                       ['Christopher Mims',
                        'Joanna Stern'
                        'Julie Jargon']},
                  {'More':
                       ['Tech Video',
                        'Tech Podcast',
                        'Startup Stock Tracker']}]
             },
            {'Markets':
                 [{'Sections':
                       ['Bonds',
                        'Commercial Real Estate',
                        'Commodities & Futures',
                        'Stocks',
                        'Personal Finance',
                        'WSJ Money']},
                  {'Columns & Blogs':
                       ['Heard on the Street',
                        'MoneyBeat',
                        'Wealth Adviser']},
                  {'Market Data':
                       ['Market Data Home',
                        'U.S. Stocks', 'U.S. Stocks',
                        'Currencies',
                        'Companies',
                        'Commodities',
                        'Bonds & Rates',
                        'Mutual Funds & ETFs']},
                  {'More':
                       ['CFO Journal',
                        'Journal Report',
                        'Markets Video',
                        'Your Money Briefing Podcast',
                        'Secrets of Wealthy Women Podcast',
                        'Search Quotes and Companies']}],
             },
            {'Opinion':
                 [{'Columnists':
                       ['Gerard Baker',
                        'Sadanand Dhume',
                        'James Freeman',
                        'William A. Galston',
                        'Daniel Henninger',
                        'Holman W. Jenkins',
                        'Andy Kessler',
                        'William McGurn',
                        'Walter Russell Mead',
                        'Peggy Noonan',
                        "Mary Anastasia O'Grady",
                        'Jason Riley',
                        'Joseph Sternberg',
                        'Kimberley A. Strassel']},
                  {'Reviews':
                       ['Books',
                        'Film',
                        'Television',
                        'Theater',
                        'Art',
                        'Masterpiece Series',
                        'Music',
                        'Dance',
                        'Opera',
                        'Exhibition',
                        'Cultural Commentary']
                   },
                  {'More':
                       ['Editorials',
                        'Commentary',
                        'Future View',
                        'Letters to the Editor',
                        'The Weekend Interview',
                        'Potomac Watch Podcast',
                        'Foreign Edition Podcast',
                        'Opinion Video',
                        'Notable & Quotable',
                        'Best of the Web Newsletter',
                        'Morning Editorial Report Newsletter']}]
             },
            {'Life & Arts':
                 [{'Sections':
                       ['Arts',
                        'Books',
                        'Cars',
                        'Food & Drink',
                        'Health',
                        'Ideas',
                        'Reading & Retreating',
                        'Real Estate',
                        'Science',
                        'Sports',
                        'Style & Fashion',
                        'Travel']},

                  {'More':
                       ['WSJ. Magazine',
                        'WSJ Puzzles',
                        'The Future of Everything',
                        'Far & Away',
                        'Life Video',
                        'Arts Video']}],
             },
            {'Real State':
                 [{'Sections':
                       ['Commercial Real Estate',
                        'House of the Day']},
                  {'More': 'Real Estate Video'}]},
            {'WSJ.Magazine':
                 [{'Sections':
                       ['Fashion',
                        'Art & Design',
                        'Travel',
                        'Food',
                        'Culture']}]}

        ]
        self.performance(1)

    def cover_look(self):  # todo: check cover news
        pass

    def performance(self, program):
        tabs = [{'World': '2'},
                {'U.S.': '3'},
                {'Politics': '4'},
                {'Economy': '5'},
                {'Business': '6'},
                {'Tech': '7'},
                {'Markets': '8'},
                {'Opinion': '9'},
                {'Life & Arts': '10'},
                {'Real State': '11'},
                {'WSJ.Magazine': '12'}]

        subs = [{'Africa': '2'},
                {'Asia': '3'},
                {'Canada': '4'},
                {'China': '5'},
                {'Europe': '6'},
                {'Latin America': '7'},
                {'Middle East': '8'}]

        if program == 0:
            i = 0
            print("1 \tHome")
            for tab in tabs:
                i += 1
                for j in tab.keys():
                    print("%s \t%s" % (tab[j], j))
                    element = self.driver.find_element_by_xpath('//nav/ul/li[' + tab[j] + ']/a')  # tab
                    element.click()
                    sleep(1)

            self.driver.close()

        if program == 1:
            index = 0
            print(' '.join(tabs[0].keys()))
            for sub in subs:
                for k in sub.keys():
                    element_to_hover_over = self.driver.find_element_by_xpath('//nav/ul/li[' + tabs[0]['World'] + ']/a')  # tab
                    hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
                    hover.perform()
                    sleep(1)
                    element = WebDriverWait(self.driver, 100).until(
                        EC.element_to_be_clickable((By.XPATH, "//nav/ul/li[" + tabs[0]['World'] + "]/div/div/ul[1]/li[" + sub[k] + "]/a"))
                    )
                    try:
                        ActionChains(self.driver).click(element).perform()
                        print(' '.join(subs[index].keys()))
                        index += 1
                    except WebDriverException:
                        print("Element is not clickable")
                    sleep(4)
            self.driver.close()


if __name__ == '__main__':
    app = App()
