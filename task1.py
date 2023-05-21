

time_swimming = input("Enter the time taken in mimutes to complete the swimming event: ")
time_cycling = input("Enter the time taken in minutes to complete the cycling event: ")
time_running = input("Enter the time taken in minutes to complete the running event: ")


total_time = float(time_swimming) + float(time_cycling) + float(time_running)
print("The total time for all three events is:", total_time)

total_time_for_all_events = total_time

#The qualifying time is 100
#using the if-elif-else statements

if total_time_for_all_events <= 100:
    print("You have received a provincial Colours Award")

elif total_time_for_all_events <= 105 :
    print("You have received a Provincial Half Colours Award")

elif total_time_for_all_events <= 110:
    print("You have received a Provincial Scroll Award")

else:
    if total_time_for_all_events > 110:
        print("You have no Award") 
