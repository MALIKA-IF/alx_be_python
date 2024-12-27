task = input("Enter your task:" )
priority = input("Priority (high/medium/low)").lower()
time_bound =input("Is it time-bound? (yes, no)").lower()


match priority:
    case "high":
         if time_bound =="yes":
            reminder ="'",task,"'you have an important task Now, that requires immediate attention today!"
         else :
            reminder ="you have an important task Now,Consider completing it when you have free time"

    case "medium" :
        if time_bound =="yes":
              reminder ="'",task,"'don't forget your project"
        else :
              reminder ="you have an important task Now,Consider completing it when you have free time"


    case "low" :
        if time_bound =="yes":
             reminder ="'",task,"'complet your project when you have time "
        else :
              reminder ="you have an important task Now,Consider completing it when you have free time"
    case _:
         reminder ="invalid priority"
print(reminder)      



