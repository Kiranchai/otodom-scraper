from config.settings import DATABASE
import logging
from database.DatabaseManager import DatabaseManager
from scraping import scraper
import helpers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    db_manager = DatabaseManager(**DATABASE)
    
    try:
        db_manager.connect()

        helpers.display_menu()
        city = helpers.get_city_choice()
        scraper.scrape_otodom_apartments_listings(connection=db_manager.connection, city_link=city)

    except Exception as e:
        logger.error(f"Error in main script: {e}")
    finally:
        db_manager.disconnect()
