"""
Module written to improve performance from a poorly performing module.
"""

import datetime
import csv

def analyze(filename):
    """Analyze data from a *.csv file"""
    start = datetime.datetime.now()
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        found = 0

        year_count = {
            "2013": 0,
            "2014": 0,
            "2015": 0,
            "2016": 0,
            "2017": 0,
            "2018": 0
        }

        for row in reader:
            if row[6] == 'ao':
                found += 1
            try:
                year_count[row[5][6:]] += 1
            except KeyError:
                pass

    print(year_count)

    print(f"'ao' was found {found} times")
    end = datetime.datetime.now()

    return (start, end, year_count, found)

def main():
    """Main method for module"""
    filename = "data/exercise.csv"
    analyze(filename)

if __name__ == '__main__':
    main()
