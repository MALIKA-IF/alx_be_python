from datetime import datetime,timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date


number =int(input("Enter the number of days to add to the current date:"))
y=display_current_datetime()
x=timedelta(days=number)
result=y+x
print(result)