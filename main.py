import random as r
import time as t

def result(rightcount,wrongcount,correctAnswer,yourAnswer):  #it will simply print the result of your currect practiced game mode 
    print("\nResult = ",rightcount,"/",10)
    print(rightcount,"answers are right and ",wrongcount,"answers are wrong")
    print("Correct answer = ",correctAnswer,end="\n")
    print("Your Answers   = ",yourAnswer,end="\n")
    if wrongcount == 0:
        print("well done...! All answers are correct...\nKeep practicing")        
    elif rightcount >=7:
        print("Good...! Work more to be batter\nKeep praciting")
    else:
        print("Poor performence...! You need to practice alot\nKeep practicing")

def getNum(op,level): # it will return random numbers by giving the level and operator for the miscllaneous(mix function)
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

def add(level, rightcount = 0, wrongcount = 0,correctAnswer = {}, yourAnswer = {} ): #in this function loop wil run for 10 times to ask question(add) and get answer from the user
    if level <= 4:
        for k in range(10):
            print("Q",k+1,sep="",end=") ")
            a,b = addMix(level)           
            q, answer, rightcount, wrongcount = adding(a,b,rightcount,wrongcount)
            yourAnswer[q] = answer      #recording the correct answer
            correctAnswer[q] = answer   #recording the user's answer
        result(rightcount,wrongcount,correctAnswer,yourAnswer)
    else:
        print("choose correct option")

def addMix(level): #it will retrun 2 random numbers for addition by giving its level 
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

def adding(a,b,rightcount,wrongcount): # it will add 2 numbers, count correct and wrond answers given by user and return the values as follows
    q = str(a)+" + "+str(b)+" = "
    c = a+b
    print(a,"+",b,"=",end="")
    answer = int(input())
    if answer == c:
        rightcount+=1
    else:
        wrongcount+=1
    return q,c,rightcount,wrongcount

def sub(level, rightcount = 0, wrongcount = 0,correctAnswer = {}, yourAnswer = {} ): #in this function loop wil run for 10 times to ask question(minus) and get answer from the user
    if level <= 4:
        for k in range(10):
            print("Q",k+1,sep="",end=") ")
            a,b = subMix(level)
            q, answer, rightcount, wrongcount = subtracting(a,b,rightcount,wrongcount)
            correctAnswer[q] = answer  #recording the correct answer
            yourAnswer[q] = answer     #recording the user's answer
        result(rightcount,wrongcount,correctAnswer,yourAnswer)
    else:
        print("choose correct option")

def subMix(level): #it will retrun 2 random numbers for subtraction by giving its level.
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

def subtracting(a,b,rightcount,wrongcount): # it will subtract 2 numbers, count correct and wrond answers given by user and return the values as follows.
    q = str(a)+" - "+str(b)+" = "
    c = a-b
    print(a,"-",b,"=",end="")
    answer = int(input())
    if answer == c:
        rightcount+=1
    else:
        wrongcount+=1
    return q,c,rightcount,wrongcount

def mul(level, rightcount = 0, wrongcount = 0,correctAnswer = {}, yourAnswer = {} ): #in this function loop wil run for 10 times to ask question(multiply) and get answer from the user
    if level <= 4: 
        for k in range(10):
            print("Q",k+1,sep="",end=") ")
            a,b = mulMix(level)
            q, answer, rightcount, wrongcount = multipling(a,b,rightcount,wrongcount)
            correctAnswer[q] = answer
            yourAnswer[q] = answer
        result(rightcount,wrongcount,correctAnswer,yourAnswer)
    else:
        print("choose correct option")

def mulMix(level): #it will retrun 2 random numbers for multiplication by giving its level.
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

def multipling(a,b,rightcount,wrongcount): # it will multiply 2 numbers, count correct and wrond answers given by user and return the values as follows.
    q = str(a)+" * "+str(b)+" = "
    c = a*b
    print(a,"*",b,"=",end="")
    answer = int(input())
    if answer == c:
        rightcount+=1
    else:
        wrongcount+=1
    return q,c,rightcount,wrongcount

def div(level, rightcount = 0, wrongcount = 0,correctAnswer = {}, yourAnswer = {} ): #in this function loop wil run for 10 times to ask question(divide) and get answer from the user
    if level <= 4: 
    if level <= 4:
        for k in range(10):
            a,b = divMix(level)
            q, answer, rightcount, wrongcount = multipling(a,b,rightcount,wrongcount)
            correctAnswer[q] = answer
            yourAnswer[q] = answer
        result(rightcount,wrongcount,correctAnswer,yourAnswer)
    else:
        print("choose correct option")

def divMix(level): #it will retrun 2 random numbers for division by giving its level.
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

def dividing(a,b,rightcount,wrongcount): # it will divide up 2 numbers, count correct and wrond answers given by user and return the values as follows.
    q = str(a)+" / "+str(b)+" = "
    c = a/b
    print(a,"/",b,"=",end="")
    answer = int(input())
    if answer == c:
        rightcount+=1
    else:
        wrongcount+=1
    return q,c,rightcount,wrongcount

def table(level, rightcount = 0, wrongcount = 0,correctAnswer = {}, yourAnswer = {} ): 
    if level <= 4: 
        for k in range(10):
            print("Q",k+1,sep="",end=") ")                            #This function will simply run for 10 times by providing the level by user
            if level == 1: #practice for table 2 to 10                #it will genrate 2 numbers for user and display it then it will ask user to
                a = r.randrange(2,11)                                 #input the correct answer and the answer will be matched by the correct answer
                b = r.randrange(1,11)                                 #if answer of user will found correct right answer will increase else wrong answer
            elif level == 2: #practice for table 10 to 20             #count will inrease.
                a = r.randrange(10,21)
                b = r.randrange(1,11)
            elif level == 3: #practice for table 18 to 25
                a = r.randrange(18,26)
                b = r.randrange(1,11)
            elif level == 4: #pracitce for table 2 to 25
                a = r.randrange(2,26)
                b = r.randrange(1,11)               
            q, answer, rightcount, wrongcount = multipling(a,b,rightcount,wrongcount)
            correctAnswer[q] = answer
            yourAnswer[q] = answer
        result(rightcount,wrongcount,correctAnswer,yourAnswer)
    else:
        print("choose correct option")
    
def mix(level, rightcount = 0, wrongcount = 0,correctAnswer = {}, yourAnswer = {} ):
    li = ['+',"-","*","/"]
    for k in range(10):
        op = li[r.randrange(4)]
        a,b = getNum(op,level)
        print("Q",k+1,sep="",end=") ")

        if op == '+':
            q, answer, rightcount, wrongcount = adding(a, b, rightcount, wrongcount)
            correctAnswer[q] = answer
            
        elif op == '-':
            q, answer, rightcount, wrongcount = subtracting(a, b, rightcount, wrongcount)
            correctAnswer[q] = answer
        
        elif op == '*':
            q, answer, rightcount, wrongcount = multipling(a, b, rightcount, wrongcount)
            correctAnswer[q] = answer
            
        elif op == '/':
            q, answer, rightcount, wrongcount = dividing(a, b, rightcount, wrongcount)
            correctAnswer[q] = answer
        
        yourAnswer[q] = answer
    result(rightcount,wrongcount,correctAnswer,yourAnswer)

def highScr(game,level):
    pass

def showoptn():
    print("Choose any option from the following to practice on it.\n")
    print("1) For addition press 1\n2) For subtraction press 2\n3) For multiplication press 3")
    print("4) For division press 4\n5) For miscllaneous press 5\n6) For table press 6 ")
    print("7) To chech highscor press 7 ")
    print("press 0 to Exit the programe...")

def chkOptn(game,level):
    if game<=6 and game >=0 and level <=4 and level >0:
        return True
    else:
        return False

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
        # t.sleep(0.037)
        print(i,end="")

#************main programe
showinfo()
i = 1
while i !=0:
    showoptn()
    try:
        game = int(input("Enter here: "))
        if game == 0:
            break
        level = int(input("Enter level: "))

        if chkOptn(game,level) == True:
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
            elif game == 7:
                highScr(game,level)
        else:
            print("\nChoose correct option...")
    except Exception:
        print("Enter only integeral value")
info()
