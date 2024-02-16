#Computation of the GWA 

def computeGWA(math_grade, sci_grade, fil_grade, eng_grade, thesis_grade, python_grade):
        
        #subject variables contain number of units 
        math_weight = 4
        sci_weight = 3
        fil_weight = 3
        eng_weight = 3
        thesis_weight = 6
        python_weight = 4

        #to get the GWA per subject, subject variables with the set units will be multiplied with the user's inputs
        mathGWA = math_grade * math_weight
        sciGWA = sci_grade * sci_weight
        filGWA = fil_grade * fil_weight
        engGWA = eng_grade * eng_weight
        thesisGWA = thesis_grade * thesis_weight
        pythonGWA = python_grade * python_weight

        #summation of the student's units 
        total_units = math_weight + sci_weight + fil_weight + eng_weight + thesis_weight + python_weight

        #summation of the GWAs of the subjects divided by the total units 
        studentGWA = ((mathGWA + sciGWA + filGWA + engGWA + thesisGWA + pythonGWA) / total_units)

        #Extracts the value of the student GWA for line 56
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

#Input the grades obtained of the student and convert it into float 
math_grade = float(input("Please input Math grade: "))
sci_grade = float(input("Please input Science grade: "))
fil_grade = float(input("Please input Filipino grade: "))
eng_grade = float(input("Please input English grade: "))
thesis_grade = float(input("Please input Thesis grade: "))
python_grade = float(input("Please input Python grade: "))

#in this line, it fill ups the paramenters with the values 
studentGWA = computeGWA(math_grade, sci_grade, fil_grade, eng_grade, thesis_grade, python_grade)

#Print with the rounded of GWA
print("GWA: ", round(studentGWA, 2))

#conditions for the GWA remarks
if studentGWA <= 3.0:
    print("Remarks: PASSED!")
else: 
    print("Remarks: FAILED!")
