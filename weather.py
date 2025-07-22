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
    return sum(conv_list) / len(conv_list)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    #data = [] # Create an empty list, I will fill it with the data that I need
    # open(csv_file, 'r') as file:
        # = csv.reader(file) #Tell Python to use the CSV reader to understand the file
        #data.append(csv_reader)
        #for row in csv_reader:

    #CHECK ERROR
 

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
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass