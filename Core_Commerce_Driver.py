import time
import keyboard
from datetime import date
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class CoreCommerce():
    """
    This is a class that instantiates a chrome webdriver instance for one of our company websites.
    It leverages this instance to post information on the company page.
    I have tried and failed to remove the time.sleep() lines, the website is very dynamic and this leads to
    many hard to eliminate StaleElementReferenceException's. From what I understand AJAX protocols may be to blame
    but its hard to know. Remove these waits at your own peril.
    """

    def __init__(self,username,password,driver,window_handle):
        """Log in. Go to listing page. """
        self.driver = driver
        self.driver.switch_to.window(window_handle)
        self.driver.get('https://mcnulty.corecommerce.com/admin/')
        self.driver.find_element_by_name('userId').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="admin-login-box-middle"]/form/div[2]/input').click()
        self.driver.get('https://mcnulty.corecommerce.com/admin/index.php?m=products_browse&sort=0')


    def check_for_product(self,SKU):
        """
        Check if product exists by searching SKU. If T select product, else copy last product.
        Note that this function runs under the assumption that SKU is unique.
        """
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="inputSearch"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="inputSearch"]').send_keys(SKU)
        time.sleep(1)
        keyboard.press_and_release('enter')
        time.sleep(1)
        try:
            #Look for "no products found" alert
            self.driver.find_element_by_xpath('//*[@id="adminFormMain"]/div/div/div[2]/div/form/div[2]/div/div')
            #if no products found then go to the end of the list and copy the last product
            self.copy_last_product()
        except NoSuchElementException:
            #if not found this means there is an element with this SKU, use that element, list just incase partial match, not sure how CC search works
            url = self.driver.find_elements_by_xpath('//a[contains(@href,"index.php?m=edit_product")]')[0].get_attribute('href')
            self.driver.get(url)
            self.product_info_url = self.driver.current_url


    def search_categories(self,Division,Company_Name):
        """ Search categories in large list (not in product page), return bool."""
        self.driver.get('https://mcnulty.corecommerce.com/admin/index.php?m=category_browse&sort=0&asc=asc&page=1')
        pg = 2
        while True:
            time.sleep(0.5)
            for row in self.driver.find_elements_by_xpath('//a[@class="email-link"]'):
                if Division in row.text:
                    return True
            try:
                self.driver.find_element_by_xpath('//a[@aria-label="Page ' + str(pg) + '"]').click()
            except NoSuchElementException:
                return False
            pg += 1


    def select_category(self,Division,Company_Name):
        """ Select category withtin product page. """
        self.driver.get(self.product_info_url)
        #go to category pop up, page needs to load properly sometimes the xpath below is linked to another element
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="informationSection"]/div[14]/div[1]/div/div[1]/a').click()
        pg = 2
        while True:
            time.sleep(0.5)
            for row in self.driver.find_elements_by_xpath('//td[contains(@id,"objectName")]/label'):
                if Division in row.text:
                    row.click()
                    self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/div[1]/a/i').click()
                    return None
            try:
                time.sleep(0.5)
                self.driver.find_elements_by_xpath('//a[@aria-label="Page ' + str(pg) + '"]')[0].click()
            except NoSuchElementException:
                raise CustomError("Can't find the category to set :/")
            pg += 1


    def add_category(self,Division,Company_Name):
        """ Add category. Calls itself to create parent category. """
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
        """ Look for category, if exists select it, else add and select. """
        if(self.search_categories(Division,Company_Name)):
            self.select_category(Division,Company_Name)
        else:
            self.add_category(Division,Company_Name)
            self.select_category(Division,Company_Name)


    def set_Information(self,Product_Name,SKU):
        """ Clear all input in Info tab, set information. """
        time.sleep(1)
        product_name_html = '<input class="form-control" type="text" name="pName[1]" value=' + '"' + Product_Name + '"' + '>'
        sku_html = '<input class="form-control" type="text" name="pNum" maxlength="60" value='+ '"' + SKU + '"' +'>'
        Product_name_location = self.driver.find_element_by_xpath('//*[@id="informationSection"]/div[1]/div[1]/div/input')
        SKU_name_location = self.driver.find_elements_by_xpath('//*[@id="informationSection"]/div[1]/div[2]/div/input')
        self.driver.execute_script("arguments[0].innerHTML = arguments[1]", Product_name_location, product_name_html)
        self.driver.execute_script("arguments[0].innerHTML = arguments[1]", SKU_name_location, sku_html)

    def copy_last_product(self):
        """ Copy the last product. Assumes that if there is a last page there must be a product on that page """
        #click to the end of product list
        self.driver.find_element_by_xpath('//*[@id="adminFormMain"]/div/div/div[64]/div/div[2]/nav/ul/a[11]').click()
        #click the first one
        self.driver.get(self.driver.find_elements_by_xpath('//a[contains(@href,"index.php?m=edit")]')[0].get_attribute('href'))
        #easier to execute javascript here than try to click the elements
        button_class = self.driver.find_element_by_xpath('//*[@id="controls"]/div/div[1]/div/div[2]/div[2]')
        class_value = 'btn-group open'
        button_dropdown_class = self.driver.find_element_by_xpath('//*[@id="controls"]/div/div[1]/div/div[2]/div[2]/a[2]')
        dropdown_class_value = 'true'
        self.driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2])", button_class,'class', class_value)
        self.driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2])", button_dropdown_class, 'aria-expanded', dropdown_class_value)
        #copy the product
        self.driver.find_element_by_xpath('//*[@id="controls"]/div/div[1]/div/div[2]/div[2]/ul/li[1]/a').click()
        #wait until the product is fully copied unti
        while('copyThisProduct=Y' in self.driver.current_url):
            time.sleep(0.01)
        self.product_info_url = self.driver.current_url


    def set_Description(self,Company_Name,Division,Cost_Center,Address_1,Address_2,DACIS,CAGE,DUNS,WRAP_Type):
        """ Set description tab. Must switch to different frame to edit text box field. """

        self.driver.find_element_by_xpath('//*[@id="headingTwo"]/h4/a').click()
        WebDriverWait(self.driver, 1).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="cke_2_contents"]/iframe')))

        #there is probably a way to for loop this but easier to debug with the hard code

        name_element = self.driver.find_element_by_xpath('/html/body/p')
        new_HTML = '<strong>Company:&nbsp;</strong>' + Company_Name
        self.driver.execute_script("arguments[0].innerHTML = arguments[1]",name_element,new_HTML)

        division_element = self.driver.find_element_by_xpath('/html/body/div[1]')
        new_HTML = '<strong>Division:&nbsp;</strong>' + Division
        self.driver.execute_script("arguments[0].innerHTML = arguments[1]",division_element,new_HTML)

        Cost_center_element = self.driver.find_element_by_xpath('/html/body/div[4]')
        new_HTML = '<div>' + Cost_Center + '</div>'
        self.driver.execute_script("arguments[0].innerHTML = arguments[1]",Cost_center_element,new_HTML)

        Address_1_element = self.driver.find_element_by_xpath('/html/body/div[5]')
        new_HTML = '<div>' + Address_1 + '</div>'
        self.driver.execute_script("arguments[0].innerHTML = arguments[1]",Address_1_element,new_HTML)

        Address_2_element = self.driver.find_element_by_xpath('/html/body/div[6]')
        new_HTML = '<div>' + Address_2 + '</div>'
        self.driver.execute_script("arguments[0].innerHTML = arguments[1]",Address_2_element,new_HTML)

        DACIS_element = self.driver.find_element_by_xpath('/html/body/div[8]')
        new_HTML = '<strong>DACIS Code:&nbsp;</strong>' + DACIS
        self.driver.execute_script("arguments[0].innerHTML = arguments[1]",DACIS_element,new_HTML)

        CAGE_element = self.driver.find_element_by_xpath('/html/body/div[9]')
        new_HTML = '<strong>CAGE:&nbsp;</strong>' + CAGE
        self.driver.execute_script("arguments[0].innerHTML = arguments[1]",CAGE_element,new_HTML)

        DUNS_element = self.driver.find_element_by_xpath('/html/body/div[10]')
        new_HTML = '<strong>DACIS Code:&nbsp;</strong>' + DUNS
        self.driver.execute_script("arguments[0].innerHTML = arguments[1]",DUNS_element,new_HTML)

        Type_element = self.driver.find_element_by_xpath('/html/body/div[11]')
        new_HTML = '<strong>Nature of Work:&nbsp;</strong>' + WRAP_Type
        self.driver.execute_script("arguments[0].innerHTML = arguments[1]",Type_element,new_HTML)

        #important line pulls frame back to main page
        self.driver.switch_to.default_content()


    def get_search_tag(self):
        """Get search tag generated from product."""
        self.driver.find_element_by_xpath('//*[@id="controls"]/div/div[1]/div/div[2]/div[2]/a[1]').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="headingSix"]/h4/a').click()
        time.sleep(0.5)
        self.search_tag = self.driver.find_element_by_xpath('//*[@id="seoSection"]/div[1]/div/input').get_attribute('value')


    def select_file(self,file_path):
        """Download the file excel file from computer"""
        self.driver.find_element_by_xpath('//*[@id="downloadSection"]/div[1]/h4/a').click()
        #send file path directly to the choose file button
        #make sure this has the file name in it/full file path, there is no error handling on the site just disconnects
        self.driver.find_element_by_xpath('//*[@id="pUpload_0"]/input').send_keys(file_path)
        time.sleep(2)
        #save the product
        self.driver.find_element_by_xpath('//*[@id="controls"]/div/div[1]/div/div[2]/div[2]/a[1]').click()


    def write_to_file(self,Product_Name):
        file_title = "WRAPs Posted " + date.today().strftime("%d%m%Y") + ".txt"
        WRAP_file = open(file_title, 'a')
        WRAP_file.write(Product_Name + "\t\t" + self.search_tag)
        WRAP_file.close()


    def make_product(self,Product_Name,SKU,Division,Company_Name,Cost_Center,Address_1,Address_2,DACIS,CAGE,DUNS,WRAP_TYPE,file_path):
        """ Check if the product exists. If T make that product link the product link, else make a new product. """
        #check if product exists
        self.check_for_product(SKU)
        #get rid of current category
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath('//*[@id="categories"]/li[2]/a').click()
            #save changes to category
            time.sleep(1)
        except NoSuchElementException:
            pass
        self.set_Information(Product_Name,SKU)
        #save changes, when we change url if we dont save, all changes are lost
        #could be implemented with threading, but trying to avoid refresh errors
        self.driver.find_element_by_xpath('//*[@id="controls"]/div/div[1]/div/div[2]/div[2]/a[1]').click()
        time.sleep(0.5)
        self.set_category(Division,Company_Name)
        #save changes
        self.driver.find_element_by_xpath('//*[@id="controls"]/div/div[1]/div/div[2]/div[2]/a[1]').click()
        time.sleep(1)
        self.set_Description(Company_Name, Division, Cost_Center, Address_1, Address_2, DACIS, CAGE, DUNS, WRAP_TYPE)
        time.sleep(1)
        self.get_search_tag()
        time.sleep(1)
        self.select_file(file_path)
        time.sleep(1)
        self.write_to_file(Product_Name)
        self.driver.get('https://mcnulty.corecommerce.com/admin/index.php?m=products_browse&sort=0')


if __name__ == '__main__':
    cc = CoreCommerce()
    cc.make_product('TEST PRODUCT','000000','TEST DIVISION','TEST COMPANY','TEST COST CENTER', 'ADDRESS 1','ADDRESS 2', 'TEST DACIS', 'CAGE', 'TEST DUNS', 'TEST TYPE',r'C:\Users\Zachary\Desktop\WRAP Poster\TEST PRODUCT\TEST_PRODUCT.xlsx')