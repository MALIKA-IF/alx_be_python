task = input("Enter your task:" )
priority = input("Priority (high/medium/low)")
time_bound =input("Is it time-bound?")


match priority:
    case "high":
         if time_bound =="yes":
            print("'",task,"'you have an important task Now, that requires immediate attention today!")
         elif time_bound =="No":
           print("you have an important task Now")

    case "medium" :
        print("'",task,"'don't forget your project")

    case "low" :
        print("'",task,"'complet your project when you have time ")



