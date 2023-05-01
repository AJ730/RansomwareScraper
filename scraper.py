from core_scraper.comparitech_scraper import scrape_comparitech
from colorama import Fore, Style

from core_scraper.cyberattack_scraper import scrape_cyberattack

if __name__ == '__main__':
    ds_1 = scrape_comparitech()
    df_2 = scrape_cyberattack()

    print( ds_1.to_string())
    print( df_2.to_string())


