import Tkinter as tk
import tkMessageBox
import ScrolledText as tkst
from Tkinter import *
from PIL import Image, ImageTk
import matplotlib

############ Frequency Filtering ############
def update_overall():
    parameter_1.insert(INSERT, "")
    parameter_1.insert(END, "")
    print(parameter_1.get(1.0, END))

    for x in range(1, 8):
        var_name = 'var{}'.format(x)
        if ((globals()[var_name]).get() == 'rate1'):
            print(("Rank_%s" %x)+": 1")
            rank=1
        elif ((globals()[var_name]).get() == 'rate2'):
            print(("Rank_%s" %x)+": 2")
            rank=2
        elif ((globals()[var_name]).get() == 'rate3'):
            print(("Rank_%s" %x)+": 3")
            rank=3
        elif ((globals()[var_name]).get() == 'rate4'):
            print(("Rank_%s" %x)+": 4")
            rank=4
        elif ((globals()[var_name]).get() == 'rate5'):
            print(("Rank_%s" %x)+": 5")
            rank=5
        else:
            print(("Rank_%s" %x)+": 0")
            rank =0

    return rank

############ ############ ############ ############

############ ############ ############ ############

# Create the main window
print("Building the GUI interface..")
root = tk.Tk()
root.title("GUI Interface - MPD - TripAdvisor Project")
#size windows
#root.geometry("900x900")
#size full windows

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%sx%s' % (width, height))
#change windows color
root.configure(background='#599442')

'''
# Set the original image label and initialize it to "no_img"
original_pic = Image.open(r"Original_Photos/no_img.png")
original_pic = original_pic.resize((450, 450), Image.ANTIALIAS)
original_photo = ImageTk.PhotoImage(original_pic)
'''
# Set the entry for the first parameter
var1_descr = " Enter a text review: "
label_descr1 = tk.Label(root, text=var1_descr, font='Helvetica 11 bold',bg = '#599442')
parameter_1 = tkst.ScrolledText(root, width =80, height=5, wrap = WORD, bd = 3, font='Helvetica 10')
#parameter_1 = tk.Entry(root, width =100, bd=3)

# Create the buttons
update_button = tk.Button(root, text = "Update", command = update_overall, font='Helvetica 10 bold',bg='white')

# Grid is used to add the widgets to root
# Alternatives are Pack and Place
label_descr1.grid(row = 9, column = 13, padx = 10)
parameter_1.grid(row = 10, column = 13,padx = 40)
update_button.grid(row = 11, column = 13)

print("GUI Interface is ready!\n")

######################### RADIOBUTTON 1 ########################################

#def selected():
#    print("Value: "+var1.get())

var1 = tk.StringVar()

#label over radiobutton
label_term1 = tk.Label(root, text= "Value:", font='Helvetica 10 bold',bg = '#599442')
label_term1.grid(row = 9, column = 1, padx=10, pady=10)

#radiobutton
rate1 = tk.Radiobutton(text='1', variable=var1,bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate1.config(indicatoron=0, bd=1, width=2, value='rate1')
rate1.grid(row=9, column=2, pady=10)

rate2 = tk.Radiobutton(text='2', variable=var1, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate2.config(indicatoron=0, bd=1, width=2, value='rate2')
rate2.grid(row=9, column=3)

rate3 = tk.Radiobutton(text='3', variable=var1, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate3.config(indicatoron=0, bd=1, width=2, value='rate3')
rate3.grid(row=9, column=4)

rate4 = tk.Radiobutton(text='4', variable=var1, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate4.config(indicatoron=0, bd=1, width=2, value='rate4')
rate4.grid(row=9, column=5)

rate5 = tk.Radiobutton(text='5', variable=var1, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate5.config(indicatoron=0, bd=1, width=2, value='rate5')
rate5.grid(row=9, column=6)

################################################################################

######################### RADIOBUTTON 2 ########################################

#def selected():
#    print("Rooms: "+var2.get())

var2 = tk.StringVar()

#label over radiobutton
label_term2 = tk.Label(root, text= "Rooms:",  font='Helvetica 10 bold',bg = '#599442')
label_term2.grid(row = 10, column = 1, padx=10, pady=10)

#radiobutton
rate1 = tk.Radiobutton(text='1', variable=var2, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate1.config(indicatoron=0, bd=1, width=2, value='rate1')
rate1.grid(row=10, column=2,pady=10)

rate2 = tk.Radiobutton(text='2', variable=var2,bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate2.config(indicatoron=0, bd=1, width=2, value='rate2')
rate2.grid(row=10, column=3)

rate3 = tk.Radiobutton(text='3', variable=var2, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate3.config(indicatoron=0, bd=1, width=2, value='rate3')
rate3.grid(row=10, column=4)

rate4 = tk.Radiobutton(text='4', variable=var2, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate4.config(indicatoron=0, bd=1, width=2, value='rate4')
rate4.grid(row=10, column=5)

rate5 = tk.Radiobutton(text='5', variable=var2 ,bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate5.config(indicatoron=0, bd=1, width=2, value='rate5')
rate5.grid(row=10, column=6)

################################################################################

######################### RADIOBUTTON 3 ########################################

#def selected():
#    print("Location: "+var3.get())

var3 = tk.StringVar()

#label over radiobutton
label_term3 = tk.Label(root, text= "Location:", font='Helvetica 10 bold',bg = '#599442')
label_term3.grid(row = 11, column = 1, padx=10, pady=10)

#radiobutton
rate1 = tk.Radiobutton(text='1', variable=var3 ,bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate1.config(indicatoron=0, bd=1, width=2, value='rate1')
rate1.grid(row=11, column=2,pady=10)

rate2 = tk.Radiobutton(text='2', variable=var3, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate2.config(indicatoron=0, bd=1, width=2, value='rate2')
rate2.grid(row=11, column=3)

rate3 = tk.Radiobutton(text='3', variable=var3, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate3.config(indicatoron=0, bd=1, width=2, value='rate3')
rate3.grid(row=11, column=4)

rate4 = tk.Radiobutton(text='4', variable=var3, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate4.config(indicatoron=0, bd=1, width=2, value='rate4')
rate4.grid(row=11, column=5)

rate5 = tk.Radiobutton(text='5', variable=var3, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate5.config(indicatoron=0, bd=1, width=2, value='rate5')
rate5.grid(row=11, column=6)

################################################################################

######################### RADIOBUTTON 4 ########################################

#def selected():
#    print("Cleanliness: "+var4.get())

var4 = tk.StringVar()

#label over radiobutton
label_term4 = tk.Label(root, text= "Cleanliness:", font='Helvetica 10 bold',bg = '#599442')
label_term4.grid(row = 12, column = 1, padx=10, pady=35)

#radiobutton
rate1 = tk.Radiobutton(text='1', variable=var4, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate1.config(indicatoron=0, bd=1, width=2, value='rate1')
rate1.grid(row=12, column=2, pady=10)

rate2 = tk.Radiobutton(text='2', variable=var4, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate2.config(indicatoron=0, bd=1, width=2, value='rate2')
rate2.grid(row=12, column=3)

rate3 = tk.Radiobutton(text='3', variable=var4, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate3.config(indicatoron=0, bd=1, width=2, value='rate3')
rate3.grid(row=12, column=4)

rate4 = tk.Radiobutton(text='4', variable=var4, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate4.config(indicatoron=0, bd=1, width=2, value='rate4')
rate4.grid(row=12, column=5)

rate5 = tk.Radiobutton(text='5', variable=var4, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate5.config(indicatoron=0, bd=1, width=2, value='rate5')
rate5.grid(row=12, column=6)

################################################################################

######################### RADIOBUTTON 5 ########################################

#def selected():
#    print("Check in :"+var5.get())

var5 = tk.StringVar()

#label over radiobutton
label_term5 = tk.Label(root, text= "Check in:", font='Helvetica 10 bold',bg = '#599442')
label_term5.grid(row = 9, column = 7, padx=10, pady=10)

#radiobutton
rate1 = tk.Radiobutton(text='1', variable=var5, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate1.config(indicatoron=0, bd=1, width=2, value='rate1')
rate1.grid(row=9, column=8,pady=10)

rate2 = tk.Radiobutton(text='2', variable=var5,bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate2.config(indicatoron=0, bd=1, width=2, value='rate2')
rate2.grid(row=9, column=9)

rate3 = tk.Radiobutton(text='3', variable=var5,bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate3.config(indicatoron=0, bd=1, width=2, value='rate3')
rate3.grid(row=9, column=10)

rate4 = tk.Radiobutton(text='4', variable=var5,bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate4.config(indicatoron=0, bd=1, width=2, value='rate4')
rate4.grid(row=9, column=11)

rate5 = tk.Radiobutton(text='5', variable=var5, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate5.config(indicatoron=0, bd=1, width=2, value='rate5')
rate5.grid(row=9, column=12)

################################################################################

######################### RADIOBUTTON 6 ########################################

#def selected():
#    print("Service: "+var6.get())

var6 = tk.StringVar()

#label over radiobutton
label_term6 = tk.Label(root, text= "Service:", font='Helvetica 10 bold',bg = '#599442')
label_term6.grid(row = 10, column = 7, padx=10, pady=10)

#radiobutton
rate1 = tk.Radiobutton(text='1', variable=var6, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate1.config(indicatoron=0, bd=1, width=2, value='rate1')
rate1.grid(row=10, column=8,pady=10)

rate2 = tk.Radiobutton(text='2', variable=var6, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate2.config(indicatoron=0, bd=1, width=2, value='rate2')
rate2.grid(row=10, column=9)

rate3 = tk.Radiobutton(text='3', variable=var6, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate3.config(indicatoron=0, bd=1, width=2, value='rate3')
rate3.grid(row=10, column=10)

rate4 = tk.Radiobutton(text='4', variable=var6, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate4.config(indicatoron=0, bd=1, width=2, value='rate4')
rate4.grid(row=10, column=11)

rate5 = tk.Radiobutton(text='5', variable=var6, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate5.config(indicatoron=0, bd=1, width=2, value='rate5')
rate5.grid(row=10, column=12)

################################################################################

######################### RADIOBUTTON 7 ########################################

#def selected():
#    print("Businness Service: "+var7.get())

var7 = tk.StringVar()

#label over radiobutton
label_term7 = tk.Label(root, text= "Businness Service:", font='Helvetica 10 bold',bg = '#599442')
label_term7.grid(row = 11, column = 7, padx=10, pady=10)

#radiobutton
rate1 = tk.Radiobutton(text='1', variable=var7, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate1.config(indicatoron=0, bd=1, width=2, value='rate1')
rate1.grid(row=11, column=8,pady=10)

rate2 = tk.Radiobutton(text='2', variable=var7, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate2.config(indicatoron=0, bd=1, width=2, value='rate2')
rate2.grid(row=11, column=9)

rate3 = tk.Radiobutton(text='3', variable=var7, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate3.config(indicatoron=0, bd=1, width=2, value='rate3')
rate3.grid(row=11, column=10)

rate4 = tk.Radiobutton(text='4', variable=var7, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate4.config(indicatoron=0, bd=1, width=2, value='rate4')
rate4.grid(row=11, column=11)

rate5 = tk.Radiobutton(text='5', variable=var7, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate5.config(indicatoron=0, bd=1, width=2, value='rate5')
rate5.grid(row=11, column=12)

############################### PRINT BN #######################################
############ Create Window ############
def create_window():
    subroot = Toplevel()
    subroot.title("Bayesian Network Model")
    subroot.geometry('500x400')
    subroot.configure(background='white')
    canvas = Canvas(subroot, width = 500, height = 400)
    tk_img = ImageTk.PhotoImage(file='ImageBayesianNet.png')
    canvas = tk.Canvas(subroot, width=450, height=350,bg = 'white', highlightbackground='white')
    canvas.create_image(240, 180, image=tk_img, anchor = CENTER)
    canvas.grid(row=1, column=1, pady = 5)
    close_window = tk.Button(subroot, text="Close Window", command=subroot.destroy, font='Helvetica 10 bold',bg='#ff4500',fg='black')
    close_window.grid(row = 2, column = 1)
    subroot.mainloop()
############ ############ ############ ############

print_button = tk.Button(
    root, text="Print Bayesian Network Model", command=create_window, anchor='w',
     activebackground="#33B5E5", font='Helvetica 10 bold',bg='white')
print_button.grid(row = 12, column = 13)

################################################################################

tripadvisor_img = ImageTk.PhotoImage(file = 'tripadvisor.jpg')
canvas1 = tk.Canvas(root, width=340, height=110,bg = '#599442', highlightbackground='#599442')
canvas1.create_image(170, 55, image=tripadvisor_img, anchor = CENTER)
canvas1.grid(row=1, column=13, pady = 3)

################################################################################

######################### RADIOBUTTON OVERALL ##################################
label_realvalue = tk.Label(root, text= "Overall value:", font='Helvetica 16 bold',bg = '#599442')
label_realvalue.grid(row = 13, column = 1, padx=10, pady=30)

var_realvalue = tk.StringVar()

#radiobutton
rate1 = tk.Radiobutton(text='1', variable=var_realvalue, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate1.config(indicatoron=0, bd=1, width=2, value='rate1')
rate1.grid(row=13, column=2,pady=10)

rate2 = tk.Radiobutton(text='2', variable=var_realvalue, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate2.config(indicatoron=0, bd=1, width=2, value='rate2')
rate2.grid(row=13, column=3)

rate3 = tk.Radiobutton(text='3', variable=var_realvalue, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate3.config(indicatoron=0, bd=1, width=2, value='rate3')
rate3.grid(row=13, column=4)

rate4 = tk.Radiobutton(text='4', variable=var_realvalue, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate4.config(indicatoron=0, bd=1, width=2, value='rate4')
rate4.grid(row=13, column=5)

rate5 = tk.Radiobutton(text='5', variable=var_realvalue, bg = 'white', font='Helvetica 9 bold', selectcolor ='#888888')
rate5.config(indicatoron=0, bd=1, width=2, value='rate5')
rate5.grid(row=13, column=6)

################################################################################
################################################################################
label_predictvalue = tk.Label(root, text= "Predict value:4", font='Helvetica 16 bold',bg = '#599442')
label_predictvalue.grid(row = 14, column = 1, padx=10)

label_accuracy = tk.Label(root, text= "Accuracy: 95%", font='Helvetica 16 bold',bg = '#599442')
label_accuracy.grid(row = 14, column = 7)
################################################################################

close_window_main = tk.Button(root, text="Close Window", command=root.destroy, font='Helvetica 10 bold',bg='#ff4500',fg='black')
close_window_main.grid(row = 1, column = 14)

root.mainloop()
