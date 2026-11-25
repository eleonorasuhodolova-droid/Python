from selenium import webdriver
from selenium.webdriver.common.by import By

def test_navigation():
    driver = webdriver.Chrome()

    # Открываем страницу
    driver.get("https://httpbin.qa-territory.online")

    # Сохраняем исходный URL для последующей проверки
    initial_url = driver.current_url

    # Находим и кликаем на ссылку с текстом "HTML Form"
    html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
    html_form_link.click()

    # Проверяем, что URL изменился на /forms/post
    # Для проверки используем утверждение (assert), чтобы тест провалился при несоответствии
    assert "/forms/post" in driver.current_url, f"Ожидался URL с /forms/post, но получен: {driver.current_url}"

    # Возвращаемся назад на главную страницу
    driver.back()

    # Проверяем, что вернулись на исходный URL
    assert driver.current_url == initial_url, f"Ожидался исходный URL {initial_url}, но получен: {driver.current_url}"

    driver.quit()
