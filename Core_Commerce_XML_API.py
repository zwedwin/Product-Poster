import requests
from CoreCommerce_XML import CoreCommerce_XML
import xml.etree.ElementTree as ET
from xml.dom import minidom
import math


class CoreCommerce_XML_API:

    def __init__(self, username, password, xml_key):
        self.username = username
        self.password = password
        self.xml_key = xml_key
        self.map = self.get_sku_map()
        self.cat_map = self.get_cat_map()


    def get_cat_list_xml(self, skip = 0, limit = 240):
        cat_edit_xml = """
        <Request version="1.0">
            <Authentication>
                <Username>""" + self.username + """</Username>
                    <Password>""" + self.password + """</Password>
                    <StoreName>mcnulty</StoreName>
                    <XMLKey>""" + self.xml_key + """</XMLKey>
            </Authentication>
            <Action>ACTION_TYPE_CATEGORY_LIST</Action>
            <Limit>""" + str(limit) + """</Limit>
            <Skip>"""  + str(skip)  + """</Skip>
            <SearchCriteria type="Partial">
            1040
            </SearchCriteria>
        </Request>
        """
        return cat_edit_xml


    def get_list_xml(self, skip, limit = 240):
        list_products_xml = """
        <Request version="1.0">
            <Authentication>
                <Username>""" + self.username + """</Username>
                <Password>""" + self.password + """</Password>
                <StoreName>mcnulty</StoreName>
                <XMLKey>""" + self.xml_key + """</XMLKey>
            </Authentication>
            <Action>ACTION_TYPE_PRODUCT_LIST</Action>
            <Limit>""" + str(limit) + """</Limit>
            <Skip>"""  + str(skip)  + """</Skip>
            <SearchCriteria type="Partial">
            1040
            </SearchCriteria>
        </Request>
        """
        return list_products_xml


    def get_prod_qty(self):
        """Gets total amount of products on Core Commerce."""
        cc_xml = requests.post('https://mcnulty.corecommerce.com/admin/_callback.php', data = self.get_list_xml(0,1))
        root = ET.fromstring(cc_xml.content)
        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
        possible_length = int(root.find('List').get('possibleLength'))
        return possible_length


    def get_alpha_cat(self, cat):
        """Gives alphabet catgorey for parent non-extant parent categories."""
        if bool((ord(cat.strip()[0].upper()) - 64) % 2):
            alph_cat = cat.strip()[0].upper() + '-' + chr(ord(cat.strip()[0]) + 1).upper()
        else:
            alph_cat = chr(ord(cat.strip()[0]) - 1).upper() + '-' + cat.strip()[0].upper()
        return alph_cat


    def alpha_cat(self, cat):
        """Provide the exact cat based on the location alphabetically."""
        alpha_cat = ['A-B (e.g., AASKI - By Light)',
        'C-D (e.g., CACI - Dynetics)', 'E-F (e.g., E3 - Fluor)',
        'G-H (e.g., Garmin - HII)', 'I-J (e.g., iAccess - Jacobs)',
        'K-L (e.g., KBRwyle - Lucayan)', 'M-N (e.g., MacB - NTT)',
        'O-P (e.g., OASIS - Pro-Sphere)', 'Q-R (e.g., QinetiQ - R&S)',
        'S-T (e.g., S2 - TWD)', 'U-V (e.g., UIC - VSE)',
        'W-X (e.g., Wegmann - WPSI)', 'X-Z (e.g., X-Ray - Z Systems)']
        for alph in alpha_cat:
            if cat in alph:
                return alph
        return None


    def add_cat(self, division_name, parent_name):
        """
        Adds category to CoreCommerce. Return catgorey id as a string.
        Added logic to change the ampersands (&) to "&amp;", required by XML.
        """
        try:
            self.cat_map[parent_name]
        except KeyError:
            parent_parent = self.get_alpha_cat(parent_name)
            parent_parent = self.alpha_cat(parent_parent)
            parent_add_xml = CoreCommerce_XML.cat_add_xml(parent_name.replace('&','&amp;'), parent_parent)
            response = requests.post('https://mcnulty.corecommerce.com/admin/_callback.php', data = parent_add_xml)
        cat_add_xml = CoreCommerce_XML.cat_add_xml(division_name.replace('&','&amp;'), parent_name.replace('&','&amp;'))
        response = requests.post('https://mcnulty.corecommerce.com/admin/_callback.php', data = cat_add_xml)
        root = ET.fromstring(response.content)
        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
        category_id = [elem.attrib['id'] for elem in root.iter('Category')][0]
        return category_id


    def get_cat_qty(self):
        """Gets total amount of categories on Core Commerce."""
        cc_cat_xml = requests.post('https://mcnulty.corecommerce.com/admin/_callback.php', data = self.get_cat_list_xml(0,1))
        root = ET.fromstring(cc_cat_xml.content)
        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
        possible_length = int(root.find('List').get('possibleLength'))
        return possible_length


    def refresh_cat_map(self):
        self.cat_map = self.get_cat_map()


    def check_for_cat(self, cat):
        try:
            self.cat_map[cat]
            return self.cat_map[cat]
        except KeyError:
            return None


    def get_cat_map(self):
        """
        Get map of current categories. Max amount of data api will alow is ~250 put limit
        at 240 to be safe products. Added logic to "skip" cats already added.
        """
        max_qty = self.get_cat_qty()
        iter = int(math.ceil(max_qty/240))
        cat_dict = {}
        for i in range(iter):
            response = requests.post('https://mcnulty.corecommerce.com/admin/_callback.php', data = self.get_cat_list_xml(240*i))
            if str(response.status_code) == "200":
                root = ET.fromstring(response.content)
                xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent = "   ")
                cat_list = [elem.text.strip() for elem in root.iter('Name')]
                cat_id_list = [elem.attrib['id'].strip() for elem in root.iter('Category')]
                cat_id = zip(cat_list, cat_id_list)
                for cat, id in cat_id:
                    cat_dict[cat] = id
            else:
                raise Exception("Status Code: " + response.status_code)
        return cat_dict


    def get_sku_map(self):
        """
        Get map of sku key and id value pairs. Max amount of data api will alow is 240 products
        at a time. Not sure why, but added logic to handle that.
        """
        max_qty = self.get_prod_qty()
        iter = int(math.ceil(max_qty/240))
        sku_id_map = {}
        for i in range(iter):
            response = requests.post('https://mcnulty.corecommerce.com/admin/_callback.php', data = self.get_list_xml(240*i))
            if str(response.status_code) == "200":
                root = ET.fromstring(response.content)
                xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent = "   ")

                sku_list = [elem.text for elem in root.iter('Sku')]
                id_list = [elem.attrib['id'] for elem in root.iter('Product')]
                sku_id = zip(sku_list, id_list)
                for sku, id in sku_id:
                    sku_id_map[sku] = id
            else:
                raise Exception("Status Code: " + response.status_code)
        return sku_id_map


    def find_product_url(self, sku):
        sku_map = self.map
        try:
            id = sku_map[sku]
        except KeyError:
            id = None
        if id != None:
            prod_url = 'https://mcnulty.corecommerce.com/admin/index.php?m=edit_product&pID=' + str(id) + '&back=1'
            return prod_url
        else:
            return None
