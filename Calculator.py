#-------------------------------Calculator---------------------------------------------

while True:
   
   
    #Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    choice = input("Select the operator you want to choose '+,-,*,%,/' : ")
   
   
    #Perform the calculation
    if choice == '+':
       result= num1+num2
    
    elif choice == '-':
       result=num1-num2
   
    elif choice == '*':
       result= num1*num2
    
    elif choice == '%':
       if num2==0:
          result= print("Cannot divide by zero")
       else:
          result=num1%num2
    
    elif choice == '/':
       if num2==0:
          result= print("Cannot divide by zero")
       else:
          result=num1/num2
       
    else:
        result = "Invalid input"
    
    
    #Display the result
    print("Result: ",num1,choice,num2,'=',result)
    
    
    #Another calculation
    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        break
