
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# driver.implicitly_wait(driver_path = r'E:\Program Files\chromedriver\chromedriver.exe'
#
# driver = webdriver.Chrome(driver_path)
# driver.get('http://www.douban.com')5)  # 隐式等待

WebDriverWait(driver, 10).until(  # 显示等待 当元素出现就返回
    EC.presence_of_element_located((By.ID, 'anony-group'))
)
# driver.find_element_by_name('weweweew')




