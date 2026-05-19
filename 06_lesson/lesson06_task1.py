from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Настройки для игнорирования предупреждений
options = Options()
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=options)

try:
    # Открываем страницу
    driver.get("http://uitestingplayground.com/ajax")

    # Находим и нажимаем синюю кнопку
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#ajaxButton"))
    )
    button.click()

    # Ожидаем появления зеленой плашки с текстом
    # (AJAX-запрос занимает около 15 секунд)
    success_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".bg-success")
        )
    )

    # Получаем текст из зеленой плашки
    text = success_message.text
    print(text)

    # Небольшая задержка, чтобы увидеть результат
    time.sleep(2)

finally:
    driver.quit()
