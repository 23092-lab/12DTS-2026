ENDORSEMENT=14
student=[]

count = 0

ass_worth = {
    "assessment_1_credits":6,
    "assessment_2_credits":6,
    "assessment_3_credits":4,
    "assessment_4_credits":3
}

grade_boundary={
    "excellence":85,
    "merit":65,
    "achieved":50,
    "not_achieved":50
}

students={

}

assessment1=[6]
assessment2=[6]
assessment3=[4]
assessment4=[3]

def calc(score,assessment):
    if score > 85:
        assessment.append("E")
    elif score >= 65:
        assessment.append("M")
    elif score >= 50:
        assessment.append("A")
    elif score < 50:
        assessment.append("N")

def endorse(assessment,student):
    if assessment1[1] == "E" and assessment2[1] == "E":
        if assessment[1] == "E" or assessment4[1] =="E":
            student.append("Excellence")
    elif assessment1[1] == "M" and assessment2[1] == "M":
        if assessment[1] == "M" or assessment4[1] =="M":
            student.append("Merit")

def int_check():
    while 1:
        try:
            count=1
            while count<=4:
                print("Assessment", count, "score:")
                if count==1:
                    assessment1.append(int(input()))
                if count==2:
                    assessment2.append(int(input()))
                if count==3:
                    assessment3.append(int(input()))
                if count==4:
                    assessment4.append(int(input()))
                count=count+1
        except ValueError:
            print("Try again")
        else:
            if value <0 or value>100:
                print("try again")
            else:
                return value

while 1:
    student.append(input("Enter your name: "))

    calc(int_check(),assessment1)
    calc(int(input("assessment2 score:")),assessment2)
    calc(int(input("assessment3 score:")),assessment3)
    calc(int(input("assessment4 score:")),assessment4)

    print("Assessment1:", assessment1)
    print("Assessment2:", assessment2)
    print("Assessment3:", assessment3)
    print("Assessment4:", assessment4)

    endorse(assessment1,student)
    print(student)
    student.clear()
