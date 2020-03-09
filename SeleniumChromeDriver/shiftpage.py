from selenium import webdriver

driver_path = r'E:\Program Files\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(driver_path)

driver.get('http://www.baidu.com')

driver.execute_script("window.open('http://www.douban.com')")
driver.switch_to.window(driver.window_handles[1])  # driver.window_handles[1] 页面句柄
# switch_to.window 跳转页面
print(driver.current_url)
