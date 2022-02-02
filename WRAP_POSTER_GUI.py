import tkinter as tk
import threading
import queue
from tkinter import ttk
from tkinter import messagebox
from WRAP_POSTER import WRAP_POSTER
import time



class WRAP_POSTER_GUI:
    """
    WRAP Poster user interface. Allows for posting a single WRAP
    or continued posting until sepcified stopped. Sepcifies
    if WRAP is posted correctly and logs any that aren't.
    """

    def __init__(self, window, WRAP_POSTER):
        self.window = window
        self.window.geometry("650x465")
        self.WP = WRAP_POSTER
        self.window.title("McNulty WRAP Poster")
        self.window.columnconfigure(0, weight = 1, pad = 10)
        self.window.columnconfigure(1, weight = 1,  pad = 10)
        self.window.rowconfigure(0)
        self.window.rowconfigure(1)
        self.window.rowconfigure(2)
        self.window.rowconfigure(3)
        self.window.rowconfigure(4)
        self.current_file_name = self.get_wrap_info()
        self.current_file_input = self.current_file()
        self.post_status_input = self.post_status()
        self.error_log_input =  self.error_log()
        self.post_next_button =  self.post_next()
        self.post_all_button = self.post_all()
        self.stop_button = self.stop()
        self.stop_button.configure(state = 'disabled')
        #This is important, bools are immutable so I kept passing by reference and getting an error
        self.bool_helper = bool_helper()


    def get_wrap_info(self):
        try:
            current_file_name = self.WP.WQ.WRAP_info['Company Name'] + " " + self.WP.WQ.WRAP_info['CAGE'] + " " + self.WP.WQ.WRAP_info['Type']
        except KeyError:
            current_file_name = ''
        return current_file_name


    def current_file(self):
        current_file = tk.Text(master = self.window, height = 1, width = 44)
        file_label = tk.Label(master = self.window, anchor = 'center', text = 'Next File:', font = 'Calibri 12')
        current_file.grid(row = 0, column = 1, padx = 1, pady = 1,  sticky = 'W')
        file_label.grid(row = 0, column = 0, padx = 1, sticky = 'E')
        current_file.configure(state = 'normal')
        current_file.delete(1.0,tk.END)
        current_file.insert(1.0,self.current_file_name)
        current_file.configure(state = 'disabled')
        return current_file


    def post_status(self):
        posting_status = tk.Text(master = self.window, height = 1, width = 44)
        posting_status.config(state = 'disabled')
        posting_label = tk.Label(master = self.window, anchor = 'center', text = 'Posting Status:', font = 'Calibri 12')
        posting_status.grid(row = 1, column = 1, padx = 1, sticky = 'W')
        posting_label.grid(row = 1, column = 0, padx = 1, sticky = 'E')
        posting_status.configure(state = 'normal')
        posting_status.delete(1.0,tk.END)
        posting_status.insert(1.0,'IDLE')
        posting_status.configure(state = 'disabled')
        return posting_status


    def error_log(self):
        error_box = tk.Text(master = self.window, height = 10, width = 44)
        error_box.configure(font = 'Calibri 12')
        error_box_label = tk.Label(master = self.window, text = 'Error Log:', font = 'Calibri 12', anchor = 'n')
        error_box.grid(row = 2, column = 1, padx = 1, sticky = 'W')
        error_box_label.grid(row = 2, column = 0, padx = 1, sticky = 'NE')
        error_box.configure(state = 'disabled')
        return error_box


    def post_next(self):
        post_next_button = tk.Button(text = 'POST', command = self.post_next_command, width = 44, font = 'Calibri 12 bold')
        post_next_button.grid(row = 3, column = 1, padx = 1, pady = 5, sticky = 'W')
        return post_next_button


    def post_all(self):
        post_all_button = tk.Button(text = 'POST ALL', command = self.post_all_command, width = 44, font = 'Calibri 12 bold')
        post_all_button.grid(row = 4, column = 1, padx = 1, pady = 5, sticky = 'W')
        return post_all_button


    def stop(self):
        stop_button = tk.Button(text = 'STOP AFTER CURRENT', command = self.stop_command, width = 44, fg = 'red', font = 'Calibri 12 bold')
        stop_button.grid(row = 5, column = 1, padx = 1, pady = 5, sticky = 'W')
        return stop_button


    def post_next_command(self):
        """
        Why the process queue call doesn't halt evaluation is confusing.
        But in order for the function to work it can't. Anyway, works.
        """
        #if there is a next wrap
        if self.WP.WQ():
            self.current_file_name = self.get_wrap_info()
            self.current_file_input.configure(state = 'normal')
            self.current_file_input.delete(1.0, tk.END)
            self.current_file_input.insert(1.0, self.current_file_name)
            self.current_file_input.configure(state = 'disabled')
            self.post_status_input.configure(state = 'disabled')
            self.post_next_button.configure(state = 'disabled')
            self.post_all_button.configure(state = 'disabled')
            self.progress()
            self.queue = queue.Queue()
            thread_task_post(self.queue, self.WP, self.current_file_input, self.post_status_input).start()
            self.process_queue()
        else:
            self.current_file_input.configure(state = 'normal')
            self.current_file_input.delete(1.0, tk.END)
            self.current_file_input.configure(state = 'disabled')
            self.post_status_input.configure(state = 'normal')
            self.post_status_input.delete(1.0, tk.END)
            self.post_status_input.insert(1.0, 'NO WRAPS TO POST')
            self.post_status_input.configure(state = 'disabled')


    def post_all_command(self):
        """
        Why the process queue call doesn't halt evaluation is confusing.
        But in order for the function to work it can't. Anyway, works.
        """
        if self.WP.WQ():
            self.current_file_name = self.get_wrap_info()
            self.current_file_input.configure(state = 'normal')
            self.current_file_input.delete(1.0, tk.END)
            self.current_file_input.insert(1.0, self.current_file_name)
            self.current_file_input.configure(state = 'disabled')
            self.post_status_input.configure(state = 'disabled')
            self.post_next_button.configure(state = 'disabled')
            self.post_all_button.configure(state = 'disabled')
            self.stop_button.configure(state = 'normal')
            self.progress()
            self.queue = queue.Queue()
            thread_task_post_all(self.queue, self.WP, self.current_file_name, self.current_file_input, self.post_status_input, self.error_log_input, self.bool_helper).start()
            self.process_queue()
        else:
            self.current_file_input.configure(state = 'normal')
            self.current_file_input.delete(1.0, tk.END)
            self.current_file_input.configure(state = 'disabled')
            self.post_status_input.configure(state = 'normal')
            self.post_status_input.delete(1.0, tk.END)
            self.post_status_input.insert(1.0, 'NO WRAPS TO POST')
            self.post_status_input.configure(state = 'disabled')


    def stop_command(self):
        self.bool_helper.make_false()
        self.stop_button.configure(state = 'disabled')
        return None


    def progress(self):
        """Progressbar creates its own thread."""
        self.prog_bar = ttk.Progressbar(
            master = self.window, orient="horizontal",
            length=444, mode="indeterminate"
            )
        self.prog_bar.grid(row = 1, column = 1, pady = 5, sticky = 'W')
        self.prog_bar.start()


    def process_queue(self):
        try:
            msg = self.queue.get(0)
            self.prog_bar.stop()
            self.prog_bar.destroy()
            if msg[0] == 'done':
                self.post_next_button.configure(state = 'normal')
                self.post_all_button.configure(state = 'normal')
                self.current_file_name = self.get_wrap_info()
                self.current_file_input.configure(state = 'normal')
                self.current_file_input.delete(1.0,tk.END)
                self.current_file_input.insert(1.0,self.current_file_name)
                self.current_file_input.configure(state = 'disabled')
                self.post_status_input.configure(state = 'normal')
                self.post_status_input.delete(1.0,tk.END)
                self.post_status_input.insert(1.0,msg[1])
                self.post_status_input.configure(state = 'disabled')
                self.stop_button.configure(state = 'disabled')
                return True
            else:
                self.post_next_button.configure(state = 'normal')
                self.post_all_button.configure(state = 'normal')
                self.error_log_input.configure(state = 'normal')
                self.error_log_input.insert(tk.END, self.current_file_name + '\n')
                self.error_log_input.configure(state = 'disabled')
                self.post_status_input.configure(state = 'normal')
                self.post_status_input.delete(1.0,tk.END)
                self.post_status_input.insert(1.0,msg[1])
                self.post_status_input.configure(state = 'disabled')
                self.current_file_name = self.get_wrap_info()
                self.current_file_input.configure(state = 'normal')
                self.current_file_input.delete(1.0,tk.END)
                self.current_file_input.insert(1.0,self.current_file_name)
                self.current_file_input.configure(state = 'disabled')
                self.stop_button.configure(state = 'disabled')
                return None
        except queue.Empty:
            self.prog_bar.step(5)
            self.window.after(50, self.process_queue)



class thread_task_post(threading.Thread):
    """Thread class to handle posting while progress bar is moving."""

    def __init__(self, queue, WRAP_POSTER, current_file_input, post_status_input):
        super().__init__()
        self.queue = queue
        self.WP = WRAP_POSTER
        self.current_file_input = current_file_input
        self.post_status_input = post_status_input


    def run(self):
        try:
            self.WP.post_product()
            self.queue.put(('done','POSTED'))
        except Exception:
            self.WP.driver.switch_to.window(self.WP.driver.window_handles[0])
            self.WP.driver.get('https://primemover.mcnulty.us/wraps/list.lasso')
            self.WP.driver.switch_to.window(self.WP.driver.window_handles[1])
            self.WP.driver.get('https://mcnulty.corecommerce.com/admin/index.php?m=products_browse&sort=0')
            self.WP.driver.switch_to.window(self.WP.driver.window_handles[2])
            self.WP.driver.get('https://ci-partners.dacis.com/wrap_rate_listing.lasso')
            self.WP.driver.switch_to.window(self.WP.driver.window_handles[0])
            self.WP.WQ.discard_WRAP()
            self.queue.put(('invalid', 'ERROR'))



class thread_task_post_all(threading.Thread):
    """Thread class to handle posting **all** while progress bar is moving."""

    def __init__(self, queue, WRAP_POSTER, current_file_name, current_file_input, post_status_input, error_log_input, bool_helper):
        super().__init__()
        self.queue = queue
        self.WP = WRAP_POSTER
        self.current_file_name = current_file_name
        self.current_file_input = current_file_input
        self.post_status_input = post_status_input
        self.error_log_input = error_log_input
        self.bool_helper = bool_helper


    def run(self):
        while True:
            try:
                if not self.WP.WQ():
                    self.queue.put(('done','NO WRAPS TO POST'))
                    #could have been pressed but we dont care, theres no next WRAP
                    self.bool_helper.make_true()
                    return None
                if self.bool_helper.keep_posting:
                    self.WP.post_product()
                    time.sleep(1)
                    self.current_file_name = self.WP.WQ.WRAP_info['Company Name'] + " " + self.WP.WQ.WRAP_info['CAGE'] + " " + self.WP.WQ.WRAP_info['Type']
                    self.current_file_input.configure(state = 'normal')
                    self.current_file_input.delete(1.0, tk.END)
                    self.current_file_input.insert(1.0, self.current_file_name)
                    self.current_file_input.configure(state = 'disabled')
                    self.post_status_input.configure(state = 'normal')
                    self.post_status_input.delete(1.0, tk.END)
                    self.post_status_input.insert(1.0, 'COMPLETE')
                    self.post_status_input.configure(state = 'disabled')
                else:
                    self.queue.put(('done','POSTED'))
                    self.bool_helper.make_true()
                    return None
            #high level except to filter out
            except Exception:
                time.sleep(1)
                #log deliquent wrap and put in problem wrap folder
                self.error_log_input.configure(state = 'normal')
                self.error_log_input.insert(tk.END, self.current_file_name + '\n')
                self.error_log_input.configure(state = 'disabled')
                self.WP.WQ.discard_WRAP()
                #change next file and posted status
                self.current_file_name = self.WP.WQ.WRAP_info['Company Name'] + " " + self.WP.WQ.WRAP_info['CAGE'] + " " + self.WP.WQ.WRAP_info['Type']
                self.current_file_input.configure(state = 'normal')
                self.current_file_input.delete(1.0, tk.END)
                self.current_file_input.insert(1.0, self.current_file_name)
                self.current_file_input.configure(state = 'disabled')
                self.post_status_input.configure(state = 'normal')
                self.post_status_input.delete(1.0, tk.END)
                self.post_status_input.insert(1.0, 'ERROR')
                self.post_status_input.configure(state = 'disabled')
                #adjust website handles irrespective of location of error occurence
                self.WP.driver.switch_to.window(self.WP.driver.window_handles[0])
                self.WP.driver.get('https://primemover.mcnulty.us/wraps/list.lasso')
                self.WP.driver.switch_to.window(self.WP.driver.window_handles[1])
                self.WP.driver.get('https://mcnulty.corecommerce.com/admin/index.php?m=products_browse&sort=0')
                self.WP.driver.switch_to.window(self.WP.driver.window_handles[2])
                self.WP.driver.get('https://ci-partners.dacis.com/wrap_rate_listing.lasso')
                self.WP.driver.switch_to.window(self.WP.driver.window_handles[0])
                #added logic to handle situation where stop is NOT pressed but there was an error with the last wrap
                #and there is no next wrap. If not caught here will cause error. Is caught in post next logic by design.

                #if there is no next wrap
                if not self.WP.WQ():
                    self.queue.put(('done','ERROR'))
                    #could have been pressed but we dont care, theres no next WRAP
                    self.bool_helper.make_true()
                    return None
                #if the stop button is pressed, exit, else just keep going
                if not self.bool_helper.keep_posting:
                    self.queue.put(('done','ERROR'))
                    self.bool_helper.make_true()
                    return None



class bool_helper():
    """
    Getting some weird reference errors with tkinter and threads.
    Made this helper class to store the keep posting variable. Bools are immutable.
    """

    def __init__(self):
        self.keep_posting = True


    def make_true(self):
        self.keep_posting = True
        return None


    def make_false(self):
        self.keep_posting = False
        return None
