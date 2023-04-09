#import modules
import sys
from datetime import date, timedelta
import sys
import re
import inflect

#inflect engine
p = inflect.engine()

#main function
def main():
    #users birthday
    birth_date = input("Birth date: ")
    try:
        #check format and prints duration in minutes
        if valid_format(birth_date):
            mins = minutes(birth_date)
            print(minutes_with_words(mins))
            
        # if format is invalid exit via sys.exit()
        else:
            sys.exit("Invalid format")
    
    #catch exception errors
    except:
        sys.exit("Something went wrong")

#calculate minutes from birthday
def minutes(birth_date):
    #split birth_date
    year, month, day = birth_date.split("-")
    #convert birth date into timedelta format
    date_of_birth = date(year= int(year), month= int(month), day= int(day))
    #define today's date
    date_of_today = date.today()
    #difference between dates
    difference = date_of_today - date_of_birth
    #convert days into minutes
    minutes = int(difference.total_seconds() // 60)
    return minutes

#convert digits into words using inflect engine
def minutes_with_words(minutes):
    words = p.number_to_words(minutes, andword="")
    return f"{words.capitalize()} minutes"

#define valid format using regular expresions
def valid_format(birth_date):
    pattern = r"^[0-9]{4}-[0-9]{2}-[0-9]{2}"
    if re.match(pattern, birth_date):
        return True
    return False

#call main function
if __name__ == "__main__":
    main()
