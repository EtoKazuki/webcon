import tkinter as tk
import tkinter.ttk as ttk


def getitem(item):
    print(item)

root = tk.Tk()

label = tk.Label(text="売上")
label.pack()

combo = ttk.Combobox(root, state='readonly')
combo["values"] = ("日本", "アメリカ", "ヨーロッパ", "その他", "総売上")
combo.current(0)
combo.pack()


# コールバック関数にgetitemcodeを定義
button = tk.Button(text="表示", command=lambda:getitem(combo.get()))
button.pack()

root.mainloop()
