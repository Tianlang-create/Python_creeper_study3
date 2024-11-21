
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.santostang.com/2018/07/04/hello-world/")
iframe = driver.find_element(By.XPATH, "//iframe[@title='livere']")
driver.switch_to.frame(iframe)
comment = driver.find_element_by_css_selector('div.reply-content')
content = comment.find_element_by_tag_name('p')
print (content.text)