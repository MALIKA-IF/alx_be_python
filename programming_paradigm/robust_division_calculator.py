def safe_divide(numerator, denominator):
    try:
        div=float(numerator)/float(denominator)
        print("The result of the division is",div)
    except ZeroDivisionError:
       print("Cannot divide by zero.")
    except ValueError:
          print("Please enter numeric values only")
       


    

