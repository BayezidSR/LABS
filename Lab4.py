def check_weekday_or_weekend(day_number): 
    if day_number == 6 or day_number == 7: 
        print("It is the weekend")

    elif day_number in [1, 2, 3, 4, 5]: 
        print("Is is the weekday")

    else: 
        print("Not a proper day") 

    return(print)

number = float(input("Insert a number from 1 to 7:" ))
result = check_weekday_or_weekend(number)
print(result) 

def get_day_name(day_number): 
    Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if day_number== 6 or day_number == 7:
            print(f"It is a weekend {Days[day_number - 1]}")

    elif day_number in [1, 2, 3, 4, 5]: 
            print(f"It is the weekday {Days[day_number - 1]}")

    else:
            print("Not a proper date, insert a number in range of 1-7")
        
    return(print) 
    
day = int(input("Insert a number form 1 to 7 ")) 
result2 = get_day_name(day)
print(result2)