# -*- coding: utf-8 -*-

# 사이즈를 조절할 수 있는 패널

import tkinter as tk

window = tk.Tk()
window.title("Paned Window")
window.geometry("640x480+50+50")

panel1 = tk.PanedWindow(bd=4, relief="raised", bg="red")
panel1.pack(fill=tk.BOTH, expand=1)
label1 = tk.Label(panel1, text="Panel1")
panel1.add(label1)

panel2 = tk.PanedWindow(panel1, bd=4, orient=tk.VERTICAL, relief="raised", bg="blue")
panel1.add(panel2)
label2 = tk.Label(panel2, text="Panel2 Top")
panel2.add(label2)

label3 = tk.Label(panel2, text="Panel2 Bottom")
panel2.add(label3)

window.mainloop()
