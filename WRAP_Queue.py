import queue
import xlwings
import os
from os import listdir
from os.path import isfile, join


class WRAP_Queue():


    def __init__(self, WRAPS_TO_POST, WRAPS_POSTED):
        self.WRAP_info = {}
        current_path = os.path.dirname(__file__)
        self.post_path = current_path + '\\' + WRAPS_TO_POST
        self.posted_path = current_path + '\\' + WRAPS_POSTED
        files_list = [f for f in listdir(self.post_path) if isfile(join(self.post_path, f))]
        self.WRAP_queue = queue.Queue()
        for file in files_list:
            self.WRAP_queue.put(self.post_path + '\\' + file)
        self.current_wrap = self.WRAP_queue.get()
        self.set_WRAP_info()


    def next_WRAP(self):
        os.system('move ' + self.current_wrap + self.posted_path)
        self.current_wrap = self.WRAP_queue.get()
        self.set_WRAP_info()


    def set_WRAP_info(self):
        self.workbook = xlwings.Book(self.current_wrap)
        self.worksheet = self.workbook.sheets[1]
        self.WRAP_info['Company Name'] = str(xlwings.Range('B2').value)
        self.WRAP_info['Division'] = str(xlwings.Range('B2').value)
        self.WRAP_info['Type'] = str(xlwings.Range('B6').value)
        self.WRAP_info['Address 1'] = str(xlwings.Range('B4').value)
        self.WRAP_info['Address 2'] = str(xlwings.Range('B5').value)
        self.WRAP_info['DACIS'] = str(xlwings.Range('H2').value)
        self.WRAP_info['CAGE'] = str(int(xlwings.Range('H3').value))
        self.WRAP_info['DUNS'] = str(int(xlwings.Range('H4').value))
        self.WRAP_info['Mat_Hand'] = str(xlwings.Range('C47').value)
        self.WRAP_info['State'] = str(self.WRAP_info['Address 2'][-8:-6])
        self.WRAP_info['City'] = str(self.WRAP_info['Address 2'][:-10])



if __name__=="__main__":
    wq = WRAP_Queue('WRAPS_TO_POST', 'WRAPS_POSTED')
    #product name, SKU, and cost center are only in Prime Mover
    WRAP_info = wq.WRAP_info
