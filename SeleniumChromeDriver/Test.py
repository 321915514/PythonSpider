
from selenium import webdriver
#  行为链
from selenium.webdriver.common.action_chains import ActionChains
driver_path = r'E:\Program Files\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('http://www.baidu.com')
actions = ActionChains(driver)
inputTag = driver.find_element_by_name('wd')
submit = driver.find_element_by_id('su')
actions.move_to_element(inputTag)
actions.send_keys_to_element(inputTag, 'python')
actions.move_to_element(submit)
actions.click(submit)
actions.perform()

