#define function perform_operation

def perform_operation(num1, num2, operation):
    if operation=="add":
        result=num1+num2
    elif operation=="subtract":
        result=num1-num2
    elif operation=="multiply":
        result=num1*num2
    elif operation=="divide":
        try:
            result=num1/num2
        except num2==0:
            result=0   
    print(result)            



