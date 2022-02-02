import time
import keyboard
from datetime import date
from difflib import SequenceMatcher
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
from Core_Commerce_XML_API import CoreCommerce_XML_API



class CoreCommerce:
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
        self.CC_XML = CoreCommerce_XML_API('Zach', 'Fearful4jesuit!', 'mcnulty_xml')
        self.driver.switch_to.window(window_handle)
        self.driver.get('https://mcnulty.corecommerce.com/admin/')
        self.driver.find_element_by_name('userId').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="admin-login-box-middle"]/form/div[2]/input').click()
        self.driver.get('https://mcnulty.corecommerce.com/admin/index.php?m=products_browse&sort=0')
        time.sleep(2)
        if self.driver.current_url != 'https://mcnulty.corecommerce.com/admin/index.php?m=products_browse&sort=0':
            raise ValueError('Invalid CC username.')


    def check_for_product(self,SKU):
        """
        Check if product exists by searching SKU. If T select product, else copy last product.
        Note that this function runs under the assumption that SKU is unique.
        """
        url = self.CC_XML.find_product_url(SKU)
        if url == None:
            self.copy_last_product()
        else:
            self.product_info_url = url
            self.driver.get(url)
            time.sleep(1)


    def search_categories(self,Division,Company_Name):
        """ Search categories in large list (not in product page), return bool."""
        search_result = self.CC_XML.check_for_cat(Division)
        if search_result == None:
            self.cat_id = None
            return False
        else:
            self.cat_id = search_result
            return True


    def select_category(self,Division,Company_Name):
        """ Select category withtin product page. """
        #go to category pop up, page needs to load properly sometimes the xpath below is linked to another element
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="informationSection"]/div[14]/div[1]/div/div[1]/a')))
        self.driver.find_element_by_xpath('//*[@id="informationSection"]/div[14]/div[1]/div/div[1]/a').click()
        pg = 2
        while True:
            time.sleep(0.5)
            label_list = self.driver.find_elements_by_xpath('//td[contains(@id,"objectName")]/label')
            id_list = self.driver.find_elements_by_xpath('//td[contains(@id,"objectName")]/input')
            label_id = zip(label_list, id_list)
            for label,id in label_id:
                row_text = label.text
                row_id = id.get_attribute('id')
                #match = SequenceMatcher(row_text,Division).ratio()
                if (Division in row_text) or (row_id == self.cat_id):
                    id.click()
                    self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/div[1]/a/i').click()
                    return None
            try:
                time.sleep(0.5)
                self.driver.find_elements_by_xpath('//a[@aria-label="Page ' + str(pg) + '"]')[0].click()
            except NoSuchElementException:
                raise CustomError("Can't find the category to set :/")
            pg += 1


    def add_category(self,Division,Company_Name):
        """ Add category. Uses XML API, handles parent category creation aswell."""
        self.cat_id = self.CC_XML.add_cat(Division, Company_Name)


    def set_category(self,Division,Company_Name):
        """ Look for category, if exists select it, else add and select. """
        if(self.search_categories(Division,Company_Name)):
            self.select_category(Division,Company_Name)
        else:
            self.add_category(Division,Company_Name)
            self.CC_XML.refresh_cat_map()
            self.driver.refresh()
            time.sleep(1)
            self.select_category(Division,Company_Name)


    def set_Information(self,Product_Name,SKU):
        """Set information for info tab."""
        time.sleep(1)
        product_name_element = self.driver.find_element_by_xpath('//*[@id="informationSection"]/div[1]/div[1]/div/input')
        sku_element = self.driver.find_element_by_xpath('//*[@id="informationSection"]/div[1]/div[2]/div/input')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="informationSection"]/div[1]/div[1]/div/input')))
        self.driver.execute_script('arguments[0].setAttribute(arguments[1], arguments[2])', product_name_element, 'value', Product_Name)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="informationSection"]/div[1]/div[2]/div/input')))
        self.driver.execute_script('arguments[0].setAttribute(arguments[1], arguments[2])', sku_element, 'value', SKU)


    def copy_last_product(self):
        """ Copy the last product. Assumes that if there is a last page there must be a product on that page."""
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
        #wait until the product is fully copied until
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
        new_HTML = '<strong>DACIS:&nbsp;</strong>' + DACIS
        self.driver.execute_script("arguments[0].innerHTML = arguments[1]",DACIS_element,new_HTML)

        CAGE_element = self.driver.find_element_by_xpath('/html/body/div[9]')
        new_HTML = '<strong>CAGE:&nbsp;</strong>' + CAGE
        self.driver.execute_script("arguments[0].innerHTML = arguments[1]",CAGE_element,new_HTML)

        DUNS_element = self.driver.find_element_by_xpath('/html/body/div[10]')
        new_HTML = '<strong>DUNS:&nbsp;</strong>' + DUNS
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
        #make sure this has the file name in it/full file path, there is no error handling on the server side, just disconnects
        self.driver.find_element_by_xpath('//*[@id="pUpload_0"]/input').send_keys(file_path)
        time.sleep(2)
        #save the product
        self.driver.find_element_by_xpath('//*[@id="controls"]/div/div[1]/div/div[2]/div[2]/a[1]').click()


    def make_product(self,Product_Name,SKU,Division,Company_Name,Cost_Center,Address_1,Address_2,DACIS,CAGE,DUNS,WRAP_TYPE,file_path):
        """ Check if the product exists. If T make that product link the product link, else make a new product. """
        #check if product exists
        try:
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
            #save changes, when we change url if we dont save all changes are lost
            #could be implemented with threading, but trying to avoid refresh errors
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="controls"]/div/div[1]/div/div[2]/div[2]/a[1]')))
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
            #add the current product to the CCXML sku:id map so we dont have to reload the product map between posts
            product_id = self.product_info_url.replace('https://mcnulty.corecommerce.com/admin/index.php?m=edit_product&pID=','').replace('&back=1','')
            self.CC_XML.map[SKU] = product_id
            self.driver.get('https://mcnulty.corecommerce.com/admin/index.php?m=products_browse&sort=0')
        except NoSuchElementException:
            #my idea here is to filter out any weirdness with the description box that regularly comes up, pretty much just ignore the erorr
            #make a new product, and log in a file that there is probably a duplicate of this file on CC

            WRAP_file = open('ERROR LOG ' + date.today().strftime("%d%m%Y") + '.txt', 'a')
            WRAP_file.write('An error occured while making: ' + Product_Name + ' ' + SKU + '. There is likely a duplicate on CC. ')

            self.driver.get('https://mcnulty.corecommerce.com/admin/index.php?m=products_browse&sort=0')
            self.copy_last_product()
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath('//*[@id="categories"]/li[2]/a').click()
                #save changes to category
                time.sleep(1)
            except NoSuchElementException:
                pass
            self.set_Information(Product_Name,SKU)
            #save changes, when we change url if we dont save all changes are lost
            #could be implemented with threading, but trying to avoid refresh errors
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="controls"]/div/div[1]/div/div[2]/div[2]/a[1]')))
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
            #add the current product to the CCXML sku:id map so we dont have to reload the product map between posts
            product_id = self.product_info_url.replace('https://mcnulty.corecommerce.com/admin/index.php?m=edit_product&pID=','').replace('&back=1','')

            WRAP_file.write('The completed product ID is:' + str(product_id) + '\n')
            WRAP_file.close()

            self.CC_XML.map[SKU] = product_id
            self.driver.get('https://mcnulty.corecommerce.com/admin/index.php?m=products_browse&sort=0')
