
student_names={
    "student1": "",
    "student2": "",
}

a1total = 6
a2total = 6
a3total = 4
a4total = 3

global a1result
global a2result
global a3result
global a4result

a1result = "n"
a2result = "n"
a3result = "n"
a4result = "n"

loop = 1

def calc(into, out):
    global a1result
    global a2result
    global a3result
    global a4result
    if into > 85:
        out = "E"
    elif into >= 65:
        out = "M"
    elif into >= 50:
        out = "A"
    elif into < 50:
        out = "N"
    print(out)


while loop == 1:
    print("=================================")
    try:
        a1 = int(input("First Assessment: "))
        a2 = int(input("Second Assessment: "))
        a3 = int(input("Third Assessment: "))
        a4 = int(input("Fourth Assessment: "))
        loop = 0
        if a1 > 100 or a2 > 100 or a3 > 100 or a3 > 100:
            print("try again")
            loop = 1
    except ValueError:
        print("try again")

calc(a1, a1result)
print("Assessment 1 results:", a1result)
calc(a2, a2result)
print("Assessment 2 results:", a2result)
calc(a3, a3result)
print("Assessment 3 results:", a3result)
calc(a4, a4result)
print("Assessment 4 results:", a4result)

gpa = ((a1 * a1total) + (a2 * a2total) + (a3 * a3total) + (a4 * a4total)) / (a1total + a2total + a3total + a4total)
print("Your gpa is:", '{0:.3f}'.format(gpa), "\n=================================")
