from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter import *

root = Tk()
root.title("Central Mass and Inertia")
root.geometry('600x400')
root.configure(background='black')
root.resizable(False, False)


def openwindow():
    root1 = Toplevel(root)
    root1.title("Distance Converter")
    root1.geometry('650x450')
    root1.configure(background='black')

    Tops = Frame(root1, width=1000, height=50, bd=16, relief="raise", background='black')
    Tops.pack(side=TOP)
    LeftMainFrame = Frame(root1, width=250, height=310, bd=8, relief="raise", background='black')
    LeftMainFrame.pack(side=LEFT)
    RightMainFrame = Frame(root1, width=250, height=310, bd=8, relief="raise", background='black')
    RightMainFrame.pack(side=RIGHT)

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
            convert2 = str('%.3lf' % (convert1)), 'Kilometer'
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

    lblMiles = Label(Tops, font=('arial', 50, 'bold'), text="Distance Converter", padx=2, pady=2, bd=2, fg="black", )
    lblMiles.grid(row=0, column=2, sticky=W)

    box = ttk.Combobox(LeftMainFrame, textvariable=value0, state='readonly', font=('arial', 13, 'bold'), width=40, )
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
    root1.mainloop()


def open2window():
    root3 = Toplevel(root)
    root3.title("Calculate Inertia")
    root3.geometry('650x350')
    root3.configure(background='black')

    Tops = Frame(root3, width=700, height=50, bd=16, relief="raise", background='black')
    Tops.pack(side=TOP)
    LeftMainFrame = Frame(root3, width=1000, height=250, bd=8, relief="raise", padx=3, pady=3, background='black')
    LeftMainFrame.pack(side=TOP)
    RightMainFrame = Frame(root3, width=10000, height=310, padx=2, pady=2, bd=8, relief="raise", background='black')
    RightMainFrame.pack(side=TOP)
    Tpps = Frame(root3, width=1000, height=100, padx=2, pady=2, bd=16, relief="raise", background='black')
    Tpps.pack(side=TOP)


    v = Entry(LeftMainFrame, width=45)
    v.grid(row=1, column=1)

    v1 = Entry(LeftMainFrame, width=45)
    v1.grid(row=2, column=1)

    def qExit():
        qExit = messagebox.askyesno("Exit System?", "Do you want to quit?")
        if qExit > 0:
            root3.destroy()
            return

    def Reset():
        v.delete(0, 'end')
        v1.delete(0, 'end')

    def calculateInertia():
        mass = v.get().split(",")
        distance = v1.get().split(",")
        print(v.get().split(","), v1.get().split(","))

        inertia = 0

        if (len(mass) == len(distance)):
            for i in range(len(mass)):
                inertia = inertia + int(mass[i]) * (int(distance[i]) ** 2)
                printed = "The rotational inertia equals to" + " " + str(inertia)

            print(inertia)
            lblConvert = Label(Tpps, font=('arial', 15, 'bold'), text=printed, bd=2, width=33,
                               bg='white', pady=2, padx=2, relief='sunken')
            lblConvert.grid(row=25, column=0)
        else:
            print("Wrong input")

    vLL = Label(LeftMainFrame,width=35, text='Mass 1, mass 2, mass 3..')
    vLL.grid(row=1, column=0)

    vLL1 = Label(LeftMainFrame, width=35, text='Radius of  mass 1, mass 2,mass 3..')
    vLL1.grid(row=2, column=0)

    lblMiles = Label(Tops, font=('arial', 50, 'bold'), text="Calculate Inertia", padx=2, pady=2, bd=2, fg="black", )
    lblMiles.grid(row=0, column=2, sticky=W)

    lblConvert = Label(Tpps, font=('arial', 15, 'bold'), bd=2, width=35,
                       bg='white', pady=2, padx=2, relief='sunken')
    lblConvert.grid(row=25, column=0)

    btncalculate = Button(RightMainFrame, text='Calculate', padx=2, pady=2, bd=2, fg='black',
                          font=('arial', 18, 'bold'),
                          width=10, height=0, command=calculateInertia)
    btncalculate.grid(row=3, column=2)
    btnReset = Button(RightMainFrame, text='Reset', padx=2, pady=2, bd=2, fg='black', font=('arial', 18, 'bold'),
                      width=10, height=0, command=Reset).grid(row=3, column=3)
    btnExit = Button(RightMainFrame, text='Exit', padx=2, pady=2, bd=2, fg='black', font=('arial', 18, 'bold'),
                     width=10, height=0, command=qExit).grid(row=3, column=4)


    root3.mainloop()


def open3window():
    root2 = Toplevel(root)
    root2.title("Center of mass")
    root2.geometry('700x400')
    root2.configure(background='black')

    Tops = Frame(root2, width=700, height=50, bd=16, relief="raise", background='black')
    Tops.pack(side=TOP)
    LeftMainFrame = Frame(root2, width=1000, height=250, bd=8, relief="raise", padx=3, pady=3, background='black')
    LeftMainFrame.pack(side=TOP)
    RightMainFrame = Frame(root2, width=1000, height=310, padx=2, pady=2, bd=8, relief="raise", background='black')
    RightMainFrame.pack(side=TOP)
    Tpps = Frame(root2, width=1000, height=100, padx=2, pady=2, bd=16, relief="raise", background='black')
    Tpps.pack(side=TOP)



    v = Entry(LeftMainFrame, width=38)
    v.grid(row=0, column=1)
    v1 = Entry(LeftMainFrame, width=38)
    v1.grid(row=1, column=1)
    v2 = Entry(LeftMainFrame, width=38)
    v2.grid(row=2, column=1)
    v3 = Entry(LeftMainFrame, width=38)
    v3.grid(row=3, column=1)

    def qExit():
        qExit = messagebox.askyesno("Exit System?", "Do you want to quit?")
        if qExit > 0:
            root2.destroy()
            return

    def calculatecenter():
        mass = v.get().split(',')
        x = v1.get().split(',')
        y = v2.get().split(',')
        z = v3.get().split(',')
        x_1 = 0
        massa = 0
        y_1 = 0
        z_1 = 0

        for i in range(len(mass)):
            x_1 = x_1 + int(mass[i]) * int(x[i])
            massa = massa + int(mass[i])
            y_1 = y_1 + int(mass[i]) * int(y[i])
            z_1 = z_1 + int(mass[i]) * int(z[i])

        distancefrom_x = x_1 / massa
        distancefrom_y = y_1 / massa
        distancefrom_z = z_1 / massa

        to_be_printed = "COMx ="+str(distancefrom_x) + " ", "COMy=" + str(distancefrom_y)+""," COMz="+str(distancefrom_z)

        lblConvert = Label(Tpps, font=('arial', 10, 'bold'), text=to_be_printed, bd=2, width=55,
                           bg='white', pady=2, padx=2, relief='sunken')
        lblConvert.grid(row=0, column=0)

    def Reset():
        v.delete(0, 'end')
        v1.delete(0, 'end')
        v2.delete(0, 'end')
        v3.delete(0, 'end')

    vL = Label(LeftMainFrame, width=35, text='Mass 1, mass 2, mass 3...')
    vL.grid(row=0, column=0)
    vL1 = Label(LeftMainFrame, width=35, text='x position of 1 mass, z position of 2 mass')
    vL1.grid(row=1, column=0)
    vL2 = Label(LeftMainFrame, width=35, text='y position of 1 mass, z position of 2 mass')
    vL2.grid(row=2, column=0)
    vL3 = Label(LeftMainFrame, width=35, text='z position of 1 mass, z position of 2 mass')
    vL3.grid(row=3, column=0)

    lblMiles = Label(Tops, font=('arial', 40, 'bold'), text="Calculate Central Mass", padx=2, pady=2, bd=2,
                     fg="black", )
    lblMiles.grid(row=0, column=2, sticky=W)

    lblConvert = Label(Tpps, font=('arial', 15, 'bold'), bd=2, width=35,
                       bg='white', pady=20, padx=20, relief='sunken')
    lblConvert.grid(row=0, column=0,)

    btncalculate = Button(RightMainFrame, text='Calculate', padx=2, pady=2, bd=2, fg='black',
                          font=('arial', 18, 'bold'),
                          width=10, height=0, command=calculatecenter)
    btncalculate.grid(row=3, column=2)
    btnReset = Button(RightMainFrame, text='Reset', padx=2, pady=2, bd=2, fg='black', font=('arial', 18, 'bold'),
                      width=10, height=0, command=Reset).grid(row=3, column=3)
    btnExit = Button(RightMainFrame, text='Exit', padx=2, pady=2, bd=2, fg='black', font=('arial', 18, 'bold'),
                     width=10, height=0, command=qExit).grid(row=3, column=4)

    root2.mainloop()



def open4window():
    new4window = Toplevel(root)
    new4window.geometry('450x400')
    new4window.resizable(False, False)
    new4window.title('Information about Rotational Inertia')

    l = Text(new4window, font=('arial', 10, 'bold'))
    l.pack()

    func = ("When a body is free to rotate around an axis, torque must be applied to change its angular momentum.\
    The amount of torque needed to cause any given angular acceleration (the rate of change in angular velocity) is\
    proportional to the moment of inertia of the body. Moment of inertia may be expressed in units of kilogram metre\
    squared (kg·m2) in SI units and pound-foot-second squared (lbf·ft·s2) in imperial or US units.\
    Moment of inertia plays the role in rotational kinetics that mass (inertia) plays in linear kinetics—both characterize\
    the resistance of a body to changes in its motion. The moment of inertia depends on how mass is distributed around\
    an axis of rotation, and will vary depending on the chosen axis. For a point-like mass, the moment of inertia about\
    some axis is given by {\displaystyle mr^{2}}mr^{2}, where {\displaystyle r}r is the distance of the point from the\
    axis, and {\displaystyle m}m is the mass. For an extended rigid body, the moment of inertia is just the sum of all the\
    small pieces of mass multiplied by the square of their distances from the axis in rotation. For an extended body of a\
    regular shape and uniform density, this summation sometimes produces a simple expression that depends on the\
    dimensions, shape and total mass of the object.\
    In 1673 Christiaan Huygens introduced this parameter in his study of the oscillation of a body hanging from a pivot,\
    known as a compound pendulum.[1] The term moment of inertia was introduced by Leonhard Euler in his book Theoria motus\
    corporum solidorum seu rigidorum in 1765,[1][2] and it is incorporated into Euler's second law.")
    l.insert(INSERT, func)

    l.config(state=DISABLED)


    new4window.mainloop()



def open5window():
    new5window = Toplevel(root)
    new5window.geometry('500x400')
    new5window.resizable(False, False)
    new5window.title('Information about Central Mass')
    m = Text(new5window, font=('arial', 10, 'bold'))
    m.pack()
    a = ("In physics, the center of mass of a distribution of mass in space (sometimes referred to as the balance point) is the unique point where the  weighted relative position of the distributed mass sums to zero. This is the point to which a force may be applied to cause a linear acceleration without an angular acceleration. Calculations in mechanics are often simplified when formulated with respect to the center of mass. It is a hypothetical point where the entire mass of an object may be assumed to be concentrated to visualise its motion. In other words, the center of mass is the particle equivalent of a given object for application of Newton's laws of motion.\
    In the case of a single rigid body, the center of mass is fixed in relation to the body, and if the body has uniform density, it will be located at the centroid. The center of mass may be located outside the physical body, as is sometimes the case for hollow or open-shaped objects, such as a horseshoe. In the case of a distribution of separate bodies, such as the planets of the Solar System, the center of mass may not correspond to the position of any individual member of the system.\The center of mass is a useful reference point for calculations in mechanics that involve masses distributed in space, such as the linear and angular momentum of planetary bodies and rigid body dynamics. In orbital mechanics, the equations of motion of planets are formulated as point masses located at the centers of mass. The center of mass frame is an inertial frame in which the center of mass of a system is at rest with respect to the origin of the coordinate system.")
    m.insert(INSERT, a)

    m.config(state=DISABLED)

    new5window.mainloop()


def qExit():
    qExit = messagebox.askyesno("Exit System?", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return


lbltop = Label(root, text="Select the operation you want to perform!", font=('arial', 20, 'bold'),
               padx=2, pady=2, bd=2, fg="black", )
lbltop.grid(row=0, column=0)
btn = Button(root, width=30, text='Convert Distance', font=('arial', 18, 'bold'), bd=2, fg="black", command=openwindow)
btn.grid(row=2, column=0)

btn2 = Button(root, width=30, text='Calculate Inertia', font=('arial', 18, 'bold'),
              padx=2, pady=2, bd=2, fg="black", command=open2window, )
btn2.grid(row=3, column=0)

btn3 = Button(root, width=30, text='Calculate Central Mass', font=('arial', 18, 'bold'),
              padx=2, pady=2, bd=2, fg="black", command=open3window, )
btn3.grid(row=4, column=0)

btn4 = Button(root, width=30, text='Information about Inertia', font=('arial', 18, 'bold'),
              padx=2, pady=2, bd=2, fg="black", command=open4window, )
btn4.grid(row=5, column=0)

btn5 = Button(root, width=30, text='Information about Central Mass', font=('arial', 18, 'bold'),
              padx=2, pady=2, bd=2, fg="black", command=open5window, )
btn5.grid(row=6, column=0)

btnExit = Button(root, width=30, text='Exit', padx=2, pady=2, bd=2, fg='black', font=('arial', 18, 'bold'),
                 command=qExit).grid(row=7, column=0)

root.mainloop()
