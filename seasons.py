import sys
from datetime import date, timedelta
import sys
import re
import inflect

p = inflect.engine()

def main():
    birth_date = input("Birth date: ")
    try:
        if valid_format(birth_date):
            mins = minutes(birth_date)
            print(minutes_with_words(mins))
        else:
            sys.exit("Invalid format")
    except:
        sys.exit("Something went wrong")

def minutes(birth_date):
    year, month, day = birth_date.split("-")
    date_of_birth = date(year= int(year), month= int(month), day= int(day))
    date_of_today = date.today()
    difference = date_of_today - date_of_birth
    minutes = int(difference.total_seconds() // 60)
    return minutes

def minutes_with_words(minutes):
    words = p.number_to_words(minutes, andword="")
    return f"{words.capitalize()} minutes"

def valid_format(birth_date):
    pattern = r"^[0-9]{4}-[0-9]{2}-[0-9]{2}"
    if re.match(pattern, birth_date):
        return True
    return False

if __name__ == "__main__":
    main()
