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
        historyDict = {}
        for k in range(len(self.sectionList) * len(self.timetable)):
            historyDict[k] = []
            
        # start filling in the timetable
        timeTableKeys = list(self.timetable.keys())
        for j in range(len(self.sectionList)):      
            for i in range(len(self.timetable)):
                
                print("\n\n----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("\nTimeSLot: ", timeTableKeys[i])  # print the keys of the time table - day and timeslot
                print("Section: ", self.sectionList[j].sectionName) # print the section name

                # if len(historyDict[i * len(self.sectionList)]) == 0:
                #     teacherPointer = 0
                #     subjectPointer = 0
                #     snapShot = History(0, 0, self.teacherList[0].section_subject_list, self.teacherList[0].daily_hours, self.teacherList[0].subjects_taught, self.teacherList[0].timeSlotOccueance, self.sectionList.daySubjectDict)
                #     historyDict[i * len(self.sectionList) + j] = snapShot
                
                (teacherPointer, subjectPointer) = self.pointerHistory[i * len(self.sectionList) + j]

                currentTeacher = self.teacherList[teacherPointer]
                currentSubject = self.subjectList[subjectPointer]
                currentSection = self.sectionList[j]

                print("\nFirst Combo", currentTeacher.teacherName, currentSubject)

                secSubPair = [self.sectionList[j].sectionName, self.subjectList[subjectPointer]]
                #print(secSubPair)


                condition1 = currentTeacher.check_section_subject(secSubPair)
                condition2 = currentTeacher.check_daily_hours(timeTableKeys[i][0])
                condition3 = currentTeacher.check_max_subjects(currentSubject)
                condition4 = currentTeacher.checkTimeSlotOccurance(timeTableKeys[i][1], timeTableKeys[i][0])
                condition5 = currentSection.checkSubjectPerDayForOneSection(timeTableKeys[i][0], currentSubject)
                condition6 = currentSection.checkSubjectCount(currentSubject)
                
                print("\n\nCONDITION CHECK: ")
                print("check_section_subject: ", condition1)
                print("check_daily_hours: ", condition2)
                print("check_max_subjects: ", condition3)
                print("checkTimeSlotOccurance: ", condition4)
                print("checkSubjectPerDayForOneSection", condition5)
                print("checkSubjectCount: ", condition6)



                while not(condition1) or not(condition2) or not(condition3) or not(condition4) or not(condition6):  # add conditions here
                                        
                    print("\n\nENTERED LOOP")
                    #print("\nInside While Loop,  teacher and subject pointer (BEFORE): ", currentTeacher, currentSubject)

                    # Increment 
                    if (teacherPointer == len(self.teacherList) - 1) and (subjectPointer == len(self.subjectList) - 1):
                        print("ALL POSSIBLE COMBINATIONS CHECKED")
                        for i in self.timetable:
                            print(i, self.timetable[i])
                        #print("\n\n", self.timetable)
                        print("\nPointer History: \n", self.pointerHistory)
                        quit()
                    else:
                        
                        if subjectPointer == len(self.subjectList) - 1:
                            teacherPointer += 1
                            subjectPointer = 0
                        else:
                            subjectPointer += 1

                    currentTeacher = self.teacherList[teacherPointer]
                    currentSubject = self.subjectList[subjectPointer]

                    print("\n\nTimeslot: ", timeTableKeys[i])
                    print("Section: ", self.sectionList[j].sectionName)
                    print("Teacher, Subject pointer: ", currentTeacher.teacherName, currentSubject)


                    secSubPair = [self.sectionList[j].sectionName, self.subjectList[subjectPointer]]

                    condition1 = currentTeacher.check_section_subject(secSubPair)
                    condition2 = currentTeacher.check_daily_hours(timeTableKeys[i][0])
                    condition3 = currentTeacher.check_max_subjects(currentSubject)
                    condition4 = currentTeacher.checkTimeSlotOccurance(timeTableKeys[i][1], timeTableKeys[i][0])
                    condition5 = currentSection.checkSubjectPerDayForOneSection(timeTableKeys[i][0], currentSubject)
                    condition6 = currentSection.checkSubjectCount(currentSubject)
                    
                    print("\nCHECK Condition Inside: ")
                    print("check_section_subject: ", condition1)
                    print("check_daily_hours: ", condition2)
                    print("check_max_subjects: ", condition3)
                    print("checkTimeSlotOccurance: ", condition4)
                    print("checkSubjectPerDayForOneSection", condition5)
                    print("checkSubjectCount: ", condition6)

                    print("\n\n Not Commited Current Combo", currentTeacher.teacherName, currentSubject)

                # enter the [teacher, subject] pair into the timeslot for the section
                print("\nCommited Current Combo", currentTeacher.teacherName, currentSubject)
                self.timetable[timeTableKeys[i]][self.sectionList[j].sectionName] = [currentTeacher.teacherName, currentSubject]
                self.pointerHistory[i * len(self.sectionList) + j] = [teacherPointer, subjectPointer]
                print("\n\nTimetable: \n", self.timetable)
                # add sec sub comb to teach object for condition 1
                currentTeacher.addCommittedSecSubToDict(secSubPair)  
                currentTeacher.subractHourForCommitedPair(timeTableKeys[i][0])    # condition 2
                currentTeacher.subMaxSubForCommittedPair(currentSubject)       # condition 3
                currentTeacher.addTimeSlotToDay(timeTableKeys[i][1], timeTableKeys[i][0])     # condition 4
                currentSection.addCommittedPairForDaySubCondition(timeTableKeys[i][0], currentSubject)     # condition 5
                currentSection.addHourToSubject(currentSubject)  # condition 6
        print("\n\nFILLED TIMETABLE: \n")
        for i in self.timetable:
            print(i, self.timetable[i])
            
        

    def getTeacherTimetable(self, teacher):
        pass

    def getSectionTimetable(self, section):
        pass



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

    # Condition 1: A single teacher teaches one subject for a section
    def check_section_subject(self, secSub_comination):
        print("list of sections and respective subjects taught: ", self.section_subject_list)
        #print("Teacher Name: ", self.teacherName)
        #print("Section Subject List:", self.section_subject_list)
        print("Incoming Sec Subject: ", secSub_comination)
        # check if the section subject combination is already being taught
        if secSub_comination[0] in self.section_subject_list:   # checking if section is being taught
            # if different subject is taught for the same section by same teacher, return invalid combination
            if self.section_subject_list[secSub_comination[0]] != secSub_comination[1]:
                return False
            else:
                return True

        # if the section subject combination is not present add to the dictionary.
        else:
            return True

    def addCommittedSecSubToDict(self, secSubComb):
        self.section_subject_list[secSubComb[0]] = secSubComb[1]
    


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
        print("TimeSlot Day:", self.timeSlotOccueance)
    


class Section:

    hoursASubjectMustBeTaught = 4

    def __init__(self, sectionName):
        self.sectionName = sectionName
        self.daySubjectDict = {"MONDAY":[], "TUESDAY":[], "WEDNESDAY":[], "THURSDAY":[], "FRIDAY":[]}
        self.subjectHourCount = {"S1" : 0, "S2" : 0, "S3" : 0, "S4" : 0, "S5" : 0}

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

# initiate the sections
#numberOfSections = int(input("Enter the number of sections: "))
sections = Derived_Data.sections
for i in sections:
    #sectionName = input("Enter the Section Name: ")
    sectionInstance = Section(i)
    DPS.addSection(sectionInstance)

# initiate the teachers
numberOfTeachers = Derived_Data.number_of_teachers
print("\n\nMinimum Number of Required Teachers: ", numberOfTeachers)
'''
for i in range(numberOfTeachers):
    teacherName = input("Enter the Teacher Name: ")
    teacherInstance = Teacher(teacherName)
    DPS.addTeacher(teacherInstance)'''

teachers = ["t1", "t2", "t3", "t4", "t5", "t6", "t7", "t8", "t9", "t10", "t11", "t12", "t13", "t14"]
for i in teachers:
    teacherInstance = Teacher(i)
    DPS.addTeacher(teacherInstance)
    

# initiate the subjects
#numberofSubjects = Derived_Data.number_of_subjects
subjects = Derived_Data.subjects
for i in subjects:
    DPS.addSubject(i)

DPS.initializeTimeTable()
DPS.generateTimetable()
