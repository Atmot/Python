# Problem 4
 # My Name:Dataman

starting_day_number_str = input("What weekday does your holiday start (Sunday = 0 to Saturday = 6)?")
length_of_stay_str = input("How many days will you be away?")

starting_day_number_int = int(starting_day_number_str)
length_of_stay_int = int(length_of_stay_str)

days_int = starting_day_number_int + length_of_stay_int

return_day_of_week = days_int % 7

print("You will return on a: ", return_day_of_week, " weekday.")
