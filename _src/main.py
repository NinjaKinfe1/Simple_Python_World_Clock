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
big_title.place(x=43, y=21)
small_title = tk.Label(first_page, text="Clock", font=("Alfa Slab One", 40), bg="#f3f3f3", fg="#333333")
small_title.place(x=121, y=141)

#latitude
la_lable=tk.Label(first_page, text="Latitude", font=("Open Sans Bold",25), bg="#f3f3f3", fg="#333333")
la_lable.place(x=128,y=237)
la_subtitle_lable=tk.Label(first_page, text="(Enter a value within the range of -90 to 90.)",font=("Open Sans Regular", 11), bg="#f3f3f3", fg="#333333")
la_subtitle_lable.place(x=47,y=286)

la_entry=tk.Entry(first_page, font=("Open Sans Bold", 15),bd=0, highlightthickness=0)
la_entry.place(x=40,y=314, width=320, height=50)

#Longitude 
lo_lable=tk.Label(first_page, text="Longitude", font=("Open Sans Bold",25), bg="#f3f3f3", fg="#333333")
lo_lable.place(x=116,y=373)
lo_subtitle_lable=tk.Label(first_page, text="(Enter a value within the range of -180 to 180.)",font=("Open Sans Regular", 11), bg="#f3f3f3", fg="#333333")
lo_subtitle_lable.place(x=39,y=423)

lo_entry=tk.Entry(first_page, font=("Open Sans Bold", 15),bd=0, highlightthickness=0)
lo_entry.place(x=40,y=451, width=320, height=50)

#Submit Button
submit=tk.Button(first_page, text="Submit", font=("Open Sans ExtraBold",19), bg="#333333", fg="#ffffff", activebackground="#f3f3f3", activeforeground="#333333", bd=0, highlightthickness=0)
submit.place(x=100,y=522, width=200, height=50)

root.mainloop()