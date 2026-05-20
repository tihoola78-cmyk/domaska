import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_form_submission(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    # Заполнение формы
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Нажать Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Ждём появления заголовка "Data types"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[text()='Data types']"))
    )

    # Получаем весь текст страницы
    page_text = driver.find_element(By.TAG_NAME, "body").text

    # Проверки через текст
    assert "Иван" in page_text
    assert "Петров" in page_text
    assert "test@skypro.com" in page_text
    assert "Ленина, 55-3" in page_text
    assert "Москва" in page_text
    assert "Россия" in page_text
    assert "QA" in page_text
    assert "SkyPro" in page_text
    assert "Zip code" in page_text
    assert "N/A" in page_text
