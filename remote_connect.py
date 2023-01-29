from tkinter import *
from tkinter import ttk
import tkinter as tk
import subprocess
import paramiko


class RShell:
    def __init__(self, root):
        root.title("Remote Shell")
        frame = ttk.Frame(root, padding=10)
        frame.grid()

        ttk.Label(frame, text="Host").grid(column=4, row=1)
        self.host = StringVar()
        entered_host = ttk.Entry(frame, width=20, textvariable=self.host)
        entered_host.grid(column=5, row=1, pady=5)  # Host Ip Box

        ttk.Label(frame, text="Port").grid(column=4, row=2)
        self.port = StringVar()
        entered_port = ttk.Entry(frame, width=20, textvariable=self.port)
        entered_port.grid(column=5, row=2, pady=5)

        ttk.Label(frame, text="User").grid(column=4, row=3)
        self.user = StringVar()
        entered_user = ttk.Entry(frame, width=20, textvariable=self.user)
        entered_user.grid(column=5, row=3, pady=5)

        ttk.Label(frame, text="Password",).grid(column=4, row=4)
        self.passw = StringVar()
        entered_passw = ttk.Entry(
            frame, width=20, show="*", textvariable=self.passw)
        entered_passw.grid(column=5, row=4, pady=5)

        ttk.Label(frame, text="Command").grid(column=4, row=6)
        self.exec = StringVar()
        entered_command = ttk.Entry(frame, width=20, textvariable=self.exec)
        entered_command.grid(column=5, row=6, pady=5)  # Execute Command Box

        self.output = StringVar()
        ttk.Label(frame, textvariable=self.output).grid(column=5, row=8)

        ttk.Label(frame, text="Remote Shell").grid(column=5, row=0)
        ttk.Button(frame, text="Execute",
                   command=self.shell).grid(column=5, row=7)
        root.bind("<Return>", self.shell)

    def shell(self, *args):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            host = self.host.get()
            port = self.port.get()
            user = self.user.get()
            passwd = self.passw.get()
            cmd = self.exec.get()
            client.connect(host, port, user, passwd)
            _, stdout, stderr = client.exec_command(cmd)
            out = stdout.readlines()
            self.output.set(out)
        except:
            print("Something is wrong, try again.")


root = Tk()
RShell(root)
root.mainloop()
