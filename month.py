#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: Oct 2019
# This program detirmines how many days there are in a month


def main():
    month = input("Enter a month: ")
    print("")

    if month == "January" or month == "March" or month == "May" or \
            month == "July" or month == "August" or month == "October" or \
            month == "December":
        print("31 days")
    elif month == "April" or month == "June" or month == \
            "September" or month == "November":
        print("30 days")
    elif month == "February":
        print("28 days/29 on leap years")
    else:
        print("This is not a valid month")


if __name__ == "__main__":
    main()
