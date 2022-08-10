# -*- coding: utf-8 -*-

# 마우스를 canvas 위에서 움직일 때,
# canvas의 좌측 상단 (0, 0)을 기준으로
# 마우스의 좌표를 주기적으로 저장

import tkinter as tk

DEBUG = False


window = tk.Tk()

color = "#ffffff"
prev_x, prev_y = (0, 0)  # 마우스를 움직이기 이전 위치
curr_x, curr_y = (0, 0)  # 마우스 왼쪽 버튼을 누른 상태로 움직였을 때 위치

canvas = tk.Canvas(window, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)


# canvas에 그려진 모든 픽셀 제거
def clear_canvas():
    canvas.delete("all")


button = tk.Button(window, text="Clear", command=clear_canvas)
button.pack(fill=tk.BOTH, expand=True)


# # 마우스의 움직임에 따라 마우스의 좌표를 저장
def update_prev_xy(event):
    global prev_x, prev_y
    if DEBUG:
        print(f"(prev_x, prev_y) {prev_x, prev_y} -> {event.x, event.y}")
    prev_x, prev_y = event.x, event.y


canvas.bind("<Motion>", update_prev_xy)


# 마우스 왼쪽 버튼(B1)을 누른 상태로 움직이는 동안
# 마우스의 경로(trajectory)를 Canvas에 그림
def draw_trajectory(event, color):
    global prev_x, prev_y, curr_x, curr_y
    curr_x, curr_y = event.x, event.y
    if DEBUG:
        print(f"draw line from {prev_x, prev_y} to {curr_x, curr_y}")
    canvas.create_line(prev_x, prev_y, curr_x, curr_y, fill=color)
    prev_x, prev_y = curr_x, curr_y


canvas.bind("<B1-Motion>", lambda event: draw_trajectory(event, color))

label = tk.Label(window, text=f"{color.upper()}", fg=color)
label.pack(fill=tk.BOTH, expand=True)

color_r = 0  # 0 ~ 255
color_g = 0  # 0 ~ 255
color_b = 0  # 0 ~ 255


def change_rgb_tuple_to_hex_code(rgb_tuple):
    return "#%02x%02x%02x" % rgb_tuple


def update_color(target):
    if target == "red":
        global color_r
        color_r = scale_r.get()
        color_r = min(max(0, color_r), 255)
    elif target == "green":
        global color_g
        color_g = scale_g.get()
        color_g = min(max(0, color_g), 255)
    elif target == "blue":
        global color_b
        color_b = scale_b.get()
        color_b = min(max(0, color_b), 255)

    global color
    rgb_tuple = (color_r, color_g, color_b)
    color = change_rgb_tuple_to_hex_code(rgb_tuple)
    label["fg"] = color
    label["text"] = color.upper()

    if DEBUG:
        print(f"color: {rgb_tuple} ({color})")


scale_r = tk.Scale(
    window,
    troughcolor="red",
    command=lambda _: update_color("red"),
    orient="horizontal",
    showvalue=False,
    to=255,
)
scale_r.pack(fill=tk.BOTH, expand=True)

scale_g = tk.Scale(
    window,
    troughcolor="green",
    command=lambda _: update_color("green"),
    orient="horizontal",
    showvalue=False,
    to=255,
)
scale_g.pack(fill=tk.BOTH, expand=True)

scale_b = tk.Scale(
    window,
    troughcolor="blue",
    command=lambda _: update_color("blue"),
    orient="horizontal",
    showvalue=False,
    to=255,
)
scale_b.pack(fill=tk.BOTH, expand=True)


def choose_random_color():
    import random

    global color, color_r, color_g, color_b
    color_r = random.randint(0, 255)
    scale_r.set(color_r)
    color_g = random.randint(0, 255)
    scale_g.set(color_g)
    color_b = random.randint(0, 255)
    scale_b.set(color_b)

    color = change_rgb_tuple_to_hex_code((color_r, color_g, color_b))
    label["fg"] = color
    label["text"] = color.upper()


button2 = tk.Button(window, text="Random Color", command=choose_random_color)
button2.pack(fill=tk.BOTH, expand=True)


window.mainloop()
