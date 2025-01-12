from datetime import datetime,timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date

def calculate_future_date():
         
        x=display_current_datetime()
        print("Current date and time:",x)
        number =int(input("Enter the number of days to add to the current date:"))
        y=timedelta(days=number)
        future_date=x+y
        print("Future date:",future_date)



calculate_future_date()



