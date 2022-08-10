import tkinter as tk

window = tk.Tk()
window.geometry("1000x700")
window.resizable(True, True)
window.minsize(1000, 700)

canvas1 = tk.Canvas(
    window,
    width=600,
    height=560,
    background="#535353",
    highlightthickness=0,
)
canvas1.grid(row=0, column=0, sticky="nwse", padx=1, pady=1)

canvas2 = tk.Canvas(
    window,
    width=140,
    height=560,
    background="#535353",
    highlightthickness=0,
)
canvas2.grid(row=0, column=1, sticky="nwse", padx=1, pady=1)

canvas3 = tk.Canvas(
    window,
    width=120,
    height=560,
    background="#535353",
    highlightthickness=0,
)
canvas3.grid(row=0, column=2, sticky="nwse", padx=1, pady=1)

canvas4 = tk.Canvas(
    window,
    width=140,
    height=560,
    background="#535353",
    highlightthickness=0,
)
canvas4.grid(row=0, column=3, sticky="nwse", padx=1, pady=1)

canvas5 = tk.Canvas(
    window,
    width=600,
    height=140,
    background="#535353",
    highlightthickness=0,
)
canvas5.grid(row=1, column=0, sticky="nwse", padx=1, pady=1)

canvas6 = tk.Canvas(
    window,
    width=400,
    height=140,
    background="#535353",
    highlightthickness=0,
)
canvas6.grid(row=1, column=1, columnspan=3, sticky="nwse", padx=1, pady=1)

# 메뉴 위에 점선 구분선 제거해주는 옵션
tearoff = False

# window 크기가 변경될 때, 내부의 canvas들도
# 같이 크기가 변경되게 해주는 코드
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar, tearoff=tearoff)
filemenu.add_command(label="Image Open")
filemenu.add_command(label="Image Erase")
filemenu.add_separator()  # 메뉴 항목 사이에 실선 구분선을 추가해주는 코드
filemenu.add_command(label="Exit", command=window.quit)

edit = tk.Menu(menubar, tearoff=tearoff)
image_rotate = tk.Menu(edit, tearoff=tearoff)
image_rotate.add_command(label="90°")
image_rotate.add_command(label="180°")
image_rotate.add_command(label="270°")

edit.add_cascade(label="image rotate", menu=image_rotate)
edit.add_command(label="image flip")
edit.add_command(label="image size")
edit.add_command(label="canvas size")

line = tk.Menu(menubar, tearoff=tearoff)
line.add_command(label="auto line")
line.add_command(label="line rectification")
line.add_command(label="noise remove")

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=edit)
menubar.add_cascade(label="Line", menu=line)

window.config(menu=menubar)

window.configure(bg="#282828")  # window 배경색 설정
window["bg"] = "#282828"

window.mainloop()
