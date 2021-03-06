import pandas as pd
import time
import pyfiglet
from fx_scraper_template import *


def main(total_pages_to_scrape: int) -> None:
    """
    Takes total number of pages to be scraped as an input and leverages the functions defined in scraper template file
    to scrape and add all the items to 'all_beers' list.
    Args:
        total_pages_to_scrape (int): It is the total number of pages to be scraped
    Returns:
        None: This function runs through each page and adds the content to the 'all_beers' list
    """
    for pgno in range(1, total_pages_to_scrape + 1):
        url_constant = 'https://www.beerwulf.com/en-GB/api/search/searchProducts?catalogCode=Beer_1&routeQuery'
        url = f'{url_constant}=all-beers&page={pgno}'

        print('\n')
        print(f'Scraping Page: {pgno}')
        print(f'Scraping Page URL: {url}')

        content = extract_content(url)
        scrape_content(content)
        
        print(f'Total Beers Grabbed: {len(all_beers)}')
        print(f'Page-{pgno} Scraped...')
        print(f'Remaining pages to scrape: {total_pages_to_scrape - pgno}')
        time.sleep(3)


def load_data() -> None:
    """
    This function loads the scraped data into a CSV file
    """
    
    beers_df = pd.DataFrame(all_beers)
    beers_df.to_csv('scraped_data.csv', encoding='utf-8', index=False)
    return


if __name__ == '__main__':
    
    total_pages = 3

    scraper_title = "BEERWULF BEERS GRABBER"
    ascii_art_title = pyfiglet.figlet_format(scraper_title, font='small')
    
    start_time = datetime.now()

    print('\n\n')
    print(ascii_art_title)
    print('Grabbing Beers...')
    print(f'Total Pages to scrape: {total_pages}')
    
    main(total_pages)
    
    end_time = datetime.now()
    scraping_time = end_time - start_time

    print('\n')
    print('All Beers Grabbed...')
    print(f'Time spent on scraping: {scraping_time}')
    print(f'Total beers grabbed: {len(all_beers)}')
    print('\n')
    print('Loading data into CSV...')
    
    load_data()
    
    print('Data Exported to CSV...')
    print('Webscraping Completed !!!')
