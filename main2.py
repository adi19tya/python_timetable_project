import Derived_Data
import random

class Teacher:
    
    def __init__(self, max_subjects):
        self.daily_hours = 3
        self.max_subjects = max_subjects
        self.subjects_taught = []
        self.section_subject_list = {} 
    
    # A single teacher teaches a given subject for  a section
    def check_section_subject(self, secSub_comination):
        # check if the section subject combination is already being taught
        if secSub_comination[0] in self.section_subject_list:
            # if different subject is taught for the same section by same teacher, return invalid combination
            if self.section_subject_list[secSub_comination[0]] != secSub_comination[1]:
                return False

        # if the section subject combination is not present add to the dictionary.
        else:
            self.section_subject_list[secSub_comination[0]] = secSub_comination[1]
            return True
    
    # No teacher will teach more than 3 hours in a day
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
    

    # No teacher will teach more than 3 subjects
    def check_max_subjects(self, subject):
        if self.max_subjects > 0:   # check if the subject count is less less than 1
            self.max_subjects -= 1
            self.subjects_taught.append(subject)
            return True
        else:
            return False
            
        
        
    
    def display_timetable(self, time_table):
        
        pass
    

class Section:
    def __init__(self, subjects):
        self.total_hours_taught = 0
        self.subject_hour = {}
        
    
        
    # Each section has 4 hours of class for 5 days in a week, 20 classes total in a week
    
    
    def add_subject_to_hour_count(self, subject):
        if subject not in self.subject_hour:    # add subject to subject hour dictionary if not present
            self.subject_hour[subject] = 1
            
        else:
            if self.subject_hour[subject] < 4:   # check if the subject is alreaady sheduled for 4 hours
                self.subject_hour[subject] += 1
                return True
            else:
                return False
                
    
    # check if each class has had 20 periods: 4 periods of each of the 5 subject
    def check_subjectclass_count(self):
        self.total_hours_taught = 0
        for i in self.subject_hour:
            self.total_hours_taught += i
        
        if self.total_hours_taught == 20:
            return True
        else:
            return False
        
    def display_timetable(self, timetable):
        pass
        
        
class Timetable:
    
    
    def __init__(self, timetable, days, number_of_sections, number_of_hours, subjects):
        self.timetable = timetable
        self.days = days
        self.number_of_sections = number_of_sections
        self.number_of_hours = number_of_hours
        self.time_slots = ["8-9", "9-10", "11-12", "12-1"]
        self.subjects = subjects
        
    
    # initiate an empty data structure to represnt a timetable and its data
    def initiate_timetable(self):
    
        for i in range(len(self.days)):
            current_day = self.days[i]
            self.timetable[current_day] = []
        
            for j in range(self.number_of_sections):
                self.timetable[current_day].append({})
        #print("\nEmpty Datastructure: ", self.timetable)
  
    def add_teacherSubject_pair(self, teacher_list, section_list):
        subject_pointer = 0
        teacher_pointer = 0
        section_pointer = 0
        subject_pointer =  random.randint(0, len(self.subjects))
        pass
    
    def revert_previous_addition(self):
        pass


time_table = {}  

# start with one teacher

    
    
    
time_table_ds = Timetable(time_table, Derived_Data.days, Derived_Data.number_of_sections, Derived_Data.number_of_hours, Derived_Data.subjects)
  
time_table_ds.initiate_timetable()

print("Emtpy TIme table Data Structure: ", time_table)


teacher_vaiable_database = []
for teacher in range(Derived_Data.number_of_teachers):
    teacher_vaiable_database.append(Teacher(Derived_Data.number_of_subjects_per_teacher))

    
