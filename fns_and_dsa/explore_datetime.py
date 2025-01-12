from datetime import datetime,timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date

def calculate_future_date():
   #      HH:MM:SS
        x=display_current_datetime()
        print("Current date and time:",x.strftime("%Y-%m-%d %H:%M:%S"))
        number =int(input("Enter the number of days to add to the current date:"))
        y=timedelta(days=number)
        future_date=x+y
        return future_date



future_date=calculate_future_date()
print("Future date:",future_date.strftime("%Y-%m-%d"))



