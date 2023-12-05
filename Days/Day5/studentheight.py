import math

student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
num2 = 0
students = 0
for num in student_heights:
  num2+=num
  students +=1
averageheight = (num2 / students)

print(f"total height = {num2}\nnumber of students = {students}\naverage height = {math.floor(averageheight)}")
  