import queue
import xlwings
import os
import openpyxl
from os import listdir
from os.path import isfile, join
import shutil

class WRAP_Queue():

    def __init__(self):
        self.WRAP_info = {}
        current_path = os.path.dirname(__file__)
        self.post_path = current_path + "\\WRAPS_TO_POST"
        self.posted_path = os.path.dirname("WRAPS_POSTED") + '\\WRAPS_POSTED'
        files_list = [f for f in listdir(self.post_path) if isfile(join(self.post_path, f))]
        self.WRAP_queue = queue.Queue()
        for file in files_list:
            self.WRAP_queue.put(self.post_path + "\\" + file)
        self.current_wrap = self.WRAP_queue.get()
        self.set_WRAP_info()


    def next_WRAP(self):
        shutil.move(self.current_wrap, self.current_wrap.replace('WRAPS_TO_POST','WRAPS_POSTED'))
        self.current_wrap = self.WRAP_queue.get()
        self.set_WRAP_info()


    def set_WRAP_info(self):
        self.workbook = openpyxl.load_workbook(self.current_wrap)
        self.worksheet = self.workbook.worksheets[1]
        keys = ["Company Name","Division","Type","Address 1","Address 2","DACIS","CAGE","DUNS","Mat_Hand"]
        range_list = ["B2","B3","B6","B4","B5","H2","H3","H4","C47"]
        for i in range(len(keys)):
            try:
                if keys[i] != "DUNS":
                    self.WRAP_info[keys[i]] = str(self.worksheet[range_list[i]].value).strip()
                else:
                    self.WRAP_info[keys[i]] = str(self.worksheet[range_list[i]].value).strip()
            except (ValueError, TypeError):
                self.WRAP_info[keys[i]] = str(self.worksheet[range_list[i]].value).strip()
            if not self.WRAP_info[keys[i]] or self.WRAP_info[keys[i]] == 'None':
                self.WRAP_info[keys[i]] =  ""
        self.workbook.close()
        self.WRAP_info['State'] = str(self.WRAP_info['Address 2'][-8:-6]).strip()
        self.WRAP_info['City'] = str(self.WRAP_info['Address 2'][:-10]).strip()
        try:
            if self.WRAP_info["CAGE"][0] == "'":
                self.WRAP_info["CAGE"] = self.WRAP_info["CAGE"][1:]
        except IndexError:
            pass
        try:
            if self.WRAP_info["DUNS"][0] == "'":
                self.WRAP_info["DUNS"] = self.WRAP_info["DUNS"][1:]
        except IndexError:
            pass
        try:
            if "." in self.WRAP_info["DUNS"]:
                self.WRAP_info["DUNS"] = self.WRAP_info["DUNS"][:self.WRAP_info["DUNS"].find(".")]
        except:
            pass
