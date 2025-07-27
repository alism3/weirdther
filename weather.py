import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    return datetime.fromisoformat(iso_string).strftime("%A %d %B %Y")



def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    float_fahrenheit = float(temp_in_fahrenheit)
    celsius = ((float_fahrenheit -32) / 1.8)
    return round(celsius, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.
    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    conv_list = []
    print(conv_list)  # To see the list before conversion
    for item in weather_data:
        print(item) #To see the items in the list
        converted_number = float(item)
        print(converted_number) # To see the converted number
        conv_list.append(converted_number)
    return round(sum(conv_list) / len(conv_list), 1)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = [] # Create an empty list, I will fill it with the data that I need
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file) #Tell Python to use the CSV reader to understand the file
        next(csv_reader) # Skip header rows 
        for row in csv_reader: ## loop through rows

            ## if has items (row truthy)
            if row:
                ## convert values row[0] 
                ## add to list 
                data.append([str(row[0]), int(row[1]), int(row[2])]) ## ** convert to int
    print(data)
    return data
 

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    weather_data_float = [float(item) for item in weather_data]
    if weather_data_float == []:
        return ()
    min_value = float('inf')  # Start with the highest possible float value
    spot_min = None
    for spot, value in enumerate(weather_data_float):
        if value < min_value:
            min_value = value
            spot_min = spot
        elif value == min_value:
            spot_min = spot
    return (min_value, spot_min)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.
    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    weather_data = [float(item) for item in weather_data]
    max_value = 0
    spot_max = None
    print(max_value)  # To see the list before conversion
    if weather_data == []:
        return ()
    else:
        for spot, value in enumerate(weather_data):
            print(spot) # To see the spot in the list
            if value > max_value:
                max_value = value
                spot_max = spot
            elif value == max_value:
                spot_max = spot
        return (max_value, spot_max)

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    num_days = len(weather_data)
    print(num_days) #Check the number of the days
    
    
    # Now I am trying to get the day with the lowest temperature
    low_temp_all = []
    for index, value in enumerate(weather_data):
        low_temp = convert_f_to_c(value[1])
        print(low_temp) #Checking
        low_temp_all.append(low_temp) 
    min_value_all = find_min(low_temp_all)
    min_overall_temp, min_index = min_value_all #unpacking
    days_min_all = weather_data[min_index]
    day_min = days_min_all[0]
    date_fix = convert_date(day_min)
    
    # Now I am trying to get the day with the Highest temperature
    high_temp_all = []
    for index, value in enumerate(weather_data):
        high_temp = convert_f_to_c(value[2])
        print(high_temp) #Checking
        high_temp_all.append(high_temp)
    max_res_all = find_max(high_temp_all)
    max_overall_temp, max_index = max_res_all #unpacking
    days_max_all = weather_data[max_index]
    day_max = days_max_all[0]
    fix_date = convert_date(day_max)
    
  # Now I am trying to get the average high temperature of the week
    average_low = calculate_mean(low_temp_all)
    average_high = calculate_mean(high_temp_all)
    return (
    f"{num_days} Day Overview\n  "
    f"The lowest temperature will be {format_temperature(min_overall_temp)}, and will occur on {date_fix}.\n  "  
    f"The highest temperature will be {format_temperature(max_overall_temp)}, and will occur on {fix_date}.\n  "  
    f"The average low this week is {format_temperature(average_low)}.\n  "
    f"The average high this week is {format_temperature(average_high)}.\n"
)


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    ##f"  Minimum Temperature: {}""

    ## '\n' is a new line (you mayneed a lot of these )
    daily_report_summary = "" #Empty string
    for value in weather_data:
        daily_summary = (
            f"---- {convert_date(value[0])} ----\n"
            f"  Minimum Temperature: {format_temperature(convert_f_to_c(value[1]))}\n"
            f"  Maximum Temperature: {format_temperature(convert_f_to_c(value[2]))}\n\n"
        )
        daily_report_summary += daily_summary # Adding this day's summary to the overall report
    return daily_report_summary