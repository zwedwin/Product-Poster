import xlwings
import json
import os
import time
import keyboard
import pyautogui
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import date


class McNulty():
    """
    Slightly modified web driver for the McNulty website. Simplified from WRAP Calculator version.
    Did not make child class as no UI to filter results from search. Material handling check function
    gave me some trouble, element attribute "value" doesnt actually display, had to put use key presses.
    Most likely a Lasso problem: website construction used Lasso framework, this makes it finicky.
    """

    def __init__(self, username, password, driver, window_handle):
        """
        Set driver instance. Switch primemover window.
        """
        self.driver = driver
        self.driver.switch_to.window(window_handle)
        self.driver.get('https://primemover.mcnulty.us/index.lasso')
        self.login(username, password)


    def type_text(self, string, web_element):
        """
        Helper function.
        Types out strings that for some webelements that wont play nice.
        """
        web_element.click()
        for char in string:
            if char.isupper():
                pyautogui.keyDown("shift")
                pyautogui.press(char)
                pyautogui.keyUp("shift")
            else:
                pyautogui.press(char)
        pyautogui.press('enter')


    def login(self, username, password):
        """
        Logs in user, throws error if you don't log in correctly.
        """
        self.username = username
        self.password = password
        self.driver.find_element_by_name("mcnulty_username").send_keys(self.username)
        self.driver.find_element_by_name("mcnulty_password").send_keys(self.password)
        self.driver.find_element_by_css_selector('body > div > div > form > button').click()
        time.sleep(1)
        if self.driver.current_url != 'https://primemover.mcnulty.us/main.lasso':
            raise ValueError("Invalid Username or Password")


    def search(self,CAGE, Type, City, State, DACIS, DUNS):
        """
        Searches for product and finds EXACT match with all fields. We aren't just scraping the product, we're editing it so we need an exact match.
        This assumes that no two products can have all the sames fields listed here.
        """
        self.driver.get('https://primemover.mcnulty.us/wraps/list.lasso')
        search_bar = self.driver.find_element_by_xpath('//*[@id="dataTable_wrapRateListing_filter"]/label/input')
        search_list = [CAGE, DACIS, DUNS]
        search_list_mod = [code for code in search_list if code.strip() != '']
        search_bar.send_keys(search_list_mod[0])
        i = 1
        while True:
            match = True
            try:
                #type of WRAP
                match = match and Type == self.driver.find_element_by_xpath('//*[@id="dataTable_wrapRateListing"]/tbody/tr['+ str(i) +']/td[4]').text
                #City
                # print(City)
                # match = match and City == self.driver.find_element_by_xpath('//*[@id="dataTable_wrapRateListing"]/tbody/tr['+ str(i) +']/td[6]').text
                #State
                # print(State)
                # match = match and State == self.driver.find_element_by_xpath('//*[@id="dataTable_wrapRateListing"]/tbody/tr['+ str(i) +']/td[7]').text
                #DACIS
                if not DACIS == "":
                    match = match and DACIS == self.driver.find_element_by_xpath('//*[@id="dataTable_wrapRateListing"]/tbody/tr['+ str(i) +']/td[8]').text
                #DUNS
                match = match and DUNS == self.driver.find_element_by_xpath('//*[@id="dataTable_wrapRateListing"]/tbody/tr['+ str(i) +']/td[10]').text
                if match:
                    product_element = self.driver.find_element_by_xpath('//*[@id="dataTable_wrapRateListing"]/tbody/tr['+str(i)+']/td[5]/a')
                    self.driver.get(product_element.get_attribute('href'))
                    return None
                i+=1
            except NoSuchElementException:
                raise ValueError("Can't find the Prime Mover product")


    def check_mat_handle(self,xl_percent):
        """
        Compares percentage on site and in excel doc. If not equal sets to Excel value.
        Something weird with DOM structure, changing the attribute "value" for the mat handling web element
        doesn't actually change the displayed value on the page. Tried sending keys and executing JS script,
        settled on manually typing. If user is typing while this is running may have complications.
        """
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[1]/a').click()
        time.sleep(0.5)
        mover_decimal_string = self.driver.find_element_by_xpath('//*[@id="companyData_materialHandelingRatePercent"]').get_attribute('value')[:-1]
        try:
            mover_decimal = float(mover_decimal_string)
        except ValueError:
            mover_decimal = 0.0
        xl_decimal = float(xl_percent)
        if xl_decimal == mover_decimal:
            return True
        else:
            xl_decimal_d = str(xl_decimal)
            element = self.driver.find_element_by_xpath('//*[@id="companyData_materialHandelingRatePercent"]')
            self.driver.execute_script('arguments[0].click();', element)
            self.driver.execute_script("arguments[0].value='"+ xl_decimal_d +"'", element)


    def get_city(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[1]/a').click()
        time.sleep(2)
        City = self.driver.find_element_by_xpath('//*[@id="companyData_city"]').get_attribute('value')
        return City


    def get_state(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[1]/a').click()
        time.sleep(2)
        State = self.driver.find_element_by_xpath('//*[@id="companyData_state"]').get_attribute('value')
        return State


    def set_4ColumnData(self, Date_Posted, Product_URL):
        """
        Set info on the 4 Column Data tab. Had to manually type some of these entries as the
        web elements kept throwing not ElementNotInteractableException's. This is an ugly one,
        but again runnign into some subtle, what I expect are Lasso related problems.
        """
        #navigate to eWRap Tab
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[6]/a').click()
        time.sleep(2)
        #select yes On eWRAP site
        self.driver.find_element_by_xpath('//*[@id="wrapData_eWrap_onSite"]').click()
        self.driver.find_element_by_xpath('//*[@id="wrapData_eWrap_onSite"]/option[2]').click()
        #date posted
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapData_eWrap_postedDate"]')))
        self.driver.find_element_by_xpath('//*[@id="wrapData_eWrap_postedDate"]').send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath('//*[@id="wrapData_eWrap_postedDate"]').send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath('//*[@id="wrapData_eWrap_postedDate"]').send_keys(Date_Posted)
        self.driver.find_element_by_xpath('//*[@id="wrapData_eWrap_postedDate"]').send_keys(Keys.TAB)
        #self.type_text(Date_Posted, self.driver.find_element_by_xpath('//*[@id="wrapData_eWrap_postedDate"]'))

        #Product_URL
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapData_eWrap_url"]')))
        self.driver.find_element_by_xpath('//*[@id="wrapData_eWrap_url"]').send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath('//*[@id="wrapData_eWrap_url"]').send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath('//*[@id="wrapData_eWrap_url"]').send_keys(Product_URL)
        #self.type_text(Product_URL, self.driver.find_element_by_xpath('//*[@id="wrapData_eWrap_url"]'))


    def get_Product_Name(self):
        """
        Gets product name from eWRap tab, will be needed for CC info set.
        """
        #navigate to eWRap Tab
        self.driver.execute_script("arguments[0].click();",self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[6]/a'))
        #self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[6]/a').click()
        #product name
        return self.driver.find_element_by_xpath('//*[@id="wrapData_eWrap_productName"]').get_attribute('value')


    def get_SKU(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[6]/a').click()
        time.sleep(2)
        SKU = self.driver.find_element_by_xpath('//*[@id="wrapData_eWrap_productCode"]').get_attribute('value')
        return SKU


    def get_Cost_Center(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[1]/a').click()
        time.sleep(0.5)
        return self.driver.find_element_by_xpath('//*[@id="companyData_costCenter"]').get_attribute('value')


    def find_select_product(self, CAGE,Type,City,State_Short,DACIS,DUNS,mat_hand):
        self.search(CAGE, Type, City, State_Short, DACIS, DUNS)
        self.check_mat_handle(mat_hand)


    def set_Product_Info(self, Product_URL):
        """
        Consolidates all neccessary post function calls to one place. Assumes product is always being posted today
        i.e. all other DACIS and CC calls are made at the same time.
        """
        date_today = date.today()
        date_string = date_today.strftime("%m/%d/%Y")
        self.set_4ColumnData(date_string, Product_URL)


    def post_WRAP(self):
        """
        This action is relatively irreversable so this is not part of set_Product_Info.
        Must be explicitly called by user once they are positive product info is correct.
        """
        self.driver.execute_script("arguments[0].click();",self.driver.find_element_by_xpath('//*[@id="formatTable"]/div[5]/div[1]/button'))
