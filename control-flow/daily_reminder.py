#ask the user for a single task
task=input("Enter your task:" )
#ask the user for its priority level
priority=input("Priority (high/medium/low): ")
#ask the user for it is time-sensitive
time_bound=input("Is it time-bound? (yes/no): ")


match priority:
    case "high":
         if time_bound =="yes":
            print("Reminder:",task,"is a ",priority,"priority task that requires immediate attention today!")
         else :
           print("Note:",task,"is a ",priority,"priority task,Consider completing it when you have free time")

    case "medium":
        if time_bound =="yes":
              print("Reminder:",task,"is a ",priority," priority task that requires immediate attention today!")
        else :
             print("Note:",task,"is a ",priority," priority task,Consider completing it when you have free time")
    case "low":
        if time_bound =="yes":
             print("Reminder:",task,"is a ",priority," priority task that requires immediate attention today!")
        else:
             print("Note:",task,"is a ",priority,"priority task, Consider completing it when you have free time")
    case _:
         print("invalid priority")





