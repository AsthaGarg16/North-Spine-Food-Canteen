import tkinter as tk  # import tkinter
from DataBase import DataBase
import time
import datetime
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image, ImageTk




class Display_Stall_Page(tk.Frame):

  def __init__(self, parent, controller):
    db = DataBase()

    tk.Frame.__init__(self, parent)
    style = ttk.Style()

    style.configure("SubHeading.TButton", font='Helvetica 10')
    # image background
    img = ImageTk.PhotoImage(Image.open("menu.jpg"))
    panel = ttk.Label(self, image=img)
    panel.image = img
    panel.place(x=0, y=0, relwidth=1, relheight=1)



    # create a for the clock
    self.lblcurrentDT = ttk.Label(self, text="", font="Times 12")
    # this is to pad the label
    self.lblcurrentDT.pack(pady=10, padx=10)
    self.clockUpdate()


    # create a label
    # This text get the data from the MainB get_ddl_StartPg_Option() function
    self.lblStallList = ttk.Label(self, text = controller.get_ddl_StartPg_Option() ,font="Times 20 italic") #db.storeList.keys()
    # this is to pad the label
    self.lblStallList.pack(pady=10, padx=10)

    # to check morning or afternoon menu
    morning_noon_night = int(time.strftime("%H%M"))
    currentDay = time.strftime("%A")

    # this is to check if the stall is open or close
    menu_Type = self.validate_openingStall(morning_noon_night, currentDay, self.lblStallList.cget("text"))


    # Add button for Adding a Page
    # command is event trigger
    # lamda help to stop the printing but only print after a click
    # controller.show_waitingTime_Frame() is to use the method in MainBuild.py
    self.btn_WaitingHours = ttk.Button(self, text="Calculate the Waiting Time", style="SubHeading.TButton",
                                      command=lambda: controller.show_waitingTime_Frame(menu_Type, controller.get_ddl_StartPg_Option() ))

    self.btn_WaitingHours.pack(padx=10, pady=10)



    # Add button for Adding a Page
    # command is event trigger
    # lamda help to stop the printing but only print after a click
    self.btn_OperatingHours = ttk.Button(self, text="Display Operating Hours", style="SubHeading.TButton",
                                   command=lambda: self.popup_OperatingHours(self.lblStallList.cget('text')))

    self.btn_OperatingHours.pack(padx=10, pady=10)

    # Add button for Adding a Page
    # command is event trigger
    # lamda help to stop the printing but only print after a click
    self.btn_PickDateTime = ttk.Button(self, text="Choose Date/Time", style="SubHeading.TButton",
                        command=lambda: self.pick_DateTime())

    self.btn_PickDateTime.pack(padx=10, pady=10)




    # get the current day
    currentDay = time.strftime("%A")
    #label to display the selcted date
    self.lblMenu_Info = ttk.Label(self)

    self.lblMenu_Info.config(text= self.menu_Infomation(menu_Type, currentDay), font='Times 14')
    # this is to pad the label
    self.lblMenu_Info.pack(pady=10, padx=10)

    # Display Menu
    #size the textbox, word wrap the text and disabled input
    self.txtDisplay = tk.Text(self, height=10, width=50, wrap='word' ,state='disabled', font='Arial 12')

    # the scroll bar for the text box
    scrollDisplay = ttk.Scrollbar(self)
    scrollDisplay.config(command= self.txtDisplay.yview)
    scrollDisplay.place(in_=self.txtDisplay, relx=1.0, relheight=1.0, bordermode="outside")

    # merge textbox and scroll bar
    self.txtDisplay.config(yscrollcommand=scrollDisplay.set)
    self.txtDisplay.pack(padx= 10, pady= 10)



    self.backButton = ttk.Button(self, text="Back", style="SubHeading.TButton",
                                   command=lambda: controller.show_StartPage_Frame())
    self.backButton.pack(padx=10, pady=10)

    #This is to update the menu being display
    self.updateMenu_Display(currentDay, menu_Type)




  # after the Operating hours button click this will popup to display the operating hours of the stall
  def popup_OperatingHours(self, stall_Name):

    # disable buttons when this pop up appear
    self.disableBtn()

    self.popup_OperatingHr = tk.Toplevel(self)
    self.popup_OperatingHr.title("Operating Hours")

    lblOperating_Hours = ttk.Label(self.popup_OperatingHr, anchor ='w', justify='left', font='Times 12')
    lblOperating_Hours.config(text=DataBase().getOperating_Hours(stall_Name))

    lblOperating_Hours.pack(padx = 10, pady = 5)

    btnClose = ttk.Button(self.popup_OperatingHr, width=10, text ="Close", style="SubHeading.TButton",
                         command=lambda: self.destroy_operatingHours())
    btnClose.pack(padx = 10, pady = 5)

    # this is when user click the close button at the top right
    self.popup_OperatingHr.protocol('WM_DELETE_WINDOW', lambda: self.windowsClose("Operating Hours"))


  # this is to close the popup operating hours frame
  def destroy_operatingHours(self):
    # enable the StallDisplay frame button
    self.enableBtn()
    self.popup_OperatingHr.destroy()

  # this is when user click the close button at the top right
  def windowsClose(self, popupWin_Name):

    if (popupWin_Name == "Date Time"):
      self.enableBtn()
      self.dt_Frame.destroy()

    elif (popupWin_Name == "Operating Hours"):
      self.enableBtn()
      self.popup_OperatingHr.destroy()


  # enable buttons on waiting hours, operating hours, pick date time and back
  def enableBtn(self):
    # enable the StallDisplay frame button
    self.btn_WaitingHours.config(state="normal")

    self.btn_OperatingHours.config(state="normal")

    self.btn_PickDateTime.config(state="normal")

    self.backButton.config(state="normal")


  # disable buttons on waiting hours, operating hours, pick date time and back
  def disableBtn(self):
    # disable buttons when this pop up appear
    self.btn_WaitingHours.config(state="disabled")

    self.btn_OperatingHours.config(state="disabled")

    self.btn_PickDateTime.config(state="disabled")

    self.backButton.config(state="disabled")



  def pick_DateTime(self):
    # disable buttons when this pop up appear
    self.disableBtn()

    # open then frame at the Toplevel (overlap of main Windows screen)
    # top will be another frame
    self.dt_Frame = tk.Toplevel(self)
    self.dt_Frame.geometry("300x300")
    self.dt_Frame.title('Select Date and Time')
    # this is when user click the close button at the top right
    self.dt_Frame.protocol('WM_DELETE_WINDOW', lambda: self.windowsClose("Date Time"))


    self.lblChoose_Date = ttk.Label(self.dt_Frame, text="Choose date", font='Times 14 bold')
    # this is to pad the label
    self.lblChoose_Date.pack(pady=10, padx=10)
    self.lblChoose_Date.place(x=100, y=25)

    #ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

    cal = DateEntry(self.dt_Frame, width=12, background='darkblue',
                    foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy', state="readonly")
    #cal.pack(padx=10, pady=10)
    cal.place(x=95, y=75)


    #select time
    self.lblChoose_Time= ttk.Label(self.dt_Frame, text="Choose time", font='Times 14 bold')
    # this is to pad the label
    #self.lblChoose_Time.pack(pady=10, padx=10)
    self.lblChoose_Time.place(x=100, y=125)

    # generate Hours and min for comboBox
    hour = []
    min = []

    #set a range for the combobox for min
    for h in range(0, 25):
      # make the value to 2 digits
      hour.append(str(h).zfill(2))

    lblHour = ttk.Label(self.dt_Frame, text="Select Hour:", font='Times 12')
    lblHour.place(x=20, y=175)

    cbHour = ttk.Combobox(self.dt_Frame, state="readonly", width=2)
    cbHour['values'] = hour
    # have the default value of the hour to display in combobox
    # current() is using index of the list therefore require to -1
    cbHour.current(self.check_Value_Zero(int(time.strftime("%H")) -1) )
    cbHour.place(x=100, y=175)

    # set a range for the combobox for min
    for m in range(0, 60):
      # make the value to 2 digits
      min.append(str(m).zfill(2))

    lblMin = ttk.Label(self.dt_Frame, text="Select Min:",font='Times 12')
    lblMin.place(x=160, y=175)

    cbMin = ttk.Combobox(self.dt_Frame, state="readonly", width=2)
    cbMin['values'] = min
    # have the default value of the min to display in combobox
    # current() is using index of the list therefore require to -1
    cbMin.current(self.check_Value_Zero(int(time.strftime("%M")) - 1))
    cbMin.place(x=230, y=175)

    # btn to get the entered day value
    btn_EnterDate = ttk.Button(self.dt_Frame, text="Select", width=10, style="SubHeading.TButton",
                                 command=lambda: self.btn_Input_DateTime(cal.get_date(), cbHour.get(), cbMin.get()))

    #btn_EnterDate.pack(pady=10, padx=10)
    btn_EnterDate.place(x=100, y=225)

  def check_Value_Zero(self, hour_or_min):

    if (hour_or_min <= 0):

      return 0
    else:
      return  hour_or_min

  # this method is required to make button click to pass inputs to the
  def btn_Input_DateTime(self, getDate, getHour, getMin):

    #enable the StallDisplay frame button
    self.enableBtn()


    selected_Date = str(getDate)
    # convert the date to a day(name), mean from 2019-1-1 = Tuesday
    day = datetime.datetime.strptime(selected_Date, '%Y-%m-%d').strftime('%A')

    combine_hour_min = getHour + getMin

    # to check morning or afternoon menu
    morning_noon_night = int(combine_hour_min)

    menu_Type = self.validate_openingStall(morning_noon_night, day, self.lblStallList.cget('text'))

    # update the label Menu_Info
    self.lblMenu_Info.config(text=self.menu_Infomation(menu_Type,day))

    # Call this method to update the display of the stall
    self.updateMenu_Display(day, menu_Type)

    # destroy Date Time Frame after a button click
    self.dt_Frame.destroy()

  def validate_openingStall(self,morning_noon_night, day, stall_Name):

    # stall all the special operating time for certain stall
    specialStall_oprating_PM = ["Japanese Stall"]
    specialStall_PM = False

    specialStall_oprating_AM = ["Miniwok Stall"]
    specialStall_AM = False


    # to check if user is searching for stall which have different oprating hours
    for stallPM in specialStall_oprating_PM:
      if (stall_Name == stallPM):
        specialStall_PM = True
    # to check if user is searching for stall which have different oprating hours
    for stallAM in specialStall_oprating_AM:
      if (stall_Name == stallAM):
        specialStall_PM = True

    if (day != "Saturday") and  (day != "Sunday"):
      # not Saturday and Sunday
      if (specialStall_PM != True) and (specialStall_AM !=True):
        # Standard operating hours of the Stalls
        if (morning_noon_night >= 500) and (morning_noon_night <= 1159):  # morning breakfast
          menu_Type = "BreakFast"
        elif (morning_noon_night >= 1200) and (morning_noon_night <= 1959):  # afternoon (lunch/dinner)
          menu_Type = "Lunch\Dinner"
        else:# shop close after 2000
          menu_Type = "Shop Close"
      elif (specialStall_oprating_PM == True) and (specialStall_oprating_AM != True):
        # stalls that open in the afternoon
        if (morning_noon_night >= 1200) and (morning_noon_night <= 1959):  # afternoon (lunch/dinner)
          menu_Type = "Lunch\Dinner"
        elif (morning_noon_night >= 500) and (morning_noon_night <= 1159):  # morning breakfast
          menu_Type = "Shop Close in the morning"
        else: # shop close after 2000
          menu_Type = "Shop Close"
      else:
        # stalls that open in the morning
        if (morning_noon_night >= 1200) and (morning_noon_night <= 1959):  # afternoon (lunch/dinner)
          menu_Type = "Shop Close in the afternoon"
        elif (morning_noon_night >= 500) and (morning_noon_night <= 1159):  # morning breakfast
          menu_Type = "BreakFast"
        else: # shop close after 2000
          menu_Type = "Shop Close"
    else:
      # is Saturday or Sunday
      menu_Type = "Shop Close"

    return menu_Type





  def clockUpdate(self):

    # this is to set the fromat of date and time
    current_Date_Time = time.strftime("%A, %d/%m/%Y, %H:%M:%S")

    # this is to set the label with the dat time
    self.lblcurrentDT.config(text = current_Date_Time)

    # this is to refresh the label
    self.lblcurrentDT.after(1000, self.clockUpdate)

  # update the list of menu displaying in the txtDisplay
  def updateMenu_Display(self, day, mor_aft_nig):


    # get the text value of the stall
    stall_Name = self.lblStallList.cget("text")

    # get the selected day value
    date_Menu = day

    # get the timing for breakfast/lunch
    menu_Type = mor_aft_nig

    #if (date_Menu != "Saturday") and (date_Menu != "Sunday"):

    # the information of the stall
    stall_infomation = DataBase().getMenu(stall_Name, date_Menu, menu_Type)
    # replace ", " with a new line
    stall_infomation = stall_infomation.replace(", ", "\n")

    #enable modification on the textbox
    self.txtDisplay.config(state= "normal")
    # clear the text box
    self.txtDisplay.delete(1.0, 'end')
    #update the textbox with values
    self.txtDisplay.insert(tk.END,stall_infomation)
    # Disable input of the textbox
    self.txtDisplay.config(state="disabled")

      #print(stall_infomation)

  # lblMenu_Info validation
  def menu_Infomation(self, menu_Type, currentDay ):

    # Special case condition to be place at the top
    if (menu_Type == "Shop Close in the morning"):
      dispplay_current_Info = self.lblStallList.cget("text") + " is close on the " + currentDay + " morning."

    elif (menu_Type == "Shop Close in the afternoon"):
      dispplay_current_Info = self.lblStallList.cget("text") + " is close on the " + currentDay + " afternoon."

    elif (menu_Type == "Shop Close"):
      dispplay_current_Info = self.lblStallList.cget("text") + " is close on the " + currentDay + "."

    else:
      dispplay_current_Info = self.lblStallList.cget("text") + " is displaying " \
                              + currentDay + " " + menu_Type + " Menu."

    return  dispplay_current_Info










