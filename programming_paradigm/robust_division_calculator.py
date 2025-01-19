class safe_divide:
   def safe_divide(numerator, denominator):
    try:
        div=numerator/denominator
        return "The result of the division is",div
    except:
        ZeroDivisionError
        return "Cannot divide by zero."
    try:
        div=float(numerator)/float(denominator)
        return div
    except:
          ValueError
          return "Please enter numeric values only"

    pass