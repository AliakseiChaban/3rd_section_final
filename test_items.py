import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket(browser):

    browser.get(link)
    btn_add_to_basket = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert btn_add_to_basket, "The 'Add to basket' button isn't found"

    time.sleep(30)
