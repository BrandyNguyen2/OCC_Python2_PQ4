# PRGRAMMER: Brandy Nguyen 
import tkinter.simpledialog
import tkinter.messagebox
import tkinter.dialog

def userInput(applicationWindow) :
    numberOfPhones = tkinter.simpledialog.askinteger("User Input", "Enter the number of phones that are in your household")
    if numberOfPhones == 0 :
        tkinter.messagebox.showwarning("Warning", "A value of zero was entered")
    elif numberOfPhones >= 20 :
        tkinter.messagebox.showerror("Error", "Display an appropriate message")
    else :
        tkinter.messagebox.showinfo("Information", "User input has been validated")
    applicationWindow.update()
    return numberOfPhones

applicationWindow = tkinter.Tk()
applicationWindow.title("Artwork")
applicationWindow.geometry("1080x960")
print(userInput(applicationWindow))
        