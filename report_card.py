Marks = []
print("Enter marks of subject: ")
for i in range(5):
    Marks.append(int(input(f"Enter a marks{i+1}: ")))

def total(x):
    return sum(x)

def Avreage(x):
    return sum(x)/len(x)

def CGPA(x):
    credit_marks= []
    credit = [2 for i in range(len(x))]
    for i in range(5):
        credit_marks.append(credit[i]*x[i])
    return sum(credit_marks)/sum(credit*10)

def result(x):
    percentage = (total(x)/(len(x)*100))*100
    if percentage >= 35:
        return "Pass"
    else:
        return "Fail"

report_card = {
    "total": total(Marks),
    "Avreage": Avreage(Marks),
    "CGPA": CGPA(Marks),
    "PASS/FAIL": result(Marks)
}

print(report_card)