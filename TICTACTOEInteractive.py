import random
row1=None
column1=None
row2 = None
column2 = None
data1=[]
data2=[]
data3=[]
data4=[]
count=0
count2=0
print("Welcome to TIC-TAC-TOE!!")
tic=input("Enter O or X as your choice --> ")
if tic=='O':
    tac='X'
else:
    tac='O'
block=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
i=0
choice=int(input("Enter 1 for Head and 0 for Tail --> "))
x=random.randint(0,1)
if choice==x:
    print("You won the toss you get the first chance : ")
    print("## Enter the row and column you want to put your choice in ##")
    row1=int(input("Row --> "))
    data1.append(row1)
    column1=int(input("Column --> "))
    data2.append(column1)
    block[row1-1][column1-1]=tic
    print(block[0][0],"|",block[0][1],"|",block[0][2])
    print(block[1][0],"|",block[1][1],"|",block[1][2])
    print(block[2][0],"|",block[2][1],"|",block[2][2])
    while True:
        i+=1
        if block[0][0]==block[0][1] and block[0][1]==block[0][2] and block[0][0]!=' ':
            if block[0][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[1][0]==block[1][1] and block[1][1]==block[1][2] and block[1][0]!=' ':
            if block[1][0]==tic:
                print("You Win!!")
            else:
                print('you Lose!!')
            break
        elif block[2][0]==block[2][1] and block[2][1]==block[2][2] and block[2][0]!=' ':
            if block[2][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][0]==block[1][0] and block[1][0]==block[2][0] and block[0][0]!=' ':
            if block[0][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][1]==block[1][1] and block[1][1]==block[2][1] and block[0][1]!=' ':
            if block[0][1]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][2]==block[1][2] and block[1][2]==block[2][2] and block[0][2]!=' ':
            if block[0][2]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][0]==block[1][1] and block[1][1]==block[2][2] and block[0][0]!=' ':
            if block[0][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][2]==block[1][1] and block[1][1]==block[2][0] and block[0][2]!=' ':
            if block[0][2]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif i%2!=0:
            print("## A.I ##")
            if row2!=None and column2!=None:
                row2=random.randint(1,3)
                data3.append(row2)
                index1+=1
                length1=len(data3)
                for j in data1:
                    if row2==j:
                        count+=1
                for k in range(0,index1):
                    if row2==data3[k]:
                        count2+=1
                while count>0 or count2>0:
                    row2=random.randint(1,3)
                    for j in data1:
                        if row2 == j:
                            count += 1
                    for k in range(0, index1):
                        if row2 == data3[k]:
                            count2 += 1
                data3[index1]=row2
                column2=random.randint(1,3)
                data4.append(column2)
                index2+=1
                length2=len(data4)
                count=0
                count2=0
                for j in data2:
                    if row2==j:
                        count+=1
                for k in range(0,index2):
                    if column2==data4[k]:
                        count2+=1
                while count>0 or count2>0:
                    column2=random.randint(1,3)
                    for j in data2:
                        if row2 == j:
                            count += 1
                    for k in range(0, index2):
                        if column2 == data4[k]:
                            count2 += 1
                data4[index2]=column2
                block[row2-1][column2-1] = tac
            else:
                row2=random.randint(1,3)
                data3.append(row2)
                index1=0
                for j in data1:
                    if row2==j:
                        count+=1
                while count>0:
                    count=0
                    row2=random.randint(1,3)
                    data3[0]=row2
                    for j in data1:
                        if row2 == j:
                            count += 1
                column2=random.randint(1,3)
                data4.append(column2)
                index2=0
                count = 0
                for j in data2:
                    if row2 == j:
                        count += 1
                while count>0:
                    count=0
                    column2=random.randint(1,3)
                    data4[0]=column2
                    for j in data2:
                        if row2 == j:
                            count += 1
                block[row2 - 1][column2 - 1] = tac
            #block[row2-1][column2-1]=tac
            print(block[0][0],"|",block[0][1],"|",block[0][2])
            print(block[1][0],"|",block[1][1],"|",block[1][2])
            print(block[2][0],"|",block[2][1],"|",block[2][2])
        elif i%2==0:
            print('## Your Turn ##')
            row1=int(input("Row --> "))
            data1.append(row1)
            column1=int(input("Column --> "))
            data2.append(column2)
            block[row1-1][column1-1]=tic
            print(block[0][0],"|",block[0][1],"|",block[0][2])
            print(block[1][0],"|",block[1][1],"|",block[1][2])
            print(block[2][0],"|",block[2][1],"|",block[2][2])
        else:
            print("Draw!!")
            break
else:
    print("## A.I won the toss ##")
    print("## A.I ##")
    row2=random.randint(1,3)
    data3.append(row2)
    index1=0
    column2=random.randint(1,3)
    data4.append(column2)
    index2=0
    block[row2-1][column2-1]=tac
    print(block[0][0],"|",block[0][1],"|",block[0][2])
    print(block[1][0],"|",block[1][1],"|",block[1][2])
    print(block[2][0],"|",block[2][1],"|",block[2][2])
    while True:
        i+=1
        if block[0][0]==block[0][1] and block[0][1]==block[0][2] and block[0][0]!=' ':
            if block[0][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[1][0]==block[1][1] and block[1][1]==block[1][2] and block[1][0]!=' ':
            if block[1][0]==tic:
                print("You Win!!")
            else:
                print('you Lose!!')
            break
        elif block[2][0]==block[2][1] and block[2][1]==block[2][2] and block[2][0]!=' ':
            if block[2][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][0]==block[1][0] and block[1][0]==block[2][0] and block[0][0]!=' ':
            if block[0][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][1]==block[1][1] and block[1][1]==block[2][1] and block[0][1]!=' ':
            if block[0][1]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][2]==block[1][2] and block[1][2]==block[2][2] and block[0][2]!=' ':
            if block[0][2]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][0]==block[1][1] and block[1][1]==block[2][2] and block[0][0]!=' ':
            if block[0][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][2]==block[1][1] and block[1][1]==block[2][0] and block[0][2]!=' ':
            if block[0][2]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif i%2==0:
            print("## A.I ##")
            row2=random.randint(1,3)
            data3.append(row2)
            index1+=1
            length1 = len(data3)
            for j in data1:
                if row2==j:
                    count+=1
            for k in range(0,index1):
                if row2==data3[k]:
                    count2+=1
            while count>0 or count2>0:
                count=0
                count2=0
                row2=random.randint(1,3)
                for j in data1:
                    if row2 == j:
                        count += 1
                for k in range(0,index1):
                    if row2==data3[k]:
                        count2+=1
            data3[index1]=row2
            count=0
            count2=0
            column2=random.randint(1,3)
            data4.append(column2)
            index2+=1
            length2 = len(data4)
            for j in data2:
                if column2==j:
                    count+=1
            for k in range(0,index2):
                if column2==data4[k]:
                    count2+=1
            while count>0 or count2>0:
                count=0
                count2=0
                column2=random.randint(1,3)
                for j in data2:
                    if column2 == j:
                        count += 1
                for k in range(0,index2):
                    if column2==data4[k]:
                        count2+=1
            data4[index2]=column2
            block[row2-1][column2-1]=tac
            print(block[0][0],"|",block[0][1],"|",block[0][2])
            print(block[1][0],"|",block[1][1],"|",block[1][2])
            print(block[2][0],"|",block[2][1],"|",block[2][2])
        elif i%2!=0:
            print("## Your Turn ##")
            row1=int(input("Row --> "))
            data1.append(row1)
            column1=int(input("Column --> "))
            data2.append(column2)
            block[row1-1][column1-1]=tic
            print(block[0][0],"|",block[0][1],"|",block[0][2])
            print(block[1][0],"|",block[1][1],"|",block[1][2])
            print(block[2][0],"|",block[2][1],"|",block[2][2])
        else:
            print("Draw!!")
            break
print("Thanks for playing!!")