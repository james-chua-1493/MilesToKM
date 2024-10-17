from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=10, pady=10)

#Label
label = Label(text="is equal to")
label.grid(row=1, column=0)
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)
km_label = Label(text="Km")
km_label.grid(row=1, column=2)
def button_clicked():
    miles= float(input.get())
    km =round(miles*1.60934)
    km_number = Label(text=f"{km}")
    km_number.grid(row=1,column=1)
#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(row=2,column=1)

#Entry
input = Entry(width=10)
input.grid(row=0, column=1)


window.mainloop()