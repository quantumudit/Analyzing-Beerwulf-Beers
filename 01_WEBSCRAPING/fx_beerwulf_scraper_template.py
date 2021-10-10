import requests
from urllib.parse import urljoin

ROOT_URL = 'https://www.beerwulf.com'
SESSION = requests.Session()

HEADERS = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0",
    "accept-language": "en-US"
}

all_beers = []

def extract_content(url: str):
    """
    This function takes the internal API URL and returns only the relevant portion from the JSON content
    Args:
        url (str): The internal API URL string
    Returns:
        The JSON content only having the required product information
    """
    
    response = SESSION.get(url, headers=HEADERS)
    json_data = response.json()
    return json_data['items']


def scrape_content(content: str) -> None:
    """
    This function takes the JSON content from 'extract_content()' function, scrapes the required fields and add then to the 'all_beers' list.
    Args:
        content (str): This is the JSON content extracted from 'extract_content()' function
    Returns:
        This function doesn't return anything but adds the data to the global list variable
    """
    
    for beer in content:
        title = beer['title']
        item_link = urljoin(ROOT_URL, beer['contentReference'])
        image_link =  urljoin(ROOT_URL, beer['images'][0]['image'])
        style = beer['style']
        alcohol_percentage = beer['alcoholPercentage']
        volume_cl = beer['volume']
        in_stock = beer['inStock']
        price_pounds = beer['displayInformationPrice']['filterPrice']
        container_type = beer['containerType']
        
        beer_details = {
            'title': title,
            'style': style,
            'alcohol_percentage': alcohol_percentage,
            'volume_centiliter': volume_cl,
            'container_type': container_type,
            'in_stock_status': in_stock,
            'price_pounds': price_pounds,
            'beer_image_url': image_link,
            'beer_details_url': item_link
        }
        
        all_beers.append(beer_details)
    return

# Testing the scraper template #
# ---------------------------- #

if __name__ == '__main__':
    URL = 'https://www.beerwulf.com/en-GB/api/search/searchProducts?catalogCode=Beer_1&routeQuery=all-beers&page=1'
    
    content = extract_content(URL)
    scrape_content(content)
    
    print(f'Total Items Scraped: {len(all_beers)}')
    print('\n')
    print(all_beers)