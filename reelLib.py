import time
import sys
import feedparser
import config

#Constants
logo_print_speed = 0.002






# Helper Functions
def delay(t):
    time.sleep(t)

# Print Functions
def delay_print(s,t=0.03):
    for c in s:
        sys.stdout.write('%s' % c)
        sys.stdout.flush()
        time.sleep(t)
    sys.stdout.write('\n')

def print_rss(post):
    print('\n')
    delay_print(post.title)
    print('- '*20)
    delay_print(post.summary)

def print_weather(obs,fore):
    print('\n')
    print('- '*20)
    delay_print("Current Temperature ("+ config.region_name +")")
    print('- '*10)
    delay_print(obs.entries[0].title.replace('°',''))
    print('\n')
    print('- '*20)
    delay_print("3 Day Forecast ("+ config.region_name +")")
    print('- '*10)
    for post in fore.entries:
        delay_print (post.title.replace('°',''))
        print('\n')

#Logo functions
def bbc_logo():
    print("\n")
    print("\n")
    delay_print('88888888ba   88888888ba     ,ad8888ba, ',logo_print_speed)
    delay_print('88      "8b  88      "8b   d8"\'    `"8b',logo_print_speed)
    delay_print('88      ,8P  88      ,8P  d8\'          ',logo_print_speed)
    delay_print('88aaaaaa8P\'  88aaaaaa8P\'  88           ',logo_print_speed)
    delay_print('88""""""8b,  88""""""8b,  88           ',logo_print_speed)
    delay_print('88      `8b  88      `8b  Y8,          ',logo_print_speed)
    delay_print('88      a8P  88      a8P   Y8a.    .a8P',logo_print_speed)
    delay_print('88888888P"   88888888P"     `"Y8888Y"\' ',logo_print_speed)

def bbc_news_logo():
    print('\n')
    print('\n')
    delay_print('88888888ba   88888888ba     ,ad8888ba,       888b      88 ',logo_print_speed)
    delay_print('88      "8b  88      "8b   d8"\'    `"8b      8888b     88 ',logo_print_speed)
    delay_print('88      ,8P  88      ,8P  d8\'                88 `8b    88 ',logo_print_speed)
    delay_print('88aaaaaa8P\'  88aaaaaa8P\'  88                 88  `8b   88   ,adPPYba,  8b      db      d8  ,adPPYba, ',logo_print_speed)
    delay_print('88""""""8b,  88""""""8b,  88                 88   `8b  88  a8P_____88  `8b    d88b    d8\'  I8[    "" ',logo_print_speed)
    delay_print('88      `8b  88      `8b  Y8,                88    `8b 88  8PP"""""""   `8b  d8\'`8b  d8\'    `"Y8ba,  ',logo_print_speed)
    delay_print('88      a8P  88      a8P   Y8a.    .a8P      88     `8888  "8b,   ,aa    `8bd8\'  `8bd8\'    aa    ]8I ',logo_print_speed)
    delay_print('88888888P"   88888888P"     `"Y8888Y"\'       88      `888   `"Ybbd8"\'      YP      YP      `"YbbdP"\' ',logo_print_speed)


def technology_logo():
    print("\n")
    delay_print('888888888888                       88                                     88 ',logo_print_speed)
    delay_print('     88                            88                                     88 ',logo_print_speed)
    delay_print('     88                            88                                     88 ',logo_print_speed)
    delay_print('     88     ,adPPYba,   ,adPPYba,  88,dPPYba,   8b,dPPYba,    ,adPPYba,   88   ,adPPYba,    ,adPPYb,d8  8b       d8 ',logo_print_speed)
    delay_print('     88    a8P_____88  a8"     ""  88P\'    "8a  88P\'   `"8a  a8"     "8a  88  a8"     "8a  a8"    `Y88  `8b     d8\' ',logo_print_speed)
    delay_print('     88    8PP"""""""  8b          88       88  88       88  8b       d8  88  8b       d8  8b       88   `8b   d8\'  ',logo_print_speed)
    delay_print('     88    "8b,   ,aa  "8a,   ,aa  88       88  88       88  "8a,   ,a8"  88  "8a,   ,a8"  "8a,   ,d88    `8b,d8\'   ',logo_print_speed)
    delay_print('     88     `"Ybbd8"\'   `"Ybbd8"\'  88       88  88       88   `"YbbdP"\'   88   `"YbbdP"\'    `"YbbdP"Y8      Y88\'    ',logo_print_speed)
    delay_print('                                                                                            aa,    ,88      d8\'     ',logo_print_speed)
    delay_print('                                                                                            "Y8bbdP"      d8\' ',logo_print_speed)

def weather_logo():
    print('\n')
    delay_print('I8,        8        ,8I                                   88 ',logo_print_speed)
    delay_print('`8b       d8b       d8\'                            ,d     88 ',logo_print_speed)
    delay_print(' "8,     ,8"8,     ,8"                             88     88 ',logo_print_speed)
    delay_print('  Y8     8P Y8     8P     ,adPPYba,  ,adPPYYba,  MM88MMM  88,dPPYba,    ,adPPYba,  8b,dPPYba, ',logo_print_speed)
    delay_print('  `8b   d8\' `8b   d8\'    a8P_____88  ""     `Y8    88     88P\'    "8a  a8P_____88  88P\'   "Y8 ',logo_print_speed)
    delay_print('   `8a a8\'   `8a a8\'     8PP"""""""  ,adPPPPP88    88     88       88  8PP"""""""  88  ',logo_print_speed)
    delay_print('    `8a8\'     `8a8\'      "8b,   ,aa  88,    ,88    88,    88       88  "8b,   ,aa  88 ',logo_print_speed)
    delay_print('     `8\'       `8\'        `"Ybbd8"\'  `"8bbdP"Y8    "Y888  88       88   `"Ybbd8"\'  88 ',logo_print_speed)


# Run Functions
def bbc_news():
    f = feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml?edition='+config.news_region) #BBC News Frontpage
    bbc_news_logo()
    for post in f.entries[:10]:
        print_rss(post)
        delay(1)
    delay(2)
    print('\n')

def bbc_technology_news():
    f = feedparser.parse('http://feeds.bbci.co.uk/news/technology/rss.xml?edition='+config.news_region) #BBC Technology News
    bbc_logo()
    technology_logo()
    for post in f.entries[:10]:
        print_rss(post)
        delay(1)
    delay(2)
    print('\n')

def bbc_weather():
    w = feedparser.parse('http://open.live.bbc.co.uk/weather/feeds/en/' + config.region_code + '/3dayforecast.rss') #BBC Weather 3 Day Forecast (Oxford)
    o = feedparser.parse('http://open.live.bbc.co.uk/weather/feeds/en/' + config.region_code + '/observations.rss') #BBC Weather Observations (Oxford)
    bbc_logo()
    weather_logo()
    print_weather(o,w)
    delay(2)
    print('\n')
