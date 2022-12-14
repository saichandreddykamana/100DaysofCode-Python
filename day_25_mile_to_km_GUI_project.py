from tkinter import *


def calculate():
    miles = miles_entry.get()
    km_result.configure(text=int(1.6 * int(miles)))


window = Tk()
window.title('Mile to Kilometer Conversion')
window.minsize(width=500, height=300)
window.maxsize(width=700, height=500)
window.configure(background='white')
heading = Label(text="Mile to KM Conversion", font=('Calibri', 24), background='white')
heading.grid(column=0, row=0, padx=5.0, pady=10.0)

miles_heading = Label(text="Enter Number of Miles", font=('Calibri', 14), background='white')
miles_heading.grid(column=0, row=1, padx=5.0, pady=10.0)

miles_entry = Entry(width=5, border='2px solid lightgray')
miles_entry.grid(column=1, row=1, padx=5.0, pady=10.0)

km_heading = Label(text="Total Number of KMs : ", font=('Calibri', 14), background='white')
km_heading.grid(column=0, row=2, padx=5.0, pady=10.0)

km_result = Label(text=" ", font=('Calibri', 14), background='white')
km_result.grid(column=1, row=2, padx=5.0, pady=10.0)

calc_btn = Button(text='Calculate', command=calculate)
calc_btn.grid(column=0, row=3, padx=5.0, pady=10.0)

window.mainloop()
