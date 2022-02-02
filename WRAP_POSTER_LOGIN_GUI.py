import threading
import os
import time
import queue
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from WRAP_POSTER import WRAP_POSTER
from WRAP_POSTER_GUI import WRAP_POSTER_GUI



class WRAP_POSTER_LOGIN_GUI:
    """
    Logs user into app, stores login usernames as environment variables.
    If the environment variables are not present requires input.
    """
    def __init__(self, window):
        self.master = window
        self.login_frame = tk.Frame(master=self.master)
        self.PM_username_input, self.PM_password_input = self.make_login_inputs('PM', 1)
        self.CC_username_input, self.CC_password_input = self.make_login_inputs('CC', 2)
        self.DACIS_username_input, self.DACIS_password_input = self.make_login_inputs('DACIS', 3)
        self.make_login_button()

        try:
            self.PM_username, self.PM_password = self.get_login_env('PM')
        except ValueError:
            self.PM_username, self.PM_password = ("", "")
            pass

        try:
            self.CC_username, self.CC_password = self.get_login_env('CC')
        except ValueError:
            self.CC_username, self.CC_password = ("", "")
            pass

        try:
            self.DACIS_username, self.DACIS_password = self.get_login_env('DACIS')
        except ValueError:
            self.DACIS_username, self.DACIS_password = ("", "")
            pass

        usernames = [self.PM_username, self.CC_username, self.DACIS_username]
        passwords = [self.PM_password, self.CC_password, self.DACIS_password]
        username_fields = [self.PM_username_input, self.CC_username_input, self.DACIS_username_input]
        password_fields = [self.PM_password_input, self.CC_password_input, self.DACIS_password_input]
        users = zip(usernames, username_fields)
        passes = zip(passwords, password_fields)

        for field_list in [users, passes]:
            for field, input in field_list:
                input.delete(0,tk.END)
                input.insert(0,field)


    def get_login_info(self):
        """Get login info after login button is pushed."""
        self.PM_username = self.PM_username_input.get()
        self.PM_password = self.PM_password_input.get()
        self.CC_username = self.CC_username_input.get()
        self.CC_password = self.CC_password_input.get()
        self.DACIS_username = self.DACIS_username_input.get()
        self.DACIS_password = self.DACIS_password_input.get()


    def get_login_env(self, website):
        var_user = website + ' Username'
        var_pass = website + ' Password'
        try:
            username = os.environ[var_user]
            password = os.environ[var_pass]
            return username, password
        except KeyError:
            raise ValueError('There is no login info avaiable.')


    def set_login_env(self, website, username, password):
        var_user = '"' + website + ' Username' + '"'
        var_pass = '"' + website + ' Password' + '"'
        os.system(f'setx {var_user}' + ' ' + '"' + f'{username}' + '"')
        os.system(f'setx {var_pass}' + ' ' + '"' + f'{password}' + '"')


    def make_login_button(self):
        self.login_button = tk.Button(master = self.login_frame, text = "LOGIN", command = self.login, width = 40)
        self.login_frame.pack()
        self.login_button.grid(row = 4, column = 2, padx = 40, pady = 10, columnspan = 4, sticky = 'E')


    def login(self):
        self.login_button['state'] = 'disabled'
        self.login_button.grid(row = 4, column = 2, padx = 10, pady = 10, columnspan = 4)
        self.progress()
        self.prog_bar.start()
        self.queue = queue.Queue()
        self.get_login_info()
        thread_task_login(self.queue, self.PM_username, self.PM_password,
                          self.CC_username, self.CC_password,
                          self.DACIS_username, self.DACIS_password).start()
        self.process_queue()


    def make_login_inputs(self, name, row):
        username = tk.Entry(master = self.login_frame, width = 25)
        password = tk.Entry(master = self.login_frame, width = 25)
        username_label = tk.Label(master = self.login_frame, text = name + " Username:")
        password_label = tk.Label(master = self.login_frame, text = name + " Password:")
        username_label.grid(row = row, column = 1, padx = 5, pady = 10, sticky = 'E')
        password_label.grid(row = row, column = 3, padx = 5, pady = 10, sticky = 'E')
        username.grid(row = row, column = 2, padx = 10, pady = 10, sticky = 'W')
        password.grid(row = row, column = 4, padx = 10, pady = 10, sticky = 'W')
        for i in range(0,5):
            self.login_frame.grid_columnconfigure(i,weight=1)
        for i in range(0,3):
            self.login_frame.grid_rowconfigure(i,weight=1)
        return username, password


    def progress(self):
        self.prog_bar = ttk.Progressbar(
            master = self.login_frame, orient="horizontal",
            length=200, mode="indeterminate"
            )
        self.prog_bar.grid(row = 4, column = 2, pady = 5, sticky = 'W')


    def process_queue(self):
        try:
            msg = self.queue.get(0)
            self.prog_bar.stop()
            self.prog_bar.destroy()
            self.login_button.grid(row = 4, column = 2, padx = 10, pady = 10, columnspan = 4)
            if msg[0] == 'done':
                self.master.destroy()
                poster_window = tk.Tk()
                WRAP_POSTER_GUI(poster_window, msg[1])
                poster_window.mainloop()
            else:
                messagebox.showerror('Small Problem...','Invalid Username or Password')
                self.login_button['state'] = 'active'
        except queue.Empty:
            self.prog_bar.step(10)
            self.master.after(100, self.process_queue)



class thread_task_login(threading.Thread):

    def __init__(self, queue, pm_user, pm_pass, cc_user, cc_pass, dacis_user, dacis_pass):
        super().__init__()
        self.queue = queue
        self.pm_user = pm_user.strip()
        self.pm_pass = pm_pass.strip()
        self.cc_user = cc_user.strip()
        self.cc_pass = cc_pass.strip()
        self.dacis_user = dacis_user.strip()
        self.dacis_pass = dacis_pass.strip()


    def run(self):
        try:
            WP = WRAP_POSTER(self.pm_user, self.pm_pass,
                             self.cc_user, self.cc_pass,
                             self.dacis_user, self.dacis_pass)
            self.set_login_env('PM', self.pm_user, self.pm_pass)
            self.set_login_env('CC', self.cc_user, self.cc_pass)
            self.set_login_env('DACIS', self.dacis_user, self.dacis_pass)
            self.queue.put(('done', WP))
        except ValueError:
            self.queue.put('invalid')


    def set_login_env(self, website, username, password):
        var_user = '"' + website + ' Username' + '"'
        var_pass = '"' + website + ' Password' + '"'
        os.system(f'setx {var_user}' + ' ' + '"' + f'{username}' + '"')
        os.system(f'setx {var_pass}' + ' ' + '"' + f'{password}' + '"')


if __name__ == '__main__':
    login_window = tk.Tk()
    login_window.title("WRAP POSTER Login")
    WRAP_POSTER_LOGIN_GUI(login_window)
    login_window.mainloop()
