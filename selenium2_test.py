from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# ================= CONFIG =================
CHROME_PORTABLE_PATH = r"C:\Chrome_Sources\chrome-win64\chrome.exe"
CHROME_DRIVER_PATH = r"C:\Chrome_Sources\chromedriver-win64\chromedriver.exe"
URL = "https://www.saucedemo.com/"

EXPECTED_PRODUCTS = {
    "Sauce Labs Backpack": 29.99,
    "Sauce Labs Bike Light": 9.99,
    "Sauce Labs Bolt T-Shirt": 15.99,
    "Sauce Labs Fleece Jacket": 49.99,
    "Sauce Labs Onesie": 7.99,
    "Test.allTheThings() T-Shirt (Red)": 15.99
}

# ================= CHROME =================
options = Options()
options.binary_location = CHROME_PORTABLE_PATH
options.add_argument("--incognito")

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

try:
    # ================= 1. LOGIN =================
    driver.get(URL)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "inventory_container"))
    )
    print("[PASS] Connexion réussie")

    # ================= 2. VERIFIER PRODUITS =================
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    print(f"Produits trouvés: {len(products)}")

    found_products = []

    for product in products:
        name_elem = product.find_element(By.CLASS_NAME, "inventory_item_name")
        price_elem = product.find_element(By.CLASS_NAME, "inventory_item_price")
        img_elem = product.find_element(By.TAG_NAME, "img")
        btn_elem = product.find_element(By.TAG_NAME, "button")

        name = name_elem.text
        price = float(price_elem.text.replace("$", ""))

        if name in EXPECTED_PRODUCTS:
            found_products.append(name)

            assert img_elem.is_displayed(), f"Image non visible: {name}"
            assert btn_elem.text.lower() == "add to cart", f"Bouton incorrect: {name}"
            assert name_elem.is_displayed() and name_elem.is_enabled(), f"Nom non cliquable: {name}"
            assert price == EXPECTED_PRODUCTS[name], f"Prix incorrect: {name}"

            print(f"[PASS] {name}")

    assert len(found_products) == len(EXPECTED_PRODUCTS), \
        f"Produits manquants: {set(EXPECTED_PRODUCTS) - set(found_products)}"

    # ================= 3. CLIQUER SUR UN PRODUIT =================
    driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_details_name"))
    )

    detail_name = driver.find_element(By.CLASS_NAME, "inventory_details_name").text
    assert detail_name == "Sauce Labs Backpack", "Mauvais produit affiché"

    print("[PASS] Page détail correcte")

    # ================= 4. RETOUR AU CATALOGUE =================
    driver.find_element(By.ID, "back-to-products").click()

    # ================= 5. VERIFIER TOTAL PRODUITS =================
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) == 6, "Nombre total de produits incorrect"

    print("[PASS] Nombre total de produits = 6")

    print("\n🎉 TEST COMPLET RÉUSSI 🎉")

except AssertionError as e:
    print(f"[FAIL] {e}")

except Exception as e:
    print(f"[ERROR] {e}")

finally:
    time.sleep(2)
    driver.quit()
