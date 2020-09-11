# author Peter Schulman pks5481@psu.edu

def getGradePoint(g1):
  if g1 == "A":
    return 4.0
  elif g1 == "A-":
    return 3.67
  elif g1 == "B+":
    return 3.33
  elif g1 == "B":
    return 3.0
  elif g1 == "B-":
    return 2.67
  elif g1 == "C+":
    return 2.33
  elif g1 == "C":
    return 2.0
  elif g1 == "D":
    return 1.0
  else :
    return 0.0
  
  
g1 = input("Enter your course 1 letter grade: ")
c1 = input("Enter your course 1 credit: ")
print(f"Grade point for course 1 is: {getGradePoint(g1)}")
gc1 = float(getGradePoint(g1)) * float(c1)

g1 = input("Enter your course 2 letter grade: ")
c2 = input("Enter your course 2 credit: ")
print(f"Grade point for course 2 is: {getGradePoint(g1)}")
gc2 = float(getGradePoint(g1)) * float(c2)

g1 = input("Enter your course 1 letter grade: ")
c3 = input("Enter your course 1 credit: ")
print(f"Grade point for course 1 is: {getGradePoint(g1)}")
gc3 = float(getGradePoint(g1)) * float(c3)

f1 = float(gc1) + float(gc2) + float(gc3) 
fc = float(c1) + float(c2) + float(c3)
f = float(f1)/ float(fc)
print("Your GPA is: " + str(f))
