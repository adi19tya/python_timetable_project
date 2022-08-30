import Derived_Data
import pandas as pd

#print(Derived_Data.teacher_subjects

# --------------------Initiate the timetable data structure--------------------#

def initiate_timetable(time_table, days, number_of_sections, number_of_hours):
    
    for i in range(len(days)):
        current_day = days[i]
        time_table[current_day] = []
        
        for j in range(number_of_sections):
            time_table[current_day].append({})
    print("\nEmpty Datastructure: ", time_table)
    
    
# -----------------------Fill in the timetable---------------------------------#

def fill_timetable(time_table, teacher_subjects, days, number_of_sections, number_of_hours, subjects):
    teacher_list = list(teacher_subjects.keys())
    subject_pointer = 0
    teacher_pointer = 0
    #print("days: ", time_table[days[0]][0][teacher_list[0]])
    #for i in range(len(days)):
    for j in range(number_of_sections):
        teacher_pointer = j # 0
        subject_pointer = j # 0
        for k in range(number_of_hours): # 0 1 2 3
            time_table[days[0]][j][teacher_list[teacher_pointer]] = subjects[subject_pointer]
            #print(time_table)
            teacher_pointer += 2
            if teacher_pointer > len(teacher_list) - 1:
                teacher_pointer -= len(teacher_list)
            subject_pointer += 2
            if subject_pointer > len(subjects) - 1:
                subject_pointer -= len(subjects)
    
    for i in range(1, len(days)):
        current_day = days[i]
        previous_day = days[i-1]
        for j in range(number_of_sections):
            if j == 0:
                time_table[current_day][j] = time_table[previous_day][-1]
            else:
                time_table[current_day][j] = time_table[previous_day][j - 1]
                
'''
def fill_timetable(time_table, teacher_subjects, days, number_of_sections, number_of_hours, subjects):
    teacher_list = list(teacher_subjects.keys())
    subject_pointer = 0
    teacher_pointer = 0
    #for i in range(len(days)):
    for i in range(1):
        current_day = days[i]
        for j in range(number_of_sections):
            teacher_pointer = j
            subject_pointer = j
            for k in range(number_of_hours):
                time_table[current_day][j][teacher_list[teacher_pointer]] = subjects[subject_pointer]
                teacher_pointer += 2
                if teacher_pointer > len(teacher_list):
                    teacher_pointer -= len(teacher_list)
                subject_pointer += 2
                if subject_pointer > len(subjects):
                    subject_pointer -= len(subjects)
    
'''    
# ----------------------------display timetable---------------------------------#

def section_timetable(time_table, section_number, days):
    master_list = []
    #print(days, type(days))
    for day in range(len(days)):
        master_list.append([])
    
    for j in range(len(days)):
        master_list[j].append(days[j])
        section = time_table[days[j]][section_number-1]
        #print(section, type(section))
        for i in section:
            pair = [i, section[i]]
            #print(pair)
            master_list[j].append(pair)
    
    time_table_df = pd.DataFrame(master_list, columns = ["DAY", "8-9", "9-10", "11-12", "12-1"])
    return time_table_df

def teacher_timetable():
    pass
    

time_table = {}
initiate_timetable(time_table, Derived_Data.days, Derived_Data.number_of_sections, Derived_Data.number_of_hours)

fill_timetable(time_table, Derived_Data.teacher_subjects, Derived_Data.days, Derived_Data.number_of_sections, Derived_Data.number_of_hours, Derived_Data.subjects)
print("\nFilled Data Structure: ", time_table)

operation = "Y"
while operation != "n":
    which_timetable = int(input("\n\nWhich timetable do you want to display:\nSection - 1\nTeacher - 2\n "))
    
    if which_timetable == 1:
        which_section = int(input("\nWhich section timetable do you want to display:\nSection A - 1\nSection B - 2\nSection C - 3\nSection D - 4\nSection E - 5\n "))
        table = section_timetable(time_table, which_section, Derived_Data.days)
        print("\nThe time table for the section\n", table)
        
    elif which_timetable == 2:
        which_teacher = int(input("\nWhich teacher's timetable do you want to display:\nTeacher 1 - 1\nTeacher 2 - 2\nTeacher 3 - 3\nTeacher 4 - 4\nTeacher 5 - 5\nTeacher 6 - 6\nTeacher 7 - 7\n"))
        teacher_timetable(time_table, which_teacher)
        
    operation = input("\nFind another time table?\n[Y/n]")