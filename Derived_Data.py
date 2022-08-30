fixedData = open("Fixed_Data.txt", "r")


# --------------read SECTIONS data and create a list-------------------------#
sections = fixedData.readline()
sections = sections.strip()
sections = sections.split(" ")
for i in range(2):
    sections.pop(0)
print("Sections :", sections, type(sections))

number_of_sections = len(sections)

# ------------------- read DAYS data and create list--------------------------#
days = fixedData.readline()
days = days.strip()
days = days.split(" ")
for i in range(2):
    days.pop(0)
print("\nDays: ", days, type(days))

number_of_days = len(days)

# ------------------------read the number of HOURS per day---------------------# 
hours = fixedData.readline()
hours = hours.strip()
hours = hours.split(" ")
for i in range(2):
    hours.pop(0)
#print(hours, type(hours))
number_of_hours = int(hours[0])
print("\nNumber of hours: ", number_of_hours)


# --------------------------READ SUBJECTS AND CREATE A LIST---------------------#

subjects = fixedData.readline()
subjects = subjects.strip()
subjects = subjects.split(" ")
for i in range(2):
    subjects.pop(0)
print("\nSubjects: ", subjects, type(subjects))

number_of_subjects = len(subjects)

# ------------------------ read the number of subjects per teacher --------------#

max_subjects = fixedData.readline()
max_subjects = max_subjects.strip()
max_subjects = max_subjects.split(" ")
for i in range(2):
    max_subjects.pop(0)
#print(max_subjects, type(max_subjects))
number_of_subjects_per_teacher = int(max_subjects[0])
print("\nMaximum Number of subjects per teacher: ", number_of_subjects_per_teacher)

# ----------------------- read and assign the names to a list----------------------#

names = fixedData.readline()
names = names.strip()
names = names.split(" ")
for i in range(2):
    names.pop(0)
print("\nNames: ", names, type(names))

names_list = len(names)

# ----------------------- Calulate the minimum number of teachers required--------#

number_of_teachers = ((number_of_sections * number_of_hours) // number_of_subjects_per_teacher) + 1

teacher_subjects = {}

subject_pointer = 0

for i in range(number_of_teachers):

    teacher_subjects[names[i]] = []
    current_teacher = names[i]
    
    for j in range(number_of_subjects_per_teacher):
    
        if subject_pointer > 4:
            subject_pointer = 0
        
        teacher_subjects[current_teacher].append(subjects[subject_pointer])
        subject_pointer += 1
    
    subject_pointer -= 2
print("\nTeachers and thier subjects: \n", teacher_subjects)

fixedData.close()