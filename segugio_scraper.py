import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def get_a2a_click_luce_position():
    url = "https://tariffe.segugio.it/costo-energia-elettrica/ricerca-offerte-energia-elettrica.aspx"

    # Configura il browser in modalità headless
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(2)

        # Seleziona il tab "Oppure calcola il consumo"
        tab = driver.find_element(By.ID, "contentForm_calcolaConsumoLink")
        tab.click()
        time.sleep(1)

        # Inserisci il consumo annuo
        consumo_input = driver.find_element(By.ID, "contentForm_txtConsumoAnn")
        consumo_input.clear()
        consumo_input.send_keys("2000")

        # Seleziona "Prezzo Fisso" dal dropdown
        tipo_select = driver.find_element(By.ID, "contentForm_ddlTipologia")
        for option in tipo_select.find_elements(By.TAG_NAME, "option"):
            if "Prezzo Fisso" in option.text:
                option.click()
                break

        # Clicca su "Mostra le offerte"
        show_button = driver.find_element(By.ID, "contentForm_btnMostraOfferte")
        show_button.click()
        time.sleep(5)

        # Estrai le offerte
        offerte = driver.find_elements(By.CSS_SELECTOR, ".offerta-row")  # Aggiorna il selettore secondo la struttura reale
        for index, offerta in enumerate(offerte, start=1):
            nome_offerta = offerta.find_element(By.CSS_SELECTOR, ".offerta-nome").text
            if "A2A Click Luce" in nome_offerta:
                return index

        return None

    finally:
        driver.quit()

if __name__ == "__main__":
    posizione = get_a2a_click_luce_position()
    if posizione:
        print(f"A2A Click Luce si trova al {posizione}° posto nel ranking.")
    else:
        print("A2A Click Luce non è presente tra le offerte.")
