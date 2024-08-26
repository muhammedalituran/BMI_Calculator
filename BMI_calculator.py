from tkinter import *

bmi=0




window = Tk()
window.minsize(width=200,height=250)
window.eval('tk::PlaceWindow . center')

weight_label = Label(text="Your weight:")
weight_label.pack()

weight_input = Entry()
weight_input.pack()

height_label = Label(text="Your height:")
height_label.pack()

height_input = Entry()
height_input.pack()


def calculate_bmi():
    global bmi
    try:
        bmi = int(weight_input.get())/((int(height_input.get())/100)**2)
    except:
        print("olmuyor")
    sonuc_label.config(text=f"Your BMI is \n{bmi}")

calculate_button = Button(text="Calculate",command=calculate_bmi)
calculate_button.pack()


sonuc_label = Label(text="Not Calculated")
sonuc_label.pack()



window.mainloop()