from calendar import day_name


def get_weekday(num):
    try:
        if num <= 0:
            return 'Number too low'
        return day_name[num-1]
    except IndexError:
        return 'Number too high'
    except TypeError:
        return 'Not a number'


weekday_name = get_weekday(7)
print(weekday_name)
