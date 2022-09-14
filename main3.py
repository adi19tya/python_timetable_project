import Derived_Data

class School:

    def __init__(self):
        self.teacherList = []
        self.sectionList = []
        self.subjectList = []
        self.timetable = {}
        self.pointerHistory = [[0,0]] * 100
        

    def addTeacher(self, teacher):
        self.teacherList.append(teacher)
    
    def addSection(self, section):
        self.sectionList.append(section)

    def addSubject(self, subject):
        self.subjectList.append(subject)

    def initializeTimeTable(self):
        print("\nTeacher List:", self.teacherList)
        print("\nSection List:", self.sectionList)
        print("\nSubject List:", self.subjectList)
        timeSlots = Timeslot.getTimeSlots()
        for i in range(len(timeSlots)):
            self.timetable[(timeSlots[i].day, timeSlots[i].timeslot)] = {}
            for k in range(len(self.sectionList)): # number of sections - 5
                self.timetable[(timeSlots[i].day, timeSlots[i].timeslot)][self.sectionList[k].sectionName] = None
        
        print("\n\n\nEmpty Data Structure:\n\n", self.timetable)



    def generateTimetable(self):

        # initialize the history dictionary
        # historyDict = {}
        # for k in range(len(self.sectionList) * len(self.timetable)):
        #     historyDict[k] = []

        teacherPointer = 0

        # start filling in the timetable
        timeTableKeys = list(self.timetable.keys())
        for sectionIdex in range(len(self.sectionList)):
            teacherSubjectCombinations = {}  
            listOfTeachers =  list(DPS.sectionList[sectionIdex].teacherSubjectCombinatons.keys()) # need to make list of objects
            for i in range(len(listOfTeachers)):
                teacherSubjectCombinations[listOfTeachers[i]] = DPS.sectionList[sectionIdex].teacherSubjectCombinatons[listOfTeachers[i]]
            print("\n\n\nTeacher Objects: ", listOfTeachers)
            print("\n\n\nTeacher Subject Maps: ", teacherSubjectCombinations)
            # listOfSubjects = []
            # for teacher in listOfTeachers:
            #     listOfSubjects.append(DPS.sectionList[sectionIdex].teacherSubjectCombinatons[teacher])
            #     pass    
            for slotIndex in range(len(timeTableKeys)):
                
                currentSection = self.sectionList[sectionIdex]
                currentSlot = timeTableKeys[slotIndex]

                print("\n\n----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("\nTimeSLot: ", currentSlot)  # print the keys of the time table - day and timeslot
                print("Section: ", currentSection.sectionName) # print the section name

                # iterate through teachers
                originalTeacher = listOfTeachers[teacherPointer].teacherName
                while True:
    
                    assigned = False
                    #iterate through subjects
                    #originalSubject = teacherSubjectCombinations[listOfTeachers[teacherPointer]]
                    while True:
                        currentTeacher = listOfTeachers[teacherPointer]
                        currentSubject = teacherSubjectCombinations[listOfTeachers[teacherPointer]] 
                        print("\nFirst Combo", currentTeacher.teacherName, currentSubject)

                        secSubPair = [currentSection.sectionName, currentSubject]
                        #print(secSubPair)

                        #condition1 = currentTeacher.check_section_subject(secSubPair)
                        condition2 = currentTeacher.check_daily_hours(currentSlot[0])
                        condition3 = currentTeacher.check_max_subjects(currentSubject)
                        condition4 = currentTeacher.checkTimeSlotOccurance(currentSlot[1], currentSlot[0])
                        #condition5 = currentSection.checkSubjectPerDayForOneSection(currentSlot[0], currentSubject)
                        condition6 = currentSection.checkSubjectCount(currentSubject)
                
                        print("\n\nCONDITION CHECK: ")
                        #print("check_section_subject: ", condition1)
                        print("check_daily_hours: ", condition2)
                        print("check_max_subjects: ", condition3)
                        print("checkTimeSlotOccurance: ", condition4)
                        #print("checkSubjectPerDayForOneSection", condition5)
                        print("checkSubjectCount: ", condition6)

                        if (condition2 and condition3 and condition4 and condition6):
                            # enter the [teacher, subject] pair into the timeslot for the section
                            print("\nCommited Current Combo", currentTeacher.teacherName, currentSubject)
                            self.timetable[currentSlot][currentSection.sectionName] = [currentTeacher.teacherName, currentSubject]
                            for i in self.timetable:
                                print(i, self.timetable[i])

                            # add sec sub comb to teach object for condition 1
                            #currentTeacher.addCommittedSecSubToDict(secSubPair)
                            currentTeacher.subractHourForCommitedPair(currentSlot[0])                             # condition 2
                            currentTeacher.subMaxSubForCommittedPair(currentSubject)                              # condition 3
                            currentTeacher.addTimeSlotToDay(currentSlot[1], currentSlot[0])                       # condition 4
                            #currentSection.addCommittedPairForDaySubCondition(currentSlot[0], currentSubject)    # condition 5
                            currentSection.addHourToSubject(currentSubject)                                       # condition 6
                            assigned = True
                            
                            #teacherPointer += 1

                            break

                        # if teacherPointer == len(listOfTeachers) - 1:
                        #     break
                        
                        # teacherPointer += 1

                    # if (assigned == True):
                    #     break

                    # Go to the next teacher. If it is the last teacher, go to the first teacher
                    if teacherPointer >= len(listOfTeachers) - 1:
                        teacherPointer = 0
                    else:
                        teacherPointer += 1

                    if (assigned == True):
                        break

                    if originalTeacher == teacherPointer:
                        print("ALL POSSIBLE COMBINATIONS CHECKED")
                        for i in self.timetable:
                            print(i, self.timetable[i])
                        # print("\n\n", self.timetable)
                        # print("\nPointer History: \n", self.pointerHistory)
                        quit()

        print("\n\nFILLED TIMETABLE: \n")
        for i in self.timetable:
            print(i, self.timetable[i])
            
        

    def getTeacherTimetable(self, teacher, calender):
        timeTableKeys = list(self.timetable.keys())

        for timeSlot in range(len(timeTableKeys)):
            dayHourComb = timeTableKeys[timeSlot]
            day = dayHourComb[0]
            hour = dayHourComb[1]

            ifFlag = False
            for slotSection in self.timetable[dayHourComb]:
                if self.timetable[dayHourComb][slotSection][0] == teacher:
                    section = slotSection
                    subject = self.timetable[dayHourComb][slotSection][1]
                    ifFlag = True
                
                if ifFlag == False:
                    section = "NO"
                    subject = "CLASS"
                
            
            calender[day][hour] = [section, subject]
        
        for cDay in calender:
            print(cDay)
            for dSlot in calender[cDay]:
                print("\t", dSlot, end = "\t")
                print(calender[cDay][dSlot], end = "\n\n")

    def getSectionTimetable(self, section, calender):

        timeTableKeys = list(self.timetable.keys())
        #print(section)
        for timeSlot in range(len(timeTableKeys)):
            dayHourComb = timeTableKeys[timeSlot]
            day = dayHourComb[0]
            hour = dayHourComb[1]
            calender[day][hour] = self.timetable[dayHourComb][section]

        for cDay in calender:
            print(cDay)
            for dSlot in calender[cDay]:
                print("\t", dSlot, end = "\t")
                print(calender[cDay][dSlot], end = "\n\n")



class Timeslot:

    timeslots = []

    @staticmethod 
    def initializeTimeslots():
        days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
        timeSlotsInADay = ["8-9", "9-10", "11-12", "12-1"]
        

        for d in range(len(days)):
            #Timeslot.timeslots[days[d]] = []
            for ts in range(len(timeSlotsInADay)):
                #Days_Timeslot_object_dataset.append(Timeslot(Days[d], TimeSlots[ts]))
                #Timeslot.timeslots[days[d]].append(Timeslot(days[d], timeSlotsInADay[ts]))
                Timeslot.timeslots.append(Timeslot(days[d], timeSlotsInADay[ts]))

        
        print("\n\nTimeslot objects:\n\n", Timeslot.timeslots)

    def __init__(self, day, timeslot):
        self.day = day
        self.timeslot = timeslot
    
    def getTimeSlots():
        #print(Timeslot.timeslots)
        return Timeslot.timeslots
        

    
class Teacher:

    maxSubjects = 3
    maxDailyHours = 3

    def __init__(self, teacherName):
        self.teacherName = teacherName
        self.dailyHourCount = {"MONDAY":0, "TUESDAY":0, "WEDNESDAY":0, "THURSDAY":0, "FRIDAY":0}
        self.subjectCount = 0
        self.subjects_taught = []
        self.section_subject_list = {}
        self.timeSlotOccueance = {"MONDAY":[], "TUESDAY":[], "WEDNESDAY":[], "THURSDAY":[], "FRIDAY":[]}

    def getTeacherName(self):
        return self.teacherName

    # Check the conditions

    # # Condition 1: One teacher, One Section, One Subject
    # def check_section_subject(self, secSub_comination):
    #     print("list of sections and respective subjects taught: ", self.section_subject_list)
    #     #print("Teacher Name: ", self.teacherName)
    #     #print("Section Subject List:", self.section_subject_list)
    #     print("Incoming Sec Subject: ", secSub_comination)
    #     # check if the section subject combination is already being taught
    #     if secSub_comination[0] in self.section_subject_list:   # checking if section is being taught
    #         # if different subject is taught for the same section by same teacher, return invalid combination
    #         if self.section_subject_list[secSub_comination[0]] != secSub_comination[1]:
    #             return False
    #         else:
    #             return True

    #     # if the section subject combination is not present add to the dictionary.
    #     else:
    #         return True

    # def addCommittedSecSubToDict(self, secSubComb):
    #     self.section_subject_list[secSubComb[0]] = secSubComb[1]
    


    # Condition 2: No teacher will teach more than 3 hours in a day
    def check_daily_hours(self, currentDay):
        # check if hour balance is remaining
        if self.dailyHourCount[currentDay] == Teacher.maxDailyHours:
            return False
        else:
            return True
    
    def subractHourForCommitedPair(self, currentDay):
        self.dailyHourCount[currentDay] += 1



    # Condition 3: No teacher will teach more than 3 subjects
    def check_max_subjects(self, subject):
        if subject in self.subjects_taught:
            return True
        else:    
            if self.subjectCount == Teacher.maxSubjects:   # check if the subject count is less less than 1
                return False
            else:
                return True
    
    def subMaxSubForCommittedPair(self, subject):
        if subject in self.subjects_taught:
            pass
        else:
            self.subjectCount += 1
            self.subjects_taught.append(subject)



    # Condition 4: Same teacher can not teach in the same timeslot
    def checkTimeSlotOccurance(self, timeslot, day):

        if timeslot in self.timeSlotOccueance[day]:
            return False
        else:
            return True
    
    def addTimeSlotToDay(self, timeslot, day):
        self.timeSlotOccueance[day].append(timeslot)
        #print("TimeSlot Day:", self.timeSlotOccueance)
    


class Section:

    hoursASubjectMustBeTaught = Derived_Data.number_of_hours

    def __init__(self, sectionName):
        self.sectionName = sectionName
        self.teacherSubjectCombinatons = {}
        self.daySubjectDict = {"MONDAY":[], "TUESDAY":[], "WEDNESDAY":[], "THURSDAY":[], "FRIDAY":[]}
        self.subjectHourCount = {}

    def getSectionName(self):
        return self.sectionName

    # Condition 5: subject taught to a section can not repeat in a day
    def checkSubjectPerDayForOneSection(self, day, subject):
        # print("\n\nInside the condition!!")
        # print(day)
        # print(self.daySubjectDict[day])
        if subject in self.daySubjectDict[day]:
            print("False")
            return False
        else:
            print("True")
            return True
        

    def addCommittedPairForDaySubCondition(self, day, subject):
        self.daySubjectDict[day].append(subject)

    # Condition 6: each subject is taught 4 times for each section
    def checkSubjectCount(self, subject):
        if self.subjectHourCount[subject] == Section.hoursASubjectMustBeTaught:
            return False
        else:
            return True

    def addHourToSubject(self, subject):
        self.subjectHourCount[subject] += 1



class History:

    # Condition 1: teacher can only teach one suject for 1 section: teacher class - section_subject 
    # Condition 2: teacher can only teach 3 hours in a day: teacher class - daily_hours
    # Condition 3: teacher can teach maximum 3 subjects: teacher class - maxSubjects
    # Condition 4: teacher can only be allotted to one section in a slot: teacher class - timeSlotOccureance

    def __init__(self, teacherPointer, subjectPointer, cond1, cond2, cond3, cond4, cond5):
        self.teacherPointer = teacherPointer
        self.subjectPointer = subjectPointer
        self.cond1 = cond1
        self.cond2 = cond2
        self.cond3 = cond3
        self.cond4 = cond4
        self.cond5 = cond5
        


# Create Timeslot Objects
Timeslot.initializeTimeslots()

# initate school object
DPS = School()


# initiate the subjects
#numberofSubjects = Derived_Data.number_of_subjects
subjects = Derived_Data.subjects
for i in subjects:
    DPS.addSubject(i)

# initiate the sections
sections = Derived_Data.sections
for i in range(len(sections)):
    #sectionName = input("Enter the Section Name: ")
    sectionInstance = Section(sections[i])
    DPS.addSection(sectionInstance)
    for j in range(len(DPS.subjectList)):
        DPS.sectionList[i].subjectHourCount[DPS.subjectList[j]] = 0

# initiate the teachers
# numberOfTeachers = Derived_Data.number_of_teachers
# print("\n\nMinimum Number of Required Teachers: ", numberOfTeachers)
'''
for i in range(numberOfTeachers):
    teacherName = input("Enter the Teacher Name: ")
    teacherInstance = Teacher(teacherName)
    DPS.addTeacher(teacherInstance)'''

teachers = ["t1", "t2", "t3", "t4", "t5", "t6", "t7", "t8", "t9"]
for i in teachers:
    teacherInstance = Teacher(i)
    DPS.addTeacher(teacherInstance)


# Create viable section:teacher:subject combinations
k = 0
for i in range(len(sections)):
    for j in range(len(subjects)):
        DPS.sectionList[i].teacherSubjectCombinatons[DPS.teacherList[k]] = DPS.subjectList[j]
        k = (k + 1) % len(teachers)

# print the teacher:section:subject combination
for i in range(len(sections)):
    print("Teacher:Section:Subject Combination:  ", DPS.sectionList[i].sectionName, DPS.sectionList[i].teacherSubjectCombinatons)
    


DPS.initializeTimeTable()
DPS.generateTimetable()

calenderDataStructure = {"MONDAY":{"7-8":None, "8-9":None, "9-10":None, "10-11":None, "11-12":None, "12-1":None, "1-2": None, "2-3":None, "3-4":None, "4-5":None, "5-6":None, "6-7":None}, "TUESDAY":{"7-8":None, "8-9":None, "9-10":None, "10-11":None, "11-12":None, "12-1":None, "1-2": None, "2-3":None, "3-4":None, "4-5":None, "5-6":None, "6-7":None}, "WEDNESDAY":{"7-8":None, "8-9":None, "9-10":None, "10-11":None, "11-12":None, "12-1":None, "1-2": None, "2-3":None, "3-4":None, "4-5":None, "5-6":None, "6-7":None}, "THURSDAY":{"7-8":None, "8-9":None, "9-10":None, "10-11":None, "11-12":None, "12-1":None, "1-2": None, "2-3":None, "3-4":None, "4-5":None, "5-6":None, "6-7":None}, "FRIDAY":{"7-8":None, "8-9":None, "9-10":None, "10-11":None, "11-12":None, "12-1":None, "1-2": None, "2-3":None, "3-4":None, "4-5":None, "5-6":None, "6-7":None}}



userInterface = "Y"

while userInterface == "Y":
        operation = int(input("\n\n\n\nWhose information do you want to display?\nTeacher Information - 1\nSection Information - 2\n"))

        # display teacher information
        if operation == 1:
            teacherOp = int(input("\n\nWhich teacher's information do you want to see?\nT1 - 1\nT2 - 2\nT3 -3\nT4 -4\nT5 -5\nT6 -6\nT7 -7\nT8 -8\nT9 -9\n"))
            
            teacherChosen = DPS.teacherList[teacherOp-1]

            teacherCalender = calenderDataStructure

            print("\n Time Table of teacher ", teacherChosen.teacherName, end = "\n\n")
            DPS.getTeacherTimetable(teacherChosen.teacherName, teacherCalender)

            print("\nSubjects Taught: \n\n\t", teacherChosen.subjects_taught)
            print("\n\nSection And the Respective Subjects Taught: \n\n\t", teacherChosen.section_subject_list)
            print("\n\nHours taught each day: \n\n\t", teacherChosen.timeSlotOccueance)
        
        else:
            sectionOp = int(input("\n\nWhich section's informtation do you want to see?\nA - 1\nB - 2\nC - 3\nD - 4\nE - 5\n"))

            sectionChosen = DPS.sectionList[sectionOp - 1]

            sectionCalender = calenderDataStructure

            print("\nTime Table of section ", sectionChosen.sectionName, end = "\n\n")
            DPS.getSectionTimetable(sectionChosen.sectionName, sectionCalender)

            print("\n\nNumber of hours each subject has been taught: \n\n\t", sectionChosen.subjectHourCount)
    
        userInterface = input("\n\n\n\n\nWould you like to see more information: [Y/n]\n\n")





'''
EXTRA SUBJECTS :
Computational Geometry
Robot Manipulators
Diffusional Mass Transfer Operations
Atmospheric Environmental Engineering
Enzyme technology
'''