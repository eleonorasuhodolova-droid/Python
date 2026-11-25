from selenium import webdriver
from selenium.webdriver.common.by import By

def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    # Находим все ссылки на странице
    links = driver.find_elements(By.TAG_NAME, "a")

    # Проверяем, что количество ссылок равно 9
    assert len(links) == 9, f"Ожидалось 9 ссылок, но найдено {len(links)}"

    # Проверяем, что все ссылки отображаются на странице
    for index, link in enumerate(links):
        assert link.is_displayed(), f"Ссылка под номером {index} не отображается на странице"

    # Проверяем, что текст первой ссылки содержит "1"
    first_link_text = links[0].text
    assert "1" in first_link_text, f"Текст первой ссылки '{first_link_text}' не содержит '1'"

    driver.quit()
