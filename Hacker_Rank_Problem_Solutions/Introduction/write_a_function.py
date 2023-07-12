def is_leap(year):
    """
    Check if the year is leap or not

    Args:
        year(int): The year to be checked
    
    Returns:
        bool: (True) if the year is leap otherwise (False)

    Example:
        >>>is_leap(2000)
        True
    """
    leap = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            leap  = True 
    return leap

year = int(input())
print(is_leap(year))
