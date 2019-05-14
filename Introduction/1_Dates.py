# Given Your BirthDate and Current Date Indentify the numnber of days...


# -Don't Panic
# -- Step 1 - Understand What the inputs are!
# Second Date should not be before  the first date -- Defensicve Coding...
# What are the outputs?? ->

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    if month == 12 and day == 30:
        month = 1
        day = 1
        year = year + 1
        return (year, month, day)
    elif day == 30:
        month += 1
        day = 1
        return(year, month, day)
    else:
        return(year, month, day+1)


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 > year2:
        return False
    if year1 == year2 and month1 > month2:
        return False
    if month1 == month2 and day1-day2 < 0:
        return False
    return True


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """

    # TODO - by the end of this lesson you will have
    #  completed this function. You do not need to complete
    #  it yet though!
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)

    return days


def testDaysBetweenDates():

    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                            2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30,
                            2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30,
                            2018, 1,  1) == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                            2013, 6, 29) == 365)

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")


# testDaysBetweenDates()

print(daysBetweenDates(2017, 12, 30,
                       2018, 1,  1))
