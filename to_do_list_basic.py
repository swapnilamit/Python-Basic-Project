Todo_list=[] #create a empty list,here we added tasks


#we use while loop to run the program until user press the option 5
while(True):
    print("WELCOME TO THE TO DO LIST")
    print(".........................")
    print("Option 1: Add Task")
    print("Option 2: Show Task")
    print("Option 3: Update Task")
    print("Option 4: Delete Task")
    print("Option 5: Close To Do List")

    choise= input("Enter Your Choise")

    if(choise=='1'): # Add Task
        task=input("Enter The Task: ")
        Todo_list.append(task)
        print("TAsk Added")

    elif(choise=='2'): #Show Task
        print("Showing Task: ")
        print(Todo_list)   

    elif(choise=='3'): #Update Task
        tasknum=int(input("Enter The Task Number: "))
        newtask=input("Enter The Update Task: ")
        Todo_list[tasknum-1]=newtask
        print("Task Update")

    elif(choise=='4'): #Delete Task
        tasknum=int(input("Enter The Num Of Task Delete: "))
        Todo_list[tasknum-1].pop()
        print("Task Delete")            

    elif(choice=='5'): #Close The Program
        print("--closing--")
        break    

    else: print("Invalid, Please Try with Option 1/2/3/4/5") #Invalid Handle