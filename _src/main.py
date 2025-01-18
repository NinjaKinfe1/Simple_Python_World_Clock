import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x600")
root.resizable(False,False)
root.iconbitmap("../media/ico/icon.ico")
root.title("Simple Python World Clock")

first_page = tk.Frame(root, bg="#f3f3f3")
first_page.place(width=400, height=600)
big_title = tk.Label(first_page, text="World", font=("Alfa Slab One", 70), bg="#f3f3f3", fg="#333333")
big_title.place(x=43, y=68)
small_title = tk.Label(first_page, text="Clock", font=("Alfa Slab One", 40), bg="#f3f3f3", fg="#333333")
small_title.place(x=121, y=188)

select_text = tk.Label(first_page, text="Select a country:", font=("Open Sans Bold", 25), bg="#f3f3f3", fg="#333333")
select_text.place(x=60, y=300)

country = ["Ethiopia","Kenya","Eritrea"]
selected = tk.StringVar()
selected.set(country[0])

dropdown_menu = ttk.Combobox(first_page, textvariable=selected, values=country, state="readonly")
dropdown_menu.config(font=("Open Sans Bold", 15))
dropdown_menu.place(x=42, y=366, width=316, height=50)

root.mainloop()