
calculate_continue = "yes"
choice_continue="yes"
""" Calculator Program """

""" Display Menu till user wish to use calculator"""

while calculate_continue == "yes":
    print("Calculator:::")
    print("1. Addition: ")
    print("2. Subtraction: ")
    print("3. Division: ")
    print("4. Multiplication: ")
    print("5. Remainder Calculation: ")
    print("6. To the Power Values: ")
    print("7. Quit: ")

    """ Take User Input"""
    
    choice = int(input("Enter your choice: "))
    
    choice_continue="yes"
    
   
    """ Compare Choice"""
    
    """ Execute choice, till user wish to continue"""
    
    
    if choice==1:
       while choice_continue=="yes":  
            num1= int(input("Enter Number 1 :"))
            num2=int(input("Enter Number 2:"))
            
            Add= num1+num2
            print(Add)
            
            choice_continue = input("Do you wish to continue? Yes/No: ")
    

    if choice==2:
       while choice_continue=="yes":
            num1= int(input("Enter Number 1 :"))
            num2=int(input("Enter Number 2:"))
            
            Sub= num1-num2
            print(Sub)
            
            choice_continue = input("Do you wish to continue? Yes/No: ")
        
    if choice==3:
       while choice_continue=="yes":
            num1= int(input("Enter Number 1 :"))
            num2=int(input("Enter Number 2:"))
            
            Div= num1/num2
            print(Div)
            
            choice_continue = input("Do you wish to continue? Yes/No: ")
            
    if choice==4:
       while choice_continue=="yes":
            num1= int(input("Enter Number 1 :"))
            num2=int(input("Enter Number 2:"))
            
            Mul= num1*num2
            print(Mul)
            
            choice_continue = input("Do you wish to continue? Yes/No: ")
            
    if choice==5:
       while choice_continue=="yes":
            num1= int(input("Enter Number 1 :"))
            num2=int(input("Enter Number 2:"))
            
            Rem= num1%num2
            print(Rem)
            
            choice_continue = input("Do you wish to continue? Yes/No: ")
            
    if choice==6:
       while choice_continue=="yes":
            num1= int(input("Enter Number 1 :"))
            num2=int(input("Enter Number 2:"))
            
            Pow= num1**num2
            print(Pow)
            
            choice_continue = input("Do you wish to continue? Yes/No: ")
            
    if choice==7:
       calculate_continue="no"
           
           
print("Closing")
           
