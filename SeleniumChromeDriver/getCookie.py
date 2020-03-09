
from selenium import webdriver

driver_path = r'E:\Program Files\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(driver_path)

driver.get('http://www.baidu.com')

for cookie in driver.get_cookies():
    print(cookie)

print(driver.get_cookie('PSTM'))

print(driver.delete_cookie('PSTM'))

print(driver.delete_all_cookies())
