from func import toDict
class DataBase():
    # Contructor of the class
    def __init__(self):

        self.day = "Monday"
        self.stallName = ""

        self.chickenRiceDetail = toDict("chickenRice.txt")
        self.chickenRiceDetail_AM = toDict("chickenRiceAM.txt")

        self.japaneseStallDetail = toDict("japanese.txt")
        self.japaneseStallDetail_AM = {"Closed": "Japanese Stall is closed in the morning"}

        self.koreanStallDetail = toDict("korean.txt")
        self.koreanStallDetail_AM = toDict("koreanAM.txt")

        self.miniWokStallDetail = {"Closed": "Miniwok Stall is closed in the morning"}
        self.miniWokStallDetail_AM = toDict("miniWokAM.txt")

        self.malayStallDetail = toDict("malay.txt")
        self.malayStallDetail_AM = toDict("malayAM.txt")
        '''
        self.stallList = {"Chicken Rice Stall": self.chickenRiceDetail[self.day],
                         "Japanese Stall": self.japaneseStallDetail[self.day],
                         "Korean Stall" : self.koreanStallDetail[self.day]}
        '''
        # print(self.stallList["Chicken Rice Stall"])

    def getMenu(self, stall_Name, day, mor_aft_nig):

        if (mor_aft_nig == 'BreakFast'):  # BreakFast Menu
            self.stallList = {"Chicken Rice Stall": self.chickenRiceDetail_AM[day],
                              "Japanese Stall": self.japaneseStallDetail_AM["Closed"],
                              "Korean Stall": self.koreanStallDetail_AM[day],
                              "Miniwok Stall": self.miniWokStallDetail_AM[day],
                              "Malay Stall":self.malayStallDetail_AM[day]}

        elif (mor_aft_nig == "Lunch\Dinner"):  # Lunch/Dinner menu
            self.stallList = {"Chicken Rice Stall": self.chickenRiceDetail[day],
                              "Japanese Stall": self.japaneseStallDetail[day],
                              "Korean Stall": self.koreanStallDetail[day],
                              "Miniwok Stall": self.miniWokStallDetail["Closed"],
                              "Malay Stall": self.malayStallDetail[day]}

        else:  # shop are close after hours
            self.stallList = {
                "Chicken Rice Stall": "There is no Menu. \nTo view Chicken Rice Stall Operating hours. \nClick on Display Operating Hours Button.",
                "Japanese Stall": "There is no Menu. \nTo view Japanese Stall Operating hours. \nClick on Display Operating Hours Button.",
                "Korean Stall": "There is no Menu. \nTo view Korean Stall Operating hours. \nClick on Display Operating Hours Button.",
                "Miniwok Stall": "There is no Menu. \nTo view Miniwok Stall Operating hours. \nClick on Display Operating Hours Button.",
                "Malay Stall": "There is no Menu. \nTo view Malay Stall Operating hours. \nClick on Display Operating Hours Button."}

        return self.stallList[stall_Name]

    def getOperating_Hours(self, stall_Name):

        operating_Hour = []
        op_hour_Display = ""

        if (stall_Name == "Chicken Rice Stall"):
            self.chickStall_OpHour = ["Weekday BreakFast:     0500Hrs - 1159Hrs",
                                      "Weekday Lunch/Dinner:    1200Hrs - 1959Hrs",
                                      "Weekday After 2000Hrs:     Close", "Weekend:     Close"]
            operating_Hour = self.chickStall_OpHour

        elif (stall_Name == "Japanese Stall"):
            self.japStall_OpHour = ["Weekday BreakFast:     Close", "Weekday Lunch/Dinner:    1200Hrs - 1959Hrs",
                                    "Weekday After 2000Hrs:     Close", "Weekend:     Close"]

            operating_Hour = self.japStall_OpHour

        elif (stall_Name == "Miniwok Stall"):
            self.miniWokStall_OpHour = ["Weekday BreakFast:     0500Hrs - 1159Hrs", "Weekday Lunch/Dinner:    Close",
                                    "Weekday After 2000Hrs:     Close", "Weekend:     Close"]

            operating_Hour = self.miniWokStall_OpHour

        elif (stall_Name == "Malay Stall"):
            self.malayStall_OpHour = ["Weekday BreakFast:     0500Hrs - 1159Hrs",
                                      "Weekday Lunch/Dinner:    1200Hrs - 1959Hrs",
                                      "Weekday After 2000Hrs:     Close", "Weekend:     Close"]

            operating_Hour = self.malayStall_OpHour

        else:
            self.koreanStall_OpHour = ["Weekday BreakFast:    0500Hrs - 1159Hrs",
                                       "Weekday Lunch/Dinner:    1200Hrs - 1959Hrs",
                                       "Weekday After 2000Hrs:     Close", "Weekend:     Close"]
            operating_Hour = self.koreanStall_OpHour

        for i in operating_Hour:
            if (i != operating_Hour[-1]):
                op_hour_Display = op_hour_Display + i + "\n\n"
            else:
                op_hour_Display = op_hour_Display + i

        return op_hour_Display

    def setDay(self, inputDay):
        self.day = inputDay

    def getDay(self):
        return self.day

    def setStallName(self, inputStallName):
        self.stallName = inputStallName

    def getStallName(self):
        return self.stallName


db = DataBase()
