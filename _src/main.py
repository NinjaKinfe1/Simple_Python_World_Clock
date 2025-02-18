import tkinter as tk
from tkinter import messagebox
import requests
import re


root = tk.Tk()
root.geometry("400x600")
root.resizable(False,False)
root.iconbitmap("../media/ico/icon.ico")
root.title("Simple Python World Clock")

#Functions
def prevent_key(event):
    pattern=r"[0-9 \x08 \. \x16 -]"
    if not re.match(pattern, event.char):
        return "break"

def submit():
    try:
        latitude = la_entry.get()
        longitude = lo_entry.get()
        if latitude == "" or longitude == "":
            messagebox.showwarning("Error","Please complete the necessary information!")
            return

        latitude = float(latitude)
        longitude = float(longitude)

        if not (-90 <= latitude <=90) or not(-180 <= longitude <=180):
            messagebox.showwarning("Error", "Please enter a number within the specified range!")
            la_entry.delete(0, tk.END)
            lo_entry.delete(0, tk.END)
            return

        else:
            first_page.place_forget()
            second_page.place(width=400, height=600)
            url = f"https://timeapi.io/api/time/current/coordinate?latitude={latitude}&longitude={longitude}"
            pull_request = requests.get(url)
            get_data = pull_request.json()
            time_text.config(text=get_data["time"])
            date_text_gui.config(text=get_data["date"])
            day_of_the_week_text_gui.config(text=get_data["dayOfWeek"])
            time_zone_text_gui.config(text=get_data["timeZone"])
            second_page.after(60000, back)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def back():
    first_page.place(width=400, height=600)
    second_page.place_forget()

#First Page
first_page = tk.Frame(root, bg="#f3f3f3")
first_page.place(width=400, height=600)
big_title = tk.Label(first_page, text="World", font=("Alfa Slab One", 70), bg="#f3f3f3", fg="#333333")
big_title.place(x=43, y=21)
small_title = tk.Label(first_page, text="Clock", font=("Alfa Slab One", 40), bg="#f3f3f3", fg="#333333")
small_title.place(x=121, y=141)

#Latitude
la_label=tk.Label(first_page, text="Latitude", font=("Open Sans Bold",25), bg="#f3f3f3", fg="#333333")
la_label.place(x=128,y=237)
la_subtitle_label=tk.Label(first_page, text="(Enter a value within the range of -90 to 90.)",font=("Open Sans Regular", 11), bg="#f3f3f3", fg="#333333")
la_subtitle_label.place(x=47,y=286)

la_entry=tk.Entry(first_page, font=("Open Sans Bold", 15),bd=0, highlightthickness=0)
la_entry.place(x=40,y=314, width=320, height=50)
la_entry.bind("<KeyPress>", prevent_key)

#Longitude
lo_label=tk.Label(first_page, text="Longitude", font=("Open Sans Bold",25), bg="#f3f3f3", fg="#333333")
lo_label.place(x=116,y=373)
lo_subtitle_label=tk.Label(first_page, text="(Enter a value within the range of -180 to 180.)",font=("Open Sans Regular", 11), bg="#f3f3f3", fg="#333333")
lo_subtitle_label.place(x=39,y=423)

lo_entry=tk.Entry(first_page, font=("Open Sans Bold", 15),bd=0, highlightthickness=0)
lo_entry.place(x=40,y=451, width=320, height=50)
lo_entry.bind("<KeyPress>", prevent_key)

#Submit Button
submit=tk.Button(first_page, text="Submit", font=("Open Sans ExtraBold",19), bg="#333333", fg="#ffffff", activebackground="#f3f3f3", activeforeground="#333333", bd=0, highlightthickness=0, command=submit)
submit.place(x=100,y=522, width=200, height=50)

#Second Page
second_page=tk.Frame(root, bg="#f3f3f3")

time_frame=tk.Frame(second_page, bg="#ffffff")
time_frame.place(width=320, height=150, x=40, y=40)
time_text=tk.Label(time_frame, font=("Alfa Slab One",70), bg="#ffffff", fg="#333333")
time_text.place(relx=0.5, anchor="center", y=70)

date_text=tk.Label(second_page, text="Date", font=("Open Sans Bold",25), bg="#f3f3f3", fg="#333333")
date_text.place(x=158, y=217)
date_text_gui=tk.Label(second_page, font=("Open Sans Regular",15), bg="#f3f3f3", fg="#333333")
date_text_gui.place(relx=0.5, anchor="center", y=287)

day_of_the_week_text=tk.Label(second_page, text="Day of The Week", font=("Open Sans Bold",25), bg="#f3f3f3", fg="#333333")
day_of_the_week_text.place(x=61, y=302)
day_of_the_week_text_gui=tk.Label(second_page, font=("Open Sans Regular",15), bg="#f3f3f3", fg="#333333")
day_of_the_week_text_gui.place(relx=0.5, anchor="center", y=372)

time_zone_text=tk.Label(second_page, text="Time Zone", font=("Open Sans Bold",25), bg="#f3f3f3", fg="#333333")
time_zone_text.place(x=112, y=387)
time_zone_text_gui=tk.Label(second_page, font=("Open Sans Regular",15), bg="#f3f3f3", fg="#333333")
time_zone_text_gui.place(relx=0.5, anchor="center",y=457)

back_button=tk.Button(second_page, text="Back", font=("Open Sans ExtraBold",25), bg="#333333", fg="#ffffff", activebackground="#f3f3f3", activeforeground="#333333", bd=0, highlightthickness=0, command=back)
back_button.place(x=100,y=522, width=200, height=50)

root.mainloop()