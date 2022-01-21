from McNulty_Driver import McNulty
from Core_Commerce_Driver import CoreCommerce
from DACIS_Driver import DACIS
from WRAP_Queue import WRAP_Queue
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class WRAP_POSTER:

    def __init__(self, pm_user, pm_pass, cc_user, cc_pass, DACIS_user, DACIS_pass):
        options = Options()
        options.headless = False
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}
        self.driver = webdriver.Chrome(options = options, desired_capabilities = caps)
        self.driver.implicitly_wait(10)
        self.driver.execute_script("window.open()")
        self.driver.execute_script("window.open()")
        self.WQ = WRAP_Queue()
        self.WRAP_INFO = self.WQ.WRAP_info
        self.pm_user = pm_user
        self.pm_pass = pm_pass
        self.MD = McNulty(pm_user, pm_pass, self.driver, self.driver.window_handles[0])
        self.CC = CoreCommerce(cc_user, cc_pass, self.driver, self.driver.window_handles[1])
        self.DACIS = DACIS(DACIS_user, DACIS_pass, self.driver, self.driver.window_handles[2])


    def post_product(self):
        #Step 1: Find and select product on primemover, get info
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.MD.find_select_product(self.WRAP_INFO['CAGE'], self.WRAP_INFO['Type'],
                                    self.WRAP_INFO['City'], self.WRAP_INFO['State'], self.WRAP_INFO['DACIS'],
                                    self.WRAP_INFO['DUNS'], self.WRAP_INFO['Mat_Hand'])
        self.WRAP_INFO['Product Name'] = self.MD.get_Product_Name()
        self.WRAP_INFO['SKU'] = self.MD.get_SKU()
        self.WRAP_INFO['Cost_Center'] = self.MD.get_Cost_Center()
        self.WRAP_INFO['City'] = self.MD.get_city()
        self.WRAP_INFO['State'] = self.MD.get_state()

        #Step 2: Post product info to core CoreCommerce
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.CC.make_product(self.WRAP_INFO['Product Name'], self.WRAP_INFO['SKU'], self.WRAP_INFO['Division'], self.WRAP_INFO['Company Name'],
                             self.WRAP_INFO['Cost_Center'], self.WRAP_INFO['Address 1'], self.WRAP_INFO['Address 2'], self.WRAP_INFO['DACIS'],
                             self.WRAP_INFO['CAGE'], self.WRAP_INFO['DUNS'], self.WRAP_INFO['Type'], self.WQ.current_wrap)
        self.WRAP_INFO['Search Tag'] = self.CC.search_tag

        #Step 3: Post info to DACIS
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.DACIS.make_product(self.WRAP_INFO['Product Name'], self.WRAP_INFO['CAGE'], self.WRAP_INFO['DACIS'], self.WRAP_INFO['Search Tag'],
                                self.WRAP_INFO['City'], self.WRAP_INFO['State'])

        #Step 4: Set prime mover link and date and save
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.MD.set_Product_Info(self.WRAP_INFO['Search Tag'])
        u_input = input('Post WRAP?')
        if(u_input == "yes"):
            self.MD.post_WRAP()

        #Step 5: Save and Close excel file
        self.WQ.workbook.save(self.WQ.current_wrap)
        self.WQ.workbook.close()
        self.WQ.next_WRAP()



if __name__ == '__main__':
    wp = WRAP_POSTER('jlauretti','L@ur3tt1Jul13n!','Zach','Fearful4jesuit!','mmcnulty','mcnulty2015')
    while True:
        wp.post_product()
