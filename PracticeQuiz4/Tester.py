# PROGRAMMER: Brandy Nguyen
import tkinter
import tkinter.ttk

class ApplicationView :
    # CONSTRUCTOR
    def __init__(self) :
        self.__applicationWindow = tkinter.Tk()
        self.__applicationWindow.title("Artwork")
        self.__applicationWindow.geometry("1080x960")

        # GRID 
        gridFrame = tkinter.ttk.Frame(self.__applicationWindow, padding = 10)
        gridFrame.pack(fill = "both")
        gridFrame.columnconfigure(0, weight = 50)
        gridFrame.columnconfigure(1, weight = 40)
        gridFrame.columnconfigure(2, weight = 10)
        gridLanguage = tkinter.ttk.Label(gridFrame, text = "Language")
        gridLanguage.grid(row = 0, column = 0, sticky = "ew")
        gridGreeting = tkinter.ttk.Label(gridFrame, text = "Greeting")
        gridGreeting.grid(row = 0, column = 1, sticky = "ew")
        gridSyllables = tkinter.ttk.Label(gridFrame, text = "Syllables")
        gridSyllables.grid(row = 0, column = 2, sticky = "ew")
        gridLanguage1 = tkinter.ttk.Label(gridFrame, text = "Hawaiian")
        gridLanguage1.grid(row = 1, column = 0, sticky = "ew")
        gridLanguage2 = tkinter.ttk.Label(gridFrame, text = "French")
        gridLanguage2.grid(row = 2, column = 0, sticky = "ew")
        gridGreeting1 = tkinter.ttk.Label(gridFrame, text = " Aloha")
        gridGreeting1.grid(row = 1, column = 1, sticky = "ew")
        gridGreeting2 = tkinter.ttk.Label(gridFrame, text = "Bonjour")
        gridGreeting2.grid(row = 2, column = 1, sticky = "ew")
        gridGreeting3 = tkinter.ttk.Label(gridFrame, text = " Hola")
        gridGreeting3.grid(row = 3, column = 1, sticky = "ew")
        gridSyllables1 = tkinter.ttk.Label(gridFrame, text = "3")
        gridSyllables1.grid(row = 1, column = 3, sticky = "ew")
        gridSyllables2 = tkinter.ttk.Label(gridFrame, text = "2")
        gridSyllables2.grid(row = 2, column = 3, sticky = "ew")
        gridSyllables3 = tkinter.ttk.Label(gridFrame, text = "2")
        gridSyllables3.grid(row = 3, column = 3, sticky = "ew")

        # GRID ENTRY 
        userLanguage = tkinter.ttk.Entry(gridFrame)
        userLanguage.grid(row = 4, column = 0, sticky = "ew")
        userGreeting = tkinter.ttk.Entry(gridFrame)
        userGreeting.grid(row = 4, column = 1, sticky = "ew")
        userSyllables = tkinter.ttk.Entry(gridFrame)
        userSyllables.grid(row = 4, column = 2, sticky = "ew")

        # SPINBOX
        numberFrame = tkinter.ttk.LabelFrame(self.__applicationWindow, text = "Number")
        numberFrame.pack(fill = "both", padx = 10, pady = 10)
        numberSpinbox = tkinter.ttk.Spinbox(numberFrame, from_ = 30, to = 90, increment = 10)
        numberSpinbox.set(30)
        numberSpinbox.pack(fill = "both", padx = 10, pady = 10)

        # CANVAS
        canvasFrame = tkinter.ttk.LabelFrame(self.__applicationWindow, text = "Graphics")
        canvasFrame.pack(fill = "both", padx = 10, pady = 10)
        canvasBox = tkinter.Canvas(canvasFrame, bg = "grey", width = 400, height = 600)
        canvasBox.pack()
        canvasBox.create_rectangle((150, 250), (250, 350), fill = "magenta", outline = "cyan")
        canvasBox.create_oval((125, 375), (175, 325), fill = "blue", outline = "white")
        canvasBox.create_line((250, 250), (400, 0), fill = "orange", width = 10)

    def getApplicationWindow(self) :
        return self.__applicationWindow.mainloop()
    
tester = ApplicationView()
tester.getApplicationWindow()

