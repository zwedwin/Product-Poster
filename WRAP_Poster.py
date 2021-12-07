import xlwings
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class CoreCommerce(username,password):

    def __init__(self):
        options = Options()
        #change after Development
        options.headless = False
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}
        self.driver = webdriver.Chrome(options = options, desired_capabilities = caps)
        self.driver.get('https://mcnulty.corecommerce.com/admin/')
        self.driver.find_element_by_name('userId').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="admin-login-box-middle"]/form/div[2]/input').click()
        self.driver.get('https://mcnulty.corecommerce.com/admin/index.php?m=products_browse&sort=0')
        self.driver.find_element_by_xpath('//*[@id="adminFormMain"]/div/div/div[2]/div/div/div/div').click()

    def search_categories(self,Division,Company_Name):
        self.driver.get('https://mcnulty.corecommerce.com/admin/index.php?m=category_browse&sort=0&asc=asc&page=1')
        pg = 2
        while True:
            for row in self.driver.find_elements_by_xpath('//a[@class="email-link"]'):
                if Division in row.text:
                    return True
            try:
                self.driver.find_element_by_xpath('//a[@aria-label="Page ' + str(pg) + '"]').click()
            except NoSuchElementException:
                return False
            pg += 1

    def select_category(self,Division,Company_Name):
        self.driver.get('https://mcnulty.corecommerce.com/admin/index.php?m=add_product&back=1')
        self.driver.find_element_by_xpath('//*[@id="informationSection"]/div[14]/div[1]/div/div[1]/a').click()
        time.sleep(0.5)
        pg = 2
        while True:
            time.sleep(0.5)
            for row in self.driver.find_elements_by_xpath('//td[contains(@id,"objectName")]/label'):
                if Division in row.text:
                    row.click()
                    self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/div[1]/a/i').click()
                    return None
            try:
                self.driver.find_elements_by_xpath('//a[@aria-label="Page ' + str(pg) + '"]')[0].click()
            except NoSuchElementException:
                raise CustomError("Can't find the category to set :/")
            pg += 1

    def add_category(self,Division,Company_Name):
        self.driver.get('https://mcnulty.corecommerce.com/admin/index.php?m=add_category')
        self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div/div[1]/div[1]/div/input').send_keys(Division)
        self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div/div[3]/div/div/div/div[1]/a').click()
        time.sleep(0.5)
        pg = 2
        while True:
            time.sleep(0.5)
            for row in self.driver.find_elements_by_xpath('//td[contains(@id,"objectName")]/label'):
                if Company_Name in row.text:
                    row.click()
                    self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/div[1]/a/i').click()
                    self.driver.find_element_by_xpath('//*[@id="controls"]/div/div[1]/div/div[2]/div/a[1]').click()
                    return None
            try:
                self.driver.find_element_by_xpath('//a[@aria-label="Page ' + str(pg) + '"]').click()
            except NoSuchElementException:
                if bool((ord(Company_Name.strip()[0].upper()) - 64) % 2):
                    alph_cat = Company_Name.strip()[0].upper() + '-' + chr(ord(Company_Name.strip()[0]) + 1).upper()
                else:
                    alph_cat = chr(ord(Company_Name.strip()[0]) - 1).upper() + '-' + Company_Name.strip()[0].upper()
                self.add_category(Company_Name,alph_cat)
                self.driver.get('https://mcnulty.corecommerce.com/admin/index.php?m=add_category')
                self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div/div[1]/div[1]/div/input').send_keys(Division)
                self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div/div[3]/div/div/div/div[1]/a').click()
                time.sleep(0.5)
                pg = 1
            pg += 1

    def set_category(self,Division,Company_Name):
        if(self.search_categories(Division,Company_Name)):
                self.select_category(Division,Company_Name)
        else:
            self.add_category(Division,Company_Name)
            self.select_category(Division,Company_Name)

    def set_Information(self,Product_Name,SKU,Price,MSRP,Sale_Price):
        self.driver.find_element_by_xpath('//*[@id="informationSection"]/div[1]/div[1]/div/input').send_keys(Product_Name)
        self.driver.find_element_by_xpath('//*[@id="informationSection"]/div[1]/div[2]/div/input').send_keys(SKU)
        self.driver.find_element_by_xpath('//*[@id="informationSection"]/div[7]/div/div/div[1]/input').send_keys(Price)
        self.driver.find_element_by_xpath('//*[@id="informationSection"]/div[8]/div[1]/div/input').send_keys(MSRP)
        self.driver.find_element_by_xpath('//*[@id="informationSection"]/div[9]/div[2]/div/input').send_keys(Sale_Price)

    def set_Description(self,Company_Name,Division,Cost_Center,Address_1,Address_2,DACIS,CAGE,DUNS,WRAP_Type):
        self.driver.get('https://mcnulty.corecommerce.com/admin/index.php?m=add_product&back=1')
        self.driver.find_element_by_xpath('//*[@id="headingTwo"]/h4/a').click()
        format_string = 'Wrap Rate Analysis (xlsx file download)\n\nCompany:\nDivision:\n\nCost Center:\nCostCenter\nAddress_1\nAddress_2\n\nDACIS Code:\nCAGE:\nDUNS:\nNature of Work:'
        WebDriverWait(self.driver, 1).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="cke_2_contents"]/iframe')))
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body'))).send_keys(format_string)
        self.driver.drag_and_drop(find_element_by_xpath('/html/body/p[1]/text()'),find_element_by_xpath('/html/body/p[2]'))
        self.driver.
        # start of drag'/html/body/p[1]'
        # end of drag
        self.driver.switch_to.default_content()

    def set_Data(self,Product_Name,SKU,Price,MSRP,Sale_Price,Division,Company_Name):
        self.driver.get('https://mcnulty.corecommerce.com/admin/index.php?m=add_product&back=1')
        self.set_category(Division,Company_Name)
        self.set_Information(self,Product_Name,SKU,Price,MSRP,Sale_Price)

if __name__ == '__main__':
    #cc = CoreCommerce() login info propreitary :)
    #cc.set_Data('TEST PRODUCT','00000','3909','00000','00000','TEST DIVISION','TEST COMPANY')
    cc.set_Description('TEST COMPANY','TEST DIVISION', 'TEST COST CENTER', 'ADDRESS 1', 'ADDRESS 2', 'TEST DACIS', 'CAGE', 'TEST DUNS', 'TEST TYPE')
