g1 = input("Enter your course 1 letter grade: ")
if g1 == "A":
  grade1 = 4.0
if g1 == "A-":
  grade1 = 3.67
if g1 == "B+":
  grade1 = 3.33
if g1 == "B":
  grade1 = 3.0
if g1 == "B-":
  grade1 = 2.67
if g1 == "C+":
  grade1 = 2.33
if g1 == "C":
  grade1 = 2.0
if g1 == "D":
  grade1 = 1.0
if g1 == "F":
  grade1 = 0.0
c1 = input("Enter your course 1 credit: ")
print("Grade point for course 1 is: " + str(grade1))

g2 = input("Enter your course 2 letter grade: ")
if g2 == "A":
  grade2 = 4.0
if g2 == "A-":
  grade2 = 3.67
if g2 == "B+":
  grade2 = 3.33
if g2 == "B":
  grade2 = 3.0
if g2 == "B-":
  grade2 = 2.67
if g2 == "C+":
  grade2 = 2.33
if g2 == "C":
  grade2 = 2.0
if g2 == "D":
  grade2 = 1.0
if g2 == "F":
  grade2 = 0.0
c2 = input("Enter your course 2 credit: ")
print("Grade point for course 3 is: " + str(grade2))

g3 = input("Enter your course 3 letter grade: ")
if g3 == "A":
  grade3 = 4.0
if g3 == "A-":
  grade3 = 3.67
if g3 == "B+":
  grade3 = 3.33
if g3 == "B":
  grade3 = 3.0
if g3 == "B-":
  grade3 = 2.67
if g3 == "C+":
  grade3 = 2.33
if g3 == "C":
  grade3 = 2.0
if g3 == "D":
  grade3 = 1.0
if g3 == "F" or g3 == "W":
  grade3 = 0.0
c3 = input("Enter your course 3 credit: ")
print("Grade point for course 3 is: " + str(grade3))
f1 = float(grade1) * float(c1) + float(grade2) * float(c2) + float(grade3) * float(c3) 
fc = float(c1) + float(c2) + float(c3)
f = float(f1)/ float(fc)
print("Your GPA is: " + str(f))
