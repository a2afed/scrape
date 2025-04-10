from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def get_offer_rank(url, brand_name):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(5)  # tempo per caricare completamente la pagina

        # Cerca le offerte
        offer_boxes = driver.find_elements(By.CLASS_NAME, "offerta-energy-box")

        for index, box in enumerate(offer_boxes):
            if brand_name.lower() in box.text.lower():
                driver.quit()
                return index + 1  # posizione trovata

        driver.quit()
        return -1  # brand non trovato
    except Exception as e:
        print(f"Errore durante lo scraping con Selenium: {e}")
        driver.quit()
        return -1

