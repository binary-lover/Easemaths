import random as r
def result(rightcount,wrongcount,correctAnswer,yourAnswer):
    if wrongcount == 0:
        print()
        print("Result = ",rightcount,"/",10)
        print("Correct answer = ",correctAnswer)
        print()
        print("Your Answers   = ",yourAnswer)
        print()
        print("well done...! All answers are correct...\nKeep practicing")
    elif rightcount >=7:
        print()
        print("Result = ",rightcount,"/",10)
        print("Correct answer = ",correctAnswer)
        print()
        print("Your Answers   = ",yourAnswer)
        print()
        print(rightcount,"answers are right and ",wrongcount,"answers are wrong")
        print("Good...! Work more to be batter\nKeep praciting")
    else:
        print()
        print("Result = ",rightcount,"/",10)
        print("Correct answer = ",correctAnswer)
        print()
        print("Your Answers   = ",yourAnswer)
        print()
        print(rightcount,"answers are right and ",wrongcount,"answers are wrong")
        print("Poor performence...! You need to practice alot\n Keep practicing")

def add(level): 
    if level <= 4:
        rightcount = 0
        wrongcount = 0
        correctAnswer = {}
        yourAnswer = {}
        questonNumList = []
        for k in range(10):
            print("Q",k+1,sep="",end=") ")
            questonNumList.append(k+1)
            if level == 1:
                a = r.randrange(20)
                b = r.randrange(15)
            elif level == 2:
                a = r.randrange(10,41)
                b = r.randrange(5,20)
            elif level == 3:
                a = r.randrange(20,51)
                b = r.randrange(20,30)
            elif level == 4:
                a = r.randrange(40,101,2)
                b = r.randrange(30,60)
            q = str(a)+" + "+str(b)+" = "
            correctAnswer[q] = a+b
            print(a,"+",b,"=",end="")
            answer = int(input())
            if answer == a+b:
                yourAnswer[q] = answer
                rightcount+=1
            else:
                yourAnswer[q] = answer
                wrongcount+=1
        result(rightcount,wrongcount,correctAnswer,yourAnswer)
    else:
        print("choose correct option")

def sub(level): 
    if level <= 4:
        rightcount = 0
        wrongcount = 0
        correctAnswer = {}
        yourAnswer = {}
        for k in range(10):
            print("Q",k+1,sep="",end=") ")
            if level == 1:
                a = r.randrange(25)
                b = r.randrange(15)
                if a < b:
                    a, b = b, a
            elif level == 2:
                a = r.randrange(10,36)
                b = r.randrange(20)
                if a < b:
                    a, b = b, a
            elif level == 3:
                a = r.randrange(20,50)
                b = r.randrange(10,30)
                if a < b:
                    a, b = b, a
            elif level == 4:
                a = r.randrange(40,111,2)
                b = r.randrange(20,50)
                if a < b:
                    a, b = b, a
            q = str(a)+" - "+str(b)+" = "
            correctAnswer[q] = a-b
            print(a,"-",b,"=",end="")
            answer = int(input())
            if answer == a-b:
                yourAnswer[q] = answer
                rightcount+=1
            else:
                yourAnswer[q] = answer
                wrongcount+=1
        result(rightcount,wrongcount,correctAnswer,yourAnswer)
    else:
        print("choose correct option")

def mul(level):
    if level <= 4: 
        rightcount = 0
        wrongcount = 0
        correctAnswer = {}
        yourAnswer = {}
        for k in range(10):
            print("Q",k+1,sep="",end=") ")
            if level == 1:
                a = r.randrange(15)
                b = r.randrange(11)
            elif level == 2:
                a = r.randrange(8,20)
                b = r.randrange(12)
            elif level == 3:
                a = r.randrange(12,25)
                b = r.randrange(1,14)
            elif level == 4:
                a = r.randrange(15,30)
                b = r.randrange(10,21)
            q = str(a)+" * "+str(b)+" = "
            correctAnswer[q] = a*b
            print(a,"*",b,"=",end="")
            answer = int(input())
            if answer == a*b:
                yourAnswer[q] = answer
                rightcount+=1
            else:
                yourAnswer[q] = answer
                wrongcount+=1
        result(rightcount,wrongcount,correctAnswer,yourAnswer)
    else:
        print("choose correct option")

def div(level): 
    if level <= 4:
        rightcount = 0
        wrongcount = 0
        correctAnswer = {}
        yourAnswer = {}
        for k in range(10):
            print("Q",k+1,sep="",end=") ")
            if level == 1:
                b = r.randrange(11)
                a = b*r.randrange(1,11)
                if b == 0:
                    b = r.randrange(1,100,3)
            elif level == 2:
                b = r.randrange(16)
                a = b*r.randrange(1,14)
                if b == 0:
                    b = r.randrange(1,111,9)
            elif level == 3:
                b = r.randrange(12,21)
                a = b*r.randrange(1,17)
            elif level == 4:
                b = r.randrange(14,25)
                a = b*r.randrange(1,21)
            q = str(a)+" / "+str(b)+" = "
            correctAnswer[q] = int(a/b)
            print(a,"/",b,"=",end="")
            answer = int(input())
            if answer == a/b:
                yourAnswer[q] = answer
                rightcount+=1
            else:
                yourAnswer[q] = answer
                wrongcount+=1
        result(rightcount,wrongcount,correctAnswer,yourAnswer)
    else:
        print("choose correct option")

def table(level):
    if level <= 4: 
        rightcount = 0
        wrongcount = 0
        correctAnswer = {}
        yourAnswer = {}
        for k in range(10):
            print("Q",k+1,sep="",end=") ")
            if level == 1: #practice for table 2 to 10
                a = r.randrange(2,11)
                b = r.randrange(1,11)
            elif level == 2: #practice for table 10 to 20
                a = r.randrange(10,21)
                b = r.randrange(1,11)
            elif level == 3: #practice for table 18 to 25
                a = r.randrange(18,26)
                b = r.randrange(1,11)
            elif level == 4: #pracitce for table 2 to 25
                a = r.randrange(2,26)
                b = r.randrange(1,11)
            q = str(a)+" * "+str(b)+" = "
            correctAnswer[q] = a*b
            print(a,"*",b,"=",end="")
            answer = int(input())
            if answer == a*b:
                yourAnswer[q] = answer
                rightcount+=1
            else:
                yourAnswer[q] = answer
                wrongcount+=1
        result(rightcount,wrongcount,correctAnswer,yourAnswer)
    else:
        print("choose correct option")
