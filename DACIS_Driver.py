import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class DACIS:
    """
    Driver for DACIS website. Similar to CC and PM driver: posts relevant info.
    Much simpler than the CC driver, website is much more static.
    """

    def __init__(self,username,password,driver,window_handle):
        """Log in. Go to listing page."""
        self.driver = driver
        self.driver.switch_to.window(window_handle)
        self.driver.get('https://ci-partners.dacis.com/index.lasso')
        self.driver.find_element_by_name('ci_username').send_keys(username)
        self.driver.find_element_by_name('ci_password').send_keys(password)
        self.driver.find_element_by_xpath('/html/body/div/div/form/button').click()
        self.driver.get('https://ci-partners.dacis.com/wrap_rate_listing.lasso')
        time.sleep(2)
        if self.driver.current_url != 'https://ci-partners.dacis.com/wrap_rate_listing.lasso':
            raise ValueError('Wrong DACIS username or password.')


    def edit_product(self, product_Name, CAGE_Code, DACIS_Company_Code, DUNS, URL, city, state):
        self.driver.find_element_by_xpath('//*[@id="productName"]').clear()
        self.driver.find_element_by_xpath('//*[@id="cageCode"]').clear()
        self.driver.find_element_by_xpath('//*[@id="dacisCompanyCode"]').clear()
        self.driver.find_element_by_xpath('//*[@id="url"]').clear()
        self.driver.find_element_by_xpath('//*[@id="city"]').clear()
        self.driver.find_element_by_xpath('//*[@id="state"]').clear()
        self.driver.find_element_by_xpath('//*[@id="dunsNumber"]').clear()
        self.driver.find_element_by_xpath('//*[@id="productName"]').send_keys(product_Name)
        self.driver.find_element_by_xpath('//*[@id="cageCode"]').send_keys(CAGE_Code)
        self.driver.find_element_by_xpath('//*[@id="dacisCompanyCode"]').send_keys(DACIS_Company_Code)
        self.driver.find_element_by_xpath('//*[@id="url"]').send_keys(URL)
        self.driver.find_element_by_xpath('//*[@id="city"]').send_keys(city)
        self.driver.find_element_by_xpath('//*[@id="state"]').send_keys(state)
        self.driver.find_element_by_xpath('//*[@id="dunsNumber"]').send_keys(DUNS)
        #save the product
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/div[2]/form/div[37]/button').click()


    def search(self, CAGE, DACIS_Company_Code, product_Name):
        if DACIS_Company_Code == "":
            search_term = CAGE
        else:
            search_term = DACIS_Company_Code
        self.driver.find_element_by_xpath('//*[@id="dataTable_wrapRates_filter"]/label/input').click()
        self.driver.find_element_by_xpath('//*[@id="dataTable_wrapRates_filter"]/label/input').send_keys(search_term)
        try:
            dacis_code_elements = self.driver.find_elements_by_xpath('//tr[contains(@role,"row")]/td[5]')
            cage_code_elements = self.driver.find_elements_by_xpath('//tr[contains(@role,"row")]/td[6]')
            product_name_elements = self.driver.find_elements_by_xpath('//tr[contains(@role,"row")]/td[2]')
            dacis_cage_name_elements = zip(dacis_code_elements, cage_code_elements, product_name_elements)
            row_counter = 1
            for dacis, cage, name in dacis_cage_name_elements:
                if (dacis.text.strip() == DACIS_Company_Code.strip()) and (cage.text.strip() == CAGE.strip()) and (name.text.strip() == product_Name.strip()):
                    self.product_url = self.driver.find_element_by_xpath('//*[@id="dataTable_wrapRates"]/tbody/tr['+str(row_counter)+']/td[1]/a').get_attribute('href')
                    self.driver.get(self.product_url)
                    return True
                row_counter += 1
            return False
        except NoSuchElementException:
            return False


    def make_product(self,product_Name, CAGE_Code, DACIS_Company_Code, DUNS, URL, city, state):
        if self.search(CAGE_Code, DACIS_Company_Code, product_Name):
            self.edit_product(product_Name, CAGE_Code, DACIS_Company_Code, DUNS, URL, city, state)
        else:
            self.driver.find_element_by_xpath('/html/body/div/div/div/div/div/nav/section/ul[2]/li[2]/a').click()
            self.edit_product(product_Name, CAGE_Code, DACIS_Company_Code, DUNS, URL, city, state)
        self.driver.get('https://ci-partners.dacis.com/wrap_rate_listing.lasso')
