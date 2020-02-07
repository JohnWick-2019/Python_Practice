
user_answer = ""
flag = True

while flag:

    num_1 = float(input("Enter first number: "))
    simbal = input("What to do?(+, -, *, /)")
    num_2 = float(input("Enter second number: "))

    if simbal == "+":
        print("The summ = {}".format((num_1 + num_2)))                         
             
    elif simbal == "-":
        print("The summ = {}".format((num_1 - num_2)))                        
        
    elif simbal == "*":
        print("The summ = {}".format((num_1 * num_2)))             
               
    elif simbal == "/":
        
        if num_2 == 0:
            print("You can`t divide by zero")

        else:
            print("The summ = {}".format((num_1 / num_2)))
            

            

print("The end!!!")        



