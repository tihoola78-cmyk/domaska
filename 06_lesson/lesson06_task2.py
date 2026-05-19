from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Настройки для игнорирования предупреждений
options = Options()
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=options)

try:
    # Открываем страницу
    driver.get("http://uitestingplayground.com/textinput")

    # Находим поле ввода
    input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
    input_field.send_keys("SkyPro")

    # Находим и нажимаем синюю кнопку
    button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
    button.click()

    # Ожидаем, пока текст кнопки изменится на "SkyPro"
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#updatingButton"), "SkyPro"
        )
    )

    # Получаем текст кнопки и выводим в консоль
    new_button_text = button.text
    print(new_button_text)

finally:
    driver.quit()
