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


print(nextDay(1999, 12, 30))
