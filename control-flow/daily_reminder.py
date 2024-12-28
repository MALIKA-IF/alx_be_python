#ask the user for a single task
task = input("Enter your task:" )
#ask the user for its priority level
priority = input("Priority (high/medium/low)").lower()
#ask the user for it is time-sensitive
time_bound =input("Is it time-bound? (yes, no)").lower()

#Finish project report' is a high priority task that requires immediate attention today!
match priority:
    case "high":
         if time_bound =="yes":
            reminder ="'",task,"is a ",priority,"priority task that requires immediate attention today!"
         else :
            reminder ="you have task Now,Consider completing it when you have free time"

    case "medium" :
        if time_bound =="yes":
              reminder ="'",task,"is a ",priority," priority task that requires immediate attention today!"
        else :
              reminder ="you have task Now,Consider completing it when you have free time"


    case "low" :
        if time_bound =="yes":
             reminder ="'",task,"is a ",priority," priority task that requires immediate attention today!"
        else :
              reminder ="you have an important task Now,Consider completing it when you have free time"
    case _:
         reminder ="invalid priority"
print(reminder)      



