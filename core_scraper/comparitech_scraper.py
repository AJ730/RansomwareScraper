import os
import shutil
from pathlib import Path
from browser_simulator.chrome_simulator.chrome_sim import ChromeSimulator
from logger import log
import pandas as pd

def scrape_comparitech():
    downloads_path = str(Path.home() / 'Downloads')

    if os.path.exists( 'comparitech/dataset.csv'):
        log.info("Succesfully scraped comparitech")
        return  pd.read_csv('./comparitech/dataset.csv')

    browser = ChromeSimulator()
    browser.get_browser()
    browser.accept_license()
    browser.accept_cookies()

    log.info(f"Downloading to path {downloads_path}")
    browser.search_by_query("https://datawrapper.dwcdn.net/gYM1o/104/dataset.csv")
    browser.halt(2)

    if not os.path.exists('comparitech'):
        os.makedirs('comparitech')


    shutil.move(downloads_path + '/dataset.csv', "./comparitech/")
    log.info("Scraping of comparitech succeeded")



    return pd.read_csv('./comparitech/dataset.csv')
