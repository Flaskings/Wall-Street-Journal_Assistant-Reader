"""MAIN MENU"""
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
# WORLD REGIONS & SECTIONS DROPDOWN ITEMS
subs = [{'Africa': '2'},  # LINK: WORLD
        {'Asia': '3'},
        {'Canada': '4'},
        {'China': '5'},
        {'Europe': '6'},
        {'Latin America': '7'},
        {'Middle East': '8'},
        {'Economy': '2'},  # LINK: US
        {'Law': '3'},
        {'New York': '4'},
        {'Politics': '5'},
        {'Election 2020': '2'},  # LINK: POLITICS
        {'Campaign Wire': '3'},
        {'Management': '2'},  # LINK BUSINESS
        {'Tech/WSJ.D': '3'},
        {'The Future of Everything': '4'},
        {'CIO Journal': '2'},  # LINK TECH
        {'The Future of Everything': '3'},
        {'Bonds': '2'},  # LINK MARKETS
        {'Commercial Real Estate': '3'},
        {'Commodities & Futures': '4'},
        {'Stocks': '5'},
        {'Personal Finance': '6'},
        {'WSJ Money': '7'},
        {'Arts': '2'},  # LINK LIFE & ARTS
        {'Books': '3'},
        {'Cars': '4'},
        {'Food & Drink': '5'},
        {'Health': '6'},
        {'Ideas': '7'},
        {'Reading & Retreating': '8'},
        {'Real Estate': '9'},
        {'Science': '10'},
        {'Sports': '11'},
        {'Style & Fashion': '12'},
        {'Travel': '13'},
        {'Commercial Real Estate': '2'},  # LINK REAL STATE
        {'House of the Day': '3'},
        {'Fashion': '2'},  # LINK WSJ MAGAZINE
        {'Art & Design': '3'},
        {'Travel': '4'},
        {'Food': '5'},
        {'Culture': '6'}
        ]

#  TODO MAIN TABS:
#    0. Home,
#    1. World,
#    2. U.S.,
#    3. Politics,
#    4. Economy,
#    5. Business,
#    6. Tech,
#    7. Markets,
#    8. Opinion,
#    9.Life & Arts
#   10.Real State
#   11.WSJ.Magazine

# TODO SPECIFIC TARGETS:
#  (2, 1, 2) World -> Regions -> China"
#  (3, 1, 3) U.S. -> Sections -> Law
#  (6, 6, 2) Business -> WSJ Pro -> Artificial Intelligence
#  (7, 1, 2) Tech -> Sections -> CIO Journal


maps = [{'Home': ''},
        {'World':
             [{'Regions':
                   [{'Africa': (2, 1, 2)},
                    {'Asia': (2, 1, 3)},
                    {'Canada': (2, 1, 4)},
                    {'China': (2, 1, 5)},
                    {'Europe': (2, 1, 6)},
                    {'Latin America': (2, 1, 7)},
                    {'Middle East': (2, 1, 8)}]},
              {'Sections': {'Economy': (2, 2, 2)}},
              {'More': {'World Video': (2, 3, 2)}}]},
        {'U.S.':
             [{'Sections':
                   [{'Economy': (3, 1, 2)},
                    {'Law': (3, 1, 3)},
                    {'New York': (3, 1, 4)},
                    {'Politics': (3, 1, 5)}]},
              {'Columns & Blogs':
                   [{'Real Time Economics': (3, 2, 2)},
                    {'Washington Wire': (3, 2, 3)}]},
              {'More':
                   [{'WSJ Noted.': (3, 3, 2)},
                    {'Journal Report': (3, 3, 3)},
                    {'U.S.Video': (3, 3, 4)},
                    {"What's News Podcast": (3, 3, 5)}]}]},
        {'Politics':
             [{'Sections':
                   [{'Election 2020': (4, 1, 2)},
                    {'Campaign Wire': (4, 1, 3)}]},
              {'More':
                   [{'WSJ/NBC News Poll': (4, 2, 2)},
                    {'Politics Video': (4, 2, 3)}]}]},
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
                    'Economy Video']}]},
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
                    'Business Podcast']}]},
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
                    'Startup Stock Tracker']}]},
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
                    'Search Quotes and Companies']}], },
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
                    'Morning Editorial Report Newsletter']}]},
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
                    'Arts Video']}], },
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
                    'Culture']}]}]
