import tkinter as tk  # import tkinter
from StallDisplay import Display_Stall_Page
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import time
import threading
import pyttsx3 # this is for text to speech




class Waiting_Time(tk.Frame):

  def __init__(self, parent, controller):

    tk.Frame.__init__(self, parent)
    style = ttk.Style()

    style.configure("SubHeading.TButton", font='Helvetica 10')
    # image background
    img = ImageTk.PhotoImage(Image.open("wait.jpg"))
    panel = ttk.Label(self, image=img)
    panel.image = img
    panel.place(x=0, y=0, relwidth=1, relheight=1)

    displayStall = Display_Stall_Page(parent, controller)

    stallname = displayStall.lblStallList.cget('text')

    self.titleText = "Enter the number of people in the queue for " + stallname

    lblWaitingTime = ttk.Label(self, text=self.titleText  , font='Times 14')
    lblWaitingTime.pack(padx = 10, pady=10)

    # this is to limit the string value to 3 char
    self.numPeople = tk.StringVar()
    self.numPeople.trace ('w', self.limitInput)
    # textvariable will check for the input being key in
    self.tbNo_Queue = tk.Entry(self, textvariable=self.numPeople)
    self.tbNo_Queue.pack(padx = 10, pady=10)


    btn_Calculate = ttk.Button(self, text="Calculate", style="SubHeading.TButton",
                              command=lambda: self.totalQueue(stallname))
    btn_Calculate.pack(padx = 10, pady=10)

    self.lbl_totalWaiting = ttk.Label(self, text="", font='Times 12' )
    self.lbl_totalWaiting.pack_forget()
    #self.lbl_totalWaiting.pack(padx = 10, pady=10)


    #controller.show_StallDisplay_Frame() is to use the method in MainBuild.py
    btn_back = ttk.Button(self, text="Back To Stall Page", style="SubHeading.TButton",
                         command=lambda: controller.show_StallDisplay_Frame())
    btn_back.pack(padx = 10, pady=10)



    #self.validate_ThisPage(morning_noon_night)

  # this is to limit the string value to 3 char
  def limitInput(self, *args):
    value = self.numPeople.get()
    if (len(value) > 3):
      self.numPeople.set(value[:3])

  def totalQueue(self, stall_name):

    numb_q = self.tbNo_Queue.get()
    try:
      queue = int(numb_q)

      if(stall_name == "Chicken Rice Stall"): # each person 1 min of waiting
        totalWaiting = queue * 1

      elif(stall_name == "Japanese Stall"): # each person 3 mins of waiting
        totalWaiting = queue * 3

      else: # the rest of the stalls each person 2 mins of waiting
        totalWaiting = queue * 2

      #Display the total waiting time
      totalTimeDisplay = ("There are "+ numb_q +" people in queue. Total waiting time for " + stall_name + " is " + str(totalWaiting) + " min")
      self.lbl_totalWaiting.config(text=totalTimeDisplay )

      self.threadingMethodFrame(totalTimeDisplay, self.lbl_totalWaiting)

      # clear the input
      self.tbNo_Queue.delete(0, 'end')

    except ValueError:
      # error message shown
      messagebox.showerror("Wrong Input", "Please enter a numeric input.")
      # clear the input
      self.tbNo_Queue.delete(0, 'end')

  # run threading for Text-to-speech
  def threadingMethodFrame(self, text_to_speech, messageRaise):

    # text to speech method
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
      # set the speaker
      speak.setProperty(rate, 90)
      # the text to read
      speak.setProperty('voice', voices[1].id)
      # the text to read
      speak.say(text_to_speech)
      # run it
      speak.runAndWait()
      # stop pyttsx3
      speak.stop()

    # display the hidden label
    def raiseMessage():
      messageRaise.pack(padx=10, pady=10)

    # locate the method to run
    speaking = threading.Thread(target=textSpeak)
    # Start threading
    speaking.start()
    # locate the method to run
    raiseLabel = threading.Thread(target=raiseMessage)
    # Start threading
    raiseLabel.start()








