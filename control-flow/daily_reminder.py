Task = input("Enter your task:" )
Priority = input("Priority (high/medium/low)")
Time_bound =input("Is it time-bound?")


match Priority:
    case "high":
         if Time_bound =="yes":
            print("'",Task,"'you have an important task Now, that requires immediate attention today!")
         elif Time_bound =="No":
           print("you have an important task Now")

    case "medium" :
        print("'",Task,"'don't forget your project")

    case "low" :
        print("'",Task,"'complet your project when you have time ")



