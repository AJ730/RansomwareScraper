from core_scraper.comparitech_scraper import scrape_comparitech
from colorama import Fore

if __name__ == '__main__':
    ds = scrape_comparitech()
    print(Fore.WHITE, ds.to_string())

