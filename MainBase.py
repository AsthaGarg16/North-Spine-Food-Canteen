import tkinter as tk  # import tkinter
from StallDisplay import Display_Stall_Page
from WaitingPage import Waiting_Time
from StartPage import StartPage
from pygame import mixer
from tkinter import ttk, messagebox
import random
import threading
import pyttsx3 # this is for text to speech
import time



class Build(tk.Tk):
  # *args mean to pass any number of arguments
  # **kwargs is keyword arguments, like dictionary keys
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)

    style=ttk.Style()
    style.configure("MainHeading", font='Times 24 italic')
    style.configure("SubHeading", font='Times 18')
    tk.Tk.iconbitmap(self, default="NTU.ico")
    # This is to display the Windows title
    self.title("North Spine Food Canteen")

    # default value for Stall
    self.selectedStall = "Korean Stall"

    # To store the Frame formate to display
    self.display = tk.Frame(self)

    # for playing music
    play_list = ["Music/Harmony.MP3", "Music/Outside.MP3", "Music/Tokyo_Sunset.MP3"]
    randomlist = random.randint(0,2)

    # to start the music player
    mixer.init()
    mixer.music.set_volume(0.4)
    # a random music will be play each time the use open the application
    mixer.music.load(str(play_list[randomlist]))
    # -1 is to replay the music
    mixer.music.play(-1)

    # this is to pack the frame
    # fill is to fill up the spaces
    # expand mean any expand if the space you have
    self.display.pack(side="top", fill="both", expand=True)

    # 0 is min size, weight is piority
    self.display.grid_rowconfigure(0, weight=1)
    self.display.grid_columnconfigure(0, weight=1)

    # Using list of pages
    windows_Page = [StartPage,Display_Stall_Page, Waiting_Time]

    # multiple windows to display
    self.frames = {}

    # this is for more than 1 frame
    for page in windows_Page:
      # this is to load all the frame
      frame = page(self.display, self) # in other .py class display = parent, self = controller

      self.frames[page] = frame
      # grid is like pack, but grid is to set to a frame
      # sticky is alignment or stratch to the windows nsew north south east west
      frame.grid(row=0, column=0, sticky="nsew")

    self.welcomeMessage = "Welcome to North Spine Food Canteen. Please select a stall."
    # Run the threading method for text to speech and raise frame
    self.threadingMethodFrame(self.welcomeMessage, StartPage)


  def saveStall(self, var):
    # this is to set the value from the drop down list at StartPage
    self.selectedStall = var.get()
    #print("Btn Click: ",self.selectedStall)
    # This is to distroy Display Stall Page frame
    app.frames[Display_Stall_Page].destroy()
    # This is to setup the display stall page
    # reason to do this is because the label at Display Stall Page will be updated accordingly
    app.frames[Display_Stall_Page] = Display_Stall_Page(self.display, self)
    app.frames[Display_Stall_Page].grid(row=0, column=0, sticky="nsew")
    app.frames[Display_Stall_Page].tkraise()

    selectStallMessage = "You have selected " + str(self.selectedStall)

    # Run the threading method for text to speech and raise frame
    self.threadingMethodFrame(selectStallMessage , Display_Stall_Page)

    #self.show_frame(Display_Stall_Page)

  # This to return the selected stall drop down list to the StallDisplay Page
  def get_ddl_StartPg_Option(self):
    #print("Label: ", self.selectedStall)
    return self.selectedStall


  # create frame method
  # cont is control
  def show_frame(self, cont):
    frame = self.frames[cont]
    # rasie the frame
    frame.tkraise()



  # create this method for the switch from frame to frame
  def show_waitingTime_Frame(self, currentOperation, shopName):

    if (currentOperation == "Shop Close") or (currentOperation == "Shop Close in the afternoon") \
        or (currentOperation == "Shop Close in the morning"):
      # error message shown
      messagebox.showerror("Shop Close", "The " + shopName + " is close now.")

    else:
      # This is to distroy Waiting Time Page frame
      app.frames[Waiting_Time].destroy()

      # This is to setup the Waiting Time page
      # reason to do this is because the label at Waiting Time Page will be updated accordingly
      app.frames[Waiting_Time] = Waiting_Time(self.display, self)
      app.frames[Waiting_Time].grid(row=0, column=0, sticky="nsew")
      app.frames[Waiting_Time].tkraise()

      readTitle = app.frames[Waiting_Time].titleText

      # Run the threading method for text to speech and raise frame
      self.threadingMethodFrame(readTitle, Waiting_Time)




  # create this method for the switch from frame to frame
  def show_StallDisplay_Frame(self):

    # stop the speech
    pyttsx3.init().stop()

    # raise the frame
    self.show_frame(Display_Stall_Page)

  # create this method for the switch from frame to frame
  def show_StartPage_Frame(self):
    # This is to distroy Waiting Time Page frame
    app.frames[StartPage].destroy()

    # This is to setup the Waiting Time page
    # reason to do this is because the label at Waiting Time Page will be updated accordingly
    app.frames[StartPage] = StartPage(self.display, self)
    app.frames[StartPage].grid(row=0, column=0, sticky="nsew")
    app.frames[StartPage].tkraise()


    # Run the threading method for text to speech and raise frame
    self.threadingMethodFrame(self.welcomeMessage, StartPage)

  # threading method for Text-to-speech
  def threadingMethodFrame(self, text_to_speech, frameRaise):

    #text to speech method
    def textSpeak():

      # if the text to speech is still run
      if (pyttsx3.init().isBusy() == True):
        # stop the speech
        pyttsx3.init().stop()
        time.sleep(0.1)

      speak = pyttsx3.init()
      # get the voice
      voices = speak.getProperty('voices')
      # get the speaking rate
      rate = speak.getProperty('rate')
      # set the speak speed
      speak.setProperty(rate, 90)
      # set the speaker
      speak.setProperty('voice', voices[1].id)
      # the text to read
      speak.say(text_to_speech)
      # run it
      speak.runAndWait()
      # stop pyttsx3
      speak.stop()

    # to raise the frame
    def raiseFrame():
      self.show_frame(frameRaise)

    # locate the method to run
    speaking = threading.Thread(target=textSpeak)
    # Start threading
    speaking.start()
    # locate the method to run
    raiseGUI = threading.Thread(target=raiseFrame)
    # Start threading
    raiseGUI.start()



# to build a Windows
app = Build()
app.mainloop()

