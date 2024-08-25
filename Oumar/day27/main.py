from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()
# my_label["text"] = "New Text"
def clique():
    my_label.config(text=input.get())


button = Button(text="Click Me", command=clique)  
button.pack()

input = Entry(width=10)
input.pack()    

# def add(*args):
#     sum = 0
#     print(args)
#     for n in args:     
#         sum += n
#     print(sum)
# add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)









window.mainloop()