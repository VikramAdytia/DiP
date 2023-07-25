import argparse
import calendar
import time


def isleap(valid_date):
    return calendar.isleap(valid_date[0])


def validate_date(date):
    try:
        valid_date = time.strptime(date, '%d.%m.%Y')
        print(f"The year {valid_date[0]} is leap" if isleap(valid_date) else f"The year {valid_date[0]} is not leap")
        return True
    except ValueError:
        print('Invalid date!')
        return False

parser = argparse.ArgumentParser(description='Check date.')
parser.add_argument('date', type=str, help='Date to check in the format DD.MM.YYYY')

args = parser.parse_args()

print(validate_date(args.date))