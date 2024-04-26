# PROGRAMMER: Brandy Nguyen
import tkinter.messagebox
import tkinter.simpledialog

def userInput(applicationWindow) :
    numberOfPhones = tkinter.simpledialog.askinteger("User Input", "Please enter the number of phones in your household")
    applicationWindow.update()
    if numberOfPhones == 0 :
        tkinter.messagebox.showwarning("Warning", "A value of zero was entered")
        applicationWindow.update()
    elif numberOfPhones < 0 :
        tkinter.messagebox.showerror("Error", "Input must be greater than zero")
        applicationWindow.update()
    else :
        tkinter.messagebox.showinfo("Validation", "User input has been validated")
        applicationWindow.update
        return numberOfPhones