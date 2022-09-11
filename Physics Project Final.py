from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter import *


root = Tk()
root.title("Distance Converter")
root.geometry('650x500+0+0')
root.configure(background='black')

Tops = Frame(root, width=100, height=10, bd=16, relief="raise", background='black')
Tops.pack(side=TOP)
LeftMainFrame = Frame(root, width=100, height=10, bd=8, relief="raise", background='black')
LeftMainFrame.pack(side=LEFT)
RightMainFrame = Frame(root, width=250, height=310, bd=8, relief="raise", background='black')
RightMainFrame.pack(side=RIGHT)
BottomMainFrame = Frame(root,width=1000, height=50, bd=16, relief="raise", background='black')
BottomMainFrame.pack(side=BOTTOM)
value0 = StringVar()
convert = DoubleVar()
distance = DoubleVar()


def ConDistance():
    if value0.get() == "Miles to Kilometers":
        convert1 = float(convert.get() * 1.609344)
        convert2 = str('%.2lf' % (convert1)), 'Kilometers'
        distance.set(convert2)
    elif (value0.get() == "Kilometers to Miles"):
        convert1 = float(convert.get() / 1.609344)
        convert2 = str('%.2lf' % (convert1)), 'Miles'
        distance.set(convert2)
    elif (value0.get() == "Meters to Kilometer"):
        convert1 = float(convert.get() * 0.001)
        convert2 = str('%.3lf' % (convert1)),'Kilometer'
        distance.set(convert2)
    elif (value0.get() == "Kilometers to Meters"):
        convert1 = float(convert.get() * 1000)
        convert2 = str('%.2lf' % (convert1)), 'Meters'
        distance.set(convert2)
    elif (value0.get() == "Meters to Inches"):
        convert1 = float(convert.get() / 0.0254)
        convert2 = str('%.2lf' % (convert1)), 'Inches'
        distance.set(convert2)
    elif (value0.get() == "inches to Meters"):
        convert1 = float(convert.get() * 0.0254)
        convert2 = str('%.3lf' % (convert1)), 'Meters'
        distance.set(convert2)
    elif (value0.get() == "Meters to Feet"):
        convert1 = float(convert.get() * 3.2808399)
        convert2 = str('%.5lf' % (convert1)), 'Feet'
        distance.set(convert2)
    elif (value0.get() == "Feet to Meters"):
        convert1 = float(convert.get() / 3.2808399)
        convert2 = str('%.3lf' % (convert1)), 'Meters'
        distance.set(convert2)
    elif (value0.get() == "") or (distance.set(0.0)):
        messagebox.showinfo("Convert?", "Make a selection, please! ")


def qExit():
    qExit = messagebox.askyesno("Exit System?", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return


def Reset():
    value0.set("Select the operation you want to perform!")
    convert.set("0.0")
    distance.set("0.0")


lblMiles = Label(Tops, font=('arial', 50, 'bold'), text="Distance Converter", padx=2, pady=2, bd=2, fg="black",)
lblMiles.grid(row=0, column=2, sticky=W)

box = ttk.Combobox(LeftMainFrame, textvariable=value0, state='readonly', font=('arial', 13, 'bold'), width=40,)
box['values'] = ('Select the operation you want to perform!', 'Kilometers to Miles', 'Miles to Kilometers',
                 'Kilometers to Meters', 'Meters to Kilometer',
                 'Meters to Feet', 'Feet to Meters', 'Meters to Inches', 'inches to Meters')
box.current(0)
box.grid(row=0, column=0)

EntMiles = Entry(LeftMainFrame, font=('arial', 20, 'bold'), textvariable=convert, bd=2, width=25, justify='center')
EntMiles.grid(row=1, column=0)
lblConvert = Label(LeftMainFrame, font=('arial', 20, 'bold'), textvariable=distance, bd=2, width=22,
                   bg='white', pady=2, padx=2, relief='sunken')
lblConvert.grid(row=2, column=0)
lblSpace = Label(LeftMainFrame, font=('arial', 20, 'bold'), bd=2, padx=2, pady=2, width=22, relief='sunken')
lblSpace.grid(row=3, column=0)

btnConvert = Button(RightMainFrame, text='Convert', padx=2, pady=2, bd=2, fg='black', font=('arial', 18, 'bold'),
                    width=10, height=0, command=ConDistance).grid(row=1, column=0)
btnReset = Button(RightMainFrame, text='Reset', padx=2, pady=2, bd=2, fg='black', font=('arial', 18, 'bold'),
                  width=10, height=0, command=Reset).grid(row=2, column=0)
btnExit = Button(RightMainFrame, text='Exit', padx=2, pady=2, bd=2, fg='black', font=('arial', 18, 'bold'),
                 width=10, height=0, command=qExit).grid(row=3, column=0)


root.mainloop()

