#Computation of the GWA 

def computeGWA(math_grade, sci_grade, fil_grade, eng_grade, thesis_grade, python_grade):
        math_weight = 4
        sci_weight = 3
        fil_weight = 3
        eng_weight = 3
        thesis_weight = 6
        python_weight = 4

        mathGWA = math_grade * math_weight
        sciGWA = sci_grade * sci_weight
        filGWA = fil_grade * fil_weight
        engGWA = eng_grade * eng_weight
        thesisGWA = thesis_grade * thesis_weight
        pythonGWA = python_grade * python_weight

        
        total_units = math_weight + sci_weight + fil_weight + eng_weight + thesis_weight + python_weight

        
        studentGWA = ((mathGWA + sciGWA + filGWA + engGWA + thesisGWA + pythonGWA) / total_units)

        return studentGWA



print("TRANSCRIPT OF RECORDS")
print("----------------------")

#Display student profile

name = "Jonie Alaban"
school = "AdZU"
age = 26

print("Name: ", name)
print("School: ", school)
print("Age: ", age)

print("----------------------")
math_grade = float(input("Please input Math grade: "))
sci_grade = float(input("Please input Science grade: "))
fil_grade = float(input("Please input Filipino grade: "))
eng_grade = float(input("Please input English grade: "))
thesis_grade = float(input("Please input Thesis grade: "))
python_grade = float(input("Please input Python grade: "))

studentGWA = computeGWA(math_grade, sci_grade, fil_grade, eng_grade, thesis_grade, python_grade)


print("GWA: ", round(studentGWA, 2))

if studentGWA <= 3.0:
    print("Remarks: PASSED!")
else: 
    print("Remarks: FAILED!")
