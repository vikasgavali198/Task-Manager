import datetime

#pssd means password, ussnm is username

def user_information(ussnm, pssd):
    name = input("enter you name please: ")
    address = input("enter your address please: ")
    age = input("please its time to tell about your age: ")
    ussnm_ = ussnm+" task.txt"
    f = open(ussnm_, 'a')
    f.write(pssd)
    f.write("\nName: ")
    f.write(name)
    f.write('\n')
    f.write("Address :")

    f.write(address)
    f.write('\n')
    f.write("Age : ")
    f.write(age)
    f.write('\n')
    f.close()

def signup():
    print("Please enter the username by which you wanna access your account : ")
    username = input("Please enter username here: ")
    password = input("Plese enter the password here: ")
    user_information(username, password)
    print("Sir please proceed towards login")
    login()

def login():
    print("Please enter your username: ")
    user_nm = input("Enter here: ")

    #password as entered while logging in
    pssd_wr = (input("Enter the password here: "))+'\n'
    try:
        usernm = user_nm+" task.txt"
        f_ =  open(usernm, 'r')

        # variable 'k' contains the password as saved
        # in the file
        k = f_.readlines(0)[0]
        f_.close()

        # cheaking if the password entered is same as the password saved while signing in
        if pssd_wr == k:
            print(
                "1--to view your data \n2--To add task \n3--Update task \n4--VIEW TASK STATUS"
            )
            a = input()
            if a == '1':
                view_data(usernm)
            elif a == '2':
                # add task
                task_information(usernm)
            elif a == '3':
                task_update(user_nm)
            elif a == '4':
                task_update(user_nm)
            else:
                print("Wrong input ! BHAI sahi input daal")
        else:
            print("SIR YOUR PASSWORD OR USERNAME IS WRONG")
            login()
    except Exception as e:
        print(e)
        login()

def view_data(username):
    ff = open(username, 'r')
    print(ff.read())
    ff.close()

def task_information(username):
    print("Sir enter no of task you want to ADD")
    j = int(input())
    f1 = open(username, 'a')

    for i in range(1, j+1):
        task = input("enter the task")
        target = input("enter the target: ")
        pp = "TASK "+str(i)+' :'
        qq = "TARGET "+str(i)+" :"

        f1.write(pp)
        f1.write(task)
        f1.write('\n')
        f1.write(qq)
        f1.write(target)
        f1.write('\n')
        print("Do you want to stop then press space bar otherwise enter")
        s = input()
        if s == ' ':
            break
    f1.close()


def task_update(username):
    username = username+" TASK.txt"
    print("Please enter the tasks which are completed ")
    task_completed = input()

    print("Enter task which ae still not started by you")
    task_not_started = input()

    print("Enter task which you are doing")
    task_ongoing = input()

    fw = open(username, 'a')
    DT = str(datetime.datetime.now())
    fw.write(DT)
    fw.write("\n")
    fw.write("COMPLETED TASK \n")
    fw.write(task_completed)
    fw.write("\n")
    fw.write("ONGOING TASK \n")
    fw.write(task_ongoing)
    fw.write("\n")
    fw.write("NOT YET STARTED\n")
    fw.write(task_not_started)
    fw.write("\n")

def task_update_viewer(username):
    ussnm = username+" TASK.txt"
    o = open(ussnm, 'r')
    print(o.read())
    o.close()


if __name__ == '__main__':
    print("WELCOME TO SHOAIB'S TASK MANAGER")
    print("Sir are you new to this software?")
    a = int(input("Typr 1 if new otherwise press 0 ::"))
    if a == 1:
        signup()
    elif a == 0:
        login()
    else:
        print("You have provided wrong input !")
