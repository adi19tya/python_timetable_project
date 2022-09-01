import Derived_Data

class School:

    def __init__(self):
        self.teacherList = []
        self.sectionList = []
        self.subjectList = []
        self.timetable = {}
        self.pointerHistory = [[0,0]] *100

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
        timeTableKeys = self.timetable.keys()
        for i in range(len(self.timetable)):       # number of tuples per time slot
            for j in range(len(self.sectionList)):

                teacherPointer = self.pointerHistory[i*j][0]
                subjectPointer = self.pointerHistory[i*j][1]


                currentTeacher = self.teacherList[teacherPointer]
                currentSubject = self.subjectList[subjectPointer]


                currentIterDay = timeTableKeys[i][0]
                if i == 0:
                    previosIterDay = timeTableKeys[i][0]
                else:
                    previosIterDay = timeTableKeys[i-1][0]
                
                if currentIterDay == previosIterDay:
                    newDay = False
                else:
                    newDay = True


                secSubPair = [self.sectionList[j].sectionName, self.subjectList[subjectPointer]]
                
                tempVar = 0
                while currentTeacher.check_section_subject(secSubPair) == False or currentTeacher.check_daily_hours(newDay) == False or currentTeacher.check_max_subjects(currentSubject) == False:  # add conditions here
                    
                    # increment teacherPointer and/or subjectPointer
                    if subjectPointer == len(self.subjectList) + 1:
                        teacherPointer += 1
                        subjectPointer = 0
                    else:
                        subjectPointer += 1

                    currentTeacher = self.teacherList[teacherPointer]
                    currentSubject = self.subjectList[subjectPointer]

                # enter the [teacher, subject] pair into the timeslot for the section
                self.timetable[timeTableKeys[i]][self.sectionList[j]] = [currentTeacher, currentSubject]
        print("\n\nfilled timetable: \n", self.timetable)
            
        

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

    def __init__(self, teacherName):
        self.teacherName = teacherName
        self.daily_hours = 3
        self.max_subjects = 3
        self.subjects_taught = []
        self.section_subject_list = {}

    def getTeacherName(self):
        return self.teacherName

    # Check the conditions

    # Condition 1: A single teacher teaches a given subject for  a section
    def check_section_subject(self, secSub_comination):
        # check if the section subject combination is already being taught
        if secSub_comination[0] in self.section_subject_list:   # checking if section is being taught
            # if different subject is taught for the same section by same teacher, return invalid combination
            if self.section_subject_list[secSub_comination[0]] != secSub_comination[1]:
                return False

        # if the section subject combination is not present add to the dictionary.
        else:
            self.section_subject_list[secSub_comination[0]] = secSub_comination[1]
            return True
    
    # Condition 2: No teacher will teach more than 3 hours in a day
    def check_daily_hours(self, new_day):
        # reset daily_hours to 3 if it is a new day
        if new_day == True:
            self.daily_hours = 3
            
        # check if hour balance is remaining
        if self.daily_hours > 0:
            self.daily_hours -= 1
            return True
        else:
            return False

    # Condition 3: No teacher will teach more than 3 subjects
    def check_max_subjects(self, subject):
        if self.max_subjects > 0:   # check if the subject count is less less than 1
            self.max_subjects -= 1
            self.subjects_taught.append(subject)
            return True
        else:
            return False
    

class Section:

    def __init__(self, sectionName):
        self.sectionName = sectionName
        
    

class Subject:
    pass



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
for i in range(numberOfTeachers):
    teacherName = input("Enter the Teacher Name: ")
    teacherInstance = Teacher(teacherName)
    DPS.addTeacher(teacherInstance)

# initiate the subjects
#numberofSubjects = Derived_Data.number_of_subjects
subjects = Derived_Data.subjects
for i in subjects:
    DPS.addSubject(i)

DPS.initializeTimeTable()
DPS.generateTimetable()

