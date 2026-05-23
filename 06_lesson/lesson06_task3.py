from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=options)

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

    # Ждём появления всех картинок с атрибутом src
    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.XPATH, "//img[@src]"))
    )

    # Находим все картинки с src
    images = driver.find_elements(By.XPATH, "//img[@src]")

    # Берём третью картинку (индекс 2)
    if len(images) >= 3:
        third_image_src = images[2].get_attribute("src")
        print(third_image_src)

finally:
    driver.quit()
