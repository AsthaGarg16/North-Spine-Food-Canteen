import tkinter as tk  # import tkinter
from PIL import Image, ImageTk
from tkinter import ttk
#from StallD import Display_Stall_Page

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # image background
        img = ImageTk.PhotoImage(Image.open("fcseats.png"))
        panel = tk.Label(self, image=img)
        panel.image = img
        panel.place(x=0, y=0, relwidth=1, relheight=1)
        style = ttk.Style()
        # defining a uniform style for button
        style.configure("MainHeading", font='Times 24 italic')
        style.configure("SubHeading.TButton", font='Helvetica 10')

        # title label on top
        TitleLabel= ttk.Label(self, text="Welcome to North Spine Food Canteen!",font='Times 24 italic')
        TitleLabel.pack(padx=20, pady=10)
        # label for selecting the stall
        IntroLabel=tk.Label(self, text="Please select the stall",font='Times 18')
        IntroLabel.pack(padx=10, pady=5)
        # list for holding names of stall
        OPTIONS=["Korean Stall","Japanese Stall","Chicken Rice Stall","Miniwok Stall","Malay Stall"]
        self.var=tk.StringVar() # for getting the name of selected stall
        self.var.set(OPTIONS[0]) # setting an initial value to the drop down list and the selected stall
        # creating a drop down list for the stalls
        dropDownList = ttk.OptionMenu(self, self.var, *OPTIONS, style="option.TMenubutton")
        dropDownList.pack(padx=10, pady=10)

        # button to the stall display page
        NextButton=ttk.Button(self,text="Next", style="SubHeading.TButton", command=lambda :controller.saveStall(self.var))
        NextButton.pack(padx=10,pady=10)
        # background for window
    def resize(self, event):
        img = Image.open("fcseats.png").resize(
            (event.width, event.height), Image.ANTIALIAS
        )
        self.img = ImageTk.PhotoImage(img)
        self.canvas.itemconfig(self.canvas_img, image=self.img)
