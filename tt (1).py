
def make_tt(n_sec, n_sub, n_teachers) :
	t = [ ]
	k = 0
	for i in range(n_sub) :
		t.append([])
		for j in range(n_sec) :
			t[i].append(k)
			k = (k + 1) % n_teachers
	print(t)
	return t

def disp(t) :
	for row in t :
		for k in row :
			print(k, end = " ")
		print()

def disp_subject_teacher_mapping(t):
	alloted = { } 
	for i in range(len(t)) :
		for j in range(len(t[i])) :
			k = t[i][j]
			if k not in alloted :
				alloted[k] = [ ]
			alloted[k].append((i, j))
	print("Allotted: ", alloted)
	return alloted	
	
def print_sectionwise_time_table(t, n_teachers, sec, n_hr_day, n_sub) :
	sec_teachers = []
	for i in range(len(t)) :
		sec_teachers.append(t[i][sec])
	print(sec_teachers)
	k_start = 0
	print("section : ", sec)
	for i in range(5) : # week
		k = k_start
		k_start = (k_start + 1) % 5 # number of weeks
		for j in range(n_hr_day) :
			print(sec_teachers[k], end = "\t")
			k = (k + 1) % n_sub
		print()
	print("-" * 40)


n_sec = 5
n_sub = 5
n_teachers = 9
n_hr_day = 4	
t = make_tt(n_sec = 5, n_sub = 5, n_teachers = 9)
disp(t)
alloted = disp_subject_teacher_mapping(t) 
for k in alloted :
	print(k)
	for (i, j) in alloted[k]:
		print("\t", "section : ", i, " subject ", j)


for i in range(n_sec) :
	print_sectionwise_time_table(t, n_teachers, i, n_hr_day, n_sub)




	
