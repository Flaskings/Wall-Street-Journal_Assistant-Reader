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
              {'Sections':
                   {'Economy': (2, 2, 2)}},
              {'More':
                   {'World Video': (2, 3, 2)}}]},
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
             [{'Blogs': {'Real Time Economics': (5, 1, 2)}},
              {'WSJ Pro':
                   [{'Bankruptcy': (5, 2, 2)},
                    {'Central Banking': (5, 2, 3)},
                    {'Private Equity': (5, 2, 4)},
                    {'Strategic Intelligence': (5, 2, 5)},
                    {'Venture Capital': (5, 2, 6)}]},
              {'More':
                   [{'Economic Forecasting Survey': (5, 3, 2)},
                    {'Economy Video': (5, 3, 3)}]}]},
        {'Business':
             [{'Sections':
                   [{'Management': (6, 1, 2)},
                    {'Tech/WSJ.D': (6, 1, 3)},
                    {'The Future of Everything': (6, 1, 4)}]},
              {'Industries':
                   [{'Aerospace & Defense': (6, 2, 2)},
                    {'Autos & Transportation': (6, 2, 3)},
                    {'Commercial Real Estate': (6, 2, 4)},
                    {'Consumer Products': (6, 2, 5)},
                    {'Energy': (6, 2, 6)},
                    {'Entrepreneurship': (6, 2, 7)},
                    {'Financial Services': (6, 2, 8)},
                    {'Food & Services': (6, 2, 9)},
                    {'Health Care': (6, 2, 10)},
                    {'Hospitality': (6, 3, 2)},  # switch
                    {'Law': (6, 3, 3)},
                    {'Manufacturing': (6, 3, 4)},
                    {'Media & Marketing': (6, 3, 5)},
                    {'Natural Resources': (6, 3, 6)},
                    {'Retail': (6, 3, 7)}]},
              {'C-Suite':
                   [{'CFO Journal': (6, 4, 2)},
                    {'CIO Journal': (6, 4, 3)},
                    {'CMO Today': (6, 4, 4)},
                    {'Logistics Report': (6, 4, 5)},
                    {'Risk & Compliance': (6, 4, 6)},
                    {'The Experience Report': (6, 4, 7)}]},
              {'Columns':
                   {'Heard on the Street': (6, 5, 2)}},
              {'WSJ Pro':
                   [{'Artificial Intelligence': (6, 6, 2)},
                    {'Bankruptcy': (6, 6, 3)},
                    {'Central Banking': (6, 6, 4)},
                    {'Cybersecurity': (6, 6, 5)},
                    {'Private Equity': (6, 6, 6)},
                    {'Strategic Intelligence': (6, 6, 7)},
                    {'Venture Capital': (6, 6, 8)}]},
              {'More':
                   [{'Business Video': (6, 7, 2)},
                    {'Journal Report': (6, 7, 3)},
                    {'Business Podcast': (6, 7, 4)}]}]},
        {'Tech':
             [{'Sections':
                   [{'CIO Journal': (7, 1, 2)},
                    {'The Future of Everything': (7, 1, 3)}]},
              {'Columns & Blogs':
                   [{'Christopher Mims': (7, 2, 2)},
                    {'Joanna Stern': (7, 2, 3)},
                    {'Julie Jargon': (7, 2, 4)}]},
              {'More':
                   [{'Tech Video': (7, 3, 2)},
                    {'Tech Podcast': (7, 3, 3)},
                    {'Startup Stock Tracker': (7, 3, 4)}]}]},
        {'Markets':
             [{'Sections':
                   [{'Bonds': (8, 1, 2)},
                    {'Commercial Real Estate': (8, 1, 3)},
                    {'Commodities & Futures': (8, 1, 4)},
                    {'Stocks': (8, 1, 5)},
                    {'Personal Finance': (8, 1, 6)},
                    {'WSJ Money': (8, 1, 7)}]},
              {'Columns & Blogs':
                   [{'Heard on the Street': (8, 2, 2)},
                    {'MoneyBeat': (8, 2, 3)},
                    {'Wealth Adviser': (8, 2, 4)}]},
              {'Market Data':
                   [{'Market Data Home': (8, 3, 2)},
                    {'U.S. Stocks': (8, 3, 3)},
                    {'Currencies': (8, 3, 4)},
                    {'Companies': (8, 3, 5)},
                    {'Commodities': (8, 3, 6)},
                    {'Bonds & Rates': (8, 3, 7)},
                    {'Mutual Funds & ETFs': (8, 3, 8)}]},
              {'More':
                   [{'CFO Journal': (8, 4, 2)},
                    {'Journal Report': (8, 4, 3)},
                    {'Markets Video': (8, 4, 4)},
                    {'Your Money Briefing Podcast': (8, 4, 5)},
                    {'Secrets of Wealthy Women Podcast': (8, 4, 6)},
                    {'Search Quotes and Companies': (8, 4, 7)}]}], },
        {'Opinion':
             [{'Columnists':
                   [{'Gerard Baker': (9, 1, 2)},
                    {'Sadanand Dhume': (9, 1, 3)},
                    {'James Freeman': (9, 1, 4)},
                    {'William A. Galston': (9, 1, 5)},
                    {'Daniel Henninger': (9, 1, 6)},
                    {'Holman W. Jenkins': (9, 1, 7)},
                    {'Andy Kessler': (9, 1, 8)},
                    {'William McGurn': (9, 1, 9)},
                    {'Walter Russell Mead': (9, 1, 10)},
                    {'Peggy Noonan': (9, 1, 11)},
                    {"Mary Anastasia O'Grady": (9, 1, 12)},
                    {'Jason Riley': (9, 1, 13)},
                    {'Joseph Sternberg': (9, 1, 14)},
                    {'Kimberley A. Strassel': (9, 1, 15)}]},
              {'Reviews':
                   [{'Books': (9, 2, 2)},
                    {'Film': (9, 2, 3)},
                    {'Television': (9, 2, 4)},
                    {'Theater': (9, 2, 5)},
                    {'Art': (9, 2, 6)},
                    {'Masterpiece Series': (9, 2, 7)},
                    {'Music': (9, 2, 8)},
                    {'Dance': (9, 2, 9)},
                    {'Opera': (9, 2, 10)},
                    {'Exhibition': (9, 2, 11)},
                    {'Cultural Commentary': (9, 2, 12)}]
               },
              {'More':
                   [{'Editorials': (9, 3, 2)},
                    {'Commentary': (9, 3, 3)},
                    {'Future View': (9, 3, 4)},
                    {'Letters to the Editor': (9, 3, 5)},
                    {'The Weekend Interview': (9, 3, 6)},
                    {'Potomac Watch Podcast': (9, 3, 7)},
                    {'Foreign Edition Podcast': (9, 3, 8)},
                    {'Opinion Video': (9, 3, 9)},
                    {'Notable & Quotable': (9, 3, 10)},
                    {'Best of the Web Newsletter': (9, 3, 11)},
                    {'Morning Editorial Report Newsletter': (9, 3, 12)}]}]},
        {'Life & Arts':
             [{'Sections':
                   [{'Arts': (10, 1, 2)},
                    {'Books': (10, 1, 3)},
                    {'Cars': (10, 1, 4)},
                    {'Food & Drink': (10, 1, 5)},
                    {'Health': (10, 1, 6)},
                    {'Ideas': (10, 1, 7)},
                    {'Reading & Retreating': (10, 1, 8)},
                    {'Real Estate': (10, 1, 9)},
                    {'Science': (10, 1, 10)},
                    {'Sports': (10, 1, 11)},
                    {'Style & Fashion': (10, 1, 12)},
                    {'Travel': (10, 1, 13)}]},

              {'More':
                   [{'WSJ. Magazine': (10, 2, 2)},
                    {'WSJ Puzzles': (10, 2, 3)},
                    {'The Future of Everything': (10, 2, 4)},
                    {'Far & Away': (10, 2, 5)},
                    {'Life Video': (10, 2, 6)},
                    {'Arts Video': (10, 2, 7)}]}], },
        {'Real State':
             [{'Sections':
                   [{'Commercial Real Estate': (11, 1, 2)},
                    {'House of the Day': (11, 1, 3)}]},
              {'More':
                   {'Real Estate Video': (11, 2, 2)}}]},
        {'WSJ.Magazine':
             [{'Sections':
                   [{'Fashion': (12, 1, 2)},
                    {'Art & Design': (12, 1, 3)},
                    {'Travel': (12, 1, 4)},
                    {'Food': (12, 1, 5)},
                    {'Culture': (12, 1, 6)}]}]}]
