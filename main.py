import random as r
import time as t
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="lucky786",database ="mathsrock")
mycursor = mydb.cursor()

def result(rightcount,level,qList,correctAnswer,yourAnswer,score,timetaken,game): 
    print("\nyour score :",score," "*10,"Result = ",rightcount,"/",10)  
    print("time taken :", timetaken,"sec","     Level :",level)
    tempTable(qList,correctAnswer,yourAnswer)
    chkHighScore(score,level,game) 
    query = "select * from temp"
    mycursor.execute(query)
    print("\nQusetions        correct ans         your ans")
    for i in mycursor:
        for j in range(3):
            x = len(str(i[j]))
            print(i[j],end=" "*(20-x))
        print()
    print()
    if rightcount == 10:
        print("well done...! All answers are correct...\nKeep practicing")        
    elif rightcount >=7:
        print("Good...! Work more to be batter\nKeep praciting")
    else:
        print("Poor performence...! You need to practice alot\nKeep practicing")

def crtTable():
    create = "create table highscore(game varchar(20), level int(3), score int(3),name varchar(30))"
    try:
        mycursor.execute(create)
    except:
        pass
    
def chkHighScore(score,level,game):
    crtTable()
    query = "select max(score) from highscore where level = {} and game = '{}'".format(level,game)
    mycursor.execute(query)
    for i in mycursor:
        if score >0:
            if i[0] is None:
                name = getName(None)
                insert(game,level,score,name)
            elif i[0] < score:
                name = getName(score)
                update(game,level,score,name)

def highScore():
    show = '''select * from highscore order by game not like 'addition',game not like 'subtraction',
    game not like 'multiplication',game not like 'division',game not like 'miscllaneous',game not like 'Table',level;'''
    try:
        mycursor.execute(show)
    except:
        print("\n****NO DATA FOUND*****\n")
        return
    print("\nGAME","LEVEL","SCORE"," NAME",sep=" "*(13))
    for i in mycursor:
        for j in range(4):
            x = len(str(i[j]))
            print(i[j],end=" "*(18-x))
        print()
    print()

def pointGen(rightcount,  inetialTime, finalTime):
    timetaken = round(finalTime - inetialTime,2)
    print("Time:",timetaken)
    score = round((rightcount*11)-(timetaken))
    return score,timetaken

def getName(mod):
    if mod is None:
        print("Congratulations..! you made a record.")
    else:
        print("Congratulations..!  you broke a record.")
    names = input("Enter your Name: ")
    return names

def update(game,level,score,name):
    query = "update highscore set score = {}, name = '{}' where level = {} and game = '{}'".format(score,name,level,game)
    mycursor.execute(query)
    mydb.commit()

def insert(game,level,score,name): 
    query = "insert into highscore(game,level,score,name) values('{}',{},{},'{}')".format(game,level,score,name)
    mycursor.execute(query)
    mydb.commit()

def tempTable(qList, correctAnswer, yourAnswer):
    delt = "drop table temp"
    creat = "create table temp( Q_list varchar(20), Correct_Ans int(3), Your_Ans int(3));"
    try: 
        mycursor.execute(delt)
    except Exception:
        pass
    finally:
        mycursor.execute(creat)
    i = 1
    while i <= 10:
        query = "insert into temp(Q_list, Correct_Ans, Your_Ans) values('{}',{},{})".format(str(i)+") "+qList[i-1],correctAnswer[i-1],yourAnswer[i-1])
        mycursor.execute(query)
        mydb.commit()
        i+=1

def getNum(op,level):
    if op == '+':
        return addMix(level)
    elif op == '-':
        return subMix(level)
    elif op == '*':
        return mulMix(level)
    elif op == '/':
        return divMix(level)
    else:
        print("unexpected error...!") 

def add(level, rightcount = 0, wrongcount = 0 ):
    game,correctAnswer,yourAnswer,qList = 'Addition',[],[],[]
    qList =[]
    if level <= 4:
        inetialTime = t.time()
        for k in range(10):
            print("Q",k+1,sep="",end=") ")
            a,b = addMix(level)        
            q, answer, rightcount, wrongcount, yourans = adding(a,b,rightcount,wrongcount)
            qList.append(q)
            yourAnswer.append(yourans)
            correctAnswer.append(answer)
        finalTime = t.time()
        score, timetaken = pointGen(rightcount, inetialTime, finalTime)
        result(rightcount,level,qList,correctAnswer,yourAnswer,score,timetaken,game)
    else:
        print("choose correct option")

def addMix(level):
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
    return a,b

def adding(a,b,rightcount,wrongcount):
    q = str(a)+" + "+str(b)
    c = a+b
    print(a,"+",b,"=",end="")
    answer = int(input())
    if answer == c:
        rightcount+=1
    else:
        wrongcount+=1
    return q,c,rightcount,wrongcount,answer

def sub(level, rightcount = 0, wrongcount = 0 ):
    game,correctAnswer,yourAnswer,qList = 'Subtraction',[],[],[]
    if level <= 4:
        inetialTime = t.time()
        for k in range(10):
            print("Q",k+1,sep="",end=") ")
            a,b = subMix(level)
            q, answer, rightcount, wrongcount, yourans = subtracting(a,b,rightcount,wrongcount)
            qList.append(q)
            correctAnswer.append(answer)
            yourAnswer.append(yourans)
        finalTime = t.time()
        score, timetaken = pointGen(rightcount, inetialTime, finalTime)
        result(rightcount,level,qList,correctAnswer,yourAnswer,score,timetaken,game)
    else:
        print("choose correct option")

def subMix(level):
    if level == 1:
        a = r.randrange(25)
        b = r.randrange(15)
    elif level == 2:
        a = r.randrange(10,36)
        b = r.randrange(20)
    elif level == 3:
        a = r.randrange(20,50)
        b = r.randrange(10,30)
    elif level == 4:
        a = r.randrange(40,111,2)
        b = r.randrange(20,50)
    if a < b:
        a, b = b, a
    return a,b

def subtracting(a,b,rightcount,wrongcount):
    q = str(a)+" - "+str(b)
    c = a-b
    print(a,"-",b,"=",end="")
    answer = int(input())
    if answer == c:
        rightcount+=1
    else:
        wrongcount+=1
    return q,c,rightcount,wrongcount,answer 

def mul(level, rightcount = 0, wrongcount = 0): 
    game,correctAnswer,yourAnswer,qList = 'Multiplication',[],[],[]
    if level <= 4:
        inetialTime = t.time()
        for k in range(10):
            print("Q",k+1,sep="",end=") ")
            a,b = mulMix(level)
            q, answer, rightcount, wrongcount, yourans = multipling(a,b,rightcount,wrongcount)
            qList.append(q)
            correctAnswer.append(answer)
            yourAnswer.append(yourans)
        finalTime = t.time()
        score, timetaken = pointGen(rightcount, inetialTime, finalTime)
        result(rightcount,level,qList,correctAnswer,yourAnswer,score,timetaken,game)
    else:
        print("choose correct option")

def mulMix(level):
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
    return a,b

def multipling(a,b,rightcount,wrongcount):
    q = str(a)+" * "+str(b)
    c = a*b
    print(a,"*",b,"=",end="")
    answer = int(input())
    if answer == c:
        rightcount+=1
    else:
        wrongcount+=1
    return q,c,rightcount,wrongcount,answer 

def div(level, rightcount = 0, wrongcount = 0): 
    game,correctAnswer,yourAnswer,qList = 'Division',[],[],[]
    if level <= 4:
        inetialTime = t.time()
        for k in range(10):
            print("Q",k+1,sep="",end=") ")
            a,b = divMix(level)
            q, answer, rightcount, wrongcount, yourans = dividing(a,b,rightcount,wrongcount)
            qList.append(q)
            correctAnswer.append(answer)
            yourAnswer.append(yourans)
        finalTime = t.time()
        score, timetaken = pointGen(rightcount, inetialTime, finalTime)
        result(rightcount,level,qList,correctAnswer,yourAnswer,score,timetaken,game)
    else:
        print("choose correct option")

def divMix(level):
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
    return a,b

def dividing(a,b,rightcount,wrongcount):
    q = str(a)+" / "+str(b)
    c = a/b
    print(a,"/",b,"=",end="")
    answer = int(input())
    if answer == c:
        rightcount+=1
    else:
        wrongcount+=1
    return q,int(c),rightcount,wrongcount,answer 

def table(level, rightcount = 0, wrongcount = 0 ):
    game,correctAnswer,yourAnswer,qList = 'Table',[],[],[]
    if level <= 4: 
        inetialTime = t.time()
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
            q, answer, rightcount, wrongcount, yourans = multipling(a,b,rightcount,wrongcount)
            qList.append(q)
            correctAnswer.append(answer)
            yourAnswer.append(yourans)
        finalTime = t.time()
        score, timetaken = pointGen(rightcount, inetialTime, finalTime)      
        result(rightcount,level,qList,correctAnswer,yourAnswer,score,timetaken,game)
    else:
        print("choose correct option")
    
def mix(level, rightcount = 0, wrongcount = 0,correctAnswer = None, yourAnswer = None ):
    if correctAnswer is None:
        correctAnswer = []
    if yourAnswer is None:
        yourAnswer = []
    game = 'Miscllaneous'
    li = ['+',"-","*","/"]   
    qList =[]
    inetialTime = t.time()
    for k in range(10):
        op = li[r.randrange(4)]
        a,b = getNum(op,level)
        print("Q",k+1,sep="",end=") ")
        if op == '+':
            q, answer, rightcount, wrongcount, yourans = adding(a, b, rightcount, wrongcount)
            
        elif op == '-':
            q, answer, rightcount, wrongcount, yourans = subtracting(a, b, rightcount, wrongcount)
        
        elif op == '*':
            q, answer, rightcount, wrongcount, yourans = multipling(a, b, rightcount, wrongcount)
            
        elif op == '/':
            q, answer, rightcount, wrongcount, yourans = dividing(a, b, rightcount, wrongcount)
        qList.append(q)
        correctAnswer.append(answer)
        yourAnswer.append(yourans)
    finalTime = t.time()
    score, timetaken = pointGen(rightcount, inetialTime, finalTime)
    result(rightcount,level,qList,correctAnswer,yourAnswer,score,timetaken,game)

def selLvl(game):
    if game == 6:        
        level = int(input("Enter level\n2 to 10 press    1\n10 to 20  press  2\n18 to 25 press   3\n2 to 25 press    4\n---------> "))
    else:
        level = int(input("Enter level\nEasy       1\nNormal     2\nHard       3\nVery Hard  4\n---------> "))
    return level

def showoptn():
    print("\nChoose any option from the following to practice on")
    print("1 Addition \n2 Subtraction \n3 Multiplication")
    print("4 Division \n5 Miscllaneous\n6 Table")
    print("7 Highscor")
    print("\npress 0 to Exit the programe...")

def chkOptn(game,level):
    return bool(game<=7 and game >=0 and level <=4 and level >0)

def info():
    print("********************************************************")
    print("********************************************************")
    print("***                                                  ***")
    print("**             MADE BY MOZAHIDUL ISLAM                **")
    print("***                                                  ***")
    print("********************************************************")
    print("********************************************************\n")  

def showinfo():
    massage = "This progrmam is made by MOZAHIDUL ISLAM \nperpos of ths program is to make your calculation faster" 
    massage+=" regarding to school project\nHope you like it...\n                        Thankyou for using\n"
    for i in massage:
        t.sleep(0.037)
        print(i,end="")

showinfo()
#************main programe
i = 1
while i !=0:
    showoptn()
    try:
        game = int(input("Enter here: "))
        if game == 0:
            break
        if game == 7:
            highScore()
            continue
        level = selLvl(game)
        if chkOptn(game,level) is True:
            if game == 1:
                add(level)
            elif game == 2:
                sub(level)
            elif game == 3:
                mul(level)
            elif game == 4:
                div(level)
            elif game == 5:
                mix(level)
            elif game == 6:
                table(level)
        else:
            print("\nChoose correct option...")
    except Exception as e:
        print(e)
info()
