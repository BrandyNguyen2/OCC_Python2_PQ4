# PROGRAMMER: Brandy Nguyen 
import tkinter
import tkinter.simpledialog
import tkinter.messagebox
# FUNCTION
def userInput(applicationWindow) :
    numberOfPhones = tkinter.simpledialog.askinteger("User Input", "Enter the number of phones that are in your household")
    applicationWindow.update()
    if numberOfPhones == 0 :
        tkinter.messagebox.showwarning("Warning", "A value of zero was entered")
        applicationWindow.update()
    elif numberOfPhones < 0 :
        tkinter.messagebox.showerror("Error", "Invalid entry ")
        applicationWindow.update()
    else :
        tkinter.messagebox.showinfo("Information", "User input has been validated")
        applicationWindow.update()
        return numberOfPhones

applicationWindow = tkinter.Tk()
applicationWindow.title("Artwork")
applicationWindow.geometry("1080x960")
print(userInput(applicationWindow))
        