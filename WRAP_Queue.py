import queue
import xlwings
import os
import openpyxl
from os import listdir
from os.path import isfile, join
import shutil

class WRAP_Queue():
    """
    Handles queue of WRAPs to post in the WRAPS_TO_POST folder. Uses openpyxl to
    get data from excel files. Did not use xlwings here as it has to open the file to read it.
    This leads to some focus errors on the selenium side.
    """

    def __init__(self):
        self.WRAP_info = {}
        self.set_WRAP_queue()
        try:
            self.current_wrap = self.WRAP_queue.get(False)
            self.set_WRAP_info()
            self.is_empty = False
        except queue.Empty:
            self.is_empty = True


    def __call__(self):
        self.set_WRAP_queue()
        try:
            self.current_wrap = self.WRAP_queue.get(False)
            self.set_WRAP_info()
            return True
        except queue.Empty:
            return False


    def set_WRAP_queue(self):
        current_path = os.path.dirname(__file__)
        self.post_path = current_path + "\\WRAPS_TO_POST"
        self.posted_path = os.path.dirname("WRAPS_POSTED") + '\\WRAPS_POSTED'
        files_list = [f for f in listdir(self.post_path) if isfile(join(self.post_path, f))]
        #there are weird windows files that start with ~$ which openpyxl does not like, filter them out
        files_list_full_sorted = [(self.post_path + '\\' + file) for file in files_list if not file.startswith('~$')]
        files_list_full_sorted.sort(key = lambda x: os.path.getmtime(x), reverse = True)
        self.WRAP_queue = queue.Queue()
        for file in files_list_full_sorted:
            self.WRAP_queue.put(file)
        return None


    def discard_WRAP(self):
        shutil.move(self.current_wrap, self.current_wrap.replace('WRAPS_TO_POST','PROBLEM_WRAPS'))
        self.set_WRAP_queue()
        #throws error if queue empty
        try:
            self.current_wrap = self.WRAP_queue.get(False)
            self.set_WRAP_info()
        except queue.Empty:
            for key in self.WRAP_info:
                self.WRAP_info[key] = ''


    def next_WRAP(self):
        shutil.move(self.current_wrap, self.current_wrap.replace('WRAPS_TO_POST','WRAPS_POSTED'))
        self.set_WRAP_queue()
        #throws error if queue empty
        try:
            self.current_wrap = self.WRAP_queue.get(False)
            self.set_WRAP_info()
        except queue.Empty:
            for key in self.WRAP_info:
                self.WRAP_info[key] = ''


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
