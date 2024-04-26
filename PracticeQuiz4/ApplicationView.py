# PROGRAMMER: Brandy Nguyen
import tkinter
import tkinter.ttk

class ApplicationWindow:
    # CONSTRUCTOR
    def __init__(self) :
        # WINDOW
        self.__applicationWindow = tkinter.Tk()
        self.__applicationWindow.title("Artwork")
        self.__applicationWindow.geometry("1080x960")
        
        # GRID
        gridFrame = tkinter.ttk.Frame(self.__applicationWindow, padding = 10)
        gridFrame.pack(fill = "both")
        gridFrame.rowconfigure(0, weight = 50)
        gridFrame.rowconfigure(1, weight = 50)
        gridFrame.rowconfigure(2, weight = 50)
        gridFrame.rowconfigure(3, weight = 50)
        gridFrame.rowconfigure(4, weight = 50)
        gridFrame.columnconfigure(0, weight = 50)
        gridFrame.columnconfigure(1, weight = 40)  
        gridFrame.columnconfigure(2, weight = 10)
        gridFrameLanguage = tkinter.ttk.Label(gridFrame, text = "Language")
        gridFrameLanguage.grid(row = 0 , column = 0, sticky = 'n')
        gridFrameGreeting = tkinter.ttk.Label(gridFrame, text = "Greeting")
        gridFrameGreeting.grid(row = 0 , column = 1, sticky = 's')
        gridFrameSyllables = tkinter.ttk.Label(gridFrame, text = "Syllables")
        gridFrameSyllables.grid(row = 0 , column = 2, sticky = 's')
        gridFrameLanguage1 = tkinter.ttk.Label(gridFrame, text = "Hawaiian")
        gridFrameLanguage1.grid(row = 1 , column = 0, sticky = 'we')
        gridFrameLanguage2 = tkinter.ttk.Label(gridFrame, text = "French")
        gridFrameLanguage2.grid(row = 2 , column = 0, sticky = 'we')
        gridFrameLanguage3 = tkinter.ttk.Label(gridFrame, text = "Spanish")
        gridFrameLanguage3.grid(row = 3 , column = 0, sticky = 'we')
        gridFrameGreeting1 = tkinter.ttk.Label(gridFrame, text = " Aloha")
        gridFrameGreeting1.grid(row = 1 , column = 1, sticky = 's')
        gridFrameGreeting2 = tkinter.ttk.Label(gridFrame, text = "Bonjour")
        gridFrameGreeting2.grid(row = 2, column = 1, sticky = 's')
        gridFrameGreeting3 = tkinter.ttk.Label(gridFrame, text = " Hola")
        gridFrameGreeting3.grid(row = 3, column = 1, sticky = 's')
        gridFrameSyllables1 = tkinter.ttk.Label(gridFrame, text = "3")
        gridFrameSyllables1.grid(row = 1, column = 2, sticky = 'e')
        gridFrameSyllables2 = tkinter.ttk.Label(gridFrame, text = "2")
        gridFrameSyllables2.grid(row = 2, column = 2, sticky = 'e')
        gridFrameSyllables3 = tkinter.ttk.Label(gridFrame, text = "2")
        gridFrameSyllables3.grid(row = 3, column = 2, sticky = 'e')

        # GRID ENTRY 
        userLanguage = tkinter.ttk.Entry(gridFrame)
        userLanguage.grid(row = 4, column = 0, sticky = "ew", padx = 2)
        userGreeting = tkinter.ttk.Entry(gridFrame)
        userGreeting.grid(row = 4, column = 1, sticky = "ew")
        userSyllables = tkinter.ttk.Entry(gridFrame)
        userSyllables.grid(row = 4, column = 2, sticky = "ew", padx = 2)

        # SPINBOX
        numberLabelFrame = tkinter.ttk.LabelFrame(self.__applicationWindow, text = "Number")
        numberLabelFrame.pack(fill = "both", padx = 10, pady = 10)
        numberSpinbox = tkinter.ttk.Spinbox(numberLabelFrame, from_ = 30, to = 90, increment = 10)
        numberSpinbox.set(60)
        numberSpinbox.pack(fill = "both", padx = 10, pady = 10) 

        # CANVAS
        graphicsFrame = tkinter.ttk.LabelFrame(self.__applicationWindow, text = "Graphics")
        graphicsFrame.pack(fill = "both", padx = 10, pady = 10)
        graphicsCanvas = tkinter.Canvas(graphicsFrame, bg = "grey", width = 400, height = 600) 
        graphicsCanvas.pack()
        graphicsCanvas.create_rectangle((150, 250), (250, 350), fill = "magenta", outline = "cyan")
        graphicsCanvas.create_oval((125, 375), (175, 325), fill = "blue", outline = "white")
        graphicsCanvas.create_line((250, 250), (400, 0), fill = "orange", width = 10)
    # METHODS
    def getApplicationWindow(self) :
        return self.__applicationWindow.mainloop()

tester = ApplicationWindow()
tester.getApplicationWindow()