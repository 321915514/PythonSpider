from selenium import webdriver
driver_path = r'E:\Program Files\chromedriver\chromedriver.exe'
options = webdriver.ChromeOptions()  # 代理
options.add_argument('--proxy-server=http://119.57.108.65:53281')
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

driver.get('http://httpbin.org/ip')

