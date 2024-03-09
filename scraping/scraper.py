from scraping.utils import get_details, get_amount_of_pages, get_links
from database import operations
import time

def scrape_otodom_apartments_listings(connection, city_link):
    amount_of_pages = get_amount_of_pages(city_link)
    for page in range(1, amount_of_pages + 1):
        links = get_links(page, city_link)
        for url in links:
            try:
                details = get_details(url, city_link)
                if details and not operations.listing_exists(connection, details['url']):
                    operations.insert_listing(connection, details)
                    print("Inserted: ", details)
            except Exception as e:
                raise e
            time.sleep(1)