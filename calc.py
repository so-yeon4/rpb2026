def main:
    print("Let's calculate. Will you add or divide?")

    Calculation type=input("Add or Divide?> ")
    if Calculation type=="Add":
        print("type two numbers for x and y!")

        x=float(input("x> "))
        y=float(input("y> "))
        print("%f+%f=%0.6f" % (x, y, add(x,y)))
    elif Calculation type=="Divide":
        print("type two numbers for x and y! you will be dividing x by y.")

        x=float(input("x> "))
        y=float(input("y> "))
        if y==0:
            print("Error: cannot divide by zero!")
        else:
            print("%f/%f=%0.6f" % (x, y, divide(x,y)))

    else:
        func()

def func():
    answer=input("We can only add or divide, sorry! Will you continue? (yes/no)> ")
    if answer=="yes":
        main()
    else:
        print("Finish!")


def add(x,y):
    return x+y

def divide(x,y):
    return x/y