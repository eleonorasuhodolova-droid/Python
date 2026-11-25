from selenium import webdriver
from selenium.webdriver.common.by import By

def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    # Находим поле ввода с именем custname и вводим имя
    name_input = driver.find_element(By.NAME, "custname")
    name_input.send_keys("ВашеИмя")  # Замените "ВашеИмя" на реальное имя

    # Находим кнопку Submit по тексту и нажимаем на неё
    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()

    # Проверяем, что URL изменился после отправки формы
    current_url = driver.current_url
    assert current_url != "https://httpbin.qa-territory.online/forms/post", "URL не изменился после отправки формы"

    driver.quit()
