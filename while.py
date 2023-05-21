# This program always asks the user to enter a number and then calculates the average.
# when the user enters -1, the program stops to ask the user to enter a number and then it calculates the average of numbers entered.

total = 0
count = 0


while True:

    user_input = int(input("Please enter a number (-1 to stop): "))
    if user_input == -1:
        break

    total += user_input
    count += 1

if count > 0:
    average =  total / count
    print(average)

else:
    print("No number entered")

