

# These are my designated constant variables.
MIN_VALID_TEMP = 40
MAX_VALID_TEMP = 100

COLD_LIMIT = 68
WARM_LIMIT = 76


# These are my declared variables and my incrementing varaibles.
temp_reading_for_avg = 0
too_cold_counter = 0
too_warm_counter = 0


# These are my user inputs for how many time they want to loop.
user_number_of_readings = int(input("How many times would you like to input a reading?"))
times_to_loop = user_number_of_readings + 1


# Start of our for loop.
for temps in range (1,times_to_loop):
    # Asking for users temp inputs.
    user_temp_reading = int(input("Using whole numbers, please enter a temperture(between 40 and 100 degrees inclusive): "))

    # User validation.
    while user_temp_reading > MAX_VALID_TEMP or user_temp_reading < MIN_VALID_TEMP:
         user_temp_reading = int(input("That is not a valid entry. Using whole numbers, please enter a temperture(between 40 and 100 degrees inclusive): "))
    
    # Incrementing temp avg.
    temp_reading_for_avg =+ user_temp_reading

    # Start of the if statement to determine if its warm or cold and then incrementing those values.
    if user_temp_reading > WARM_LIMIT:

