import tkinter as tk
from time import time

clicks = []
temp_clicks = []


def click():
    clicks.append(time())

    if len(clicks) > 1:
        temp_clicks.clear()
        for i in range(len(clicks)):
            temp_clicks.append(clicks[i] - clicks[i - 1])
        print(temp_clicks)
    else:
        print(1)


def save():
    f = open("clicks-demo.ta", "a")
    for tempClick in temp_clicks:
        if not str(tempClick).startswith("-"):
            f.write(str(tempClick) + "\n")
    f.close()


root = tk.Tk()

tk.Button(root, text='Click', command=click).pack(padx=5, pady=5)
tk.Button(root, text='Save', command=save).pack(padx=5, pady=5)

tk.mainloop()
