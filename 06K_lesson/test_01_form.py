import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Edge(options=options)
    yield driver
    driver.quit()


def test_form_validation(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    # Заполнение формы
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # Zip code оставляем пустым
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Нажать Submit
    driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    ).click()

    # Ждём появления результатов валидации
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
    )

    # Проверка: поле Zip code должно быть красным (alert-danger)
    zip_code_alert = driver.find_element(By.ID, "zip-code")
    zip_classes = zip_code_alert.get_attribute("class")
    assert "alert-danger" in zip_classes, "Zip code не подсвечен красным"

    # Проверка остальных полей (должны быть зелёными - alert-success)
    green_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in green_fields:
        field_alert = driver.find_element(By.ID, field_id)
        field_classes = field_alert.get_attribute("class")
        assert "alert-success" in field_classes, \
            f"Поле {field_id} не подсвечено зелёным"
