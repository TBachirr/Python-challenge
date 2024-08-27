from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=1, row=0)

label = Label(text="Miles")
label.grid(column=2, row=0)

label = Label(text="is equal to")
label.grid(column=0, row=1)

label = Label(text="Km")
label.grid(column=2, row=1)

labelkm = Label(text="0")
labelkm.grid(column=1, row=1)
def convert():
    miles = float(input.get())
    km = miles * 1.609
    labelkm.config(text=km)
    
button = Button(text="convert", command=convert)
button.grid(column=1, row=2)
window.mainloop()