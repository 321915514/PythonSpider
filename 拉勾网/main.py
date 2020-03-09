from selenium import webdriver
from lxml import etree
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class requesst_url():
    driver_path = r'E:\Program Files\chromedriver\chromedriver.exe'

    def __init__(self):
        self.driver = webdriver.Chrome(requesst_url.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.positions = []

    def run(self):
        self.driver.get(self.url)
        self.driver.find_element_by_xpath("//div[@class='body-btn']").click()
        while True:
            source = self.driver.page_source
            self.parse_page(source)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='pager_container']//span[last()]"))
            )
            next_btn = self.driver.find_element_by_xpath("//div[@class='pager_container']//span[last()]")
            if 'pager_next_disabled' in next_btn.get_attribute('class'):
                break
            else:
                next_btn.click()

    def parse_page(self, source):
        html = etree.HTML(source)
        detail_urls = html.xpath("//a[@class='position_link']/@href")
        for detail_url in detail_urls:
            self.driver.execute_script("window.open('%s')" % detail_url)
            self.driver.switch_to.window(self.driver.window_handles[1])
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='job-name']"))
            )
            source = self.driver.page_source
            self.parse_detail_page(source)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_detail_page(self, source):
        html = etree.HTML(source)
        position_name = html.xpath("//div[@class='job-name']/@title")[0]
        spans = html.xpath("//dd[@class='job_request']")[0]
        salary = spans.xpath(".//span[@class='salary']/text()")[0].strip()
        city = re.sub(r"[\s/]", '', spans.xpath(".//span/text()")[1]).strip()
        work_years = re.sub(r"[\s/]", '', spans.xpath(".//span/text()")[2]).strip()
        company_name = html.xpath("//div[@class='job_company_content']//em/text()")[0].strip()
        require = re.sub(r"[\s/]", '', spans.xpath(".//span/text()")[3]).strip()
        description = "".join(html.xpath("//div[@class='job-detail']//text()")).strip()
        position = {
            'position_name': position_name,
            'salary': salary,
            'city': city,
            'work_years': work_years,
            'company_name': company_name,
            'require': require,
            'description': description
        }
        self.positions.append(position)
        print(position)



def main():
    requesst_url().run()


if __name__ == '__main__':
    main()
