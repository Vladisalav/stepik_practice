import time
from selenium.webdriver.common.by import By

def test_element_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(20)
    button = len(browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button"))
    assert button > 0, '!!!ЭЛЕМЕНТ НЕ НАЙДЕН!!!'

#pytest -s -v --language=fr --browser_name=chrome test_items.py