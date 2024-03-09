import requests
from bs4 import BeautifulSoup
import re


URL = 'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def extract_price_and_currency(text):
    if text is None:
        return None, None

    if "Zapytaj" in text:
        return None, None

    price_patterns = [
        r'(\d+(?:\.\d+)?)(?:\s*(?:zł|PLN))?',
        r'(\d+(?:\.\d+)?)(?:\s*(?:EUR|€))?',
    ]

    for pattern in price_patterns:
        match = re.search(pattern, text)
        if match:
            price = match.group(1)
            currency = "PLN" if "zł" in match.group() else "EUR" if "EUR" in match.group() else None
            return price, currency

def get_details(url, city_link):
    res = requests.get('https://www.otodom.pl'+url, headers=HEADERS)
    soup = BeautifulSoup(res.content, "html.parser")

    price_element = soup.find('strong', attrs={"data-cy": "adPageHeaderPrice"})
    price_text = price_element.get_text().replace(" ", "") if price_element else None
    price, price_currency = extract_price_and_currency(price_text)
    
    square_footage_element = soup.find('div', attrs={"data-testid": "table-value-area"})
    square_footage = square_footage_element.get_text().split(" ")[0].replace(',','.') if square_footage_element else None

    building_ownership_element = soup.find('div', attrs={"data-testid": "table-value-building_ownership"})
    building_ownership = building_ownership_element.get_text() if building_ownership_element else None

    number_of_rooms_element = soup.find('div', attrs={"data-testid": "table-value-rooms_num"})
    number_of_rooms_text = number_of_rooms_element.get_text().split(" ")[0] if number_of_rooms_element else None

    if number_of_rooms_text and number_of_rooms_text.isdigit():
        number_of_rooms = number_of_rooms_text
    else:
        number_of_rooms = None

    construction_status_element = soup.find('div', attrs={"data-testid": "table-value-construction_status"})
    construction_status = construction_status_element.get_text() if construction_status_element else None
   
    floor_element = soup.find('div', attrs={"data-testid": "table-value-floor"})
    floor = floor_element.get_text() if floor_element else None

    rent_element = soup.find('div', attrs={"data-testid": "table-value-rent"})
    rent_text = rent_element.get_text().replace(" ", "") if rent_element else None
    rent, rent_currency = extract_price_and_currency(rent_text)

    parking_element = soup.find('div', attrs={"data-testid": "table-value-car"})
    parking = parking_element.get_text() if parking_element else None

    heating_element = soup.find('div', attrs={"data-testid": "table-value-heating"})
    heating = heating_element.get_text() if heating_element else None

    city = city_link.rsplit('/', 1)[-1]

    return {"url": url.split('/pl/oferta/')[1], "price" : price, "price_currency": price_currency,"square_footage": square_footage,"building_ownership": building_ownership,"number_of_rooms": number_of_rooms, "construction_status": construction_status, "floor": floor, "rent": rent, "rent_currency": rent_currency, "parking": parking, "heating": heating, "city": city}


def get_amount_of_pages(city_link):
    response = requests.get(URL+city_link, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    last_page_elements = soup.find_all('li', class_='css-1tospdx')

    if last_page_elements:
        last_page = last_page_elements[-1].text.strip()
        return int(last_page) if last_page.isdigit() else 1
    else:
        raise Exception("No elements found with the specified class name")

def get_links(page, city_link):
    response = requests.get(URL+city_link+'?page='+str(page), headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    links = soup.find_all('a', class_='css-16vl3c1 e1njvixn0')
    unique_urls = set(i['href'] for i in links)
    return unique_urls

