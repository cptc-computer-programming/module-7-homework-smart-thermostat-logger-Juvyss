

# These are my designated constant variables.
MIN_VALID_TEMP = 40
MAX_VALID_TEMP = 100

COLD_LIMIT = 68
WARM_LIMIT = 76


# These are my declared variables and my incrementing varaibles.
temp_reading_for_avg = 0



# These are my user inputs for how many time they want to loop.
user_number_of_readings = int(input("How many times would you like to input a reading?"))
times_to_loop = user_number_of_readings + 1


# Start of our for loop.
for temps in range (1,times_to_loop):
    user_temp_reading = int(input("Using whole numbers, please enter a temperture(between 40 and 100 degrees inclusive): "))
        if user_temp_reading > MAX_VALID_TEMP or user_temp_reading < MIN_VALID_TEMP:
            user_temp_reading = int(input("That is not a valid entry. Using whole numbers, please enter a temperture(between 40 and 100 degrees inclusive): "))
        