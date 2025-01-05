from utils import *
from tkinter import *
import csv

r = Tk()
r.title("Fifa Renderz Player Data")
r.geometry("600x400")
# test

# declaring string variable for url
url_var=StringVar()

def submit():
    url = url_var.get()
    url_var.set("")
    
    with open("data.csv", 'a', encoding="utf-8", newline='') as file:
        w = csv.writer(file)
        all_stats = getStats(url) # stat values
        w.writerow(all_stats)


url_label = Label(r, text='URL',font=('calibre',10, 'bold'))
url_label.grid(row=0)
url_entry = Entry(r, textvariable=url_var, font=('calibre',10,'normal'), width=40)
url_entry.grid(row=0, column=1,padx=10)


submit_button = Button(r, text='submit', width=5, command=submit)
submit_button.grid(row=0, column=2)

destroy_button = Button(r, text='close window', width=10, command=r.destroy)
destroy_button.grid(row=1, column=1)

r.mainloop()

# 

    

    
