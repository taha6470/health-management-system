import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food : "))
        if(c==1):
            value=input("type here\n")
            with open("taha-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("taha-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food : "))
        if (c == 1):
            value = input("type here\n")
            with open("hamza-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("hamza-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food : "))
        if (c == 1):
            value = input("type here\n")
            with open("umer-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("umer-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("Please enter valid input (1(Taha),2(Hamza),3(Umer)")
def retrieve(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food : "))
        if(c==1):
            with open("taha-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("taha-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food : "))
        if (c == 1):
            with open("hamza-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("hamza-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food : "))
        if (c == 1):
            with open("umer-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("umer-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Please enter valid input (Taha,Hamza,Umer)")
print("health management system: ")
a=int(input("Press 1 for log the value and 2 for retrieve : "))

if a==1:
    b = int(input("Press 1 for Taha 2 for Hamza 3 for Umer : "))
    take(b)
elif a==2:
    b = int(input("Press 1 for Taha 2 for Hamza 3 for Umer : "))
    retrieve(b)
else : 
    print("You selected an unkown option")