from selenium import webdriver
import time, math

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    first_btn = browser.find_element_by_tag_name("button")
    first_btn.click()
    
    
    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    textBr = browser.find_element_by_id("answer")
    textBr.send_keys(y)
    btn = browser.find_element_by_tag_name("button")
    btn.click()

finally:
    time.sleep(20)
    browser.quit()