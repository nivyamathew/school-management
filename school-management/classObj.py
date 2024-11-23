classObj ={
  "name": "class A",
  "teacherName": "Mary",
  "students": [
    {
      "name": "Ravi",
      "id": "101",
      "marks": [
        { "subject": "English", "mark": 25 },
        { "subject": "Maths", "mark": 48 },
        { "subject": "Physics", "mark": 40 },
        { "subject": "Chemistry", "mark": 30 },
        { "subject": "Computer", "mark": 20 }
      ]
    },
    {
      "name": "Aju",
      "id": "102",
      "marks": [
        { "subject": "English", "mark": 35 },
        { "subject": "Maths", "mark": 38 },
        { "subject": "Physics", "mark": 33 },
        { "subject": "Chemistry", "mark": 34 },
        { "subject": "Computer", "mark": 30 }
      ]
    },
    {
      "name": "Mini SS",
      "id": "103",
      "marks": [
        { "subject": "English", "mark": 12 },
        { "subject": "Maths", "mark": 49 },
        { "subject": "Physics", "mark": 18 },
        { "subject": "Chemistry", "mark": 30 },
        { "subject": "Computer", "mark": 40 }
      ]
    },
    {
      "name": "Binu",
      "id": "104",
      "marks": [
        { "subject": "English", "mark": 49 },
        { "subject": "Maths", "mark": 49 },
        { "subject": "Physics", "mark": 47 },
        { "subject": "Chemistry", "mark": 46 },
        { "subject": "Computer", "mark": 50 }
      ]
    }
  ]
}


# 1.Write a function to print the name of the class: "class A".
def get_name_of_class():    
  return classObj.get("name")

class_name = get_name_of_class()
print(f"1. {class_name}")

# 2.Write a function to print the teacher's name: "Mary".
def get_teacher_name():
  return classObj.get("teacherName")

teacher_name = get_teacher_name()
print(f"2. {teacher_name}")


# 3. Write a function to print the names of all the students in the class.
def get_students_name():
  for student in classObj["students"]:
    print(student["name"])
  
get_students_name()

# 4.Write a function to print the IDs of all the students in the class.
def get_students_ID() :
  for student in classObj["students"]:
    print(student["id"])

get_students_ID()

# 5.Write a function to print the subject names for a specific student.
def get_student_name(student_name):
  for student in classObj["students"]:
    if(student["name"] == student_name):
      print([subject["subject"] for subject in student['marks']])

get_student_name("Aju")

# 6.Write a function to print the marks of a specific student in all subjects.
def get_student_marks(student_name):
  for student in classObj["students"]:
    if(student["name"] == student_name):
      print(student["marks"])

get_student_marks("Binu")

# 7.Write a function to calculate and print the average marks for a specific student.
def get_average_mark(student_name):
  for student in classObj["students"]:
    if(student["name"] == student_name):
      marks = ([mark["mark"] for mark in student["marks"]])
      avg = sum(marks)/len(marks)
      print(avg)

get_average_mark("Mini SS")

# 8.Write a function to calculate and print the total marks for a specific student.
def get_total_marks(student_name):
  for student in classObj["students"]:
    if(student["name"] == student_name):
      marks = ([mark["mark"] for mark in student["marks"]])
      total_marks = sum(marks)
      print(total_marks)

get_total_marks("Mini SS")

# 9.Write a function to calculate and print the average marks for all students in a specific subject.
def get_total_average_mark_for_a_subject(subject_name):
  marks_list = []

  for student in classObj["students"]:
    for mark in student["marks"]:
      if(mark["subject"] == subject_name):
        marks_list.append(mark["mark"])

  average_mark = sum(marks_list) / len(marks_list)
  print(average_mark)

get_total_average_mark_for_a_subject("Computer")

# 10.Write a function to calculate and print the total marks for all students in a specific subject.
def get_total_mark_for_a_subject(subject_name):
  marks_list = []

  for student in classObj["students"]:
    for mark in student["marks"]:
      if(mark["subject"] == subject_name):
        marks_list.append(mark["mark"])

  total_marks = sum(marks_list)
  print(total_marks)

get_total_mark_for_a_subject("Computer")

# 11.Write a function to find and print the student with the highest marks in a specific subject.
def get_student_with_highest_mark_in_a_subject(subject_name):
  highest_marks = 0
  highest_student =""

  for student in classObj["students"]:
    for mark in student["marks"]:
      if(mark["subject"] == subject_name):
        if mark['mark'] > highest_marks:
          highest_marks = mark['mark']
          highest_student = student['name']
  print(highest_student)

get_student_with_highest_mark_in_a_subject("Maths")

# 12.Write a function to find and print the student with the lowest marks in a specific subject.
def get_student_with_lowest_mark_in_a_subject(subject_name):
  lowest_marks = 100
  lowest_student =""

  for student in classObj["students"]:
    for mark in student["marks"]:
      if(mark["subject"] == subject_name):
        if mark['mark'] < lowest_marks:
          lowest_marks = mark['mark']
          lowest_student = student['name']
  print(lowest_student)

get_student_with_lowest_mark_in_a_subject("Maths")

# 13.Write a function to find and print the student with the highest total marks.

def get_student_with_highest_marks():
  highest_mark = 0
  highest_student = None
  for student in classObj["students"]:
    total_marks = sum(mark["mark"] for mark in student["marks"])
    if total_marks > highest_mark:
      highest_mark = total_marks
      highest_student = student["name"]
  print(highest_student)

get_student_with_highest_marks()  

# 14.Write a function to find and print the student with the lowest total marks.
def get_student_with_lowest_marks():
  lowest_mark = 1000
  lowest_student = None
  for student in classObj["students"]:
    total_marks = sum(mark["mark"] for mark in student["marks"])
    if total_marks < lowest_mark:
      lowest_mark = total_marks
      lowest_student = student["name"]
  print(lowest_student)

get_student_with_lowest_marks()

#15. Write a function to find and print the subject with the highest average marks.
def get_student_with_highest_average_mark():
  highest_average_mark = 0
  highest_average_student = None
  for student in classObj["students"]:
    total_mark_list =[mark["mark"] for mark in student["marks"]]
    average_mark = sum(total_mark_list) / len(total_mark_list)
    if average_mark > highest_average_mark:
      highest_average_mark = average_mark
      highest_average_student = student["name"]
  print(highest_average_student)

get_student_with_highest_average_mark()

# 16.Write a function to find and print the subject with the lowest average marks.
def get_student_with_lowest_average_mark():
  lowest_average_mark = 1000
  lowest_average_student = None
  for student in classObj["students"]:
    total_mark_list =[mark["mark"] for mark in student["marks"]]
    print(total_mark_list)
    average_mark = sum(total_mark_list) / len(total_mark_list)
    if average_mark < lowest_average_mark:
      lowest_average_mark = average_mark
      lowest_average_student = student["name"]
  print(lowest_average_student)

get_student_with_lowest_average_mark()

# 17.Write a function to calculate and print the overall average marks for the class.
def get_average_mark_of_class():
  total_mark_list = []
  for student in classObj["students"]:
    total_marks_of_each_student = sum([mark["mark"] for mark in student["marks"]])
    total_mark_list.append(total_marks_of_each_student)
  average_mark_of_class = sum(total_mark_list) / len(total_mark_list)
  print(average_mark_of_class)

get_average_mark_of_class()    

# 18.Write a function to calculate and print the overall total marks for the class.
def get_total_mark_of_class():
  total_mark_list = []
  for student in classObj["students"]:
    total_marks_of_each_student = sum([mark["mark"] for mark in student["marks"]])
    total_mark_list.append(total_marks_of_each_student)
  total_mark_of_class = sum(total_mark_list)
  print(total_mark_of_class)

get_total_mark_of_class()

# 19.Write a function to calculate and print the average marks for each subject.
def get_average_mark_of_each_subject():
  subject_totals = {}
  subject_counts ={}
  for student in classObj["students"]:
    for mark in student["marks"]:
      subject = mark["subject"]
      marks = mark["mark"]
      if subject in subject_totals:
        subject_totals[subject] += marks
        subject_counts[subject] += 1
      else:
        subject_totals[subject] = marks
        subject_counts[subject] = 1

  subject_averages = {}
  for subject in subject_totals:
    average = subject_totals[subject] / subject_counts[subject]
    subject_averages[subject] = average
  print(subject_averages)

get_average_mark_of_each_subject()

# 20.Write a function to calculate and print the total marks for each subject

def get_total_mark_of_each_subject():
  subject_totals = {}

  for student in classObj["students"]:
    for mark in student["marks"]:
      subject = mark["subject"]
      marks = mark["mark"]
      if subject in subject_totals:
        subject_totals[subject] += marks
      else:
        subject_totals[subject] = marks

  print(subject_totals)

get_total_mark_of_each_subject()

# 21. Write a function to find and print the subject with the highest total marks.
def get_highest_subject_total():
  subject_totals = {}

  for student in classObj["students"]:
    for mark in student["marks"]:
      subject = mark["subject"]
      marks = mark["mark"]
      if subject in subject_totals:
        subject_totals[subject] += marks
      else:
        subject_totals[subject] = marks

  highest_subject_with_total_mark = max(subject_totals, key=subject_totals.get)
  print(highest_subject_with_total_mark)

get_highest_subject_total()

# 22.Write a function to find and print the subject with the lowest total marks.
def get_lowest_subject_total():
  subject_totals = {}

  for student in classObj["students"]:
    for mark in student["marks"]:
      subject = mark["subject"]
      marks = mark["mark"]
      if subject in subject_totals:
        subject_totals[subject] += marks
      else:
        subject_totals[subject] = marks

  lowest_subject_with_total_mark = min(subject_totals, key=subject_totals.get)
  print(lowest_subject_with_total_mark)

get_lowest_subject_total()

# 23.Write a function to find and print the student(s) with the highest average marks.
def get_student_with_highest_average_marks():
  students_with_avg=[]

  for student in classObj["students"]:
    total_marks = sum(mark["mark"] for mark in student["marks"])
    average_marks = total_marks / len(student["marks"])
    students_with_avg.append({"name": student["name"], "average": average_marks})
    print(total_marks)
  highest_avg = max(students_with_avg, key=lambda x: x["average"])["average"]
    
  students_with_highest_avg = [student["name"] for student in students_with_avg if student["average"] == highest_avg]

  print(students_with_highest_avg)

get_student_with_highest_average_marks()

# 24.Write a function to find and print the student(s) with the lowest average marks.
def get_student_with_lowest_average_marks():
  students_with_avg=[]

  for student in classObj["students"]:
    total_marks = sum(mark["mark"] for mark in student["marks"])
    average_marks = total_marks / len(student["marks"])
    students_with_avg.append({"name": student["name"], "average": average_marks})
  lowest_avg = min(students_with_avg, key=lambda x: x["average"])["average"]    
  students_with_lowest_avg = [student["name"] for student in students_with_avg if student["average"] == lowest_avg]

  print(students_with_lowest_avg)

get_student_with_lowest_average_marks()

# 25.Write a function to find and print the student(s) with the highest total marks.
def get_students_with_highest_marks():
  students_with_total_marks =[]
  for student in classObj["students"]:
    total_marks = sum(mark["mark"] for mark in student["marks"])
    students_with_total_marks.append({"name": student["name"], "total_marks": total_marks})
  highest_mark = max(students_with_total_marks, key=lambda x: x["total_marks"])["total_marks"]
  students_with_highest_total = [student["name"] for student in students_with_total_marks if student["total_marks"] == highest_mark]
  print(students_with_highest_total)

get_students_with_highest_marks()  

# 26.Write a function to find and print the student(s) with the lowest total marks.
def get_students_with_lowest_marks():
  students_with_total_marks =[]
  for student in classObj["students"]:
    total_marks = sum(mark["mark"] for mark in student["marks"])
    students_with_total_marks.append({"name": student["name"], "total_marks": total_marks})
  lowest_mark = min(students_with_total_marks, key=lambda x: x["total_marks"])["total_marks"]
  students_with_lowest_total = [student["name"] for student in students_with_total_marks if student["total_marks"] == lowest_mark]
  print(students_with_lowest_total)

get_students_with_lowest_marks()

# 27. Write a function to calculate and print the number of students who scored above a certain mark in a specific subject.
def get_student_count_with_more_mark(subject_name, subject_mark):
  student_count = 0
  for student in classObj["students"]:
    for mark in student["marks"]:
      if(mark["subject"] == subject_name):
        if mark["mark"] > subject_mark:
          student_count += 1
  print(student_count)

get_student_count_with_more_mark("Maths", 48)

# 28. Write a function to calculate and print the number of students who scored below a certain mark in a specific subject.
def get_student_count_with_less_mark(subject_name, subject_mark):
  student_count = 0
  for student in classObj["students"]:
    for mark in student["marks"]:
      if(mark["subject"] == subject_name):
        if mark["mark"] < subject_mark:
          student_count += 1
  print(student_count)

get_student_count_with_less_mark("English", 26)

# 29.Write a function to calculate and print the number of students who scored above a certain mark in all subjects
def get_student_count_with_more_mark_in_all_sub(score):
  student_count = 0
  for student in classObj["students"]:
    total_marks = sum(mark["mark"] for mark in student['marks'])
    if total_marks > score:
      student_count += 1
  print(student_count)

get_student_count_with_more_mark_in_all_sub(149)

# 30.Write a function to calculate and print the number of students who scored below a certain mark in all subjects
def get_student_count_with_less_mark_in_all_sub(score):
  student_count = 0
  for student in classObj["students"]:
    total_marks = sum(mark["mark"] for mark in student['marks'])
    if total_marks < score:
      student_count += 1
  print(student_count)

get_student_count_with_less_mark_in_all_sub(189)

# 31. Write a function to calculate and print the percentage of students who scored above a certain mark in a specific subject.
def get_percentage_of_with_more_marks(subject_name, subject_mark):
  student_count = 0
  total_student_count = 0
  for student in classObj["students"]:
    for mark in student["marks"]:
      if(mark["subject"] == subject_name):
        total_student_count += 1
        if mark["mark"] > subject_mark:
          student_count += 1

  percentage_of_students = (student_count/ total_student_count) * 100
  print(f"{int(percentage_of_students)}%")

get_percentage_of_with_more_marks("Maths", 50)

# 32.Write a function to calculate and print the percentage of students who scored below a certain mark in a specific subject.
def get_percentage_of_with_less_marks(subject_name, subject_mark):
  student_count = 0
  total_student_count = 0
  for student in classObj["students"]:
    for mark in student["marks"]:
      if(mark["subject"] == subject_name):
        total_student_count += 1
        if mark["mark"] < subject_mark:
          student_count += 1

  percentage_of_students = (student_count/ total_student_count) * 100
  print(f"{int(percentage_of_students)}%")

get_percentage_of_with_less_marks("English", 25)

# 33.Write a function to calculate and print the percentage of students who scored above a certain mark in all subjects.
def get_percentage_with_more_mark_in_all_sub(score):
  student_count = 0
  total_student_count = 0
  for student in classObj["students"]:
    total_marks = sum(mark["mark"] for mark in student['marks'])
    total_student_count += 1
    if total_marks > score:
      student_count += 1
  
  percentage_of_students = (student_count/ total_student_count) * 100
  print(f"{int(percentage_of_students)}%")

get_percentage_with_more_mark_in_all_sub(189)

# 34.Write a function to calculate and print the percentage of students who scored below a certain mark in all subjects.
def get_percentage_with_less_mark_in_all_sub(score):
  student_count = 0
  total_student_count = 0
  for student in classObj["students"]:
    total_marks = sum(mark["mark"] for mark in student['marks'])
    total_student_count += 1
    if total_marks < score:
      student_count += 1
  
  percentage_of_students = (student_count/ total_student_count) * 100
  print(f"{int(percentage_of_students)}%")

get_percentage_with_less_mark_in_all_sub(189)

# 35.Write a function to find and print the student(s) with the highest percentage of marks.
def get_students_with_highest_percentage_of_marks():
  students_with_highest_percentage =[]
  for student in classObj["students"]:
    total_percentage_of_marks = (sum(mark["mark"] for mark in student["marks"])/ 250)*100
    students_with_highest_percentage.append({"name": student["name"],"total_marks": total_percentage_of_marks})

  highest_percentage_of_mark = max(students_with_highest_percentage, key=lambda x: x["total_marks"])["total_marks"]
  students_with_highest_percentage = [student["name"] for student in students_with_highest_percentage if student["total_marks"] == highest_percentage_of_mark]
  print(students_with_highest_percentage)

get_students_with_highest_percentage_of_marks()

# 36.Write a function to find and print the student(s) with the lowest percentage of marks.
def get_students_with_lowest_percentage_of_marks():
  students_with_lowest_percentage =[]
  for student in classObj["students"]:
    total_percentage_of_marks = (sum(mark["mark"] for mark in student["marks"])/ 250)*100
    students_with_lowest_percentage.append({"name": student["name"],"total_marks": total_percentage_of_marks})

  lowest_percentage_of_mark = min(students_with_lowest_percentage, key=lambda x: x["total_marks"])["total_marks"]
  students_with_lowest_percentage = [student["name"] for student in students_with_lowest_percentage if student["total_marks"] == lowest_percentage_of_mark]
  print(students_with_lowest_percentage)

get_students_with_lowest_percentage_of_marks()

# 37.Write a function to find and print the subject(s) with the highest percentage of marks.

def get_highest_percentage_subject():
  subject_totals = {}
  subject_percentage = {}

  for student in classObj["students"]:
    for mark in student["marks"]:
      subject = mark["subject"]
      marks = mark["mark"]
      if subject in subject_totals:
        subject_totals[subject] += marks        
      else:
        subject_totals[subject] = marks 

    for subject, total_marks in subject_totals.items():
      percentage = (total_marks / 200) * 100
      subject_percentage[subject] = percentage   

    highest_subject_with_total_percentage = max(subject_percentage, key=subject_totals.get)
  print(highest_subject_with_total_percentage)

get_highest_percentage_subject()

# 38.Write a function to find and print the subject(s) with the lowest percentage of marks.

def get_lowest_percentage_subject():
  subject_totals = {}
  subject_percentage = {}

  for student in classObj["students"]:
    for mark in student["marks"]:
      subject = mark["subject"]
      marks = mark["mark"]
      if subject in subject_totals:
        subject_totals[subject] += marks        
      else:
        subject_totals[subject] = marks 

    for subject, total_marks in subject_totals.items():
      percentage = (total_marks / 200) * 100
      subject_percentage[subject] = percentage   

    lowest_subject_with_total_percentage = min(subject_percentage, key=subject_totals.get)
  print(lowest_subject_with_total_percentage)

get_lowest_percentage_subject()

# 39.Write a function to find and print the student(s) with the highest percentage of marks in a specific subject.
def get_highest_percentage_in_specific_subject(subject_name):
  students_with_highest_percentage=[]

  for student in classObj["students"]:
    for mark in student["marks"]:
      if(mark["subject"] == subject_name):
        percentage = ((int(mark["mark"])/50) *100)
        students_with_highest_percentage.append({"name": student["name"], "percentage": percentage})
  highest_avg = max(students_with_highest_percentage, key=lambda x: x["percentage"])["percentage"]
    
  students_with_highest_percent= [student["name"] for student in students_with_highest_percentage if student["percentage"] == highest_avg]
  print(students_with_highest_percent)

get_highest_percentage_in_specific_subject('Maths')

# 40.Write a function to find and print the student(s) with the lowest percentage of marks in a specific subject.
def get_lowest_percentage_in_specific_subject(subject_name):
  students_with_lowest_percentage=[]

  for student in classObj["students"]:
    for mark in student["marks"]:
      if(mark["subject"] == subject_name):
        percentage = ((int(mark["mark"])/50) *100)
        students_with_lowest_percentage.append({"name": student["name"], "percentage": percentage})
  lowest_percent = min(students_with_lowest_percentage, key=lambda x: x["percentage"])["percentage"]
    
  students_with_lowest_percent = [student["name"] for student in students_with_lowest_percentage if student["percentage"] == lowest_percent]
  print(students_with_lowest_percent)

get_lowest_percentage_in_specific_subject('Computer')

# 41.Write a function to find and print the subject(s) with the highest percentage of marks for a specific student.
def get_highest_percentage_mark_for_a_subject(student_name):
  subjects_with_highest_percentage = []
  for student in classObj["students"]:
    if student["name"] == student_name:
      for mark in student['marks']:
        percentage = (int(mark["mark"])/50)*100
        subjects_with_highest_percentage.append({"subject": mark["subject"],"percentage": percentage})
      highest_percent = max(subjects_with_highest_percentage, key=lambda x: x["percentage"])["percentage"]

      subjects_with_highest_percent = [mark["subject"] for mark in subjects_with_highest_percentage if mark["percentage"] == highest_percent]

  print(subjects_with_highest_percent)

get_highest_percentage_mark_for_a_subject("Binu")

# 42.Write a function to find and print the subject(s) with the lowest percentage of marks for a specific student.
def get_lowest_percentage_mark_for_a_subject(student_name):
  subjects_with_lowest_percentage = []
  for student in classObj["students"]:
    if student["name"] == student_name:
      for mark in student['marks']:
        percentage = (int(mark["mark"])/50)*100
        subjects_with_lowest_percentage.append({"subject": mark["subject"],"percentage": percentage})
      lowest_percent = min(subjects_with_lowest_percentage, key=lambda x: x["percentage"])["percentage"]

      subjects_with_lowest_percent = [mark["subject"] for mark in subjects_with_lowest_percentage if mark["percentage"] == lowest_percent]

  print(subjects_with_lowest_percent)

get_lowest_percentage_mark_for_a_subject("Mini SS")

# 43. Write a function to find and print the subject(s) in which all students scored above a certain mark.

# def get_subject_above_score(score):
#   for student in classObj["students"]:
#     for mark in student["marks"]:
#       if mark["mark"] > score:
#         print(mark["mark"])

# get_subject_above_score(23)