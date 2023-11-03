import tkinter as tk
from tkinter import messagebox
import random
def click():
    code = ""
    psw1 = random.randint(1, 13)
    letter_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    psw3 = random.choice([i for i in range(14, 28) if i not in [psw1 - 1, psw1 + 1]])
    k = [k for k in letter_list[psw1 - 1: psw3]]

    while len(code) < 7:
        code += random.choice(k)
    if len(str(psw1)) == 1:
        result = f'{0}{psw1} {code} {psw3}'
    else:
        result = f'{psw1} {code} {psw3}'
    return lbl_result.configure(text = result, font = ("Times New Roman", 20))



def close():
    window.destroy()


window = tk.Tk()
window.geometry('960x540')
bg_img = tk.PhotoImage(file = 'image3.png')
window.title("Генерирование код-ключа")

lbl_bg = tk.Label(window, image = bg_img)
lbl_bg.place(x = 0, y = 0, relwidth = 1, relheight = 1)

frame = tk.Frame(window)
frame.place(relx = 0.5, rely = 0.5, anchor = 'center')

lbl_H= tk.Label(frame, text = 'Добро пожаловать!', font = ("Times New Roman", 25))
lbl_H.grid(column = 1, row = 0, padx = 50, pady = 10)

lbl_gen = tk.Label(frame, text = "Генерация ключа: ", font = ("Times New Roman", 20))
lbl_gen.grid(column = 1, row = 2, pady = 10)

btn_gen = tk.Button(frame, text = "Жми, чтобы получить код:", command = click, font = ("Times New Roman", 15))
btn_gen.grid(column = 1, row = 3, padx = 10, pady = 5)
lbl_result = tk.Label(frame, text = "Он будет тут.", font = ("Times New Roman", 15))
lbl_result.grid(column = 2, row = 3)

btn_close = tk.Button(frame, text = "Выйти", command = close, font = ("Times New Roman", 15))
btn_close.grid(column = 1, row = 4, padx = 15, pady = 15)

window.mainloop()