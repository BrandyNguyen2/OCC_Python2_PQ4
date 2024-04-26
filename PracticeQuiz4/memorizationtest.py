# PROGRAMMER: Brandy Nguyen
import tkinter.ttk
import tkinter

class ApplicationWindow: 
    def __init__(self) :
        self.__applicationWindow = tkinter.Tk()
        self.__applicationWindow.title("Artwork")
        self.__applicationWindow.geometry("1080x960")

        # GRID 
        gridFrame = tkinter.ttk.Label(self.__applicationWindow, padding = 10)
        gridFrame.pack(fill = "both")
        gridFrame.rowconfigure(0, weight = 50)
        gridFrame.rowconfigure(1, weight = 50)
        gridFrame.rowconfigure(2, weight = 50)
        gridFrame.rowconfigure(3, weight = 50)
        gridFrame.rowconfigure(4, weight = 50)
        gridFrame.columnconfigure(0, weight = 50)
        gridFrame.columnconfigure(1, weight = 40)
        gridFrame.columnconfigure(2, weight = 10)
        gridLanguage = tkinter.ttk.Label(gridFrame, text = "Language")
        gridLanguage.grid(row = 0, column = 0, sticky = "ew")
        gridGreeting = tkinter.ttk.Label(gridFrame, text = "Greeting")
        gridGreeting.grid(row = 0, column = 1, sticky = "ew")
        gridSyllables = tkinter.ttk.Label(gridFrame, text = "Syllables")
        gridSyllables.grid(row = 0 , column = 2, sticky = "ew")
        gridLanguage1 = tkinter.ttk.Label(gridFrame, text = "Hawaiian")
        gridLanguage1.grid(row = 1, column = 1, sticky = 'w')
        gridLanguage2 = tkinter.ttk.Label(gridFrame, text = "French")
        gridLanguage2.grid(row = 2, column = 0, sticky = "w")
        gridLanguage3 = tkinter.ttk.Label(gridFrame, text = "Spanish")
        gridLanguage3.grid(row = 3, column = 0, sticky = "w")
        gridGreeting1 = tkinter.ttk.Label(gridFrame, text = "Aloha")
        gridGreeting1.grid(row = 1, column = 1, sticky = "s")
        gridGreeting2 = tkinter.ttk.Label(gridFrame, text = "Bonjour")
        gridGreeting2.grid(row = 2, column = 1, sticky= "s")
        gridGreeting3 = tkinter.ttk.Label(gridFrame, text = "Hola")
        gridGreeting3.grid(row = 3, column = 1, sticky = "s")
        gridSyllables1 = tkinter.ttk.Label(gridFrame, text = "3")
        gridSyllables1.grid(row = 1, column = 2, sticky = "e")
        gridSyllables2 = tkinter.ttk.Label(gridFrame, text = "2")
        gridSyllables2.grid(row = 2, column = 2, sticky = "e")
        gridSyllables3 = tkinter.ttk.Label(gridFrame, text = "2")
        gridSyllables3.grid(row = 3, column = 2, sticky = "e")
        userLanguage = tkinter.ttk.Entry(gridFrame)
        userLanguage.grid(row = "4", column = 0, sticky = "ew", padx = 2)
        userGreeting = tkinter.ttk.Entry(gridFrame)
        userGreeting.grid(row = 4 , column = 1, sticky = "ew")
        userSyllables = tkinter.ttk.Entry(gridFrame)
        userSyllables.grid(row = 4, column = 2, sticky = "ew", padx = 2)

        # SPINBOX
        numberFrame = tkinter.ttk.LabelFrame(self.__applicationWindow, text = "Number")
        numberFrame.pack(fill = "both", padx = 10, pady = 10)
        numberSpinbox = tkinter.ttk.Spinbox(numberFrame, from_ = 30, to = 90, increment = 10)
        numberSpinbox.set(60)
        numberSpinbox.pack(fill = "both", padx = 10, pady = 10)

        # CANVAS
        graphicsFrame = tkinter.ttk.LabelFrame(self.__applicationWindow, text = "Graphics")
        graphicsFrame.pack(filling = "both", padx = 10, pady = 10)
        graphicsCanvas = tkinter.Canvas(graphicsFrame, bg = "grey", width = 400, height = 600)
        graphicsCanvas.pack()
        graphicsCanvas.create_rectangle((200, 300), (200, 200), fill = "magenta", outline = "cyan")
        graphicsCanvas.create_oval((200, 200), (175, 200), fill = "blue", outline = "white")
        graphicsCanvas.create_line((200, 175), (400, 0), fill = "orange", width = 10)

    def getApplicationWindow(self) :
        return self.__applicationWindow